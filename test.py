from git import Repo
import os
import sys

repo = Repo(os.path.abspath('.'))
notebook_path = sys.argv[0].split('/')[-1]
repo.index.add([notebook_path])
repo.index.commit(message='test')
repo.remote().push()