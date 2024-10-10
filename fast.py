from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain.text_splitter import RecursiveCharacterTextSplitter

embed_model = FastEmbedEmbeddings(model_name="BAAI/bge-base-en-v1.5")

def semChunk(data):
  text_splitter = RecursiveCharacterTextSplitter(
  chunk_size=1000,
  chunk_overlap=0,
  length_function=len,
  is_separator_regex=False,
  separators=['.']
)
  
 
  naive_chunks = text_splitter.split_text(data)
  #print(naive_chunks)
  semantic_chunker = SemanticChunker(embed_model, breakpoint_threshold_type="percentile")
  print("Sematic chunking is over")
  batch_size = 32  # or any appropriate number based on system capacity
  # Chunk naive chunks into smaller batches for processing
  for i in range(0, len(naive_chunks), batch_size):
    chunk_batch = naive_chunks[i:i+batch_size]
    semantic_chunks = semantic_chunker.create_documents(chunk_batch)
    print(f"Processed batch {i//batch_size + 1}")

  print("Stored in semantic_chunks")
  chunks=[]
  for semantic_chunk in semantic_chunks:
    print("loop is taking place")
    chunks.append(semantic_chunk.page_content)
    #print(semantic_chunk,"\n\n\n")
  #print(chunks)
  return chunks
