#!/usr/bin/python

import os
import re
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
        return matched_filename[0] + ".S" + matched_filename[1] + "E" + matched_filename[2] + matched_filename[3]
                
    def transformTvShowFilename(self, matched_filename):
        return matched_filename[0] + ".S" + matched_filename[1] + "E" + matched_filename[2] + matched_filename[3]

    def extractTvShowDir(self, matched_filename):
        return [matched_filename[0], matched_filename[0] + " - Season " + matched_filename[1]]
          
    def move(self, dir, file_name):
        tv_show_match = self.isTvShow(file_name)
        if tv_show_match:
            print file_name + "[tv show]"
            self.transformTvShowFilename(tv_show_match.groups())
            self.extractTvShowDir(tv_show_match.groups())
        elif self.isMovie(file_name):
            print file_name + "[movie]"
        else:
            print file_name + "[unknown]"
                
        
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