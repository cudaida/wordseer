import unittest
from structureextractor import *
import tokenizer
from lxml import etree

class ExtractorTests(unittest.TestCase):
    def setUp(self):
        self.structure_file = "tests/data/structure.json"
        self.input_file = "tests/data/articles/post1.xml"
        self.xml = etree.parse(self.input_file)
        t = tokenizer.Tokenizer()
        self.extractor = StructureExtractor(t, self.structure_file)

    @unittest.skip("Depends on extract_unit_information()")
    def test_extract(self):
        with open(self.input_file) as f:
            documents = self.extractor.extract(f)

    @unittest.skip("Root selector problems")
    def test_extract_unit_information(self):
        pass

    @unittest.skip("Root selector problems")
    def test_get_sentences(self):
        pass

    @unittest.skip("Depends on get_xpath_attribute")
    def test_get_metadata(self):
        pass

    @unittest.skip("Root selector problems")
    def test_get_xpath_attribute(self):
        pass

    def test_get_xpath_text(self):
        xpaths = {"./author/text()": ["rachel"],
            "./title/text()": ["Post 1"],
            "./time/text()": ["2012-02-23"],
            "./number/text()": ["1"],
            "./tags/tag/text()": ["Tag 0", "Tag 3"],
            "   ": ["\n2012-02-23\nPost 1\nrachel\n\n Tag 0\n Tag " +\
                "3\n\n1\n\n\tThis is the text of post 1. I love clouds.\n\n"]}
        for xpath, text in xpaths.items():
            result = get_xpath_text(xpath, self.xml.getroot())
            self.failUnless(result == text)

def main():
    unittest.main()

if __name__ == "__main__":
    main()