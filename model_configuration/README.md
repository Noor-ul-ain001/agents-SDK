# 🚀 Agent Configuration Examples

This repository demonstrates **three levels of configuration** for Agents using the `agents` framework:

---

## 🔹 1. Global-level Configuration

Global config applies to the **entire application**.
All agents and runs use these defaults unless explicitly overridden.

```python
set_default_openai_client(external_client)
set_default_openai_api("chat_completions")

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")
result = Runner.run_sync(agent, "Hello")
```

✅ Use when you want **shared defaults** across the whole app.

---

## 🔹 2. Agent-level Configuration

The agent carries its **own model and instructions**.
This agent always uses the given model, regardless of runner or global config.

```python
agent = Agent(
    name="Assistant",
    instructions="Aap sirf Urdu mein jawab dein.",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",
        openai_client=client
    ),
)
result = Runner.run_sync(agent, "I am learning Agentic AI")
```

✅ Use when you want the agent to be **self-contained** with its own “locked” setup.

---

## 🔹 3. Runner-level Configuration

Configuration is passed at **run time** via `RunConfig`.
The agent itself has no model; the runner decides which one to use.

```python
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(name="Assistant", instructions="You are a helpful assistant")
result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)
```

✅ Use when you want to **swap models dynamically per run**.

---

## ⚖️ Configuration Hierarchy

1. **Agent-level config** → highest priority
2. **Runner-level config** → overrides global defaults
3. **Global config** → baseline for everything

---
⚖️ Priority Order

Agent-level config → Highest priority (always wins if defined).

Runner-level config → Used if agent doesn’t have its own model/settings.

Global config → Baseline defaults, used only when nothing else is specified.
