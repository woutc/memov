Info
----
**MeMov**  
Version: 0.1  
Author: Wout Clymans (woutclymans@gmail.com)

This script will query the directory set in the config.py file (DOWNLOAD_DIR) for any
files that look like movies or tv shows.  The files will then be
renamed and moved to the respective video directory. After all files
are moved/renamed.

**This script is VERY heavily based on https://github.com/dralthiace/sort-shows.pl**
All credits to him for the inital idea and making it work in perl.

Details
-------

###CONFIGURATION
In the root of the repository there is a file called `config.py`that contains
the setup for the script work correctly.
Have a look at the variables and add values if needed.

###TESTING
[![Build Status](https://travis-ci.org/woutc/memov.svg?branch=master)](https://travis-ci.org/woutc/memov)

There are unit tests for the script located in the `tests`folder.
To run the unit tests, execute the following:
    `python -m tests.memov_test`

###IDENTIFICATION

TV Shows are identified if they have the S##E## notation (season/episode)
Movies are identified by the following variable in config.py
`MOVIE_INDICATORS` and have an extension listen in variable `EXTENSIONS`.

###MOVE

Files are moved to the directory specified below (TVSHOWS_DIR or MOVIES_DIR)
TV Shows are moved to:  
  `TVSHOWS_DIR/{show_name}/{show_name} - {season}/{file}`  
Movies are moved to:  
  `MOVIES_DIR/{file}`

###RENAME

TV Show file names are normalized to be recognized by XBMC:

* special characters are removed
* capitalization changed to first character of each word
* extra whitespace removed
* spaces are converted to periods (.)
* rest of name (after S##E##) is left alone (this can contain useful info)

Movies are not renamed, only moved.
