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
        self.memov_mock = MemovMock()

    def testMovieAviXvid(self):
        self.memov_mock.move("/Downloads/", "Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi") 
        self.assertEqual(self.memov_mock.new_file, "/movies/Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi")   
        
    def testMovieDvdMinusRip(self):
        self.memov_mock.move("/Downloads/", "Marilyn Manson - Guns, God and Government World Tour - DVD-rip 480x272 PSP - NLizer.mp4") 
        self.assertEqual(self.memov_mock.new_file, "/movies/Marilyn Manson - Guns, God and Government World Tour - DVD-rip 480x272 PSP - NLizer.mp4")       
        
    def testMovie720p(self):
        self.memov_mock.move("/Downloads/", "lion king 720p - zeberzee.mp4") 
        self.assertEqual(self.memov_mock.new_file, "/movies/lion king 720p - zeberzee.mp4")     
        
    def testMoviePartlyDownloaded(self):
        self.memov_mock.move("/Downloads/", "Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi.part") 
        self.assertEqual(self.memov_mock.new_file, "")            
                
    def testTvShowSmallCaseSerie(self):
        self.memov_mock.move("/Downloads/", "Family.Guy.s12e14.HDTV.x264-2HD.mp4") 
        self.assertEqual(self.memov_mock.new_file, "/shows/Family Guy/Family Guy - Season 12/Family.Guy.S12E14.HDTV.x264-2HD.mp4")
        
    def testTvShowOnlyEpisodeInfo(self):
        self.memov_mock.move("/Downloads/", "Family Guy s8 e14.mp4") 
        self.assertEqual(self.memov_mock.new_file, "/shows/Family Guy/Family Guy - Season 8/Family.Guy.S08E14.mp4")
        
    def testTvShowSpaceAfterEpisodeInfo(self):
        self.memov_mock.move("/Downloads/", "The.Simpsons.S25E14- HDTV.x264-LOL.mp4") 
        self.assertEqual(self.memov_mock.new_file, "/shows/The Simpsons/The Simpsons - Season 25/The.Simpsons.S25E14.HDTV.x264-LOL.mp4")        
        
    @unittest.skip("To be implemented")
    def testTvShowLittleEpisodeInfoSeason3(self):
        self.memov_mock.move("/Downloads/", "revenge.307.hdtv-lol.mp4") 
        self.assertEqual(self.memov_mock.new_file, "/shows/Revenge/Revenge - Season 3/Revenge.S03E07.hdtv-lol.mp4")  
    
    @unittest.skip("To be implemented")    
    def testTvShowLittleEpisodeInfoSeason10(self):
        self.memov_mock.move("/Downloads/", "greys.anatomy.1018.hdtv-lol.mp4") 
        self.assertEqual(self.memov_mock.new_file, "/shows/Greys Anatomy/Greys Anatomy - Season 10/Greys.Anatomy.S10E18.hdtv-lol.mp4")           
    
    def testTvShowPartlyDownloaded(self):
        self.memov_mock.move("/Downloads/", "Revenge.S03E10.HDTV.x264-LOL.mp4.part") 
        self.assertEqual(self.memov_mock.new_file, "")                      
                
    def testConfigList(self):
        config = ["a", "b", "c"]
        result = self.memov_mock._createConfigList(config)
        self.assertEqual(result, "a|b|c")              

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MemovTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
