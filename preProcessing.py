from langchain_text_splitters import RecursiveCharacterTextSplitter
import re

def recursiveChunk(doc):
    tempChunk=[]
    splitter=RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=0,
    separators=["\n\n","."],
    is_separator_regex=False
    )

    chunks=splitter.create_documents([doc])



    for i,chunk in enumerate(chunks):
        c=chunk.page_content.strip('.')
        c=c.strip('|')
        c= re.sub(r'[^\S ]+', '', c)
        print('\n','\n','\n',c)
        tempChunk.append(c)
        #print(f"Chunk {i+1}:\n{chunk.page_content}\n")
    return tempChunk

