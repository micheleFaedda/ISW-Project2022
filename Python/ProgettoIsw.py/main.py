import sys
import string
import time
class TextAnalyzer():

    def __init__(self, text_file_name, stopword_file_name):
        self.punctuation = {char: ' ' for char in list(string.punctuation)}
        self.text = TextAnalyzer._list_of_words_from_file(self, text_file_name)
        self.stopwords = list(set(TextAnalyzer._list_of_words_from_file(self, stopword_file_name)))



    def save_frequency_into_file(self,output_file_name):
        frequency_dictionary = TextAnalyzer.text_fequency(self)
        with open(output_file_name, 'w') as output_file:
            for item in frequency_dictionary.items():
                output_file.write(str(item[0]) + ','+str(item[1])+'\n')

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
                line_without_puntactions = TextAnalyzer._remove_punctuation_from_line(self,line)
                list_of_stopwords.extend(line_without_puntactions.strip().lower().split(' '))
        return list_of_stopwords

if __name__ == '__main__':

    text, stopwords, input_frequency = sys.argv[1:]
    text_analizer = TextAnalyzer(text,stopwords)
    #start = time.time()
    text_analizer.prepare_text_for_analysis_from_file()

    print(text_analizer.text_fequency())
    #print(time.time()-start)
    text_analizer.save_frequency_into_file('output.txt')
    print(string.punctuation)