# Module 6: Generative AI

## Overview
This module introduces Large Language Models (LLMs) and generative AI techniques, with a focus on building practical applications using LangChain and Retrieval-Augmented Generation (RAG).

## Prerequisites
- Module 5: Deep Learning (understanding of transformers helpful)
- Module 1: Python Fundamentals
- An OpenAI API key (or compatible LLM provider)

## Learning Objectives
By the end of this module, you will be able to:
- Understand the architecture and capabilities of Large Language Models
- Use LangChain to build LLM-powered applications
- Apply prompt engineering techniques for better results
- Load and process documents for use with LLMs
- Split documents into chunks suitable for retrieval
- Build a Retrieval-Augmented Generation (RAG) system

## Study Order

### LLM Foundations
1. **01_basic_of_llm.ipynb** - Introduction to LLMs, tokens, and the OpenAI API
2. **02_use_case.ipynb** - Common LLM use cases and application patterns

### Document Processing
3. **03_document_loader.ipynb** - Loading documents (PDFs, text, web pages) with LangChain
4. **04_document_splitter.ipynb** - Splitting documents into chunks for retrieval

## Additional Resources
- **notebook/M4 L1 Introduction to Retrieval.pdf** - Overview of retrieval concepts
- **notebook/M4 L4 Document Splitters and Chunkers.pdf** - In-depth guide to chunking strategies
- **notebook/langchain_prompt_engineering_v2.pdf** - Prompt engineering techniques
- **notebook/prompt_template.pdf** - LangChain prompt templates reference
- **notebook/RAG_architecture.pages** - RAG system architecture overview
- **notebook/langchain_lagacy_code.pdf** - LangChain legacy code reference

## Key Concepts to Master
- Tokens, context windows, and model limits
- Prompt engineering (zero-shot, few-shot, chain-of-thought)
- Embeddings and vector stores
- Document loaders and text splitters
- Retrieval-Augmented Generation (RAG) pipeline
- LangChain components: chains, retrievers, and agents

## Setup
```bash
pip install langchain langchain_community openai pymupdf pypdf
```

Set your API key before running notebooks:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Next Module
Ready to deploy your models? Move to **Module 7: MLOps** to learn about production deployment, monitoring, and CI/CD for ML systems.
