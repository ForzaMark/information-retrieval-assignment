import pyterrier as pt
import os

def create_index(documents, config, indexLocation=False):
    indexer = pt.IterDictIndexer(
        indexLocation if indexLocation else "/tmp/index", 
        overwrite=True, 
        meta={'docno': 100, 'text': 20480},
        stopwords=config['stopwords'],
        stemmer=config['stemmer']
    )
    index_ref = indexer.index(({'docno': i.doc_id, 'text': i.text} for i in documents))
    return pt.IndexFactory.of(index_ref)
