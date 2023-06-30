import os
from datetime import datetime

import git


def extract_all_raw(repo_path, file_path, raw_output_path, perform_output_dir_cleanup=False):
    # Create the output directory if it doesn't exist
    os.makedirs(raw_output_path, exist_ok=True)

    # Perform output directory cleanup if enabled
    if perform_output_dir_cleanup:
        # Empty the output directory
        for file_name in os.listdir(raw_output_path):
            file_path = os.path.join(raw_output_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # Open the repository
    repo = git.Repo(repo_path)

    # Access the main branch
    branch = repo.branches['main']

    # Iterate over the commits on the main branch
    for commit in repo.iter_commits(branch):
        try:
            # Retrieve file contents from the commit
            file_contents = commit.tree[file_path].data_stream.read().decode('utf-8')

            # Extract commit metadata
            commit_timestamp = datetime.fromtimestamp(commit.committed_date)
            commit_hash = commit.hexsha

            # Generate the filename using an f-string
            filename = f"{commit_timestamp.strftime('%Y%m%d_%H%M%S')}_{commit_hash}.json"
            file_output_path = os.path.join(raw_output_path, filename)

            # Print metadata
            print(f'Commit: {commit.hexsha}')
            print(f'Timestamp: {commit_timestamp.isoformat()}')
            print(f'Output file: {file_output_path}')
            print('----------------------------------------')

            # Write the file contents to the output file
            with open(file_output_path, 'w') as output_file:
                output_file.write(file_contents)
        except KeyError:
            # The file is not found in the commit
            print(f'File {file_path} not found in {commit.hexsha}')

if __name__ == "__main__":
    if os.getenv("CI") == 'true':
        extract_all_raw('demodiff_berlin', 'data/results.json', 'data_raw')
    else:
        from settings import repo_path, file_path, perform_output_dir_cleanup, raw_output_path
        extract_all_raw(repo_path, file_path, raw_output_path, perform_output_dir_cleanup)
