# scripts/lib/sources.py
from __future__ import annotations
import json, os
from pathlib import Path
from typing import Callable, Optional, Set

def split_csv(s: Optional[str]) -> list[str]:
    if not s:
        return []
    return [p.strip() for p in s.split(",") if p.strip()]

class SourceRegistry:
    def __init__(self, registry_path: str):
        data = json.loads(Path(registry_path).read_text(encoding="utf-8"))
        self.by_id: dict[str, dict] = {}
        self.alias_to_id: dict[str, str] = {}
        for entry in data:
            sid = entry["id"]
            self.by_id[sid] = entry
            for alias in [sid] + entry.get("aliases", []):
                self.alias_to_id[alias.upper()] = sid

    def resolve(self, src_str: Optional[str]) -> Optional[str]:
        if not src_str:
            return None
        return self.alias_to_id.get(src_str.upper())

def build_source_predicate(
    registry: SourceRegistry,
    toggle_config_path: str = "config/sources.toggle.json",
    profile_name: Optional[str] = None,
    allow_sources: Set[str] = frozenset(),
    deny_sources: Set[str] = frozenset(),
    allow_categories: Set[str] = frozenset(),
    deny_categories: Set[str] = frozenset(),
) -> Callable[[str], bool]:
    cfg = json.loads(Path(toggle_config_path).read_text(encoding="utf-8"))
    prof_name = profile_name or cfg.get("default_profile")
    profile = cfg["profiles"][prof_name]

    # Profile-level sets
    p_allow_src = set(profile.get("allow_sources", []))
    p_deny_src  = set(profile.get("deny_sources", []))
    p_allow_cat = set(profile.get("allow_categories", []))
    p_deny_cat  = set(profile.get("deny_categories", []))

    def is_enabled(src_id: str) -> bool:
        meta = registry.by_id.get(src_id)
        if not meta:
            return False
        enabled = bool(meta.get("default_enabled", False))
        cat = meta.get("category")

        # Profile category toggles
        if cat in p_allow_cat: enabled = True
        if cat in p_deny_cat:  enabled = False
        # Profile source toggles
        if src_id in p_allow_src: enabled = True
        if src_id in p_deny_src:  enabled = False

        # CLI category toggles
        if cat in allow_categories: enabled = True
        if cat in deny_categories:  enabled = False
        # CLI source toggles (deny wins)
        if src_id in allow_sources: enabled = True
        if src_id in deny_sources:  enabled = False

        return enabled

    return is_enabled
