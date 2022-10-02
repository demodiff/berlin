#!/usr/bin/env bash

for i in $(git log --format='%H'); do
  git show $i:data/results.jsonl > ../data/jsonl/$(git show -s --format=%cd --date=format:'%Y%m%d-%H%M%S' $i)-$i.jsonl
done
