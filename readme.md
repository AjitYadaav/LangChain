# LangChain Learning

This repository contains my hands-on learning of **LangChain**, one component at a time. Every topic includes both theoretical understanding and practical implementation using Python.

---

# What is LangChain?

LangChain is an open-source framework that simplifies the development of applications powered by Large Language Models (LLMs).

It provides reusable building blocks that help developers connect LLMs with prompts, external data sources, memory, tools, and agents, making it easier to build real-world AI applications such as chatbots, question-answering systems, RAG pipelines, and AI assistants.

---

# Why LangChain?

Working directly with an LLM API is sufficient for simple tasks like text generation.

However, real-world AI applications often require much more than just generating text. For example:

- Maintaining conversation history
- Reading documents (PDFs, databases, websites)
- Retrieving relevant information (RAG)
- Calling external tools or APIs
- Executing multi-step workflows
- Building autonomous AI agents

LangChain provides abstractions and components that make these tasks easier to implement and maintain.

---

# LangChain Components

This repository will cover the major components of LangChain.

- ✅ Models
- ⏳ Prompts
- ⏳ Chains
- ⏳ Memory
- ⏳ Indexes (Retrievers & Vector Stores)
- ⏳ Agents

---

# 1. Models

Models are the core component of LangChain. They are responsible for generating or processing information using AI models.

LangChain mainly works with two categories of models:

- **Language Models**
- **Embedding Models**

---

## 1.1 Language Models

Language Models generate human-like text based on the given input.

Examples:

- Chatbots
- Question Answering
- Summarization
- Translation
- Content Generation

Language Models can be further divided into two types:

### LLMs (Large Language Models)

LLMs accept a single text prompt and generate a text response.

Example:

```
Prompt
↓

LLM

↓

Generated Text
```

Example implemented in this repository:

```
01-Models/
    └── 01-LLMs/
        └── 1_llm_gemini.py
```

---

### Chat Models

Chat Models are designed for conversations.

Instead of a single text prompt, they work with messages such as:

- System Message
- Human Message
- AI Message

Example:

```
System
↓

Human

↓

AI Response
```

Examples implemented:

```
01-Models/
    └── 02-ChatModels/
        ├── Gemini
        ├── Hugging Face API
        └── Hugging Face Local Model
```

---

## Providers Used

In this repository I experimented with multiple model providers.

### Open-source Models

- TinyLlama (Local)
- Hugging Face Models

These models can be downloaded and executed locally without purchasing an API.

---

### Closed-source Models

Examples include:

- OpenAI GPT
- Anthropic Claude
- Google Gemini

The implementation in LangChain is almost identical. The primary difference is that closed-source models require an API key and typically involve usage-based pricing.

For demonstration, this repository uses **Google Gemini API** and **Hugging Face** models.

---

## 1.2 Embedding Models

Embedding Models do **not generate text**.

Instead, they convert text into high-dimensional numerical vectors that capture semantic meaning.

Embedding models are widely used in:

- Semantic Search
- Recommendation Systems
- Similarity Search
- Retrieval-Augmented Generation (RAG)
- Vector Databases

> **Note:** Embedding Models will be explored in a later section of this repository.

---

# Technologies Used

- Python
- LangChain
- Hugging Face
- Google Gemini
- Transformers

---

# Learning Progress

| Component | Status |
|-----------|--------|
| Models | ✅ Completed |
| Prompts | ⏳ |
| Chains | ⏳ |
| Memory | ⏳ |
| Indexes | ⏳ |
| Agents | ⏳ |

---

# Repository Goal

The objective of this repository is to document my complete LangChain learning journey—from understanding the fundamentals to building advanced applications such as Retrieval-Augmented Generation (RAG), AI Agents, and conversational AI systems.