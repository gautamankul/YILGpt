from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.vector_stores.faiss import FaissVectorStore
import os

def build_index():
    # Get the directory where ingestion.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate up to the project root and into the 'data' folder
    data_path = os.path.join(current_dir, "..", "data")

    # Load documents
    # In E:\YILGpt\rag\ingestion.py

    # Update this line:
    documents = SimpleDirectoryReader(data_path, recursive=True).load_data()

    # Embedding model
    embed_model = OpenAIEmbedding(model="text-embedding-3-small")

    # Semantic chunking
    parser = SemanticSplitterNodeParser(
        buffer_size=1,
        breakpoint_percentile_threshold=95,
        embed_model=embed_model
    )

    nodes = parser.get_nodes_from_documents(documents)

    # FAISS vector store
    vector_store = FaissVectorStore(dim=1536)

    # Create index
    index = VectorStoreIndex(
        nodes,
        embed_model=embed_model,
        vector_store=vector_store
    )

    return index, nodes