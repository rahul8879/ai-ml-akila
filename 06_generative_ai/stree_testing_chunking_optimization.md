# 📘 Module: Advanced Chunking & RAG Optimization

In Retrieval-Augmented Generation (RAG), **Chunking** is the process of breaking down large documents into smaller, meaningful units. If your chunking is bad, your LLM will hallucinate, no matter how good the model is.

---

## 1. The "Information Density" Trade-off
Every chunking strategy must balance two competing forces:

| Metric | Small Chunks (100-400 chars) | Large Chunks (1000-2000 chars) |
| :--- | :--- | :--- |
| **Precision** | 🎯 High (Finds exact sentences) | 📉 Low (Retrieves "noisy" extra text) |
| **Context** | 📉 Low (Loses the "Subject") | 🎯 High (Keeps related rules together) |
| **Use Case** | Fact-checking, Names, Dates. | Legal, Finance, Complex Logic. |

---

## 2. Why "Recursive" is the Industry Standard
Unlike a "Fixed" splitter that cuts text like a pair of scissors (often mid-word), **Recursive Character Splitting** works like a **Tree Hierarchy**:
1. Try to split by **Double Newline** (`\n\n`) -> Keeps Paragraphs.
2. If too big, split by **Single Newline** (`\n`) -> Keeps Sentences.
3. If still too big, split by **Spaces** (` `) -> Keeps Words.

---

## 3. The Anatomy of a "Stress Test"
A Stress Test is a controlled experiment to find the **"Breaking Point"** of your data retrieval.

### Key Metrics to Analyze:
* **Context Fracture:** Does the chunk contain the "Answer" but lose the "Question"? (e.g., "Min Salary: ₹25k" exists, but "Bajaj Personal Loan" is missing).
* **Sentence Mutilation:** Check if the splitter cut a sentence in half at the start/end of a chunk.
* **Overlap Efficiency:** Is your overlap providing "Glue" or just wasting expensive Database storage?

---

## 4. The "Overlap" Strategy: Contextual Glue
Overlap is not just duplicate data; it is the **bridge** between ideas.
* **0% Overlap:** High risk of losing data at the edges.
* **10-15% Overlap:** Ideal for most Financial/Technical PDFs.
* **25%+ Overlap:** High redundancy; may cause the LLM to repeat itself.

---

## 5. Pro-Optimization: "Metadata Prepending"
When your stress test shows that small chunks lose context, don't just make the chunks bigger. Use **Metadata Prepending**:
> **Original Chunk:** "Interest rate is 10.5%."
> **Optimized Chunk:** "Product: Personal Loan | Bank: Bajaj | Section: Rates | Content: Interest rate is 10.5%."

---

## 🔗 External Resources for Deep Learning

### 🛠️ Hands-on Tutorials
* **[Greg Kamradt: 5 Levels of Text Splitting](https://github.com/FullStackRetrieval-com/RetrievalTutorials)**: The absolute best visual guide to every strategy from Character to Semantic.
* **[Pinecone: Chunking Strategies for LLMs](https://www.pinecone.io/learn/chunking-strategies/)**: A deep dive into the math of why chunking matters for Vector Databases.

### 📜 Technical Documentation
* **[LangChain: Text Splitters Concepts](https://python.langchain.com/docs/concepts/#text-splitters)**: Understand the base classes and logic behind the code you are writing.
* **[Unstructured.io: Preprocessing for RAG](https://unstructured.io/blog)**: Great articles on how to handle messy PDFs and tables which often break standard chunking.

### 🎥 Video Lectures
* **[DeepLearning.AI: LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)**: Short course by Andrew Ng and Harrison Chase covering document loading and splitting.