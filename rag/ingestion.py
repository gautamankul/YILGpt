from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core import Settings
import faiss
import os


def build_index():
    # Get the directory where ingestion.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate up to the project root and into the 'data' folder
    data_path = os.path.join(current_dir, "..", "data")

    # Update this line:
    documents = SimpleDirectoryReader(data_path, recursive=True).load_data()

    # Hugging Face Embeddings
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")
    Settings.llm = None  # prevents OpenAI fallback
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

    parser = SemanticSplitterNodeParser(
        buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
    )

    nodes = parser.get_nodes_from_documents(documents)

    # Create FAISS index manually
    faiss_index = faiss.IndexFlatL2(384)

    vector_store = FaissVectorStore(faiss_index=faiss_index)

    index = VectorStoreIndex(nodes, embed_model=embed_model, vector_store=vector_store)

    return index, nodes
