import unittest
from memov import Memov

class MemovTest(unittest.TestCase):
    def testMovieAviXvid(self):
        x = Memov()
        self.assertTrue(x.isMovie("Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi"))
        
    def testMovieDvdMinusRip(self):
        x = Memov()
        self.assertTrue(x.isMovie("Marilyn Manson - Guns, God and Government World Tour - DVD-rip 480x272 PSP - NLizer.mp4"))
        
    def testMovie720p(self):
        x = Memov()
        self.assertTrue(x.isMovie("lion king 720p - zeberzee.mp4"))        
        
    def testMoviePartlyDownloaded(self):
        x = Memov()
        self.assertFalse(x.isMovie("Nymphomaniac 2013 Volume II UNRATED WEBRip XviD MP3-RARBG.avi.part"))           
                
    def testTvShowSmallCaseSerie(self):
        x = Memov()
        self.assertTrue(x.isTvShow("Family.Guy.s12e14.HDTV.x264-2HD.mp4"))
        
    def testTvShowOnlyEpisodeInfo(self):
        x = Memov()
        self.assertTrue(x.isTvShow("Family Guy s12 e14.mp4"))      
        
    @unittest.skip("To be implemented")    
    def testTvShowLittleEpisodeInfo(self):
        x = Memov()
        self.assertTrue(x.isTvShow("revenge.307.hdtv-lol.mp4"))       
    
    def testTvShowPartlyDownloaded(self):
        x = Memov()
        self.assertFalse(x.isTvShow("Revenge.S03E10.HDTV.x264-LOL.mp4.part"))              
        
    def testTransformTvShowFileName(self):
        x = Memov()
        self.assertEqual(x.transformTvShowFilename(["The.Simpsons", "25", "14", ".HDTV.x264-LOL.mp4"]), "The.Simpsons.S25E14.HDTV.x264-LOL.mp4")          

    @unittest.skip("To be implemented")    
    def testExtactTvShowDir(self):
        x = Memov()
        self.assertEqual(x.extractTvShowDir(["The.Simpsons", "25", "14", ".HDTV.x264-LOL.mp4"]), ["The Simpsons", "The Simpsons - Season 25"])      
                
    def testConfigList(self):
        x = Memov()
        config = ["a", "b", "c"]
        result = x._createConfigList(config)
        self.assertEqual(result, "a|b|c")              

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MemovTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
