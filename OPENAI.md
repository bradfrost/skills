# Use these skills in Codex & ChatGPT

You can install all 16 public skills locally in Codex and upload the same
collection to your ChatGPT account. Each skill keeps its supporting files,
including the design-system references and limits documentation.

## Codex

From this checkout, run:

```bash
python3 scripts/install-codex.py
```

This links the skills into `~/.agents/skills/`, which means updates you pull
into this checkout also update your local skills. If you already have copies,
add `--replace`; the installer backs them up outside the discovery directory
before linking the current versions. You can choose another destination with
`--dest /path/to/skills`.

The skills become available on your next turn. If they don't appear, restart
Codex and check the Skills selector. You can invoke one directly with a name
such as `$ds-inspection` or `$storybook-to-product`.

## ChatGPT

Build the plugin archive:

```bash
python3 scripts/package-openai.py
```

In ChatGPT, open **Plugins > Add > Upload plugin archive** and select
`dist/brad-frost-skills.zip`. Choose **Add plugin**, then **Install plugin**.
Confirm the detail page shows **Skills 16** and **Manage / Try in chat**.
Start a new chat to use it.

These upload controls are available on Brad's account as of October 22, 2026;
availability may differ for other accounts. Mobile uses the same account
installation, but check availability on your device before relying on it.

An upload is a snapshot. After updating this checkout, rebuild and upload the
archive again. Use `--version 1.0.1` to choose the next package version.
The archive includes a source commit and file checksums in
`package-receipt.json`; it excludes Git history and local configuration.
Plain YAML descriptions are quoted in the archive for parser compatibility;
skill instructions and supporting files stay unchanged.

## What installation means

The limits skills carry instructions and optional Claude Code hooks.
Installing this collection does not turn those hooks into Codex or ChatGPT
enforcement. On these surfaces, limits remain advisory; the shipped
[enforcement matrix](skills/mental-health/limits-setup/ENFORCEMENT.md) explains
the distinction. Run `$setup-brad-frost-skills` in a new session if you need
to configure your own limits.

Design-system work still needs access to your design system, product, and
any tools named by the skill. Installing instructions does not connect those
services or grant access to them.

For Brad's installations, deployment still needs to be recorded through
bf-brain's deployed-surfaces registry process. The archive receipt records
what was packaged; it does not update that registry.

Official references: [Build skills](https://learn.chatgpt.com/docs/build-skills),
[Package a plugin](https://developers.openai.com/plugins/build/plugins), and
[Use plugins](https://learn.chatgpt.com/docs/plugins).
