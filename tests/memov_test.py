import unittest
from memov import Memov
import config

class MemovMock(Memov):
    def __init__(self):
        config.MOVIE_DIR = "/movies/"
        config.TV_SHOW_DIR = "/shows/"
        Memov.__init__(self)
        self.orig_file = ""
        self.new_file = ""     

    def createTvShowDir(self, tv_show_dir):
        pass
        
    def moveFile(self, orig_file, new_file):
        self.orig_file = orig_file
        self.new_file = new_file           

class MemovTest(unittest.TestCase):
    def setUp(self):
        self.memov = Memov()

    def testMovieAviXvid(self):
        self.assertTrue(self.memov.isMovie("Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi"))
        
    def testMovieDvdMinusRip(self):
        self.assertTrue(self.memov.isMovie("Marilyn Manson - Guns, God and Government World Tour - DVD-rip 480x272 PSP - NLizer.mp4"))
        
    def testMovie720p(self):
        self.assertTrue(self.memov.isMovie("lion king 720p - zeberzee.mp4"))        
        
    def testMoviePartlyDownloaded(self):
        self.assertFalse(self.memov.isMovie("Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi.part"))           
                
    def testTvShowSmallCaseSerie(self):
        self.assertTrue(self.memov.isTvShow("Family.Guy.s12e14.HDTV.x264-2HD.mp4"))
        
    def testTvShowOnlyEpisodeInfo(self):
        self.assertTrue(self.memov.isTvShow("Family Guy s12 e14.mp4"))      
        
    @unittest.skip("To be implemented")    
    def testTvShowLittleEpisodeInfo(self):
        self.assertTrue(self.memov.isTvShow("revenge.307.hdtv-lol.mp4"))       
    
    def testTvShowPartlyDownloaded(self):
        self.assertFalse(self.memov.isTvShow("Revenge.S03E10.HDTV.x264-LOL.mp4.part"))              

    def testCleanUpTvShowFileName(self):
        self.assertEqual(self.memov.cleanUpTvShowFilename(["The.Simpsons", "25", "4", ".HDTV.x264-LOL.mp4"]), ['The Simpsons', '25', '04', '.HDTV.x264-LOL.mp4'])
        
    def testCleanUpTvShowFileNameWithSpace(self):
        self.assertEqual(self.memov.cleanUpTvShowFilename(["The.Simpsons", "25", "4", "- title.mp4"]), ['The Simpsons', '25', '04', 'title.mp4'])               
                
    def testTransformTvShowFileName(self):
        self.assertEqual(self.memov.transformTvShowFilename(["The Simpsons", "25", "14", ".HDTV.x264-LOL.mp4"]), "The.Simpsons.S25E14.HDTV.x264-LOL.mp4")          
  
    def testExtractTvShowDir(self):
        self.assertEqual(self.memov.extractTvShowDir(['The Simpsons', '25', '14', '.HDTV.x264-LOL.mp4']), ["The Simpsons", "The Simpsons - Season 25"])     
        
    def testMoveTvShow(self):
        memov_mock = MemovMock()
        memov_mock.move("/Downloads/", "Family.Guy.s12e14.HDTV.x264-2HD.mp4")
        self.assertEqual(memov_mock.new_file, "/shows/Family Guy/Family Guy - Season 12/Family.Guy.S12E14.HDTV.x264-2HD.mp4")  
        
    def testMoveMovie(self):
        memov_mock = MemovMock()
        memov_mock.move("/Downloads/", "Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi") 
        self.assertEqual(memov_mock.new_file, "/movies/Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi")               
                
    def testConfigList(self):
        config = ["a", "b", "c"]
        result = self.memov._createConfigList(config)
        self.assertEqual(result, "a|b|c")              

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MemovTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
