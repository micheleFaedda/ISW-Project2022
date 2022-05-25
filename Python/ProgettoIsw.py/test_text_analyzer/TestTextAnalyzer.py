
import unittest
from main import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):

    text_analyzer = TextAnalyzer('test_output.txt', 'test_output.txt', 1)

    def test_text_analyzer_return_exception_file_not_found(self):
        self.assertRaises(FileNotFoundError, TextAnalyzer.list_of_words_from_file,self.text_analyzer, 'pippo.txt')

    def test_text_analyzer_remove_puntaction(self):
        expected = 'i m  the text  without  puntuactions '
        actual = self.text_analyzer.remove_punctuation_from_line('i\'m? the text, without, puntuactions;')
        self.assertEqual(expected,actual)

    def test_text_analyzer_remove_stopwords(self):
        expected = ['word','random','beautiful']
        self.text_analyzer.text = ['word','is','random','and','beautiful']
        self.text_analyzer.stopwords = ['is','and']
        self.text_analyzer.remove_stopwords()
        actual = self.text_analyzer.text
        self.assertEqual(expected,actual)

    def test_text_analyzer_return_correct_frequency_of_word(self):
        expected = {'word' : 1 , 'random' : 1 , 'beautiful' : 1}
        actual = self.text_analyzer.text_frequency_of_words()
        self.assertEqual(expected, actual)

    def test_text_analyzer_return_correct_frequency_of_composite_word(self):
        expected = {'word,random' : 1 , 'random,beautiful' : 1}
        self.text_analyzer.text = ['word', 'random', 'beautiful']
        self.text_analyzer.limit_frequency = 1
        actual = self.text_analyzer.text_frequency_of_composite_words()
        self.assertEqual(expected, actual)

    def test_text_analyzer_limit_frequency_of_composite_word_respected(self):
        expected = {}
        self.text_analyzer.text = ['word', 'random', 'beautiful']
        self.text_analyzer.limit_frequency = 2
        actual = self.text_analyzer.text_frequency_of_composite_words()
        self.assertEqual(expected, actual)

    def test_text_analyzer_save_correctly_output_frequency(self):
        expected_words = ['word,1\n','random,1\n','beautiful,1\n']
        self.text_analyzer.text = ['word', 'random', 'beautiful']
        frequency = self.text_analyzer.text_frequency_of_words()
        self.text_analyzer.save_frequency_into_file('test_output.txt',frequency)
        with open('test_output.txt') as file:
            actual_words = file.readlines()

        self.assertEqual(expected_words, actual_words)

if __name__ == '__main__':
    pass



