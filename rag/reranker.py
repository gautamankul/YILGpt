from llama_index.postprocessor.cohere_rerank import CohereRerank

def get_reranker():
    return CohereRerank(top_n=3)