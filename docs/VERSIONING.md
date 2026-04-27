# Versioning

The Meeting Behind the Meeting uses semantic versioning: `MAJOR.MINOR.PATCH`.

The current version is `0.2.2`.

## MAJOR

Increment `MAJOR` for breaking changes, including:

- Breaking the documented output contract.
- Renaming or removing required output sections.
- Changing installation layout or packaging in a way that requires user migration.
- Dropping support for a previously documented platform.

## MINOR

Increment `MINOR` for backward-compatible additions, including:

- New analysis modules.
- New frameworks, references, templates, or examples.
- New supported platforms or packaging surfaces.
- Additive output sections that do not break existing consumers.

## PATCH

Increment `PATCH` for backward-compatible maintenance, including:

- Bug fixes.
- Documentation improvements.
- Test fixes.
- Clarifications that do not change the output contract.

## Release Rules

- Keep `VERSION`, `CHANGELOG.md`, package metadata, and release notes aligned.
- Document any output-contract change before release.
- Verify installation instructions for each supported platform before publishing.
