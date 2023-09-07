#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 sakakibara <sakakibara@dyana>
#
# Distributed under terms of the MIT license.

from git import Repo

repo = Repo.init("../")
commits = repo.iter_commits(all=True, max_count=10)

for commit in commits:
    print(commit.message)
