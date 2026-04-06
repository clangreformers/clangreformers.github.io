# Clang Reformers Repository Agent Skill

This skill defines the operational principles for managing the **clangreformers.github.io** repository. It specializes in multilingual Jekyll content related to Chinese language history and character studies.

## Core Responsibilities

1. **Multilingual Content Synchronization**:
   - Ensure every post or page has a corresponding version in English (`.md`), Chinese-Simplified (`-cn.md`), and Chinese-Traditional (`-tw.md`).
   - Maintain frontmatter consistency across language versions (e.g., `layout`, `ref`, `lang`, `sidebar`).

2. **Jekyll Structure Compliance**:
   - Posts are stored in `_posts/` with the filename format `YYYY-MM-DD-title-lang.md`.
   - Data files in `_data/` (e.g., `navigation.yml`) must be updated when new sections are added.
   - Layouts and includes (like `timeline-widget.html`) should be used for common UI elements.

3. **Character Studies (Shuowen)**:
   - Manage data in `dictionaries/` and `glossary/`.
   - Use scripts in `scripts/` for data extraction and processing where applicable.

4. **Self-Reflection & Improvement**:
   - After every significant task, update the `knowledge.json` file in the `.agent/` directory with new findings, user preferences, and corrected errors.
   - Refer to `knowledge.json` at the start of every session to align with the latest "learned" rules.

## Standard Patterns

- **Language Codes**: `en` (English), `cn` (Simplified Chinese), `tw` (Traditional Chinese).
- **Frontmatter**:
  - `ref`: A unique identifier to link different language versions of the same page.
  - `lang`: The language of the document.
- **Image Assets**: Store in `assets/images/` and use root-relative paths (e.g., `/assets/images/banner.png`).

## Self-Correction Loop

- **Analyze**: Review the user's feedback (e.g., "Use 16/10 aspect ratio instead of 16/9").
- **Codify**: Add the preference to `knowledge.json`.
- **Apply**: Ensure all subsequent changes follow the new preference.
