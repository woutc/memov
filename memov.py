#!/usr/bin/python

import os
import re
import string
import shutil
import errno
import config


class Memov:
    def __init__(self):
        extensions = self._createConfigList(config.EXTENSIONS)
        movie_indicators = self._createConfigList(config.MOVIE_INDICATORS)
        self.tv_pattern = re.compile("([-._ \w]+)[-._ ]S(\d{1,2}).?E(\d{1,2})([^\/]*\.(?:" + extensions + ")$)", re.IGNORECASE)
        self.movie_pattern = re.compile("(?:" + movie_indicators + ")(.*)\.(?:" + extensions + ")$", re.IGNORECASE)

    def isMovie(self, filename):
        result = self.movie_pattern.search(filename)
        return result

    def isTvShow(self, filename):
        result = self.tv_pattern.search(filename)
        return result

    def cleanUpTvShowFilename(self, matched_filename):
        matched_filename[0] = re.sub(r"[-._]", r" ", matched_filename[0].lower())
        matched_filename[0] = string.capwords(matched_filename[0])
        matched_filename[1] = "%02d" % int(matched_filename[1])
        matched_filename[2] = "%02d" % int(matched_filename[2])
        matched_filename[3] = re.sub(r"^- ", r"", matched_filename[3])
        return matched_filename

    def transformTvShowFilename(self, matched_filename):
        return matched_filename[0].replace(" ", ".") + ".S" + matched_filename[1] + "E" + matched_filename[2] + matched_filename[3]

    def extractTvShowDir(self, matched_filename):
        return [matched_filename[0], matched_filename[0] + " - Season " + matched_filename[1]]

    def move(self, dir, file_name):
        orig_file = os.path.join(dir, file_name)
        tv_show_match = self.isTvShow(file_name)
        if tv_show_match:
            tv_show_title = list(tv_show_match.groups())
            tv_show_title = self.cleanUpTvShowFilename(tv_show_title)
            tv_show_dir = self.extractTvShowDir(tv_show_title) 
            tv_show_title = self.transformTvShowFilename(tv_show_title)    
            self.moveTvShow(orig_file, tv_show_dir, tv_show_title)
        elif self.isMovie(file_name):
            full_path = os.path.join(config.MOVIE_DIR, file_name)
            self.moveFile(orig_file, full_path)
        else:
            print file_name + "[unknown]"
            
    def moveTvShow(self, orig_file, tv_show_dir, tv_show_title):
        directory = os.path.join(config.TV_SHOW_DIR, tv_show_dir[0], tv_show_dir[1])
        self.createTvShowDir(directory)
        self.moveFile(orig_file, os.path.join(directory, tv_show_title))
        
    def moveFile(self, orig_file, new_file):
        print "Moving file: " + orig_file + " to " + new_file
        shutil.move(orig_file, new_file)

    def createTvShowDir(self, tv_show_dir):
        try:
            os.makedirs(tv_show_dir)
        except OSError, e: 
            if e.errno != errno.EEXIST: 
                raise      

    def run(self, downloaddir):
        self.walkdir(downloaddir)

    def walkdir(self, dir):
        for root, subFolders, files in os.walk(dir):
            for file_name in files:
                self.move(root, file_name)
            for folder in subFolders:
                self.walkdir(folder)

    def _createConfigList(self, list_):
        result = ""
        for item in list_:
            result += item + "|"
        return result.rstrip("|")

if __name__ == '__main__':
    Memov().run(config.DOWNLOAD_DIR)
