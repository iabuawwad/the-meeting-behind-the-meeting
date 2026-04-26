# Release Checklist

Use this checklist before publishing a release of The Meeting Behind the Meeting.

## Version

- Confirm `VERSION` contains the intended semantic version.
- Confirm `CHANGELOG.md` has an entry for the release.
- Confirm package metadata references the same version.

## Documentation

- Review `README.md` for current scope, outputs, platforms, and guardrails.
- Review `docs/INSTALL.md`, `docs/USAGE.md`, and `docs/TESTING.md`.
- Verify platform-specific claims against current official documentation.
- Confirm no exaggerated claims were introduced.

## Skill Content

- Keep each `SKILL.md` concise.
- Move long procedures to `frameworks/`, `references/`, or `templates/`.
- Confirm the transcript quality gate is present and cannot be skipped.
- Confirm behavioral interpretation is framed as evidence-based hypothesis.

## Packaged Reference Resources

- Confirm book summaries are user-created.
- Confirm no full books are included.
- Confirm no PDF, ePub, MOBI, or AZW3 files are included.
- Confirm no private transcripts are included.
- Confirm `resources/book-summaries/` is copied into each installable skill package.

## Validation

- Run the repository test suite.
- Validate package manifests and YAML files.
- Check all required files are present.
- Inspect sample outputs for evidence discipline and responsible-use guardrails.

## Publishing

- Tag the release with the exact version.
- Publish only after tests pass.
- Include release notes that describe user-visible changes.
