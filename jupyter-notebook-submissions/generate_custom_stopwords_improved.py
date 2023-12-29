from create_index import create_index

def generate_custom_stopwords_improved(training_qrels, original_documents, run):
    qrels = training_qrels.qrels_data.values.tolist()

    queryIdIndex = 0
    docIdIndex = 2
    relevanceIndex = 3

    # Filter relevant documents
    relevant_documents = [item for item in qrels if item[relevanceIndex] == 1]

    # Filter relevant retrieved documents
    relevant_retrieved_documents = []
    for item in relevant_documents:
        query_id, doc_id = item[queryIdIndex], item[docIdIndex]
        is_document_retrieved_in_top_10 = doc_id in run.get_top_documents(query_id, 10)

        if is_document_retrieved_in_top_10:
            relevant_retrieved_documents.append(doc_id)

    relevant_retrieved_documents_list = []

    for document in list(original_documents):
        if document.doc_id in relevant_retrieved_documents:
            relevant_retrieved_documents_list.append(document)

    index_from_relevant_retrieved = create_index(relevant_retrieved_documents_list, {'stopwords': None, 'stemmer': None})

    lexicon = index_from_relevant_retrieved.getLexicon()
    term_frequencies = [(term, le.getFrequency()) for term, le in lexicon]
    sorted_term_frequencies = sorted(term_frequencies, key=lambda x: x[1], reverse=True)

    fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
    
    for stopword_list_length in fibonacci_numbers:
    
        file_path = f"./stopwordlists/stopwords_from_relevant_retrieved_{stopword_list_length}.txt"

        with open(file_path, 'w') as file:
                file.write("")

        with open(file_path, 'a') as file:
                for term, le in sorted_term_frequencies[:stopword_list_length]:
                    string_to_append = f"{term}\n"
                    file.write(string_to_append) 