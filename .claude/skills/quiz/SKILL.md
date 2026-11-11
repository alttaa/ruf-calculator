---
name: quiz
description: Quiz Alex on RUF concepts or commands he has learned so far.
disable-model-invocation: true
argument-hint: "[topic, e.g. cards, slicing, venv, pytest]"
---

Quiz Alex on: $ARGUMENTS
(If no topic is given, pick from the "Learned" lines in docs/SESSION_LOG.md.)

- Ask ONE question at a time, 5 questions total, easy to harder.
- Use concrete values (e.g. "what does parse_card('Ks') return?") before abstract ones.
- Mix: predict-the-output, fix-the-bug, and terminal-command questions.
- After each answer: say right/wrong in one line, explain briefly, then ask the next.
- End with a score and the one concept worth reviewing.
