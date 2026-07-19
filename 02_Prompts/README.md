# Prompts

## What is a Prompt?

A **prompt** is the input or instruction given to a Large Language Model (LLM) to generate a response.

It tells the model **what task to perform** and **how to perform it**.

**Example**

```text
Summarize the research paper "Attention Is All You Need."
```

---

# Why are Prompts Important?

The quality of an LLM's output depends heavily on the quality of the prompt.

A well-designed prompt helps:

- Produce more accurate responses.
- Reduce ambiguity.
- Control the response style.
- Specify output format.
- Improve reasoning and task completion.

---

# Prompt Flow

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

# Types of Prompts

## 1. Static Prompt

A static prompt is a fixed instruction sent directly to the LLM.

The user writes the complete prompt manually.

**Example**

```text
Summarize the paper "Attention Is All You Need."
```

### Workflow

```text
User
   │
   ▼
Prompt
   │
   ▼
LLM
   │
   ▼
Response
```

### Advantages

- Simple
- Easy to implement
- Good for quick testing

### Limitations

- No control over output style
- Depends entirely on how well the user writes the prompt
- Difficult to maintain in larger applications

---

## 2. Dynamic Prompt

A dynamic prompt is generated at runtime by combining a predefined template with user inputs.

Instead of writing the complete prompt, the user provides only the required information.

Example inputs:

- Research Paper
- Explanation Style
- Explanation Length

These values are inserted into a Prompt Template before sending it to the LLM.

### Workflow

```text
User Inputs
        │
        ▼
Prompt Template
        │
        ▼
Generated Prompt
        │
        ▼
LLM
        │
        ▼
Response
```

### Advantages

- Consistent prompt structure
- Better output quality
- Easier to maintain
- Scalable for real-world applications

---

# Prompt Components

A prompt generally consists of:

- Task
- Context
- Constraints
- Output Format

Example:

```text
Summarize the paper in 100 words using simple language.
```

Here,

- Task → Summarize
- Context → Research Paper
- Constraint → 100 Words
- Output Style → Simple Language

---

# PromptTemplate in LangChain

LangChain provides the `PromptTemplate` class to create reusable and dynamic prompts.

Instead of hardcoding prompts, placeholders are defined inside a template.

Example placeholders:

```text
{paper_input}
{style_input}
{length_input}
```

At runtime, LangChain replaces these placeholders with actual user inputs before sending the final prompt to the LLM.

---

# Prompting in LangChain

Basic invocation:

```python
result = model.invoke(user_input)
```

For dynamic prompting:

```text
User Inputs
      │
      ▼
PromptTemplate
      │
      ▼
Formatted Prompt
      │
      ▼
LLM
      │
      ▼
Generated Response
```

---

# Mini Projects

## 1. Static Prompt Demo

Built a simple research assistant where the user directly enters a prompt.

**Tech Stack**

- Streamlit
- LangChain
- Gemini API

Workflow

```text
User
   │
   ▼
Prompt
   │
   ▼
LangChain
   │
   ▼
Gemini
   │
   ▼
Response
```

---

## 2. Dynamic Prompt Demo

Built a research assistant using `PromptTemplate`.

The application allows users to select:

- Research Paper
- Explanation Style
- Explanation Length

These inputs are inserted into a prompt template before sending the request to Gemini.

Workflow

```text
User
      │
      ▼
Select Inputs
      │
      ▼
PromptTemplate
      │
      ▼
Formatted Prompt
      │
      ▼
Gemini
      │
      ▼
Generated Response
```

---

# LLM vs Chat Model

## LLM

Example:

```python
GoogleGenerativeAI
```

- Accepts plain text input
- Returns plain text output

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

Example:

```python
ChatGoogleGenerativeAI
```

- Works with messages
- Supports conversations
- Returns an AIMessage object

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

Although both interfaces can generate similar responses, **Chat Models are preferred** because they integrate naturally with Prompt Templates, LCEL, Chains, RAG, and Agents.

---

# What I Learned

- What a prompt is
- Importance of prompt engineering
- Static prompts
- Dynamic prompts
- PromptTemplate
- Prompt components
- Building Streamlit applications with LangChain
- Difference between LLMs and Chat Models
- Managing API keys using `.env`
- Working with virtual environments (`venv`)

---

# Key Takeaways

- Prompts determine how an LLM behaves.
- Better prompts generally produce better outputs.
- Static prompts are simple but less flexible.
- Dynamic prompts improve consistency and scalability.
- PromptTemplate is used to generate prompts dynamically.
- Chat Models are recommended for modern LangChain applications.

---

# Interview Questions

### What is a prompt?

A prompt is the instruction or input given to an LLM to generate a response.

---

### What is Prompt Engineering?

Prompt Engineering is the process of designing effective prompts to improve the quality and reliability of an LLM's output.

---

### What is the difference between a static prompt and a dynamic prompt?

A static prompt is fixed and written manually by the user.

A dynamic prompt is generated using a template and user-provided values.

---

### Why do we use PromptTemplate?

PromptTemplate allows developers to create reusable, maintainable, and consistent prompts by replacing placeholders with runtime values.

---

### What is the difference between an LLM and a Chat Model?

An LLM works with plain text input/output, while a Chat Model works with conversational messages and supports multi-turn interactions.

---

### Which interface should be preferred in LangChain?

For most modern applications, `ChatGoogleGenerativeAI` (or other chat models) should be preferred because it integrates well with Prompt Templates, LCEL, Chains, RAG, and Agents.

---

### What does `model.invoke()` do?

It sends the prompt to the model and returns the generated response.