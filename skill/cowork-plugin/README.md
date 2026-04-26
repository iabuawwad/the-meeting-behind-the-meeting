# The Meeting Behind the Meeting - Cowork Plugin

This directory contains the Claude Cowork plugin wrapper for **The Meeting Behind the Meeting**.

The plugin bundles only one skill:

- `skills/the-meeting-behind-the-meeting/SKILL.md`

It does not bundle connectors, MCP servers, or elevated permissions.

## Installation

1. Open Claude Desktop.
2. Go to the Cowork tab.
3. Open Customize.
4. Browse plugins or upload the custom plugin file.
5. Install the plugin.
6. Invoke the skill with the `/` command or the `+` button.

## Cowork Desktop Plugin Delivery

Cowork Desktop plugins are the correct delivery mechanism for skills in Cowork because plugins can bundle skills for installation and invocation inside the Cowork experience.

This plugin is intentionally conservative:

- Skills: included
- Connectors: not included
- MCP servers: not included
- Elevated permissions: not requested

## Packaged Skill

The included skill is an evidence-based meeting analysis skill for transcripts, meeting notes, conversation threads, interviews, voice notes, minutes, action items, decisions, and risks.

The skill must run the transcript quality gate before advanced interpretation and must not present behavioral interpretation as fact.
