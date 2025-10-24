#!/usr/bin/env python3
"""
Hygiene check: fail if any tracked text file contains a UTF-8 BOM or CRLF line endings.
- Determines "text" by scanning for NUL bytes (binary => skip).
- Scans *all tracked files* via `git ls-files -z`.
Exit: 0 OK, 1 violations, 2 internal error.
"""
from __future__ import annotations
import subprocess, sys

CHUNK = 65536

def tracked_files():
    out = subprocess.check_output(["git","ls-files","-z"])
    return [p for p in out.decode("utf-8").split("\x00") if p]

def is_binary(path:str)->bool:
    try:
        with open(path, "rb") as f:
            block = f.read(CHUNK)
        return b"\x00" in block
    except Exception:
        return False

def has_bom(path:str)->bool:
    try:
        with open(path, "rb") as f:
            return f.read(3) == b"\xef\xbb\xbf"
    except Exception:
        return False

def has_crlf(path:str)->bool:
    try:
        with open(path, "rb") as f:
            prev = b""
            while True:
                chunk = f.read(CHUNK)
                if not chunk: return False
                buf = prev + chunk
                if b"\r\n" in buf: return True
                prev = buf[-1:]
    except Exception:
        return False

def main()->int:
    try:
        files = tracked_files()
    except Exception as e:
        print(f"::error title=Hygiene internal error::git ls-files failed: {e}")
        return 2

    bom, crlf = [], []
    for p in files:
        if p.startswith(".git/"):  # guard
            continue
        if is_binary(p):
            continue
        if has_bom(p):
            bom.append(p)
        if has_crlf(p):
            crlf.append(p)

    if bom:
        print("::error title=BOM detected::The following files contain a UTF-8 BOM:")
        print("\n".join(bom))
    if crlf:
        print("::error title=CRLF detected::The following files contain CRLF line endings:")
        print("\n".join(crlf))

    if bom or crlf:
        return 1
    print("Hygiene checks passed (no BOM, LF-only).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
