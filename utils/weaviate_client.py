import weaviate
from weaviate.classes.config import Property, DataType, Configure, Tokenization
import os 


docs = """
    I am working on a masters in software engineering
"""

grcp_host = os.environ["GRPC_HOST"]
http_host = os.environ["HTTP_HOST"]

# client = weaviate.connect_to_custom(
#     grpc_host=grcp_host,         
#     http_host=http_host,
#     http_port=80,
#     http_secure=False,
#     grpc_port=50051,
#     grpc_secure=False
# )

collection_name = "Newsletters"
# ollama_api = "http://ollama:11434"
# model = "nomic-embed-text"


def add_to_store(article, date, topic):
    with weaviate.connect_to_custom(
        grpc_host=grcp_host,         
        http_host=http_host,
        http_port=80,
        http_secure=False,
        grpc_port=50051,
        grpc_secure=False
    ) as client:
        test = client.collections.get(collection_name)
        test.data.insert(properties={"date": date, "text": article, "topic": topic})
        



# client.close()


# def episodic_recall(query, collection_name):
    
#     # Load Database Collection
#     test = client.collections.get(collection_name)

#     # Hybrid Semantic/BM25 Retrieval
#     memory = test.query.hybrid(
#         query=query,
#         alpha=0.5,
#         limit=1,
#     )
    
#     return memory


# query = "Talking about my masters"

# collection_name = "john"

# try:
#     recall = episodic_recall(query, collection_name)
#     print(recall.objects[0].uuid)


#     client.close()
# except Exception as e:
#     print("ERROR")
#     print(e)
#     client.close()



