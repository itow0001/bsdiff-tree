'''
Created on Aug 5, 2016
@author: iitow
'''
import os
from terminal import shell
from random import randint

class Manager(object):
    '''
    handles all actions for bstree
    '''
    def __init__(self,options):
        '''
        Constructor
        :param options: Dict, argparse menu options
        '''
        self.options = options
        self.path = "%s/%s" % (self.options.path,"tmp")
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.excludes = self.options.excludes
        self.origin = self.options.origin
        self.new = self.options.new
        self.origin_arr = []
        self.new_arr = []
        self.excluded = []
        self.errors = []
        self._set_arrays()
        self.delta = self._filedelta()
        self.union = self._fileunion()
        self.bsdiffs = self.bsdiff()

    def _walk(self,path,excludes=[]):
        ''' performs scan on all files
        :param path: String
        :param excludes: List, list of excludes
        '''
        paths = []
        if self.options.debug:
            print excludes
        for root, directories, filenames in os.walk(path):
            for filename in filenames:
                if excludes:
                    for exclude in excludes:
                        root = root.replace(path,'')
                        filepath =  "%s/%s" % (root, filename)
                        if exclude in filepath:
                            self.excluded.append(filepath)
                        else:
                            paths.append(filepath)
                else:
                    paths.append(filepath)
                    
        return paths

    def _set_arrays(self):
        '''
        Walk both origin path & new path
        '''
        self.origin_arr = self._walk(self.origin,excludes=self.excludes)
        self.new_arr = self._walk(self.new,excludes=self.excludes)

    def _filedelta(self):
        '''
        get files delta of origin & new
        '''
        return list(set(self.origin_arr) - set(self.new_arr))

    def _fileunion(self):
        '''
        get the union of both origin & new
        '''
        return list(set(self.origin_arr) | set(self.new_arr))

    def _bsdiff(self,base_a, base_b,tag='tag'):
        '''
        perform a bsdiff
        :param base_a: String, path to file a 
        :param base_b: String, path to file b
        :param tag: tag of file
        '''
        cmd = "cd %s; bsdiff %s %s %s" % (self.path,
                                          base_a,
                                          base_b,
                                          tag)
        if self.options.debug:
            print cmd
        session = shell(cmd)
        if self.options.debug:
            print session
        if session.get('code') > 0:
            print "Error: %s" % (base_a)
            self.errors.append(base_a)
        return session.get('stdout')

    def bsdiff(self):
        '''
        Generate bsdiff origin file of self
        Generate bsdiff origin file to new file
        diff compare origin to new
        '''
        diffs = []
        for file_path in self.union:
            tag_origin = "%s%s" % ('origin',file_path.replace('/','.'))
            tag_new = "%s%s" % ('new',file_path.replace('/','.'))
            path_origin = "%s%s" % (self.origin,file_path)
            path_new = "%s%s" % (self.new,file_path)
            self._bsdiff(path_origin, path_origin, tag_origin)
            self._bsdiff(path_origin, path_new, tag_new)
            session = shell("diff %s %s" % (tag_origin,tag_new))
            output = session.get('stdout')
            if("differ\n" in output):
                print "Found: %s" % file_path
                diffs.append(file_path)
            else:
                print " Pass: %s" % file_path
        self._write(diffs)
        return diffs

    def _write(self,arr):
        '''
        Write diffs found to file
        :param arr: List, all files to write out to tree.diff
        '''
        filename = "%s/tree.diff" % (self.path)
        cnt_diffs = 0
        cnt_delta = 0
        cnt_errors = 0
        cnt_excluded = 0
        with open(filename, 'w') as bs_diff:
            for path in arr:
                bs_diff.write("bsdiff,%s\n"% path)
                cnt_diffs+=1
            for path in self.delta:
                bs_diff.write("delta,%s\n"% path)
                cnt_delta+=1
            for path in self.excluded:
                bs_diff.write("exclude,%s\n"% path)
                cnt_excluded+=1
            for path in self.errors:
                bs_diff.write("error,%s\n"% path)
                cnt_errors+=1
        print " bsdiffs: %s" % (str(cnt_diffs))
        print "   delta: %s" % (str(cnt_delta))
        print "excluded: %s" % (str(cnt_excluded))
        print "  errors: %s" % (str(cnt_errors))
        print "   TOTAL: %s" % (str(cnt_diffs+cnt_delta))
        print " results: %s" % (filename)
        print "Complete"