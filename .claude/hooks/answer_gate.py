"""Inject answer questions on UserPromptSubmit."""
from gate_context import emit_context

if __name__ == "__main__":
    emit_context("UserPromptSubmit", "ANSWER_GATES.md")
