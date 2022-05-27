import string
import sys
from test_text_analyzer.TestTextAnalyzer import *
import time


class TextAnalyzer:

    def __init__(self, text_file_name, stopword_file_name, limit_frequency):
        self.punctuation = {char: ' ' for char in list(string.punctuation)}
        self.text = TextAnalyzer.list_of_words_from_file(self, text_file_name)
        self.stopwords = list(set(TextAnalyzer.list_of_words_from_file(self, stopword_file_name)))
        self.limit_frequency = int(limit_frequency)

    def save_frequency_into_file(self, output_file_name, frequency_dictionary):
        with open(output_file_name, 'w') as output_file:
            for item in frequency_dictionary.items():
                output_file.write(str(item[0]) + ',' + str(item[1]) + '\n')

    def text_frequency_of_words(self):
        frequency_dictionary = {}
        for word in self.text:
            if word in frequency_dictionary:
                frequency_dictionary[word] += 1
            else:
                frequency_dictionary[word] = 1
        return TextAnalyzer.order_frequency_by_value_and_word(self, frequency_dictionary)

    def prepare_text_for_analysis_from_file(self):
        TextAnalyzer.remove_stopwords(self)
        TextAnalyzer.remove_word_with_single_charatcter(self)

    def remove_stopwords(self):
        self.text = list(filter(None, [word for word in self.text if word not in self.stopwords]))

    def remove_word_with_single_charatcter(self):
        self.text = list(filter(None, [word for word in self.text if len(word) != 1]))

    def remove_punctuation_from_line(self, line):
        return line.translate(str.maketrans(self.punctuation))

    def order_frequency_by_value_and_word(self, dict_of_words):
        return_key_from_item = lambda item: item[0]
        dict_of_words = dict(sorted(dict_of_words.items(), key=return_key_from_item))

        return_values_from_item = lambda item: item[1]
        return dict(sorted(dict_of_words.items(), key=return_values_from_item, reverse=True))

    def list_of_words_from_file(self, file_name):
        list_of_stopwords = []
        with open(file_name) as file:
            for line in file:
                line_without_puntactions = TextAnalyzer.remove_punctuation_from_line(self, line)
                list_of_stopwords.extend(line_without_puntactions.strip().lower().split(' '))
        return list_of_stopwords

    def text_frequency_of_composite_words(self):
        dict_pair_words_frequency = {}

        for i in range(len(self.text) - 1):
            composite_words = self.text[i] + "," + self.text[i + 1]
            if composite_words in dict_pair_words_frequency:
                dict_pair_words_frequency[composite_words] += 1
            else:
                dict_pair_words_frequency[composite_words] = 1

        dict_pair_words_filtered = TextAnalyzer.filter_frequency_dict_by_limit(self, dict_pair_words_frequency)

        return TextAnalyzer.order_frequency_by_value_and_word(self, dict_pair_words_filtered)

    def filter_frequency_dict_by_limit(self, dict_composite_words):
        return {key: value for key, value in dict_composite_words.items() if value >= self.limit_frequency}


if __name__ == '__main__':
    #testing command
    #unittest.main()

    text, stopwords, input_frequency = sys.argv[1:]
    start_time = time.time()
    text_analyzer = TextAnalyzer(text, stopwords, input_frequency)
    text_analyzer.prepare_text_for_analysis_from_file()
    frequency_analysis_of_words = text_analyzer.text_frequency_of_words()
    text_analyzer.save_frequency_into_file('output.txt', frequency_analysis_of_words)
    frequency_analysis_of_composite_words = text_analyzer.text_frequency_of_composite_words()
    text_analyzer.save_frequency_into_file('compositeOutput.txt', frequency_analysis_of_composite_words)
    print((time.time() - start_time))
