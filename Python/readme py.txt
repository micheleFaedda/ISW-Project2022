importiamo la libreria string perchè sfrutteremo string.punctuation che ha tutti i caratteri di punteggiatura
importiamo sys che contiene gli unitTest
importiamo time per calcolare l'efficienza nei test

definiamo classe TextAnalyzer che ha il metodo costrutture che prende in input:
nome del file da analizzare, nome del file con le stopwords, limite di frequenza

come attributi la classe avrà:
puntuaction -> che sarà un dizionario che avrà una chiave per ogni punteggiatura (presa dalla lib string) e valore inizializzato a carattere vuoto
text -> lista che conterrà tutte le parole del testo
stopwords -> lista che conterrà tutte le stopwords
limit_frequency -> limite di frequenza per filtrare

save_frequency_into_file -> dato in input un nome file e un dizionario contenente chiave la parola e valore la frequenza, per tutti gli items del dizionario scriverà su file in output le coppie della forma "chiave,frequenza\n" dove la chiave può essere sia "parola" sia "parola1,parola2" in quando viene utilizzata per generare tutt'e due i file di output.

text_frequency_of_words -> per ogni parola nell'attributo di classe text andrà a calcolarmi la sua frequenza, restituendomi in output un dizionario ordinato per frequenza e a parità per parola, che conterrà le coppie parole - frequenza.

prepare_text_for_analysis_from_file -> si occupa di rimuovere le stopwords dal testo e le parole con un singolo carattere.

remove_stopwords -> filtra tutto il testo togliendo le stopwords e castando a list

remove_word_with_single_charatcter -> filtra tutto il testo togliendo le parole con singolo carattere e castando a list

remove_punctuation_from_line -> per ogni linea del testo sostituisce con uno spazio vuoto i caratteri di punteggiatura

order_frequency_by_value_and_word -> prende in input un dizionario di parole e crea in output un dizionario ordinato per frequenza e a parità per parola

list_of_words_from_file -> apre il file passato in ingresso, per ogni linea rimuove la punteggiatura dalla linea e ed estende la lista che si restituisce in output togliendo spazi vuoti e trasformando in minuscolo.

text_frequency_of_composite_words -> per ogni parola del testo le prendo a coppie, se la parola è già stata inserita nel dizionario di parole composte allora aumento la frequenza di 1, altrimenti inserisco 1.
Poi creo un dizionario di coppie filtrandole per il limite superiore e dopodichè lo restituisco ordinato per valore e a parità per parola.

filter_frequency_dict_by_limit -> prende in input un dizionario di parole composte e restituisce un dizionario con le parole composte che hanno una frequenza superiore al limite