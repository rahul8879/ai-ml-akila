# 🏗️ AI Text Chunking Strategies: A Deep Dive

This document outlines the different ways to break down PDF data (like Bajaj Finance Loan documents) for Large Language Models (LLMs) and Vector Databases.

---

## 1. Character-Based Chunking
The simplest form of splitting. It cuts text after a fixed number of characters regardless of the content.

* **Logic:** Uses a fixed-size window.
* **Best For:** Simple text files with no nested structure.
* **Parameters:**
    * `chunk_size`: Total characters per chunk (e.g., 1000).
    * `chunk_overlap`: Characters to "carry over" to the next chunk to maintain context (e.g., 200).
    * `separator`: The character used to split (default is `""`).

---

## 2. Recursive Character Chunking
The "Industry Standard" for LangChain. It tries to keep semantic units (paragraphs and sentences) together.

* **Logic:** It attempts to split by a list of characters in order: `["\n\n", "\n", " ", ""]`. It only moves to the next separator if the current chunk is still too large.
* **Best For:** Most PDFs and financial documents because it respects bullet points and paragraphs.

* **Parameters:**
    * `chunk_size`: Maximum characters allowed per chunk.
    * `chunk_overlap`: Important for keeping context between fragments.

---

## 3. Token-Based Chunking
Splits text based on "Tokens" (how the LLM actually "reads" text) rather than raw characters.

* **Logic:** Since 1000 characters $\approx$ 750 tokens, this ensures your data fits perfectly into an LLM's context window without being cut off mid-word.
* **Best For:** Staying within API limits and optimizing for models like GPT-4 or Gemini.
* **Parameters:**
    * `encoding_name`: The model's specific tokenizer (e.g., `cl100k_base` for OpenAI).
    * `chunk_size`: Measured in tokens.

---

## 4. Semantic Chunking
The most advanced "meaning-based" strategy. It ignores character counts and focuses on topic shifts.

* **Logic:** It uses **Embeddings** to calculate the "meaning distance" between sentences. When the distance exceeds a certain threshold, it creates a "breakpoint."

* **Best For:** Complex policies where one page might cover three different topics (e.g., Eligibility, Fees, and Legal).

### 🧪 Semantic Parameters (The "Sensitivity" Dial)
| Parameter | Description |
| :--- | :--- |
| `embeddings` | **Required.** The model used to "understand" the text meaning. |
| `breakpoint_threshold_type` | The math used to find the cut: `percentile`, `standard_deviation`, or `interquartile`. |
| `breakpoint_threshold_amount` | The sensitivity value. Higher = Fewer/Larger chunks. Lower = More/Smaller chunks. |

---

## 📉 Summary Comparison

| Strategy | Speed | Context Quality | Complexity |
| :--- | :--- | :--- | :--- |
| **Character** | ⚡ Fast | ❌ Poor | Low |
| **Recursive** | ✅ Fast | ⭐ Good | Medium |
| **Semantic** | 🐢 Slow | 🏆 Excellent | High |

---

## 💡 Recommendation for Bajaj Finance PDFs
For **Personal Loan Eligibility** documents, start with **Recursive Character Chunking** (Size: 1000, Overlap: 200). If the AI starts mixing up different rules, upgrade to **Semantic Chunking** using the `percentile` threshold at 95% to ensure topic purity.