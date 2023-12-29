from tira.third_party_integrations import ir_datasets
import pyterrier as pt

def load_dataset(training_dataset):
    queries = pt.io.read_topics(ir_datasets.topics_file(training_dataset), format='trecxml')

    dataset = ir_datasets.load(training_dataset)
    return {'documents': dataset.docs_iter(), 'queries': queries, 'topics': dataset.queries_iter()}