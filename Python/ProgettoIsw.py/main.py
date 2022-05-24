import sys
import string
import time
class TextAnalyzer():

    def __init__(self, text_file_name, stopword_file_name, limit_frequency):
        self.punctuation = {char: ' ' for char in list(string.punctuation)}
        self.text = TextAnalyzer._list_of_words_from_file(self, text_file_name)
        self.stopwords = list(set(TextAnalyzer._list_of_words_from_file(self, stopword_file_name)))
        self.limit_frequency = limit_frequency



    def save_frequency_into_file(self,output_file_name):
        frequency_dictionary = TextAnalyzer.text_fequency(self)
        with open(output_file_name, 'w') as output_file:
            for item in frequency_dictionary.items():
                output_file.write(str(item[0]) + ','+str(item[1])+'\n')

    def save_frequency_into_file_pair(self, output_file_name):
        frequency_dictionary = TextAnalyzer.composite_words_from_text(self)
        with open(output_file_name, 'w') as output_file:
            for item in frequency_dictionary.items():
                output_file.write(str(item[0]) + ',' + str(item[1]) + '\n')

    def text_fequency(self):
        frequency_dictionary = {}
        for word in self.text:
            if word in frequency_dictionary:
                frequency_dictionary[word] +=1
            else:
                frequency_dictionary[word] = 1
        return_values_from_item= lambda item: item[1]
        return dict(sorted(frequency_dictionary.items(), key=return_values_from_item,reverse=True))


    def prepare_text_for_analysis_from_file(self):
        #TextAnalyzer._remove_punctuation(self)
        TextAnalyzer._remove_stopwords(self)

    def _remove_stopwords(self):
        self.text = list(filter(None ,[  word for word in self.text if word not in self.stopwords]))

    def _remove_punctuation_from_line(self ,line):
        return line.translate(str.maketrans( self.punctuation))

    def _list_of_words_from_file(self, file_name):
        list_of_stopwords = []
        with open(file_name) as file:
            for line in file:
                line_without_puntactions = TextAnalyzer._remove_punctuation_from_line(self, line)
                list_of_stopwords.extend(line_without_puntactions.strip().lower().split(' '))
        return list_of_stopwords

    def composite_words_from_text(self):
        dict_pair_words_frequency = {}

        for i in range(len(self.text) - 1):
                composite_words = self.text[i] + "," + self.text[i+1]
                if composite_words in dict_pair_words_frequency:
                    dict_pair_words_frequency[composite_words] += 1
                else:
                    dict_pair_words_frequency[composite_words] = 1

        return_values_from_item = lambda item: item[1]
        dict_pair_words_filtered = TextAnalyzer.filter_items_dict_by_limit(self, dict_pair_words_frequency)
        return dict(sorted(dict_pair_words_filtered.items(), key=return_values_from_item, reverse=True))

    def filter_items_dict_by_limit(self, dict_composite_words):
        return {key: value for key,value in dict_composite_words.items() if value >= self.limit_frequency}



if __name__ == '__main__':

    text, stopwords, input_frequency = sys.argv[1:]
    text_analizer = TextAnalyzer(text,stopwords, input_frequency)
    #start = time.time()
    text_analizer.prepare_text_for_analysis_from_file()

    print(text_analizer.text_fequency())
    #print(time.time()-start)
    text_analizer.save_frequency_into_file('output.txt')

    print(string.punctuation)
    text_analizer.composite_words_from_text()
    text_analizer.save_frequency_into_file_pair('compositeOutput.txt')