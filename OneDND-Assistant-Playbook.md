# One D&D Repo — Assistant Playbook (Environment, Guardrails, and Routines)

> Audience: **ChatGPT + user** working together in this project.  
> Goal: avoid preventable churn (encoding, line endings, shell/version quirks, CI name issues) and keep changes safe, small, and green.

---

## 1) Canonical Environment (assume these unless told otherwise)

- **OS**: Windows 10/11
- **Repo root (absolute path)**:  
  `C:\MyGitHubRepos\Onednd-Rules-and-Builds`
- **PowerShell**: **7.5.4** (use PS7 syntax, but avoid fancy constructs that break PS5.1)
- **Python**: **3.11** (local + CI)
- **GitHub Actions**:
  - `actions/checkout@v4`
  - `actions/setup-python@v5` (python-version `3.11`)
  - `actions/cache@v4`
  - `actions/upload-artifact@v4`
- **Local hygiene gate**: `python scripts/ci/hygiene_check.py` (must pass before any commit)
- **CI workflow**: `.github/workflows/ci-validate.yml` (single matrix)
- **Matrix targets** (baseline): `spell`, `index:spells_by_class_level`
- **Public docs**: under `docs/` (e.g., `docs/reports/...`), **not** `/reports`
- **Branch**: `master`

> **Assistant rule**: **always** use the absolute repo path above in scripts; **never** default to `C:\Users\…`.

---

## 2) Non-Negotiable Hygiene Rules

1. **Encoding**: UTF-8 **without BOM**.
2. **Line endings**: **LF** only (no CRLF) for tracked text (YAML, JSON, py, ps1, md, etc.).
3. **Hygiene must pass locally** before *any* `git commit`:
   ```powershell
   Set-Location C:\MyGitHubRepos\Onednd-Rules-and-Builds
   python scripts/ci/hygiene_check.py
   ```
4. **Pre-commit hook** is installed and runs the same checker; expect commits to fail if hygiene fails.
5. **Artifact names** in CI must be sanitized to `[A-Za-z0-9_.-]` only.

---

## 3) PowerShell Guidance (so scripts run first time)

- **Do not** use the PS7 ternary `? :` or null-coalescing when the same block might be run in PS5.1; prefer explicit `if/else`.
- Always compute or force the **repo root** before touching files:
  ```powershell
  $repo = "C:\MyGitHubRepos\Onednd-Rules-and-Builds"
  Set-Location $repo
  ```
- When writing files that go into git, **write bytes** as UTF-8 (no BOM) and **force LF**:
  ```powershell
  $content = $content -replace "`r`n","`n" -replace "`r","`n"
  $bytes   = [Text.Encoding]::UTF8.GetBytes($content)
  [IO.File]::WriteAllBytes($path, $bytes)
  ```
- Avoid `gh` CLI assumptions; don’t depend on tools not guaranteed on the box.
- When patching YAML from PowerShell, write the **entire file** back (LF, no BOM). Avoid heredocs that contain `${{ … }}`—they often trip quoting.

---

## 4) GitHub Actions (YAML) Guardrails

- Keep a **single** consolidated workflow: `.github/workflows/ci-validate.yml`.
- Always **pin** Python to `3.11`.
- **Hygiene job** runs first and gates the matrix.
- **Never** use matrix values directly as artifact names—**sanitize**:
  ```yaml
  - name: Compute safe artifact name
    if: always()
    shell: bash
    run: |
      set -euo pipefail
      SAFE="logs-$(printf "%s" "${{ matrix.target }}" | sed -E 's/[^A-Za-z0-9_.-]+/-/g')"
      echo "ART_NAME=$SAFE" >> "$GITHUB_ENV"
  - name: Upload logs
    if: always()
    uses: actions/upload-artifact@v4
    with:
      name: ${{ env.ART_NAME }}
      path: ci_out/${{ matrix.target }}/**
      if-no-files-found: error
      retention-days: 7
  ```
- If a YAML change fails with “`'run' is already defined`” or similar, it’s usually a **duplicate key** or heredoc/quoting problem—rewrite the step cleanly.

---

## 5) Working Rhythm (to keep CI green and churn low)

**For any change:**

1) **One step at a time**. Do the smallest safe change.  
2) Run the local hygiene gate:
   ```powershell
   Set-Location C:\MyGitHubRepos\Onednd-Rules-and-Builds
   python scripts/ci/hygiene_check.py
   ```
3) Commit & push:
   ```powershell
   git add <files>
   git commit -m "<clear, single-purpose message>"
   git push
   ```
4) Check **Actions**. If red, fix *that exact* failure—don’t pile on new changes.

**When adding a new CI target:**

- Add the target to the matrix.
- Add a `case` branch invoking the right validator, writing to `ci_out/${{ matrix.target }}`.
- Keep the summary/upload steps unchanged—sanitizer handles names.

---

## 6) Public Documentation vs Private Scratch

- Keep `/reports/` **ignored** (private scratch).
- Publish snapshots to `docs/reports/…` and **unignore**:
  ```gitignore
  reports/
  # Allow public report snapshots while keeping private /reports ignored
  !docs/reports/
  !docs/reports/**
  ```
- Normalize published docs to LF + no BOM before committing.

---

## 7) Error Glossary → Immediate Fix

- **“Unexpected UTF-8 BOM … line 1 col 1”**  
  *Fix*: strip BOM → write back as UTF-8 (no BOM) + LF → run hygiene → commit.

- **“CRLF detected” (pre-commit or CI)**  
  *Fix*: convert to LF at **byte level** (not just editor setting) → re-run hygiene.

- **“Provided artifact name … is empty / invalid”**  
  *Fix*: ensure the sanitize step runs and uses the `sed` rule above; no `tr` ranges.

- **“.gitignore prevented docs/reports/ from being tracked”**  
  *Fix*: add `!docs/reports/` and `!docs/reports/**` *after* the `reports/` rule.

- **“Python was not found” (hook)**  
  *Fix*: ensure Python 3.11 is installed and available as `python`/`py`; if needed, update hook to try `py`, then `python3`, then `python`.

---

## 8) Assistant Interaction Contract (how I will behave)

- I will **always** assume:
  - repo root = `C:\MyGitHubRepos\Onednd-Rules-and-Builds`
  - PowerShell 7.5.4
  - Python 3.11
- I will propose **one step at a time** and wait for console output before offering the next step.
- I will **not** use `?:` or PS7-only syntax in scripts unless you say PS7-only is acceptable.
- I will **not** rely on uninstalled tools (`gh`, etc.).
- I will **not** paste fragile YAML heredocs with `${{ }}`; I’ll write/replace whole files with LF/no-BOM bytes.
- I will always include a **local hygiene check** before any `git commit` lines I provide.
- I will sanitize artifact names and avoid changes that can reintroduce BOM/CRLF.

---

## 9) Quick Copy-Paste Library

**Normalize a file to UTF-8 (no BOM) + LF (PowerShell):**
```powershell
param([string]$Path)
[byte[]]$b = [IO.File]::ReadAllBytes($Path)
$start = 0; if ($b.Length -ge 3 -and $b[0]-eq 0xEF -and $b[1]-eq 0xBB -and $b[2]-eq 0xBF) { $start = 3 }
[byte[]]$slice = New-Object byte[] ($b.Length - $start); [Array]::Copy($b, $start, $slice, 0, $slice.Length)
$ms = New-Object IO.MemoryStream; $i = 0
while ($i -lt $slice.Length) {
  if ($slice[$i] -eq 13) { if ($i+1 -lt $slice.Length -and $slice[$i+1]-eq 10) { [void]$ms.WriteByte(10); $i+=2 } else { [void]$ms.WriteByte(10); $i++ } }
  else { [void]$ms.WriteByte($slice[$i]); $i++ }
}
[IO.File]::WriteAllBytes($Path, $ms.ToArray())
```

**Local hygiene gate:**
```powershell
Set-Location C:\MyGitHubRepos\Onednd-Rules-and-Builds
python scripts/ci/hygiene_check.py
```

**CI artifact name sanitizer (YAML):**
```yaml
SAFE="logs-$(printf "%s" "${{ matrix.target }}" | sed -E 's/[^A-Za-z0-9_.-]+/-/g')"
```

---

## 10) Versions & Pinning (for future me)

- **PowerShell**: 7.5.4
- **Python**: 3.11
- **Actions**:
  - `actions/checkout@v4`
  - `actions/setup-python@v5` (`python-version: '3.11'`)
  - `actions/cache@v4`
  - `actions/upload-artifact@v4`
