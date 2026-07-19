# Prompts

## What is a Prompt?

A **prompt** is the input or instruction given to a Large Language Model (LLM) to generate a response.

It tells the model **what task to perform** and **how to perform it**.

**Example:**

```text
Summarize the research paper "Attention Is All You Need."
```

---

## Why are Prompts Important?

The quality of an LLM's output depends heavily on the quality of the prompt.

A well-written prompt can:
- Produce more accurate responses.
- Reduce ambiguity.
- Control the style and format of the output.
- Improve reasoning and task completion.

---

## Prompt Flow

```text
User
   │
   ▼
Prompt
   │
   ▼
LLM (Gemini / GPT / Claude)
   │
   ▼
Generated Response
```

---

## Prompt Types

### 1. Simple Prompt

A direct instruction to the model.

**Example**

```text
Explain the Transformer architecture.
```

---

### 2. Instruction Prompt

Specifies exactly what the model should do.

**Example**

```text
Summarize the following research paper in 5 bullet points.
```

---

### 3. Contextual Prompt

Provides additional context before asking a question.

**Example**

```text
You are an AI researcher.

Explain Attention Is All You Need to a beginner.
```

---

## Prompt Components

A prompt may contain:

- Task
- Context
- Constraints
- Output format

Example:

```text
Summarize the paper in 100 words using simple language.
```

Here,

- Task → Summarize
- Context → Research paper
- Constraint → 100 words
- Output Style → Simple language

---

# Prompting in LangChain

LangChain sends the prompt to an LLM or Chat Model.

Example:

```python
result = model.invoke(user_input)
```

where

```python
user_input = st.text_input("Enter your prompt")
```

The entered text becomes the prompt for the model.

---

# Mini Project

### Research Tool

Built a simple research assistant using:

- Streamlit
- LangChain
- Google Gemini API

Workflow

```text
User
   │
   ▼
Streamlit UI
   │
   ▼
User enters prompt
   │
   ▼
LangChain
   │
   ▼
Gemini 2.5 Flash
   │
   ▼
Generated Response
   │
   ▼
Displayed on Streamlit
```

---

# LLM vs Chat Model

## LLM

```python
GoogleGenerativeAI
```

- Takes plain text as input.
- Returns plain text as output.

```text
String
   │
   ▼
LLM
   │
   ▼
String
```

---

## Chat Model

```python
ChatGoogleGenerativeAI
```

- Works with messages.
- Supports conversations.
- Returns an AIMessage object.

```text
Human Message
System Message
AI Message
        │
        ▼
Chat Model
        │
        ▼
AI Message
```

Although both may produce similar responses, **Chat Models are preferred for modern LangChain applications** because they support conversations, system instructions, prompt templates, chains, RAG, and agents.

---

# What I Learned

- What a prompt is.
- Importance of prompt quality.
- Different prompt styles.
- Sending prompts to an LLM using LangChain.
- Building a Streamlit application powered by Gemini.
- Difference between LLM and Chat Model.
- Managing API keys using `.env`.
- Running projects inside a virtual environment (`venv`).

---

# Key Takeaways

- A prompt is the instruction given to an LLM.
- Better prompts generally produce better outputs.
- LangChain provides a simple interface to interact with LLMs.
- Streamlit can quickly build an interactive UI for LLM applications.
- Chat Models are recommended for most modern LangChain projects.

---

# Interview Questions

### What is a prompt?

A prompt is the input or instruction provided to an LLM to generate a response.

---

### Why are prompts important?

They determine the quality, relevance, and structure of the model's output.

---

### What is the difference between an LLM and a Chat Model?

An LLM works with plain text input/output, whereas a Chat Model works with conversational messages and supports multi-turn interactions.

---

### Which interface should be preferred in LangChain?

For modern applications, `ChatGoogleGenerativeAI` (or other chat models) is generally preferred because it integrates well with Prompt Templates, LCEL, Chains, RAG, and Agents.

---

### What does `model.invoke()` do?

It sends the input prompt to the model and returns the generated response.