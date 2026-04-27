# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses semantic versioning.

## [Unreleased]

- No unreleased changes.

## [0.2.3] - 2026-04-27

### Fixed

- Replaced bulk intake questions with guided one-question-at-a-time wizard flow.
- Made normal invocation sufficient when a transcript is attached or pasted.
- Simplified Claude Desktop plugin manifest for better validation.
- Removed unsupported frontmatter fields from Desktop-facing SKILL.md files.

### Changed

- Skill now shows progress during intake using Question X of Y.
- Skill provides numbered choices and recommended defaults.

## [0.2.2] - 2026-04-27

### Fixed

- Corrected release ZIP packaging so all framework, template, reference, and resource files are included.
- Enforced interactive intake behaviour before deep analysis.
- Added mandatory numeric transcript quality, reconstruction, and sentiment confidence scoring.
- Clarified participant context/profile workflow for Claude Desktop, Cowork, Claude Code, and Codex.

### Changed

- Default runtime mode is now Interactive Deep Mode.
- Autonomous mode must be explicitly requested.

## [0.2.1] - 2026-04-27

### Fixed

- Added proper release ZIP packaging for Claude Skill upload.
- Added proper Claude Cowork plugin ZIP structure.
- Prevented normal users from accidentally uploading GitHub source ZIPs.

### Added

- Build scripts for skill ZIP and plugin ZIP release assets.
- Installation documentation for non-technical users.

## [0.2.0] - Public skill packaging

- Add complete framework, reference, template, example, and testing structure.
- Add Claude Code, Claude Cowork plugin, and ChatGPT Codex packaging.
- Package user-created book summary reference guides under `resources/book-summaries/`.
- Add public-safe responsible-use guardrails and release validation tests.

## [0.1.0] - Initial private alpha

- Create initial placeholder scaffold.
