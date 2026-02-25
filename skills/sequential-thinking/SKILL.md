---
name: sequential-thinking
description: Use this skill when encountering complex problems requiring step-by-step breakdown, multi-stage planning, debugging, or analysis with unclear scope. Invokes sequential-thinking MCP for iterative reasoning, revisions, and branching.
---

# Sequential Thinking Skill

## When to Use
Invoke if the task involves:
- Breaking down complex problems into steps
- Planning with potential revisions
- Debugging intricate issues
- Exploring design alternatives
- Any multi-step reasoning where scope evolves
- Trigger on code/planning files (globs **/*.md)

## Core Workflow
Call the `sequentialthinking` MCP tool iteratively:

1. **Start sequence**: Send initial thought with estimates.
{"thought": "Initial analysis...", "thoughtNumber": 1, "totalThoughts": 5, "nextThoughtNeeded": true}

2. **Continue/Revise**: Update based on prior output.
{"thought": "Building on step 1...", "thoughtNumber": 2, "totalThoughts": 6, "nextThoughtNeeded": true, "isRevision": false}

For revisions: Add `"isRevision": true, "revisesThought": 1`

3. **Branch if needed**: `"branchFromThought": 2, "branchId": "alt-path"`

4. **Conclude**: Set `"nextThoughtNeeded": false` when solved

Review server response (thought history, tool recs) before next call. Repeat until `nextThoughtNeeded: false`.