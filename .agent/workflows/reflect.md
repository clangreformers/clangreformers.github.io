---
description: Perform a self-reflection on the current session to update the agent's knowledge and instructions.
---

1. **Analyze Session History**
   - Review recent commands, file edits, and user feedback.
   - Identify recurring patterns, errors, or specific preferences expressed by the user.

2. **Extract Key Insights**
   - **Preference Update**: Check if the user specified a new style, format, or standard (e.g., "Use 16/10 aspect ratio").
   - **Error Correction**: Note any mistakes made by the agent that the user corrected (e.g., "The filename should have a -cn suffix").
   - **Pattern Discovery**: Observe common file locations or naming conventions used in this session.

3. **Update Knowledge Base**
   - Append new "Learned Lessons" to `knowledge.json`.
   - Update `preferences` or `common_patterns` in `knowledge.json`.

4. **Refine Skill Instructions**
   - If a learned lesson is foundational, update `SKILL.md` to reflect the new standard.

5. **Commit Knowledge**
   - Ensure `knowledge.json` and `SKILL.md` are saved to the repository.

6. **Summary of reflection**
   - Provide a brief summary of what was learned and updated for the user.
