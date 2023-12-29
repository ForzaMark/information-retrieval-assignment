import os
import pyterrier as pt
 
import math

def generate_custom_stopwords(documents):
    indexer = pt.IterDictIndexer(
        "/tmp/index_for_stopwords", 
        overwrite=True,
        stemmer=None,
        stopwords=None,
        meta={'docno': 100, 'text': 20480},
    )
    index_ref = indexer.index(({'docno': i.doc_id, 'text': i.text} for i in documents))
    index = pt.IndexFactory.of(index_ref)


    stopword_list_length = 550
    print("stopword list length:", stopword_list_length)
    lexicon = index.getLexicon()
    
    
    term_frequencies = [(term, le.getFrequency()) for term, le in lexicon]
    term_frequencies_normalised = [(term, -math.log(le.getFrequency()/len(lexicon))) for term, le in lexicon]

    # postings = index.getDirectIndex().getPostings(term)
    # df_term = postings.getDocumentFrequency()

    sorted_term_frequencies = sorted(term_frequencies, key=lambda x: x[1], reverse=True)
    sorted_term_frequencies_normalised = sorted(term_frequencies_normalised, key=lambda x: x[1])

    file_path = './stopwordlists/custom_stopwords.txt'
    file_path2 = './stopwordlists/custom_stopwords_normalised.txt' 

    reset_file(file_path)
    reset_file(file_path2)

    with open(file_path, 'a') as file:
        for term, le in sorted_term_frequencies[:stopword_list_length]:
            string_to_append = f"{term}\n"
            file.write(string_to_append)   

    with open(file_path2, 'a') as file:
        for term, le in sorted_term_frequencies_normalised[:stopword_list_length]:
            string_to_append = f"{term}\n"
            file.write(string_to_append)   

def reset_file(file_path):
    with open(file_path, 'w') as file:
        file.write("")
