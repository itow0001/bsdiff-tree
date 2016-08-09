## Install
```
python setup.py install
or.
pip install bstree
```

## Usage
```
optional arguments:
  -h, --help   show this help message and exit
  -o ORIGIN    Origin tree, base path
  -n NEW       New tree, base path
  -p PATH      absolute path to place output
  -e EXCLUDES  exclude files or directories
  -d           enable debug messages
  --version    show program's version number and exit
```
## example
```
cd ~
mkdir -p origin
cd origin touch apples.txt
echo "hello world" > apples.txt
mkdir -p new
cd origin touch apples.txt
echo "findme I`m different" > apples.txt
mkdir -p files
bstree -o ~/origin -n ~/new -p ~/files
```

