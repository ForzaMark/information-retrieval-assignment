import pyterrier as pt

def create_model(index):
    return pt.BatchRetrieve(index, wmodel="BM25")