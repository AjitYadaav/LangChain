# Models in LangChain

> The Models component is one of the core building blocks of LangChain. It provides a unified interface to interact with different Large Language Models (LLMs), Chat Models, and Embedding Models from various providers such as OpenAI, Google Gemini, Anthropic, and Hugging Face.

---

# Table of Contents

1. Introduction
2. Why Models?
3. Types of Models
4. LLMs
5. Chat Models
6. Embedding Models
7. Closed Source vs Open Source Models
8. Hugging Face
9. Embedding and Semantic Search
10. Model Selection Guide
11. Important LangChain Methods
12. Folder Structure
13. Common Mistakes
14. Interview Questions
15. Key Takeaways

---

# 1. Introduction

A language model is the intelligence behind every Generative AI application.

Without a model, LangChain cannot generate text, answer questions, summarize documents, create embeddings, or perform reasoning.

LangChain itself **does not contain an AI model**.

Instead, it provides a common interface to communicate with models developed by different AI companies.

```
Application
      │
      ▼
 LangChain
      │
      ▼
 Language Model
      │
      ▼
 Response
```

---

# 2. Why Models?

Suppose we directly used every provider.

```
OpenAI API
Google API
Anthropic API
Hugging Face API
```

Every provider has a different SDK, different syntax, and different response format.

LangChain solves this by providing one common interface.

Example:

```python
model.invoke("Hello")
```

Whether the model is GPT, Gemini, Claude, or another provider, the programming experience remains nearly identical.

---

# 3. Types of Models

LangChain mainly provides three categories of models.

```
Models
│
├── LLMs
├── Chat Models
└── Embedding Models
```

---

# 4. LLMs

## Definition

LLMs generate text from text prompts.

Input:

```
Text
```

Output:

```
Generated Text
```

Example:

```python
llm.invoke("What is AI?")
```

Output:

```
Artificial Intelligence is...
```

### Common Models

- GPT
- Gemini
- Claude

### Use Cases

- Text generation
- Summarization
- Translation
- Question Answering
- Story generation

---

# 5. Chat Models

## Definition

Chat Models are optimized for conversational applications.

Unlike traditional LLMs, they accept structured messages.

```
System Message

↓

Human Message

↓

AI Message
```

Example:

```python
response = model.invoke("What is the capital of India?")
```

Response:

```python
AIMessage(
    content="New Delhi..."
)
```

### AIMessage contains

- content
- metadata
- token usage
- finish reason

### Use Cases

- Chatbots
- AI Assistants
- Customer Support
- RAG Applications
- AI Agents

---

# 6. Embedding Models

## Definition

Embedding Models convert text into numerical vectors.

Input

```
Text
```

↓

Embedding Model

↓

```
[0.13, -0.42, ...]
```

Output = Vector

Unlike LLMs, embedding models **do not generate text**.

Their job is to capture the semantic meaning of text.

---

## Why Embeddings?

Computers cannot directly compare the meaning of two sentences.

Instead, they compare vectors.

Example:

```
"What is AI?"

↓

Embedding

↓

[0.21, -0.44, ...]
```

---

## LangChain Methods

### embed_query()

Used for a single query.

```python
embedding.embed_query(
    "What is AI?"
)
```

Returns

```
One Vector
```

---

### embed_documents()

Used for multiple documents.

```python
embedding.embed_documents(
    [
        "Delhi...",
        "Paris...",
        "Tokyo..."
    ]
)
```

Returns

```
List of Vectors
```

---

# 7. Closed Source vs Open Source Models

## Closed Source

Examples

- OpenAI GPT
- Google Gemini
- Anthropic Claude

Characteristics

- API access only
- Model weights are not publicly available
- Managed by the provider

---

## Open Source

Examples

- Llama
- Gemma
- Phi
- Mistral
- TinyLlama

Characteristics

- Model weights are publicly available
- Can run locally
- Can be fine-tuned

---

# 8. Hugging Face

Hugging Face is **not a model**.

It is a platform that hosts thousands of AI models.

Think of it as GitHub for machine learning models.

```
Hugging Face

↓

Llama

Gemma

Phi

TinyLlama

Mistral

...
```

Models can be

- Downloaded
- Run locally
- Accessed using the Inference API

---

# 9. Embeddings and Semantic Search

This is the foundation of Retrieval-Augmented Generation (RAG).

Workflow:

```
Documents

↓

Embedding Model

↓

Document Vectors

↓

User Query

↓

Query Vector

↓

Cosine Similarity

↓

Most Relevant Document
```

Example

Query:

```
Tell me about MS Dhoni
```

Document similarity scores

```
Virat Kohli → 0.64

MS Dhoni → 0.75 ✅

Sachin → 0.61

Rohit → 0.62

Bumrah → 0.61
```

The document with the highest similarity score is retrieved.

---

# 10. Model Selection Guide

| Task | Model Type |
|-------|------------|
| Generate text | LLM |
| Build chatbot | Chat Model |
| Semantic search | Embedding Model |
| RAG | Chat Model + Embedding Model |
| Vector Database | Embedding Model |

---

# 11. Important LangChain Methods

### LLM

```python
invoke()
```

---

### Chat Model

```python
invoke()
```

Returns

```
AIMessage
```

---

### Embedding Model

```python
embed_query()
```

```python
embed_documents()
```

---

# 12. Folder Structure

```
01_Models
│
├── 1.LLMs
├── 2.ChatModels
├── 3.EmbeddingModels
└── assets
```

---

# 13. Common Mistakes

❌ LangChain contains its own LLM.

✔ LangChain is a framework.

---

❌ Hugging Face is a model.

✔ Hugging Face is a model hub.

---

❌ Embedding models generate answers.

✔ They generate vectors.

---

❌ Cosine Similarity understands language.

✔ It only compares vectors.

The semantic understanding comes from the embedding model.

---

# Interview Questions

### Q1. What is the Models component in LangChain?

The Models component provides a unified interface to interact with different AI models (LLMs, Chat Models, and Embedding Models). It abstracts provider-specific APIs, allowing developers to switch between models like OpenAI, Gemini, Anthropic, or Hugging Face with minimal code changes.

---

### Q2. Difference between LLMs and Chat Models?

| LLMs | Chat Models |
|------|-------------|
| Accept plain text as input | Accept structured messages (System, Human, AI) |
| Mainly designed for text completion | Designed for conversational AI |
| Output is generated text | Output is conversational responses with context |
| Example: GPT-3 Completion | Example: ChatGPT, Gemini Chat |

---

### Q3. What is an Embedding?

An embedding is a dense numerical vector that represents the semantic meaning of text. Similar texts produce similar vectors, making it easier for computers to compare meanings instead of exact words.

---

### Q4. Why do we need Embeddings?

Embeddings allow computers to measure semantic similarity between texts. They are used for:
- Semantic Search
- Document Retrieval
- Recommendation Systems
- Clustering
- RAG applications

---

### Q5. Difference between `embed_query()` and `embed_documents()`?

| `embed_query()` | `embed_documents()` |
|-----------------|---------------------|
| Converts a single query into an embedding | Converts multiple documents into embeddings |
| Used during search | Used while indexing documents |
| Returns one vector | Returns a list of vectors |

---

### Q6. Explain Semantic Search.

Semantic Search retrieves information based on the **meaning** of the query rather than exact keyword matches. It compares embeddings of the query with document embeddings and returns the most semantically similar documents.

---

### Q7. What is Cosine Similarity?

Cosine Similarity is a metric used to measure how similar two vectors are by calculating the cosine of the angle between them.

- Value = **1** → Identical meaning
- Value = **0** → Unrelated
- Value = **-1** → Opposite direction

It is widely used to find the most relevant documents in vector databases.

---

### Q8. Difference between Closed Source and Open Source Models?

| Closed Source | Open Source |
|---------------|-------------|
| Model weights are private | Model weights are publicly available |
| Accessed through APIs | Can be downloaded and run locally |
| Limited customization | Can be fine-tuned and modified |
| Examples: GPT-4, Gemini, Claude | Examples: Llama, Mistral, Falcon |

---

### Q9. Why is Hugging Face popular?

Hugging Face is a platform that hosts thousands of pre-trained AI models, datasets, and ML tools. It enables developers to easily discover, download, fine-tune, and deploy models, making AI development faster and more accessible.

---

### Q10. Why are embeddings required in RAG?

RAG retrieves relevant documents before generating a response. Since vector databases store embeddings rather than raw text, the user's query is converted into an embedding and compared with stored document embeddings. The most similar documents are retrieved and passed to the LLM to generate an accurate answer.

---

# Key Takeaways

- LangChain provides a unified interface to interact with AI models.
- LLMs generate text by predicting the next token.
- Chat Models are optimized for conversational interactions.
- Embedding Models convert text into semantic vectors.
- Embeddings power semantic search and document retrieval.
- Cosine Similarity measures similarity between embeddings.
- Hugging Face is a popular platform for AI models and datasets.
- RAG uses embeddings to retrieve relevant context before generation.

---

## Revision Checklist

- [x] I can explain the Models component.
- [x] I know the difference between LLMs, Chat Models, and Embedding Models.
- [x] I understand embeddings.
- [x] I understand semantic search.
- [x] I know how cosine similarity works.
- [x] I can explain why embeddings are required in RAG.
- [x] I can explain closed-source vs open-source models.

