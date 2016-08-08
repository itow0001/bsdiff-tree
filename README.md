
**********************************************
 File @ ***/main.py***

None

**********************************************
 File @ ***/bsdiff_tree/__init__.py***

Modules __init__.py

**********************************************
 File @ ***/bsdiff_tree/__main__.py***

Main entry for bstree


***def menu***: 

The Menu is here
**********************************************

***def main***: 

This is used in the cli and from a couple places
**********************************************
**********************************************
 File @ ***/bsdiff_tree/modules/__init__.py***

None

**********************************************
 File @ ***/bsdiff_tree/modules/manager.py***

Created on Aug 5, 2016

@author: iitow


***class Manager***: 

classdocs
**********************************************

***def __init__***: 

Constructor
**********************************************

***def _walk***: 

performs scan on all files

**:param path:** String

**:param excludes:** List, list of excludes
**********************************************

***def _set_arrays***: 

Walk both origin path & new path
**********************************************

***def _filedelta***: 

get files delta of origin & new
**********************************************

***def _fileunion***: 

get the union of both origin & new
**********************************************

***def _bsdiff***: 

perform a bsdiff

**:param base_a:** String, path to file a 

**:param base_b:** String, path to file b

**:param tag:** tag of file
**********************************************

***def bsdiff***: 

1. Generate bsdiff origin file of self
2. Generate bsdiff origin file to new file
3. diff compare origin to new
**********************************************

***def _write***: 

Write diffs found to file

**:param arr:** List, all files to write out to tree.diff
**********************************************
**********************************************
 File @ ***/bsdiff_tree/modules/terminal.py***

Created on Nov 18, 2015


**:author:** iitow


***def waitfor***: 

poll the child for input


**:param fd:** forked process
**********************************************

***def event***: 

find all output and inspect it for searches dict key & value


**:param fd:** forked process

**:param searches:** dictionary key value pair
**********************************************

***def set_rsa***: 

logs into system via ssh
and appends to authorized_keys using username password


**:param     host:** name over the server

**:param  rsa_pub:** absolute path to your id_rsa.pub

**:param     user:** host login creds

**:param password:** host login creds

**:param home_dir:** home directory for user
**********************************************

***def create_rsa_public***: 

generate a public key from the private key


**:param rsa_private:** path to private key
**********************************************

***def ssh***: 

Run a single ssh command on a remote server


**:param server:** username@servername

**:param cmd:** single command you wish to run
**********************************************

***def rsync***: 

Performs an rsync of files; requires ssh keys setup.


**:param   server:** username@server

**:param      src:** full path of src directory/file

**:param     dest:** full path to dest directory

**:param   option:** [pull] get file from a remote,
[push] put a file from your server into a remote

**:param   remote:** [True] assumes we are working with
a remote system, [False] assumes we are copying files locally

**:param excludes:** exclude directory, or file from array

**:note:** --delete will delete files on dest if it does not match src
**********************************************

***def sig_exception***: 

None
**********************************************

***def shell***: 

Run Shell commands  [Non Blocking, no Buffer, print live, log it]


**:param cmd:** String command

**:param verbose:**bool

**:param strict:**bool will exit based on code if enabled

**:return:**  {command, stdout, code} as dict
**********************************************

***def _exit_clean***: 

cleans .tmp_shell files before exit
**********************************************