import pandas as pd
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter, 
    CharacterTextSplitter, 
    TokenTextSplitter
)

def compare_chunking_strategies(documents, chunk_size=1000, chunk_overlap=200):
    results = []
    
    # Define the strategies to test
    strategies = {
        "Recursive": RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        ),
        "Character": CharacterTextSplitter(
            separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap
        ),
        "Token": TokenTextSplitter(
            chunk_size=int(chunk_size/4), chunk_overlap=int(chunk_overlap/4)
        )
    }

    for name, splitter in strategies.items():
        chunks = splitter.split_documents(documents)
        
        # Record stats for optimization analysis
        results.append({
            "Strategy": name,
            "Total Chunks": len(chunks),
            "Avg Chunk Length": sum(len(c.page_content) for c in chunks) / len(chunks),
            "Sample Chunk": chunks[0].page_content[:150] + "..." # Preview of the first chunk
        })

    # Return a DataFrame for easy comparison
    return pd.DataFrame(results)