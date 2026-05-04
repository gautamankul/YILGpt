# from llama_index.core.retrievers import VectorIndexRetriever, BM25Retriever, QueryFusionRetriever
from rag.ingestion import build_index
from llama_index.core.retrievers import VectorIndexRetriever, QueryFusionRetriever
from llama_index.retrievers.bm25 import BM25Retriever  # <--- New import path

index, nodes = build_index()

def get_retriever():

    vector_retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=5
    )

    bm25_retriever = BM25Retriever.from_defaults(
        nodes=nodes
    )

    retriever = QueryFusionRetriever(
        [vector_retriever, bm25_retriever],
        similarity_top_k=5,
        num_queries=2,
        mode="reciprocal_rerank"
    )

    return retriever