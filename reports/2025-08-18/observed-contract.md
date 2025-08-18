# Observed Contract (2025-08-18)

_Baseline root_: `C:\MyGitHubRepos\Onednd-Rules-and-Builds\rules\2024`

_Compared against upstream_: `C:\MyGitHubRepos\Onednd-Rules-and-Builds\reports\2025-08-18\upstream-shapes.md`


---

## ./rules/2024/action.json

Detected entries: **18** (mode: largest-list:action)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 18/18 (100%) |  |  |

| `name` | yes | str | 18/18 (100%) | Attack, Dash, Disengage, Dodge, Don or Doff a Shield, End Concentration, Escape a Grapple, Help, Hide, Improvising an Action, Influence, Magic, Opportunity Attack, Ready, Search, Study, Two-Weapon Fighting, Utilize |  |

| `page` | yes | int | 18/18 (100%) | 15, 213, 219, 361, 363, 365, 366, 367, 368, 369, 371, 372, 373, 375, 377 |  |

| `source` | yes | str | 18/18 (100%) | XPHB |  |

| `time` | yes | list | 18/18 (100%) |  |  |

| `srd52` | no | bool | 15/18 (83%) | True |  |

| `basicRules2024` | no | bool | 5/18 (28%) | True |  |

| `seeAlsoAction` | no | list | 2/18 (11%) |  |  |



---

## ./rules/2024/background.json

Detected entries: **16** (mode: largest-list:background)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `ability` | yes | list | 16/16 (100%) |  |  |

| `edition` | yes | str | 16/16 (100%) | one |  |

| `entries` | yes | list | 16/16 (100%) |  |  |

| `feats` | yes | list | 16/16 (100%) |  |  |

| `hasFluff` | yes | bool | 16/16 (100%) | True |  |

| `hasFluffImages` | yes | bool | 16/16 (100%) | True |  |

| `name` | yes | str | 16/16 (100%) | Acolyte, Artisan, Charlatan, Criminal, Entertainer, Farmer, Guard, Guide, Hermit, Merchant, Noble, Sage, Sailor, Scribe, Soldier, Wayfarer |  |

| `page` | yes | int | 16/16 (100%) | 178, 179, 180, 181, 182, 183, 184, 185 |  |

| `skillProficiencies` | yes | list | 16/16 (100%) |  |  |

| `source` | yes | str | 16/16 (100%) | XPHB |  |

| `startingEquipment` | yes | list | 16/16 (100%) |  |  |

| `toolProficiencies` | yes | list | 16/16 (100%) |  |  |

| `basicRules2024` | no | bool | 4/16 (25%) | True |  |

| `srd52` | no | bool | 1/16 (6%) | True |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `additionalSources`, `additionalSpells`, `basicRules`, `fromFeature`, `languageProficiencies`, `otherSources`, `prerequisite`, `reprintedAs`, `skillToolLanguageProficiencies`, `srd`, `weaponProficiencies`



---

## ./rules/2024/backgroundFluff.json

Detected entries: **16** (mode: largest-list:backgroundFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 16/16 (100%) |  |  |

| `images` | yes | list | 16/16 (100%) |  |  |

| `name` | yes | str | 16/16 (100%) | Acolyte, Artisan, Charlatan, Criminal, Entertainer, Farmer, Guard, Guide, Hermit, Merchant, Noble, Sage, Sailor, Scribe, Soldier, Wayfarer |  |

| `source` | yes | str | 16/16 (100%) | XPHB |  |



---

## ./rules/2024/baseitem.json

Detected entries: **77** (mode: largest-list:baseitem)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `edition` | yes | str | 77/77 (100%) | one |  |

| `name` | yes | str | 77/77 (100%) |  |  |

| `page` | yes | int | 77/77 (100%) | 215, 219, 221, 222, 224, 225 |  |

| `rarity` | yes | str | 77/77 (100%) | none |  |

| `source` | yes | str | 77/77 (100%) | XPHB |  |

| `type` | yes | str | 77/77 (100%) | A\|XPHB, HA\|XPHB, INS\|XPHB, LA\|XPHB, MA\|XPHB, M\|XPHB, R\|XPHB, SCF\|XPHB, S\|XPHB |  |

| `value` | yes | float, int | 77/77 (100%) |  |  |

| `weight` | no | float, int | 76/77 (99%) |  |  |

| `srd52` | no | bool | 75/77 (97%) | True |  |

| `basicRules2024` | no | bool | 61/77 (79%) | True |  |

| `hasFluffImages` | no | bool | 51/77 (66%) | True |  |

| `dmg1` | no | str | 40/77 (52%) | 1, 1d10, 1d12, 1d4, 1d6, 1d8, 2d6 |  |

| `dmgType` | no | str | 40/77 (52%) | B, P, S |  |

| `mastery` | no | list | 40/77 (52%) |  |  |

| `weaponCategory` | no | str | 40/77 (52%) | martial, simple |  |

| `weapon` | no | bool | 38/77 (49%) | True |  |

| `property` | no | list | 37/77 (48%) |  |  |

| `entries` | no | list | 21/77 (27%) |  |  |

| `range` | no | str | 16/77 (21%) | 100/400, 150/600, 20/60, 25/100, 30/120, 30/90, 40/120, 80/320 |  |

| `ac` | no | int | 13/77 (17%) | 11, 12, 13, 14, 15, 16, 17, 18, 2 |  |

| `armor` | no | bool | 12/77 (16%) | True |  |

| `ammoType` | no | str | 9/77 (12%) | arrow\|xphb, bolt\|xphb, firearm bullet\|xphb, needle\|xphb, sling bullet\|xphb |  |

| `dmg2` | no | str | 9/77 (12%) | 1d10, 1d8 |  |

| `stealth` | no | bool | 7/77 (9%) | True |  |

| `group` | no | list | 6/77 (8%) |  |  |

| `scfType` | no | str | 6/77 (8%) | arcane, druid |  |

| `packContents` | no | list | 5/77 (6%) |  |  |

| `sword` | no | bool | 5/77 (6%) | True |  |

| `axe` | no | bool | 3/77 (4%) | True |  |

| `crossbow` | no | bool | 3/77 (4%) | True |  |

| `hammer` | no | bool | 3/77 (4%) | True |  |

| `strength` | no | str | 3/77 (4%) | 13, 15 |  |

| `arrow` | no | bool | 2/77 (3%) | True |  |

| `bolt` | no | bool | 2/77 (3%) | True |  |

| `bow` | no | bool | 2/77 (3%) | True |  |

| `bulletFirearm` | no | bool | 2/77 (3%) | True |  |

| `bulletSling` | no | bool | 2/77 (3%) | True |  |

| `club` | no | bool | 2/77 (3%) | True |  |

| `firearm` | no | bool | 2/77 (3%) | True |  |

| `mace` | no | bool | 2/77 (3%) | True |  |

| `miscTags` | no | list | 2/77 (3%) |  |  |

| `needleBlowgun` | no | bool | 2/77 (3%) | True |  |

| `polearm` | no | bool | 2/77 (3%) | True |  |

| `spear` | no | bool | 2/77 (3%) | True |  |

| `dagger` | no | bool | 1/77 (1%) | True |  |

| `lance` | no | bool | 1/77 (1%) | True |  |

| `rapier` | no | bool | 1/77 (1%) | True |  |

| `staff` | no | bool | 1/77 (1%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/action.json

Detected entries: **20** (mode: largest-list:action)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 20/20 (100%) |  |  |

| `name` | yes | str | 20/20 (100%) | Attack, Dash, Disengage, Dodge, Don or Doff a Shield, End Concentration, Escape a Grapple, Help, Hide, Identify a Spell, Improvising an Action, Influence, Magic, Opportunity Attack, Ready, Search, Study, Two-Weapon Fighting, Utilize, Waking Someone |  |

| `page` | yes | int | 20/20 (100%) | 15, 213, 219, 361, 363, 365, 366, 367, 368, 369, 371, 372, 373, 375, 377, 77, 85 |  |

| `source` | yes | str | 20/20 (100%) | XGE, XPHB |  |

| `time` | yes | list | 20/20 (100%) |  |  |

| `srd52` | no | bool | 15/20 (75%) | True |  |

| `basicRules2024` | no | bool | 5/20 (25%) | True |  |

| `seeAlsoAction` | no | list | 2/20 (10%) |  |  |

| `fromVariant` | no | str | 1/20 (5%) | Spellcasting\|XGE |  |



---

## ./rules/2024/baseline/2025-08-11_core/background.json

Detected entries: **16** (mode: largest-list:background)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `ability` | yes | list | 16/16 (100%) |  |  |

| `edition` | yes | str | 16/16 (100%) | one |  |

| `entries` | yes | list | 16/16 (100%) |  |  |

| `feats` | yes | list | 16/16 (100%) |  |  |

| `hasFluff` | yes | bool | 16/16 (100%) | True |  |

| `hasFluffImages` | yes | bool | 16/16 (100%) | True |  |

| `name` | yes | str | 16/16 (100%) | Acolyte, Artisan, Charlatan, Criminal, Entertainer, Farmer, Guard, Guide, Hermit, Merchant, Noble, Sage, Sailor, Scribe, Soldier, Wayfarer |  |

| `page` | yes | int | 16/16 (100%) | 178, 179, 180, 181, 182, 183, 184, 185 |  |

| `skillProficiencies` | yes | list | 16/16 (100%) |  |  |

| `source` | yes | str | 16/16 (100%) | XPHB |  |

| `startingEquipment` | yes | list | 16/16 (100%) |  |  |

| `toolProficiencies` | yes | list | 16/16 (100%) |  |  |

| `basicRules2024` | no | bool | 4/16 (25%) | True |  |

| `srd52` | no | bool | 1/16 (6%) | True |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `additionalSources`, `additionalSpells`, `basicRules`, `fromFeature`, `languageProficiencies`, `otherSources`, `prerequisite`, `reprintedAs`, `skillToolLanguageProficiencies`, `srd`, `weaponProficiencies`



---

## ./rules/2024/baseline/2025-08-11_core/backgroundFluff.json

Detected entries: **16** (mode: largest-list:backgroundFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 16/16 (100%) |  |  |

| `images` | yes | list | 16/16 (100%) |  |  |

| `name` | yes | str | 16/16 (100%) | Acolyte, Artisan, Charlatan, Criminal, Entertainer, Farmer, Guard, Guide, Hermit, Merchant, Noble, Sage, Sailor, Scribe, Soldier, Wayfarer |  |

| `source` | yes | str | 16/16 (100%) | XPHB |  |



---

## ./rules/2024/baseline/2025-08-11_core/baseitem.json

Detected entries: **86** (mode: largest-list:baseitem)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `edition` | yes | str | 86/86 (100%) | one |  |

| `name` | yes | str | 86/86 (100%) |  |  |

| `page` | yes | int | 86/86 (100%) | 215, 219, 221, 222, 224, 225, 72, 73 |  |

| `rarity` | yes | str | 86/86 (100%) | none |  |

| `source` | yes | str | 86/86 (100%) | XDMG, XPHB |  |

| `type` | yes | str | 86/86 (100%) | AF\|XDMG, A\|XPHB, HA\|XPHB, INS\|XPHB, LA\|XPHB, MA\|XPHB, M\|XPHB, R\|XPHB, SCF\|XPHB, S\|XPHB |  |

| `weight` | no | float, int | 85/86 (99%) |  |  |

| `value` | no | float, int | 77/86 (90%) |  |  |

| `srd52` | no | bool | 75/86 (87%) | True |  |

| `basicRules2024` | no | bool | 61/86 (71%) | True |  |

| `hasFluffImages` | no | bool | 51/86 (59%) | True |  |

| `dmg1` | no | str | 48/86 (56%) | 1, 1d10, 1d12, 1d4, 1d6, 1d8, 2d10, 2d6, 2d8, 3d6, 3d8, 6d8 |  |

| `dmgType` | no | str | 48/86 (56%) | B, N, P, R, S |  |

| `mastery` | no | list | 48/86 (56%) |  |  |

| `weaponCategory` | no | str | 48/86 (56%) | martial, simple |  |

| `weapon` | no | bool | 46/86 (53%) | True |  |

| `property` | no | list | 45/86 (52%) |  |  |

| `range` | no | str | 24/86 (28%) | 100/300, 100/400, 120/360, 150/600, 20/60, 25/100, 30/120, 30/90, 40/120, 50/150, 80/240, 80/320 |  |

| `entries` | no | list | 21/86 (24%) |  |  |

| `ammoType` | no | str | 17/86 (20%) | arrow\|xphb, bolt\|xphb, energy cell\|xdmg, firearm bullet\|xphb, needle\|xphb, sling bullet\|xphb |  |

| `ac` | no | int | 13/86 (15%) | 11, 12, 13, 14, 15, 16, 17, 18, 2 |  |

| `armor` | no | bool | 12/86 (14%) | True |  |

| `firearm` | no | bool | 10/86 (12%) | True |  |

| `age` | no | str | 9/86 (10%) | futuristic, modern |  |

| `dmg2` | no | str | 9/86 (10%) | 1d10, 1d8 |  |

| `reload` | no | int | 8/86 (9%) | 15, 2, 30, 5, 50, 6 |  |

| `valueRarity` | no | str | 8/86 (9%) | rare, very rare |  |

| `stealth` | no | bool | 7/86 (8%) | True |  |

| `group` | no | list | 6/86 (7%) |  |  |

| `scfType` | no | str | 6/86 (7%) | arcane, druid |  |

| `packContents` | no | list | 5/86 (6%) |  |  |

| `sword` | no | bool | 5/86 (6%) | True |  |

| `axe` | no | bool | 3/86 (3%) | True |  |

| `crossbow` | no | bool | 3/86 (3%) | True |  |

| `hammer` | no | bool | 3/86 (3%) | True |  |

| `miscTags` | no | list | 3/86 (3%) |  |  |

| `strength` | no | str | 3/86 (3%) | 13, 15 |  |

| `arrow` | no | bool | 2/86 (2%) | True |  |

| `bolt` | no | bool | 2/86 (2%) | True |  |

| `bow` | no | bool | 2/86 (2%) | True |  |

| `bulletFirearm` | no | bool | 2/86 (2%) | True |  |

| `bulletSling` | no | bool | 2/86 (2%) | True |  |

| `club` | no | bool | 2/86 (2%) | True |  |

| `mace` | no | bool | 2/86 (2%) | True |  |

| `needleBlowgun` | no | bool | 2/86 (2%) | True |  |

| `polearm` | no | bool | 2/86 (2%) | True |  |

| `spear` | no | bool | 2/86 (2%) | True |  |

| `cellEnergy` | no | bool | 1/86 (1%) | True |  |

| `dagger` | no | bool | 1/86 (1%) | True |  |

| `lance` | no | bool | 1/86 (1%) | True |  |

| `rapier` | no | bool | 1/86 (1%) | True |  |

| `staff` | no | bool | 1/86 (1%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/book.json

Detected entries: **5** (mode: largest-list:book)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `author` | yes | str | 5/5 (100%) | Wizards RPG Team |  |

| `contents` | yes | list | 5/5 (100%) |  |  |

| `cover` | yes | dict | 5/5 (100%) |  |  |

| `group` | yes | str | 5/5 (100%) | core, screen, supplement |  |

| `id` | yes | str | 5/5 (100%) | XDMG, XGE, XMM, XPHB, XScreen |  |

| `name` | yes | str | 5/5 (100%) | Dungeon Master's Guide (2024), Dungeon Master's Screen (2024), Monster Manual (2025), Player's Handbook (2024), Xanathar's Guide to Everything |  |

| `published` | yes | str | 5/5 (100%) | 2017-11-21, 2024-09-17, 2024-11-12, 2025-02-18 |  |

| `source` | yes | str | 5/5 (100%) | XDMG, XGE, XMM, XPHB, XScreen |  |



---

## ./rules/2024/baseline/2025-08-11_core/class.json

Detected entries: **12** (mode: largest-list:class)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 12/12 (100%) | True |  |

| `classFeatures` | yes | list | 12/12 (100%) |  |  |

| `classTableGroups` | yes | list | 12/12 (100%) |  |  |

| `edition` | yes | str | 12/12 (100%) | one |  |

| `featProgression` | yes | list | 12/12 (100%) |  |  |

| `hasFluff` | yes | bool | 12/12 (100%) | True |  |

| `hasFluffImages` | yes | bool | 12/12 (100%) | True |  |

| `hd` | yes | dict | 12/12 (100%) |  |  |

| `multiclassing` | yes | dict | 12/12 (100%) |  |  |

| `name` | yes | str | 12/12 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `page` | yes | int | 12/12 (100%) | 100, 108, 118, 128, 138, 152, 164, 50, 58, 68, 78, 90 |  |

| `primaryAbility` | yes | list | 12/12 (100%) |  |  |

| `proficiency` | yes | list | 12/12 (100%) |  |  |

| `source` | yes | str | 12/12 (100%) | XPHB |  |

| `srd52` | yes | bool | 12/12 (100%) | True |  |

| `startingEquipment` | yes | dict | 12/12 (100%) |  |  |

| `startingProficiencies` | yes | dict | 12/12 (100%) |  |  |

| `subclassTitle` | yes | str | 12/12 (100%) | Barbarian Subclass, Bard Subclass, Cleric Subclass, Druid Subclass, Fighter Subclass, Monk Subclass, Paladin Subclass, Ranger Subclass, Rogue Subclass, Sorcerer Subclass, Warlock Subclass, Wizard Subclass |  |

| `casterProgression` | no | str | 8/12 (67%) | artificer, full, pact |  |

| `preparedSpellsChange` | no | str | 8/12 (67%) | level, restLong |  |

| `preparedSpellsProgression` | no | list | 8/12 (67%) |  |  |

| `spellcastingAbility` | no | str | 8/12 (67%) | cha, int, wis |  |

| `cantripProgression` | no | list | 6/12 (50%) |  |  |

| `additionalSpells` | no | list | 5/12 (42%) |  |  |

| `optionalfeatureProgression` | no | list | 2/12 (17%) |  |  |

| `spellsKnownProgressionFixed` | no | list | 1/12 (8%) |  |  |

| `spellsKnownProgressionFixedAllowLowerLevel` | no | bool | 1/12 (8%) | True |  |

| `spellsKnownProgressionFixedByLevel` | no | dict | 1/12 (8%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `advancement`, `basicRules`, `isSidekick`, `migrationVersion`, `otherSources`, `preparedSpells`, `reprintedAs`, `spellsKnownProgression`, `srd`



---

## ./rules/2024/baseline/2025-08-11_core/classFeature.json

Detected entries: **156** (mode: largest-list:classFeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 156/156 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 156/156 (100%) | XPHB |  |

| `entries` | yes | list | 156/156 (100%) |  |  |

| `level` | yes | int | 156/156 (100%) | 1, 10, 11, 13, 14, 15, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 9 |  |

| `name` | yes | str | 156/156 (100%) |  |  |

| `page` | yes | int | 156/156 (100%) |  |  |

| `source` | yes | str | 156/156 (100%) | XPHB |  |

| `basicRules2024` | no | bool | 155/156 (99%) | True |  |

| `srd52` | no | bool | 155/156 (99%) | True |  |

| `consumes` | no | dict | 12/156 (8%) |  |  |

| `header` | no | int | 11/156 (7%) | 2 |  |

| `foundrySystem` | no | dict | 1/156 (1%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/classFluff.json

Detected entries: **12** (mode: largest-list:classFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 12/12 (100%) |  |  |

| `images` | yes | list | 12/12 (100%) |  |  |

| `name` | yes | str | 12/12 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `source` | yes | str | 12/12 (100%) | XPHB |  |



---

## ./rules/2024/baseline/2025-08-11_core/condition.json

Detected entries: **15** (mode: largest-list:condition)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 15/15 (100%) | True |  |

| `entries` | yes | list | 15/15 (100%) |  |  |

| `name` | yes | str | 15/15 (100%) | Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious |  |

| `page` | yes | int | 15/15 (100%) | 361, 365, 367, 369, 370, 371, 372, 373, 376 |  |

| `source` | yes | str | 15/15 (100%) | XPHB |  |

| `srd52` | yes | bool | 15/15 (100%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/feat.json

Detected entries: **92** (mode: largest-list:feat)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 92/92 (100%) |  |  |

| `name` | yes | str | 92/92 (100%) |  |  |

| `page` | yes | int | 92/92 (100%) | 110, 120, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 73, 74, 75 |  |

| `source` | yes | str | 92/92 (100%) | XGE, XPHB |  |

| `prerequisite` | no | list | 82/92 (89%) |  |  |

| `category` | no | str | 77/92 (84%) | EB, FS, FS:P, FS:R, G, O |  |

| `ability` | no | list | 66/92 (72%) |  |  |

| `srd52` | no | bool | 19/92 (21%) | True |  |

| `basicRules2024` | no | bool | 17/92 (18%) | True |  |

| `additionalSpells` | no | list | 11/92 (12%) |  |  |

| `hasFluffImages` | no | bool | 8/92 (9%) | True |  |

| `skillProficiencies` | no | list | 6/92 (7%) |  |  |

| `toolProficiencies` | no | list | 5/92 (5%) |  |  |

| `repeatable` | no | bool | 4/92 (4%) | True |  |

| `repeatableHidden` | no | bool | 4/92 (4%) | True |  |

| `armorProficiencies` | no | list | 3/92 (3%) |  |  |

| `senses` | no | list | 3/92 (3%) |  |  |

| `expertise` | no | list | 2/92 (2%) |  |  |

| `languageProficiencies` | no | list | 2/92 (2%) |  |  |

| `resist` | no | list | 2/92 (2%) |  |  |

| `weaponProficiencies` | no | list | 2/92 (2%) |  |  |

| `_versions` | no | list | 1/92 (1%) |  |  |

| `savingThrowProficiencies` | no | list | 1/92 (1%) |  |  |

| `skillToolLanguageProficiencies` | no | list | 1/92 (1%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `activities`, `additionalSources`, `bonusSenses`, `effects`, `migrationVersion`, `optionalfeatureProgression`, `reprintedAs`, `srd`, `system`, `traitTags`



---

## ./rules/2024/baseline/2025-08-11_core/featFluff.json

Detected entries: **8** (mode: largest-list:featFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 8/8 (100%) |  |  |

| `name` | yes | str | 8/8 (100%) | Boon of Fate, Boon of Skill, Fey-Touched, Healer, Poisoner, Ritual Caster, Two-Weapon Fighting, Weapon Master |  |

| `source` | yes | str | 8/8 (100%) | XPHB |  |



---

## ./rules/2024/baseline/2025-08-11_core/hazard.json

Detected entries: **30** (mode: largest-list:hazard)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 30/30 (100%) |  |  |

| `name` | yes | str | 30/30 (100%) |  |  |

| `page` | yes | int | 30/30 (100%) | 30, 362, 365, 367, 371, 376, 68, 69, 76, 77, 78, 79 |  |

| `source` | yes | str | 30/30 (100%) | XDMG, XPHB |  |

| `trapHazType` | no | str | 13/30 (43%) | ENV, GEN |  |

| `rating` | no | list | 12/30 (40%) |  |  |

| `hasFluffImages` | no | bool | 2/30 (7%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/hazardFluff.json

Detected entries: **2** (mode: largest-list:hazardFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 2/2 (100%) |  |  |

| `name` | yes | str | 2/2 (100%) | Green Slime, Webs |  |

| `source` | yes | str | 2/2 (100%) | XDMG |  |



---

## ./rules/2024/baseline/2025-08-11_core/item.json

Detected entries: **776** (mode: largest-list:item)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 776/776 (100%) |  |  |

| `source` | yes | str | 776/776 (100%) | XDMG, XGE, XMM, XMtS, XPHB |  |

| `page` | no | int | 437/776 (56%) |  |  |

| `rarity` | no | str | 437/776 (56%) | common, legendary, none, rare, uncommon, unknown (magic), very rare |  |

| `migrationVersion` | no | int | 339/776 (44%) | 3 |  |

| `type` | no | str | 334/776 (43%) |  |  |

| `entries` | no | list | 331/776 (43%) |  |  |

| `activities` | no | list | 317/776 (41%) |  |  |

| `value` | no | int | 244/776 (31%) |  |  |

| `srd52` | no | bool, str | 215/776 (28%) | Efficient Quiver, Feather Token, Whip, Handy Haversack, True |  |

| `basicRules2024` | no | bool | 197/776 (25%) | True |  |

| `weight` | no | float, int | 149/776 (19%) |  |  |

| `effects` | no | list | 146/776 (19%) |  |  |

| `wondrous` | no | bool | 97/776 (12%) | True |  |

| `hasFluffImages` | no | bool | 90/776 (12%) | True |  |

| `lootTables` | no | list | 87/776 (11%) |  |  |

| `reqAttune` | no | bool, str | 64/776 (8%) | True, by a Spellcaster, by a druid or ranger, by a dwarf, by a spellcaster, by a warlock, by a wizard |  |

| `miscTags` | no | list | 43/776 (6%) |  |  |

| `tier` | no | str | 43/776 (6%) | minor |  |

| `reprintedAs` | no | list | 40/776 (5%) |  |  |

| `hasRefs` | no | bool | 35/776 (5%) | True |  |

| `detail1` | no | str | 34/776 (4%) |  |  |

| `resist` | no | list | 22/776 (3%) |  |  |

| `charges` | no | int | 21/776 (3%) | 1, 10, 3, 4, 6, 7 |  |

| `recharge` | no | str | 21/776 (3%) | dawn |  |

| `rechargeAmount` | no | int, str | 20/776 (3%) | 3, {@dice 1d4}, {@dice 1d6 + 1}, {@dice 1d6 + 4}, {@dice 1d6} |  |

| `containerCapacity` | no | dict | 19/776 (2%) |  |  |

| `spellScrollLevel` | no | int | 19/776 (2%) | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |  |

| `optionalfeatures` | no | list | 18/776 (2%) |  |  |

| `weaponCategory` | no | str | 18/776 (2%) | martial, simple |  |

| `reqAttuneTags` | no | list | 17/776 (2%) |  |  |

| `baseItem` | no | str | 16/776 (2%) | longsword\|xphb, scale mail\|xphb, shield\|xphb, studded leather armor\|xphb, warhammer\|xphb |  |

| `dmg1` | no | str | 16/776 (2%) | 1d6, 1d8 |  |

| `dmgType` | no | str | 16/776 (2%) | B, R, Y |  |

| `property` | no | list | 16/776 (2%) |  |  |

| `ac` | no | int | 15/776 (2%) | 12, 14, 2 |  |

| `dmg2` | no | str | 15/776 (2%) | 1d10, 1d8 |  |

| `bonusAc` | no | str | 14/776 (2%) | +1, +2 |  |

| `detail2` | no | str | 14/776 (2%) | Aberrations, Beasts, Celestials, Constructs, Dragons, Elementals, Fey, Fiends, Giants, Humanoids, Monstrosities, Oozes, Plants, Undead |  |

| `mastery` | no | list | 13/776 (2%) |  |  |

| `staff` | no | bool | 13/776 (2%) | True |  |

| `stealth` | no | bool | 10/776 (1%) | True |  |

| `ability` | no | dict | 8/776 (1%) |  |  |

| `carryingCapacity` | no | int | 8/776 (1%) | 1320, 195, 225, 420, 450, 480, 540 |  |

| `packContents` | no | list | 8/776 (1%) |  |  |

| `speed` | no | int | 8/776 (1%) | 40, 50, 60 |  |

| `crew` | no | int | 7/776 (1%) | 1, 10, 20, 40, 60, 80 |  |

| `scfType` | no | str | 7/776 (1%) | arcane, druid, holy |  |

| `vehAc` | no | int | 7/776 (1%) | 11, 13, 15 |  |

| `vehHp` | no | int | 7/776 (1%) | 100, 300, 50, 500 |  |

| `vehSpeed` | no | float, int | 7/776 (1%) | 1, 1.5, 2, 2.5, 3, 4, 8 |  |

| `capCargo` | no | float, int | 6/776 (1%) | 0.5, 1, 10, 100, 150, 200 |  |

| `capPassenger` | no | int | 6/776 (1%) | 150, 20, 3, 6, 60 |  |

| `seeAlsoVehicle` | no | list | 6/776 (1%) |  |  |

| `bonusWeapon` | no | str | 5/776 (1%) | +1, +2, +3 |  |

| `group` | no | list | 5/776 (1%) |  |  |

| `otherSources` | no | list | 5/776 (1%) |  |  |

| `vehDmgThresh` | no | int | 5/776 (1%) | 10, 15, 20 |  |

| `focus` | no | bool, list | 4/776 (1%) | True |  |

| `barDimensions` | no | dict | 3/776 (0%) |  |  |

| `bonusSpellAttack` | no | str | 3/776 (0%) | +1, +2, +3 |  |

| `range` | no | str | 3/776 (0%) | 20/60, 30, 60/120 |  |

| `attachedSpells` | no | dict, list | 2/776 (0%) |  |  |

| `bonusSavingThrow` | no | str | 2/776 (0%) | +1 |  |

| `foundryActivities` | no | list | 2/776 (0%) |  |  |

| `foundrySystem` | no | dict | 2/776 (0%) |  |  |

| `conditionImmune` | no | list | 1/776 (0%) |  |  |

| `curse` | no | bool | 1/776 (0%) | True |  |

| `immune` | no | list | 1/776 (0%) |  |  |

| `light` | no | list | 1/776 (0%) |  |  |

| `modifySpeed` | no | dict | 1/776 (0%) |  |  |

| `system` | no | dict | 1/776 (0%) |  |  |

| `weightNote` | no | str | 1/776 (0%) | (full) |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `_merge`, `additionalEntries`, `additionalSources`, `age`, `alias`, `ammoType`, `atomicPackContents`, `basicRules`, `bonusAbilityCheck`, `bonusProficiencyBonus`, `bonusSavingThrowConcentration`, `bonusSpellSaveDc`, `bonusWeaponAttack`, `bonusWeaponDamage`, `crewMax`, `crewMin`, `critThreshold`, `dexterityMax`, `firearm`, `grantsLanguage`, `grantsProficiency`, `hasFluff`, `img`, `poison`, `poisonTypes`, `reach`, `reqAttuneAlt`, `seeAlsoDeck`, `sentient`, `shippingCost`, `srd`, `strength`, `tattoo`, `travelCost`, `typeAlt`, `valueRarity`, `vulnerable`

- Present here, not seen upstream: `foundryActivities`, `foundrySystem`



---

## ./rules/2024/baseline/2025-08-11_core/itemEntry.json

Detected entries: **7** (mode: largest-list:itemEntry)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entriesTemplate` | yes | list | 7/7 (100%) |  |  |

| `name` | yes | str | 7/7 (100%) | Armor of Resistance, Dragon Scale Mail, Grenade, Ioun Stone, Potion of Resistance, Ring of Resistance, Scroll of Protection |  |

| `source` | yes | str | 7/7 (100%) | XDMG |  |



---

## ./rules/2024/baseline/2025-08-11_core/itemFluff.json

Detected entries: **378** (mode: largest-list:itemFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 378/378 (100%) |  |  |

| `source` | yes | str | 378/378 (100%) | XDMG, XGE, XPHB |  |

| `images` | no | list | 321/378 (85%) |  |  |

| `_copy` | no | dict | 57/378 (15%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/itemGroup.json

Detected entries: **34** (mode: largest-list:itemGroup)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `items` | yes | list | 34/34 (100%) |  |  |

| `name` | yes | str | 34/34 (100%) |  |  |

| `page` | yes | int | 34/34 (100%) |  |  |

| `rarity` | yes | str | 34/34 (100%) | artifact, legendary, none, rare, uncommon, varies, very rare |  |

| `source` | yes | str | 34/34 (100%) | XDMG, XPHB |  |

| `srd52` | no | bool | 22/34 (65%) | True |  |

| `type` | no | str | 22/34 (65%) | AT\|XPHB, GS\|XPHB, GV\|XDMG, INS\|XPHB, MA\|XPHB, M\|XPHB, P\|XPHB, RD\|XDMG, RG\|XDMG, SCF\|XPHB, SC\|XPHB, WD\|XDMG |  |

| `basicRules2024` | no | bool | 20/34 (59%) | True |  |

| `hasFluffImages` | no | bool | 15/34 (44%) | True |  |

| `lootTables` | no | list | 14/34 (41%) |  |  |

| `entries` | no | list | 13/34 (38%) |  |  |

| `reqAttune` | no | bool, str | 13/34 (38%) | True, by a Spellcaster, by a bard, by a spellcaster, by a warlock |  |

| `wondrous` | no | bool | 12/34 (35%) | True |  |

| `itemsHidden` | no | bool | 11/34 (32%) | True |  |

| `weight` | no | float, int | 8/34 (24%) | 0.5, 1, 2, 4, 45, 5 |  |

| `miscTags` | no | list | 6/34 (18%) |  |  |

| `recharge` | no | str | 5/34 (15%) | dawn |  |

| `charges` | no | int | 4/34 (12%) | 5, 6 |  |

| `rechargeAmount` | no | str | 4/34 (12%) | {@dice 1d4 + 1}, {@dice 1d6} |  |

| `reqAttuneTags` | no | list | 4/34 (12%) |  |  |

| `focus` | no | list | 3/34 (9%) |  |  |

| `scfType` | no | str | 3/34 (9%) | arcane, druid, holy |  |

| `attachedSpells` | no | dict | 2/34 (6%) |  |  |

| `ability` | no | dict | 1/34 (3%) |  |  |

| `ac` | no | int | 1/34 (3%) | 14 |  |

| `baseItem` | no | str | 1/34 (3%) | scale mail\|xphb |  |

| `bonusAc` | no | str | 1/34 (3%) | +1 |  |

| `curse` | no | bool | 1/34 (3%) | True |  |

| `dmg1` | no | str | 1/34 (3%) | 1d6 |  |

| `dmg2` | no | str | 1/34 (3%) | 1d8 |  |

| `dmgType` | no | str | 1/34 (3%) | B |  |

| `hasRefs` | no | bool | 1/34 (3%) | True |  |

| `mastery` | no | list | 1/34 (3%) |  |  |

| `property` | no | list | 1/34 (3%) |  |  |

| `staff` | no | bool | 1/34 (3%) | True |  |

| `stealth` | no | bool | 1/34 (3%) | True |  |

| `weaponCategory` | no | str | 1/34 (3%) | simple |  |



---

## ./rules/2024/baseline/2025-08-11_core/itemMastery.json

Detected entries: **8** (mode: largest-list:itemMastery)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 8/8 (100%) | True |  |

| `entries` | yes | list | 8/8 (100%) |  |  |

| `name` | yes | str | 8/8 (100%) | Cleave, Graze, Nick, Push, Sap, Slow, Topple, Vex |  |

| `page` | yes | int | 8/8 (100%) | 214 |  |

| `source` | yes | str | 8/8 (100%) | XPHB |  |

| `srd52` | yes | bool | 8/8 (100%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/itemProperty.json

Detected entries: **12** (mode: largest-list:itemProperty)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `abbreviation` | yes | str | 12/12 (100%) | 2H, A, AF, BF, F, H, L, LD, R, RLD, T, V |  |

| `entries` | yes | list | 12/12 (100%) |  |  |

| `page` | yes | int | 12/12 (100%) | 213, 214, 72 |  |

| `source` | yes | str | 12/12 (100%) | XDMG, XPHB |  |

| `template` | yes | str | 12/12 (100%) | {{prop_name}}, {{prop_name}} (Range {{item.range}} ft.; {{item.ammoType}}), {{prop_name}} ({{item.dmg2}}), {{prop_name}} ({{item.range}} ft.), {{prop_name}} ({{item.range}} ft.; {{item.ammoType}}), {{prop_name}} ({{item.reload}} shots) |  |

| `basicRules2024` | no | bool | 9/12 (75%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/itemType.json

Detected entries: **28** (mode: largest-list:itemType)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `abbreviation` | yes | str | 28/28 (100%) |  |  |

| `name` | yes | str | 28/28 (100%) |  |  |

| `page` | yes | int | 28/28 (100%) | 213, 214, 215, 219, 220, 221, 222, 230, 231, 72 |  |

| `source` | yes | str | 28/28 (100%) | XDMG, XPHB |  |

| `basicRules2024` | no | bool | 22/28 (79%) | True |  |

| `entries` | no | list | 11/28 (39%) |  |  |

| `_copy` | no | dict | 1/28 (4%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/itemTypeAdditionalEntries.json

Detected entries: **2** (mode: largest-list:itemTypeAdditionalEntries)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `appliesTo` | yes | str | 2/2 (100%) | GS\|PHB, INS\|PHB |  |

| `entries` | yes | list | 2/2 (100%) |  |  |

| `name` | yes | str | 2/2 (100%) | Gaming Set, Instrument |  |

| `source` | yes | str | 2/2 (100%) | XGE |  |



---

## ./rules/2024/baseline/2025-08-11_core/language.json

Detected entries: **19** (mode: largest-list:language)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 19/19 (100%) | True |  |

| `entries` | yes | list | 19/19 (100%) |  |  |

| `name` | yes | str | 19/19 (100%) | Abyssal, Celestial, Common, Common Sign Language, Deep Speech, Draconic, Druidic, Dwarvish, Elvish, Giant, Gnomish, Goblin, Halfling, Infernal, Orc, Primordial, Sylvan, Thieves' Cant, Undercommon |  |

| `page` | yes | int | 19/19 (100%) | 37 |  |

| `source` | yes | str | 19/19 (100%) | XPHB |  |

| `srd52` | yes | bool | 19/19 (100%) | True |  |

| `type` | yes | str | 19/19 (100%) | rare, standard |  |

| `dialects` | no | list | 1/19 (5%) |  |  |

| `script` | no | str | 1/19 (5%) | Draconic |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `additionalSources`, `basicRules`, `fonts`, `hasFluffImages`, `otherSources`, `reprintedAs`, `srd`, `typicalSpeakers`



---

## ./rules/2024/baseline/2025-08-11_core/languageScript.json

Detected entries: **1** (mode: largest-list:languageScript)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `fonts` | yes | list | 1/1 (100%) |  |  |

| `name` | yes | str | 1/1 (100%) | Draconic |  |

| `source` | yes | str | 1/1 (100%) | XPHB |  |



---

## ./rules/2024/baseline/2025-08-11_core/legendaryGroup.json

Detected entries: **23** (mode: largest-list:legendaryGroup)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 23/23 (100%) |  |  |

| `page` | yes | int | 23/23 (100%) |  |  |

| `regionalEffects` | yes | list | 23/23 (100%) |  |  |

| `source` | yes | str | 23/23 (100%) | XMM |  |



---

## ./rules/2024/baseline/2025-08-11_core/magicItems.json

Detected entries: **24** (mode: largest-list:magicItems)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 24/24 (100%) |  |  |

| `page` | yes | int | 24/24 (100%) | 218, 326 |  |

| `source` | yes | str | 24/24 (100%) | XDMG |  |

| `table` | yes | list | 24/24 (100%) |  |  |

| `type` | yes | str | 24/24 (100%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/magicvariant.json

Detected entries: **18** (mode: largest-list:magicvariant)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `migrationVersion` | yes | int | 18/18 (100%) | 3 |  |

| `name` | yes | str | 18/18 (100%) | Ammunition of Slaying, Berserker Axe, Defender, Demon Armor, Dwarven Plate, Efreeti Chain, Energy Bow, Flame Tongue, Frost Brand, Hammer of Thunderbolts, Luck Blade, Mariner's Armor, Moonblade, Nine Lives Stealer, Oathbow, Sword of Vengeance, Sword of Wounding, Walloping Ammunition |  |

| `source` | yes | str | 18/18 (100%) | XDMG |  |

| `activities` | no | list | 13/18 (72%) |  |  |

| `effects` | no | list | 13/18 (72%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/monster.json

Detected entries: **522** (mode: largest-list:monster)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `hasToken` | yes | bool | 522/522 (100%) | True |  |

| `name` | yes | str | 522/522 (100%) |  |  |

| `size` | yes | list | 522/522 (100%) |  |  |

| `source` | yes | str | 522/522 (100%) | XDMG, XGE, XMM, XPHB |  |

| `type` | yes | dict, str | 522/522 (100%) | aberration, beast, celestial, construct, dragon, elemental, fey, fiend, giant, humanoid, monstrosity, ooze, plant, undead |  |

| `ac` | no | list | 521/522 (100%) |  |  |

| `alignment` | no | list | 521/522 (100%) |  |  |

| `cha` | no | int | 521/522 (100%) |  |  |

| `con` | no | int | 521/522 (100%) |  |  |

| `dex` | no | int | 521/522 (100%) |  |  |

| `hp` | no | dict | 521/522 (100%) |  |  |

| `int` | no | int | 521/522 (100%) |  |  |

| `page` | no | int | 521/522 (100%) |  |  |

| `passive` | no | int | 521/522 (100%) |  |  |

| `speed` | no | dict | 521/522 (100%) |  |  |

| `str` | no | int | 521/522 (100%) |  |  |

| `wis` | no | int | 521/522 (100%) |  |  |

| `action` | no | list | 519/522 (99%) |  |  |

| `hasFluffImages` | no | bool | 518/522 (99%) | True |  |

| `miscTags` | no | list | 518/522 (99%) |  |  |

| `damageTags` | no | list | 511/522 (98%) |  |  |

| `cr` | no | dict, str | 504/522 (97%) |  |  |

| `environment` | no | list | 503/522 (96%) |  |  |

| `hasFluff` | no | bool | 503/522 (96%) | True |  |

| `senses` | no | list | 406/522 (78%) |  |  |

| `senseTags` | no | list | 396/522 (76%) |  |  |

| `soundClip` | no | dict | 373/522 (71%) |  |  |

| `languages` | no | list | 372/522 (71%) |  |  |

| `languageTags` | no | list | 360/522 (69%) |  |  |

| `actionTags` | no | list | 339/522 (65%) |  |  |

| `trait` | no | list | 334/522 (64%) |  |  |

| `basicRules2024` | no | bool | 333/522 (64%) | True |  |

| `skill` | no | dict | 333/522 (64%) |  |  |

| `srd52` | no | bool | 332/522 (64%) | True |  |

| `treasure` | no | list | 299/522 (57%) |  |  |

| `traitTags` | no | list | 258/522 (49%) |  |  |

| `conditionInflict` | no | list | 236/522 (45%) |  |  |

| `savingThrowForced` | no | list | 231/522 (44%) |  |  |

| `save` | no | dict | 197/522 (38%) |  |  |

| `immune` | no | list | 196/522 (38%) |  |  |

| `conditionImmune` | no | list | 189/522 (36%) |  |  |

| `initiative` | no | dict | 187/522 (36%) |  |  |

| `otherSources` | no | list | 179/522 (34%) |  |  |

| `spellcasting` | no | list | 132/522 (25%) |  |  |

| `spellcastingTags` | no | list | 132/522 (25%) |  |  |

| `resist` | no | list | 123/522 (24%) |  |  |

| `bonus` | no | list | 111/522 (21%) |  |  |

| `group` | no | list | 111/522 (21%) |  |  |

| `savingThrowForcedSpell` | no | list | 105/522 (20%) |  |  |

| `conditionInflictSpell` | no | list | 76/522 (15%) |  |  |

| `gear` | no | list | 71/522 (14%) |  |  |

| `damageTagsSpell` | no | list | 70/522 (13%) |  |  |

| `legendary` | no | list | 43/522 (8%) |  |  |

| `reaction` | no | list | 42/522 (8%) |  |  |

| `dragonAge` | no | str | 41/522 (8%) | adult, ancient, wyrmling, young |  |

| `legendaryGroup` | no | dict | 35/522 (7%) |  |  |

| `legendaryActionsLair` | no | int | 34/522 (7%) | 4 |  |

| `familiar` | no | bool | 25/522 (5%) | True |  |

| `savingThrowForcedLegendary` | no | list | 23/522 (4%) |  |  |

| `vulnerable` | no | list | 22/522 (4%) |  |  |

| `pbNote` | no | str | 16/522 (3%) | equals its summoner's, equals your Proficiency Bonus |  |

| `_versions` | no | list | 12/522 (2%) |  |  |

| `summonedBySpell` | no | str | 12/522 (2%) | Animate Objects\|XPHB, Find Steed\|XPHB, Giant Insect\|XPHB, Summon Aberration\|XPHB, Summon Beast\|XPHB, Summon Celestial\|XPHB, Summon Construct\|XPHB, Summon Dragon\|XPHB, Summon Elemental\|XPHB, Summon Fey\|XPHB, Summon Fiend\|XPHB, Summon Undead\|XPHB |  |

| `summonedBySpellLevel` | no | int | 12/522 (2%) | 2, 3, 4, 5, 6 |  |

| `summonedByClass` | no | str | 4/522 (1%) | Ranger\|XPHB, Sorcerer\|PHB |  |

| `altArt` | no | list | 2/522 (0%) |  |  |

| `_copy` | no | dict | 1/522 (0%) |  |  |

| `attachedItems` | no | list | 1/522 (0%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `actionNote`, `alias`, `alignmentPrefix`, `basicRules`, `conditionInflictLegendary`, `damageTagsLegendary`, `dragonCastingColor`, `effects`, `isNamedCreature`, `isNpc`, `legendaryActions`, `legendaryHeader`, `level`, `migrationVersion`, `mythic`, `mythicHeader`, `prototypeToken`, `reactionHeader`, `reprintedAs`, `shortName`, `sizeNote`, `srd`, `tokenCredit`, `variant`



---

## ./rules/2024/baseline/2025-08-11_core/monsterFluff.json

Detected entries: **603** (mode: largest-list:monsterFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 603/603 (100%) |  |  |

| `source` | yes | str | 603/603 (100%) | XMM, XPHB |  |

| `_copy` | no | dict | 340/603 (56%) |  |  |

| `entries` | no | list | 248/603 (41%) |  |  |

| `images` | no | list | 247/603 (41%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/object.json

Detected entries: **10** (mode: largest-list:object)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `ac` | yes | int | 10/10 (100%) | 15, 19 |  |

| `entries` | yes | list | 10/10 (100%) |  |  |

| `hasToken` | yes | bool | 10/10 (100%) | True |  |

| `hp` | yes | int | 10/10 (100%) | 100, 150, 20, 200, 30, 50, 75 |  |

| `name` | yes | str | 10/10 (100%) | Ballista, Cannon, Flamethrower Coach, Keg Launcher, Lightning Cannon, Mangonel, Ram, Siege Tower, Suspended Cauldron, Trebuchet |  |

| `objectType` | yes | str | 10/10 (100%) | SW |  |

| `page` | yes | int | 10/10 (100%) | 96, 97 |  |

| `size` | yes | list | 10/10 (100%) |  |  |

| `source` | yes | str | 10/10 (100%) | XDMG |  |

| `actionEntries` | no | list | 9/10 (90%) |  |  |

| `hasFluffImages` | no | bool | 2/10 (20%) | True |  |

| `tokenCredit` | no | str | 2/10 (20%) | Games Workshop, Ruane Manning |  |



---

## ./rules/2024/baseline/2025-08-11_core/objectFluff.json

Detected entries: **2** (mode: largest-list:objectFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 2/2 (100%) |  |  |

| `name` | yes | str | 2/2 (100%) | Keg Launcher, Mangonel |  |

| `source` | yes | str | 2/2 (100%) | XDMG |  |



---

## ./rules/2024/baseline/2025-08-11_core/optionalfeature.json

Detected entries: **80** (mode: largest-list:optionalfeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 80/80 (100%) |  |  |

| `source` | yes | str | 80/80 (100%) | XGE, XPHB |  |

| `migrationVersion` | no | int | 50/80 (62%) | 3 |  |

| `activities` | no | list | 48/80 (60%) |  |  |

| `entries` | no | list | 30/80 (38%) |  |  |

| `featureType` | no | list | 30/80 (38%) |  |  |

| `page` | no | int | 30/80 (38%) | 155, 156, 157, 29, 30, 56, 57 |  |

| `prerequisite` | no | list | 20/80 (25%) |  |  |

| `effects` | no | list | 19/80 (24%) |  |  |

| `consumes` | no | dict | 8/80 (10%) |  |  |

| `additionalSpells` | no | list | 6/80 (8%) |  |  |

| `srd52` | no | bool | 5/80 (6%) | True |  |

| `reprintedAs` | no | list | 2/80 (2%) |  |  |

| `featProgression` | no | list | 1/80 (1%) |  |  |

| `system` | no | dict | 1/80 (1%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/race.json

Detected entries: **10** (mode: largest-list:race)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `creatureTypes` | yes | list | 10/10 (100%) |  |  |

| `edition` | yes | str | 10/10 (100%) | one |  |

| `entries` | yes | list | 10/10 (100%) |  |  |

| `hasFluff` | yes | bool | 10/10 (100%) | True |  |

| `hasFluffImages` | yes | bool | 10/10 (100%) | True |  |

| `name` | yes | str | 10/10 (100%) | Aasimar, Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, Orc, Tiefling |  |

| `page` | yes | int | 10/10 (100%) | 186, 187, 188, 189, 191, 192, 193, 194, 195, 197 |  |

| `size` | yes | list | 10/10 (100%) |  |  |

| `sizeEntry` | yes | dict | 10/10 (100%) |  |  |

| `soundClip` | yes | dict | 10/10 (100%) |  |  |

| `source` | yes | str | 10/10 (100%) | XPHB |  |

| `speed` | yes | int | 10/10 (100%) | 30, 35 |  |

| `basicRules2024` | no | bool | 9/10 (90%) | True |  |

| `darkvision` | no | int | 7/10 (70%) | 120, 60 |  |

| `srd52` | no | bool | 6/10 (60%) | True |  |

| `_versions` | no | list | 5/10 (50%) |  |  |

| `additionalSpells` | no | list | 3/10 (30%) |  |  |

| `resist` | no | list | 2/10 (20%) |  |  |

| `skillProficiencies` | no | list | 2/10 (20%) |  |  |

| `feats` | no | list | 1/10 (10%) |  |  |

| `traitTags` | no | list | 1/10 (10%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `ability`, `additionalSources`, `age`, `armorProficiencies`, `basicRules`, `blindsight`, `conditionImmune`, `creatureTypeTags`, `entryData`, `heightAndWeight`, `immune`, `languageProficiencies`, `lineage`, `migrationVersion`, `otherSources`, `reprintedAs`, `srd`, `toolProficiencies`, `vulnerable`, `weaponProficiencies`



---

## ./rules/2024/baseline/2025-08-11_core/raceFeature.json

Detected entries: **11** (mode: largest-list:raceFeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `migrationVersion` | yes | int | 11/11 (100%) | 3 |  |

| `name` | yes | str | 11/11 (100%) | Adrenaline Rush, Breath Weapon, Celestial Revelation, Draconic Flight, Dwarven Toughness, Healing Hands, Large Form, Luck, Powerful Build, Relentless Endurance, Stonecunning |  |

| `raceName` | yes | str | 11/11 (100%) | Aasimar, Dragonborn, Dwarf, Goliath, Halfling, Orc |  |

| `raceSource` | yes | str | 11/11 (100%) | XPHB |  |

| `source` | yes | str | 11/11 (100%) | XPHB |  |

| `activities` | no | list | 8/11 (73%) |  |  |

| `effects` | no | list | 7/11 (64%) |  |  |

| `system` | no | dict | 3/11 (27%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/raceFluff.json

Detected entries: **10** (mode: largest-list:raceFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 10/10 (100%) |  |  |

| `images` | yes | list | 10/10 (100%) |  |  |

| `name` | yes | str | 10/10 (100%) | Aasimar, Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, Orc, Tiefling |  |

| `source` | yes | str | 10/10 (100%) | XPHB |  |



---

## ./rules/2024/baseline/2025-08-11_core/reward.json

Detected entries: **19** (mode: largest-list:reward)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 19/19 (100%) |  |  |

| `name` | yes | str | 19/19 (100%) | Arcane Study Charm, Blessing of Health, Blessing of Magic Resistance, Blessing of Protection, Blessing of Understanding, Blessing of Valhalla, Blessing of Weapon Enhancement, Blessing of Wound Closure, Charm of Animal Conjuring, Charm of Darkvision, Charm of Feather Falling, Charm of Heroism, Charm of Restoration, Charm of Vitality, Charm of the Slayer, Observatory Charm, Reliquary Charm, Sanctuary Charm, Sanctum Charm |  |

| `page` | yes | int | 19/19 (100%) | 336, 343, 344, 345, 346, 98, 99 |  |

| `source` | yes | str | 19/19 (100%) | XDMG |  |

| `type` | yes | str | 19/19 (100%) | Blessing, Charm |  |

| `additionalSpells` | no | list | 8/19 (42%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/sense.json

Detected entries: **4** (mode: largest-list:sense)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 4/4 (100%) |  |  |

| `name` | yes | str | 4/4 (100%) | Blindsight, Darkvision, Tremorsense, Truesight |  |

| `page` | yes | int | 4/4 (100%) | 361, 365, 377 |  |

| `source` | yes | str | 4/4 (100%) | XPHB |  |

| `srd52` | yes | bool | 4/4 (100%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/skill.json

Detected entries: **18** (mode: largest-list:skill)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `ability` | yes | str | 18/18 (100%) | cha, dex, int, str, wis |  |

| `entries` | yes | list | 18/18 (100%) |  |  |

| `name` | yes | str | 18/18 (100%) | Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, Survival |  |

| `page` | yes | int | 18/18 (100%) | 14 |  |

| `source` | yes | str | 18/18 (100%) | XPHB |  |

| `srd52` | yes | bool | 18/18 (100%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/spell.json

Detected entries: **486** (mode: largest-list:spell)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 486/486 (100%) |  |  |

| `source` | yes | str | 486/486 (100%) | XGE, XPHB |  |

| `migrationVersion` | no | int | 288/486 (59%) | 3 |  |

| `activities` | no | list | 287/486 (59%) |  |  |

| `components` | no | dict | 198/486 (41%) |  |  |

| `duration` | no | list | 198/486 (41%) |  |  |

| `entries` | no | list | 198/486 (41%) |  |  |

| `level` | no | int | 198/486 (41%) | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |  |

| `page` | no | int | 198/486 (41%) |  |  |

| `range` | no | dict | 198/486 (41%) |  |  |

| `school` | no | str | 198/486 (41%) | A, C, D, E, I, N, T, V |  |

| `time` | no | list | 198/486 (41%) |  |  |

| `effects` | no | list | 171/486 (35%) |  |  |

| `miscTags` | no | list | 155/486 (32%) |  |  |

| `areaTags` | no | list | 127/486 (26%) |  |  |

| `basicRules2024` | no | bool | 99/486 (20%) | True |  |

| `srd52` | no | bool, str | 99/486 (20%) | Arcane Hand, Arcane Sword, Floating Disk, Private Sanctum, Tiny Hut, True |  |

| `damageInflict` | no | list | 86/486 (18%) |  |  |

| `savingThrow` | no | list | 86/486 (18%) |  |  |

| `entriesHigherLevel` | no | list | 69/486 (14%) |  |  |

| `otherSources` | no | list | 43/486 (9%) |  |  |

| `system` | no | dict | 33/486 (7%) |  |  |

| `conditionInflict` | no | list | 30/486 (6%) |  |  |

| `hasFluffImages` | no | bool | 23/486 (5%) | True |  |

| `meta` | no | dict | 17/486 (3%) |  |  |

| `spellAttack` | no | list | 16/486 (3%) |  |  |

| `abilityCheck` | no | list | 13/486 (3%) |  |  |

| `scalingLevelDice` | no | dict, list | 13/486 (3%) |  |  |

| `affectsCreatureType` | no | list | 11/486 (2%) |  |  |

| `reprintedAs` | no | list | 10/486 (2%) |  |  |

| `damageResist` | no | list | 6/486 (1%) |  |  |

| `damageImmune` | no | list | 5/486 (1%) |  |  |

| `additionalSources` | no | list | 1/486 (0%) |  |  |

| `alias` | no | list | 1/486 (0%) |  |  |

| `damageVulnerable` | no | list | 1/486 (0%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `basicRules`, `conditionImmune`, `hasFluff`, `srd`



---

## ./rules/2024/baseline/2025-08-11_core/spellFluff.json

Detected entries: **61** (mode: largest-list:spellFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 61/61 (100%) |  |  |

| `name` | yes | str | 61/61 (100%) |  |  |

| `source` | yes | str | 61/61 (100%) | XGE, XPHB |  |



---

## ./rules/2024/baseline/2025-08-11_core/status.json

Detected entries: **2** (mode: largest-list:status)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 2/2 (100%) | True |  |

| `entries` | yes | list | 2/2 (100%) |  |  |

| `name` | yes | str | 2/2 (100%) | Concentration, Surprised |  |

| `page` | yes | int | 2/2 (100%) | 363, 376 |  |

| `source` | yes | str | 2/2 (100%) | XPHB |  |

| `srd52` | yes | bool | 2/2 (100%) | True |  |



---

## ./rules/2024/baseline/2025-08-11_core/subclass.json

Detected entries: **79** (mode: largest-list:subclass)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 79/79 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 79/79 (100%) | PHB, XPHB |  |

| `edition` | yes | str | 79/79 (100%) | classic, one |  |

| `name` | yes | str | 79/79 (100%) |  |  |

| `page` | yes | int | 79/79 (100%) |  |  |

| `shortName` | yes | str | 79/79 (100%) |  |  |

| `source` | yes | str | 79/79 (100%) | XGE, XPHB |  |

| `subclassFeatures` | yes | list | 79/79 (100%) |  |  |

| `hasFluffImages` | no | bool | 60/79 (76%) | True |  |

| `additionalSpells` | no | list | 48/79 (61%) |  |  |

| `hasFluff` | no | bool | 21/79 (27%) | True |  |

| `srd52` | no | bool | 12/79 (15%) | True |  |

| `basicRules2024` | no | bool | 11/79 (14%) | True |  |

| `otherSources` | no | list | 4/79 (5%) |  |  |

| `reprintedAs` | no | list | 4/79 (5%) |  |  |

| `subclassTableGroups` | no | list | 4/79 (5%) |  |  |

| `optionalfeatureProgression` | no | list | 3/79 (4%) |  |  |

| `spellcastingAbility` | no | str | 3/79 (4%) | int, wis |  |

| `cantripProgression` | no | list | 2/79 (3%) |  |  |

| `casterProgression` | no | str | 2/79 (3%) | 1/3 |  |

| `preparedSpellsChange` | no | str | 2/79 (3%) | level |  |

| `preparedSpellsProgression` | no | list | 2/79 (3%) |  |  |

| `featProgression` | no | list | 1/79 (1%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `advancement`, `basicRules`, `fluff`, `isReprinted`, `migrationVersion`, `spellsKnownProgression`, `srd`



---

## ./rules/2024/baseline/2025-08-11_core/subclassFeature.json

Detected entries: **509** (mode: largest-list:subclassFeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 509/509 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 509/509 (100%) | PHB, XPHB |  |

| `entries` | yes | list | 509/509 (100%) |  |  |

| `level` | yes | int | 509/509 (100%) | 1, 10, 11, 13, 14, 15, 17, 18, 2, 20, 3, 6, 7, 8, 9 |  |

| `name` | yes | str | 509/509 (100%) |  |  |

| `page` | yes | int | 509/509 (100%) |  |  |

| `source` | yes | str | 509/509 (100%) | XGE, XPHB |  |

| `subclassShortName` | yes | str | 509/509 (100%) |  |  |

| `subclassSource` | yes | str | 509/509 (100%) | XGE, XPHB |  |

| `header` | no | int | 389/509 (76%) | 1, 2 |  |

| `srd52` | no | bool | 70/509 (14%) | True |  |

| `basicRules2024` | no | bool | 65/509 (13%) | True |  |

| `consumes` | no | dict | 51/509 (10%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/subclassFluff.json

Detected entries: **72** (mode: largest-list:subclassFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 72/72 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 72/72 (100%) | PHB, XPHB |  |

| `name` | yes | str | 72/72 (100%) |  |  |

| `shortName` | yes | str | 72/72 (100%) |  |  |

| `source` | yes | str | 72/72 (100%) | XGE, XPHB |  |

| `images` | no | list | 60/72 (83%) |  |  |

| `entries` | no | list | 21/72 (29%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/table.json

Detected entries: **423** (mode: largest-list:table)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `colStyles` | yes | list | 423/423 (100%) |  |  |

| `name` | yes | str | 423/423 (100%) |  |  |

| `rows` | yes | list | 423/423 (100%) |  |  |

| `source` | yes | str | 423/423 (100%) | XDMG, XGE, XMM, XPHB, XScreen |  |

| `colLabels` | no | list | 415/423 (98%) |  |  |

| `caption` | no | str | 412/423 (97%) |  |  |

| `page` | no | int | 406/423 (96%) |  |  |

| `chapter` | no | dict | 307/423 (73%) |  |  |

| `type` | no | str | 98/423 (23%) | table |  |

| `basicRules2024` | no | bool | 50/423 (12%) | False, True |  |

| `srd52` | no | bool | 50/423 (12%) | False, True |  |

| `footnotes` | no | list | 31/423 (7%) |  |  |

| `colLabelRows` | no | list | 7/423 (2%) |  |  |

| `isNameGenerator` | no | bool | 7/423 (2%) | True |  |

| `parentEntity` | no | dict | 3/423 (1%) |  |  |

| `basicRules` | no | bool | 1/423 (0%) | False |  |

| `srd` | no | bool | 1/423 (0%) | False |  |



---

## ./rules/2024/baseline/2025-08-11_core/tableGroup.json

Detected entries: **7** (mode: largest-list:tableGroup)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `chapter` | yes | dict | 7/7 (100%) |  |  |

| `name` | yes | str | 7/7 (100%) | Background; I became..., Class Training; I became..., Random Magic Items - Arcana, Random Magic Items - Armaments, Random Magic Items - Implements, Random Magic Items - Relics, Tables; Weather |  |

| `source` | yes | str | 7/7 (100%) | XDMG, XGE, XScreen |  |

| `tables` | yes | list | 7/7 (100%) |  |  |

| `type` | yes | str | 7/7 (100%) | tableGroup |  |

| `page` | no | int | 6/7 (86%) | 326, 328, 329, 330, 64, 66 |  |



---

## ./rules/2024/baseline/2025-08-11_core/trap.json

Detected entries: **20** (mode: largest-list:trap)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 20/20 (100%) |  |  |

| `name` | yes | str | 20/20 (100%) | Bear Trap, Collapsing Roof, Crossbow Trap, Falling Net, Falling Portcullis, Fiery Blast Trap, Fire-Casting Statue, Hidden Pit, Net Trap, Path of Blades, Pit Trap, Poison Needle Trap, Poisoned Darts, Poisoned Needle, Poisoned Tempest, Rolling Stone, Scything Blade Trap, Sleep of Ages Trap, Sphere of Crushing Doom, Spiked Pit |  |

| `page` | yes | int | 20/20 (100%) | 100, 101, 102, 103, 113, 114, 118, 119, 120 |  |

| `rating` | yes | list | 20/20 (100%) |  |  |

| `source` | yes | str | 20/20 (100%) | XDMG, XGE |  |

| `trapHazType` | yes | str | 20/20 (100%) | CMPX, SMPL, TRP |  |

| `trigger` | yes | list | 20/20 (100%) |  |  |

| `countermeasures` | no | list | 12/20 (60%) |  |  |

| `effect` | no | list | 9/20 (45%) |  |  |

| `duration` | no | list | 8/20 (40%) |  |  |

| `srd52` | no | bool | 8/20 (40%) | True |  |

| `eActive` | no | list | 3/20 (15%) |  |  |

| `eDynamic` | no | list | 3/20 (15%) |  |  |

| `initiative` | no | int | 3/20 (15%) | 1, 3 |  |

| `eConstant` | no | list | 1/20 (5%) |  |  |

| `hasFluffImages` | no | bool | 1/20 (5%) | True |  |

| `initiativeNote` | no | str | 1/20 (5%) | but see the dynamic element below |  |



---

## ./rules/2024/baseline/2025-08-11_core/trapFluff.json

Detected entries: **1** (mode: largest-list:trapFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 1/1 (100%) |  |  |

| `name` | yes | str | 1/1 (100%) | Poisoned Darts |  |

| `source` | yes | str | 1/1 (100%) | XDMG |  |



---

## ./rules/2024/baseline/2025-08-11_core/variantrule.json

Detected entries: **149** (mode: largest-list:variantrule)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 149/149 (100%) |  |  |

| `name` | yes | str | 149/149 (100%) |  |  |

| `ruleType` | yes | str | 149/149 (100%) | C, O, V, VO |  |

| `source` | yes | str | 149/149 (100%) | XDMG, XGE, XPHB, XScreen |  |

| `page` | no | int | 148/149 (99%) |  |  |

| `basicRules2024` | no | bool | 117/149 (79%) | True |  |

| `srd52` | no | bool | 117/149 (79%) | True |  |

| `type` | no | str | 34/149 (23%) | entries, section |  |

| `reprintedAs` | no | list | 2/149 (1%) |  |  |



---

## ./rules/2024/baseline/2025-08-11_core/vehicle.json

Detected entries: **1** (mode: largest-list:vehicle)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `ac` | yes | int | 1/1 (100%) | 20 |  |

| `capCrew` | yes | int | 1/1 (100%) | 1 |  |

| `capPassenger` | yes | int | 1/1 (100%) | 1 |  |

| `entries` | yes | list | 1/1 (100%) |  |  |

| `hasFluffImages` | yes | bool | 1/1 (100%) | True |  |

| `hasToken` | yes | bool | 1/1 (100%) | True |  |

| `hp` | yes | int | 1/1 (100%) | 200 |  |

| `immune` | yes | list | 1/1 (100%) |  |  |

| `name` | yes | str | 1/1 (100%) | Apparatus of Kwalish |  |

| `page` | yes | int | 1/1 (100%) | 229 |  |

| `size` | yes | str | 1/1 (100%) | L |  |

| `source` | yes | str | 1/1 (100%) | XDMG |  |

| `speed` | yes | dict | 1/1 (100%) |  |  |

| `srd` | yes | str | 1/1 (100%) | Apparatus of the Crab |  |

| `terrain` | yes | list | 1/1 (100%) |  |  |

| `vehicleType` | yes | str | 1/1 (100%) | OBJECT |  |



---

## ./rules/2024/baseline/2025-08-11_core/vehicleFluff.json

Detected entries: **1** (mode: largest-list:vehicleFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 1/1 (100%) |  |  |

| `name` | yes | str | 1/1 (100%) | Apparatus of Kwalish |  |

| `source` | yes | str | 1/1 (100%) | XDMG |  |



---

## ./rules/2024/book.json

Detected entries: **2** (mode: largest-list:book)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `group` | yes | str | 2/2 (100%) | core |  |

| `id` | yes | str | 2/2 (100%) | XPHB |  |

| `name` | yes | str | 2/2 (100%) | Player's Handbook (2024) |  |

| `published` | yes | str | 2/2 (100%) | 2024-09-17 |  |

| `source` | yes | str | 2/2 (100%) | XPHB |  |

| `author` | no | str | 1/2 (50%) | Wizards RPG Team |  |

| `contents` | no | list | 1/2 (50%) |  |  |

| `cover` | no | dict | 1/2 (50%) |  |  |



---

## ./rules/2024/class.json

Detected entries: **22** (mode: largest-list:class)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 22/22 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `source` | yes | str | 22/22 (100%) | XPHB |  |

| `basicRules2024` | no | bool | 12/22 (55%) | True |  |

| `classFeatures` | no | list | 12/22 (55%) |  |  |

| `classTableGroups` | no | list | 12/22 (55%) |  |  |

| `edition` | no | str | 12/22 (55%) | one |  |

| `featProgression` | no | list | 12/22 (55%) |  |  |

| `hasFluff` | no | bool | 12/22 (55%) | True |  |

| `hasFluffImages` | no | bool | 12/22 (55%) | True |  |

| `hd` | no | dict | 12/22 (55%) |  |  |

| `multiclassing` | no | dict | 12/22 (55%) |  |  |

| `page` | no | int | 12/22 (55%) | 100, 108, 118, 128, 138, 152, 164, 50, 58, 68, 78, 90 |  |

| `primaryAbility` | no | list | 12/22 (55%) |  |  |

| `proficiency` | no | list | 12/22 (55%) |  |  |

| `srd52` | no | bool | 12/22 (55%) | True |  |

| `startingEquipment` | no | dict | 12/22 (55%) |  |  |

| `startingProficiencies` | no | dict | 12/22 (55%) |  |  |

| `subclassTitle` | no | str | 12/22 (55%) | Barbarian Subclass, Bard Subclass, Cleric Subclass, Druid Subclass, Fighter Subclass, Monk Subclass, Paladin Subclass, Ranger Subclass, Rogue Subclass, Sorcerer Subclass, Warlock Subclass, Wizard Subclass |  |

| `advancement` | no | list | 10/22 (45%) |  |  |

| `migrationVersion` | no | int | 10/22 (45%) | 3 |  |

| `casterProgression` | no | str | 8/22 (36%) | artificer, full, pact |  |

| `preparedSpellsChange` | no | str | 8/22 (36%) | level, restLong |  |

| `preparedSpellsProgression` | no | list | 8/22 (36%) |  |  |

| `spellcastingAbility` | no | str | 8/22 (36%) | cha, int, wis |  |

| `cantripProgression` | no | list | 6/22 (27%) |  |  |

| `additionalSpells` | no | list | 5/22 (23%) |  |  |

| `optionalfeatureProgression` | no | list | 2/22 (9%) |  |  |

| `spellsKnownProgressionFixed` | no | list | 1/22 (5%) |  |  |

| `spellsKnownProgressionFixedAllowLowerLevel` | no | bool | 1/22 (5%) | True |  |

| `spellsKnownProgressionFixedByLevel` | no | dict | 1/22 (5%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `basicRules`, `isSidekick`, `otherSources`, `preparedSpells`, `reprintedAs`, `spellsKnownProgression`, `srd`



---

## ./rules/2024/classFeature.json

Detected entries: **402** (mode: largest-list:classFeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 402/402 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 402/402 (100%) | XPHB |  |

| `level` | yes | int | 402/402 (100%) | 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9 |  |

| `name` | yes | str | 402/402 (100%) |  |  |

| `source` | yes | str | 402/402 (100%) | XPHB |  |

| `basicRules2024` | no | bool | 283/402 (70%) | True |  |

| `entries` | no | list | 283/402 (70%) |  |  |

| `page` | no | int | 283/402 (70%) |  |  |

| `srd52` | no | bool | 283/402 (70%) | True |  |

| `migrationVersion` | no | int | 118/402 (29%) | 3 |  |

| `activities` | no | list | 65/402 (16%) |  |  |

| `effects` | no | list | 37/402 (9%) |  |  |

| `isIgnored` | no | bool | 24/402 (6%) | True |  |

| `entryData` | no | dict | 16/402 (4%) |  |  |

| `consumes` | no | dict | 12/402 (3%) |  |  |

| `header` | no | int | 12/402 (3%) | 2 |  |

| `system` | no | dict | 11/402 (3%) |  |  |

| `subEntities` | no | dict | 2/402 (0%) |  |  |



---

## ./rules/2024/classFluff.json

Detected entries: **12** (mode: largest-list:classFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 12/12 (100%) |  |  |

| `images` | yes | list | 12/12 (100%) |  |  |

| `name` | yes | str | 12/12 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `source` | yes | str | 12/12 (100%) | XPHB |  |



---

## ./rules/2024/condition.json

Detected entries: **15** (mode: largest-list:condition)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 15/15 (100%) | True |  |

| `entries` | yes | list | 15/15 (100%) |  |  |

| `name` | yes | str | 15/15 (100%) | Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious |  |

| `page` | yes | int | 15/15 (100%) | 361, 365, 367, 369, 370, 371, 372, 373, 376 |  |

| `source` | yes | str | 15/15 (100%) | XPHB |  |

| `srd52` | yes | bool | 15/15 (100%) | True |  |



---

## ./rules/2024/feat.json

Detected entries: **117** (mode: largest-list:feat)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 117/117 (100%) |  |  |

| `source` | yes | str | 117/117 (100%) | XPHB |  |

| `category` | no | str | 77/117 (66%) | EB, FS, FS:P, FS:R, G, O |  |

| `entries` | no | list | 77/117 (66%) |  |  |

| `page` | no | int | 77/117 (66%) | 110, 120, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211 |  |

| `prerequisite` | no | list | 67/117 (57%) |  |  |

| `ability` | no | list | 55/117 (47%) |  |  |

| `migrationVersion` | no | int | 40/117 (34%) | 3 |  |

| `activities` | no | list | 27/117 (23%) |  |  |

| `effects` | no | list | 21/117 (18%) |  |  |

| `srd52` | no | bool | 19/117 (16%) | True |  |

| `basicRules2024` | no | bool | 17/117 (15%) | True |  |

| `additionalSpells` | no | list | 8/117 (7%) |  |  |

| `hasFluffImages` | no | bool | 8/117 (7%) | True |  |

| `repeatable` | no | bool | 4/117 (3%) | True |  |

| `repeatableHidden` | no | bool | 4/117 (3%) | True |  |

| `skillProficiencies` | no | list | 4/117 (3%) |  |  |

| `toolProficiencies` | no | list | 4/117 (3%) |  |  |

| `armorProficiencies` | no | list | 3/117 (3%) |  |  |

| `senses` | no | list | 3/117 (3%) |  |  |

| `system` | no | dict | 3/117 (3%) |  |  |

| `expertise` | no | list | 2/117 (2%) |  |  |

| `weaponProficiencies` | no | list | 2/117 (2%) |  |  |

| `_versions` | no | list | 1/117 (1%) |  |  |

| `resist` | no | list | 1/117 (1%) |  |  |

| `savingThrowProficiencies` | no | list | 1/117 (1%) |  |  |

| `skillToolLanguageProficiencies` | no | list | 1/117 (1%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `additionalSources`, `bonusSenses`, `languageProficiencies`, `optionalfeatureProgression`, `reprintedAs`, `srd`, `traitTags`



---

## ./rules/2024/featFluff.json

Detected entries: **8** (mode: largest-list:featFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 8/8 (100%) |  |  |

| `name` | yes | str | 8/8 (100%) | Boon of Fate, Boon of Skill, Fey-Touched, Healer, Poisoner, Ritual Caster, Two-Weapon Fighting, Weapon Master |  |

| `source` | yes | str | 8/8 (100%) | XPHB |  |



---

## ./rules/2024/hazard.json

Detected entries: **5** (mode: largest-list:hazard)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 5/5 (100%) |  |  |

| `name` | yes | str | 5/5 (100%) | Burning, Dehydration, Falling, Malnutrition, Suffocation |  |

| `page` | yes | int | 5/5 (100%) | 362, 365, 367, 371, 376 |  |

| `source` | yes | str | 5/5 (100%) | XPHB |  |



---

## ./rules/2024/hazardFluff.json

Top-level type: **dict**


Top-level keys (sample): `hazardFluff`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/item.json

Detected entries: **520** (mode: largest-list:item)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 520/520 (100%) |  |  |

| `source` | yes | str | 520/520 (100%) | XDMG, XPHB |  |

| `page` | no | int | 496/520 (95%) |  |  |

| `rarity` | no | str | 496/520 (95%) | artifact, common, legendary, none, rare, uncommon, very rare |  |

| `srd52` | no | bool, str | 489/520 (94%) | Apparatus of the Crab, Dragon Orb, Efficient Quiver, Feather Token, Anchor, Feather Token, Bird, Feather Token, Fan, Feather Token, Swan Boat, Feather Token, Tree, Feather Token, Whip, Handy Haversack, Instant Fortress, Iron Bands of Binding, Marvelous Pigments, Mysterious Deck, True |  |

| `basicRules2024` | no | bool | 457/520 (88%) | True |  |

| `entries` | no | list | 443/520 (85%) |  |  |

| `type` | no | str | 325/520 (62%) |  |  |

| `lootTables` | no | list | 278/520 (53%) |  |  |

| `weight` | no | float, int | 254/520 (49%) |  |  |

| `hasFluffImages` | no | bool | 223/520 (43%) | True |  |

| `value` | no | int | 177/520 (34%) |  |  |

| `wondrous` | no | bool | 172/520 (33%) | True |  |

| `reqAttune` | no | bool, str | 152/520 (29%) | True, by a bard, cleric, druid, sorcerer, warlock, or wizard, by a bard, cleric, or druid, by a cleric or paladin, by a cleric, druid, or paladin, by a cleric, druid, or warlock, by a druid, by a druid, sorcerer, warlock, or wizard, by a dwarf, by a sorcerer, warlock, or wizard, by a spellcaster, by a wizard |  |

| `miscTags` | no | list | 89/520 (17%) |  |  |

| `attachedSpells` | no | dict, list | 71/520 (14%) |  |  |

| `charges` | no | int | 51/520 (10%) | 10, 12, 20, 24, 3, 4, 5, 50, 6, 7 |  |

| `recharge` | no | str | 48/520 (9%) | dawn |  |

| `optionalfeatures` | no | list | 47/520 (9%) |  |  |

| `rechargeAmount` | no | int, str | 46/520 (9%) | 1, 3, {@dice 1d3}, {@dice 1d4 + 1}, {@dice 1d4 + 3}, {@dice 1d4}, {@dice 1d6 + 1}, {@dice 1d6 + 4}, {@dice 1d6}, {@dice 1d8 + 2}, {@dice 2d8 + 4}, {@dice 4d6 + 2} |  |

| `hasRefs` | no | bool | 44/520 (8%) | True |  |

| `resist` | no | list | 42/520 (8%) |  |  |

| `ability` | no | dict | 29/520 (6%) |  |  |

| `baseItem` | no | str | 29/520 (6%) | dagger\|xphb, greatclub\|xphb, javelin\|xphb, longsword\|xphb, mace\|xphb, plate armor\|xphb, quarterstaff\|xphb, scale mail\|xphb, scimitar\|xphb, shield\|xphb, studded leather armor\|xphb, trident\|xphb, warhammer\|xphb |  |

| `activities` | no | list | 24/520 (5%) |  |  |

| `dmg1` | no | str | 24/520 (5%) | 1d4, 1d6, 1d8 |  |

| `dmgType` | no | str | 24/520 (5%) | B, P, R, S, Y |  |

| `mastery` | no | list | 24/520 (5%) |  |  |

| `migrationVersion` | no | int | 24/520 (5%) | 3 |  |

| `reqAttuneTags` | no | list | 24/520 (5%) |  |  |

| `weaponCategory` | no | str | 24/520 (5%) | martial, simple |  |

| `bonusAc` | no | str | 21/520 (4%) | +1, +2, +5 |  |

| `property` | no | list | 21/520 (4%) |  |  |

| `detail1` | no | str | 20/520 (4%) | amethyst, black, blue, brass, bronze, citrine, copper, garnet, gold, green, jade, jet, pearl, red, sapphire, silver, spinel, topaz, tourmaline, white |  |

| `containerCapacity` | no | dict | 19/520 (4%) |  |  |

| `ac` | no | int | 18/520 (3%) | 12, 14, 18, 2 |  |

| `light` | no | list | 17/520 (3%) |  |  |

| `dmg2` | no | str | 16/520 (3%) | 1d10, 1d8 |  |

| `poison` | no | bool | 14/520 (3%) | True |  |

| `bonusWeapon` | no | str | 13/520 (2%) | +1, +2, +3 |  |

| `poisonTypes` | no | list | 13/520 (2%) |  |  |

| `staff` | no | bool | 13/520 (2%) | True |  |

| `modifySpeed` | no | dict | 11/520 (2%) |  |  |

| `otherSources` | no | list | 11/520 (2%) |  |  |

| `stealth` | no | bool | 11/520 (2%) | True |  |

| `spellScrollLevel` | no | int | 10/520 (2%) | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |  |

| `bonusSpellAttack` | no | str | 9/520 (2%) | +1, +2, +3 |  |

| `carryingCapacity` | no | int | 8/520 (2%) | 1320, 195, 225, 420, 450, 480, 540 |  |

| `packContents` | no | list | 8/520 (2%) |  |  |

| `speed` | no | int | 8/520 (2%) | 40, 50, 60 |  |

| `crew` | no | int | 7/520 (1%) | 1, 10, 20, 40, 60, 80 |  |

| `effects` | no | list | 7/520 (1%) |  |  |

| `seeAlsoVehicle` | no | list | 7/520 (1%) |  |  |

| `vehAc` | no | int | 7/520 (1%) | 11, 13, 15 |  |

| `vehHp` | no | int | 7/520 (1%) | 100, 300, 50, 500 |  |

| `vehSpeed` | no | float, int | 7/520 (1%) | 1, 1.5, 2, 2.5, 3, 4, 8 |  |

| `bonusSavingThrow` | no | str | 6/520 (1%) | +1, +2 |  |

| `capCargo` | no | float, int | 6/520 (1%) | 0.5, 1, 10, 100, 150, 200 |  |

| `capPassenger` | no | int | 6/520 (1%) | 150, 20, 3, 6, 60 |  |

| `range` | no | str | 6/520 (1%) | 20/60, 30/120, 60/120 |  |

| `group` | no | list | 5/520 (1%) |  |  |

| `scfType` | no | str | 5/520 (1%) | druid, holy |  |

| `vehDmgThresh` | no | int | 5/520 (1%) | 10, 15, 20 |  |

| `grantsProficiency` | no | bool | 2/520 (0%) | True |  |

| `immune` | no | list | 2/520 (0%) |  |  |

| `seeAlsoDeck` | no | list | 2/520 (0%) |  |  |

| `alias` | no | list | 1/520 (0%) |  |  |

| `bonusAbilityCheck` | no | str | 1/520 (0%) | +1 |  |

| `bonusProficiencyBonus` | no | str | 1/520 (0%) | +1 |  |

| `bonusSpellSaveDc` | no | str | 1/520 (0%) | +2 |  |

| `bonusWeaponDamage` | no | str | 1/520 (0%) | +2 |  |

| `conditionImmune` | no | list | 1/520 (0%) |  |  |

| `curse` | no | bool | 1/520 (0%) | True |  |

| `focus` | no | list | 1/520 (0%) |  |  |

| `strength` | no | str | 1/520 (0%) | 15 |  |

| `system` | no | dict | 1/520 (0%) |  |  |

| `weightNote` | no | str | 1/520 (0%) | (full) |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `_merge`, `additionalEntries`, `additionalSources`, `age`, `ammoType`, `atomicPackContents`, `barDimensions`, `basicRules`, `bonusSavingThrowConcentration`, `bonusWeaponAttack`, `crewMax`, `crewMin`, `critThreshold`, `detail2`, `dexterityMax`, `firearm`, `grantsLanguage`, `hasFluff`, `img`, `reach`, `reprintedAs`, `reqAttuneAlt`, `sentient`, `shippingCost`, `srd`, `tattoo`, `tier`, `travelCost`, `typeAlt`, `valueRarity`, `vulnerable`



---

## ./rules/2024/itemEntry.json

Top-level type: **dict**


Top-level keys (sample): `itemEntry`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/itemFluff.json

Detected entries: **54** (mode: largest-list:itemFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 54/54 (100%) |  |  |

| `name` | yes | str | 54/54 (100%) |  |  |

| `source` | yes | str | 54/54 (100%) | XPHB |  |



---

## ./rules/2024/itemGroup.json

Detected entries: **25** (mode: largest-list:itemGroup)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `items` | yes | list | 25/25 (100%) |  |  |

| `name` | yes | str | 25/25 (100%) |  |  |

| `page` | yes | int | 25/25 (100%) |  |  |

| `rarity` | yes | str | 25/25 (100%) | legendary, none, rare, uncommon, varies, very rare |  |

| `source` | yes | str | 25/25 (100%) | XDMG, XPHB |  |

| `srd52` | no | bool | 22/25 (88%) | True |  |

| `basicRules2024` | no | bool | 20/25 (80%) | True |  |

| `type` | no | str | 16/25 (64%) | AT\|XPHB, GS\|XPHB, GV\|XDMG, INS\|XPHB, MA\|XPHB, P\|XPHB, RG\|XDMG, SCF\|XPHB, SC\|XPHB, WD\|XDMG |  |

| `hasFluffImages` | no | bool | 12/25 (48%) | True |  |

| `entries` | no | list | 9/25 (36%) |  |  |

| `wondrous` | no | bool | 9/25 (36%) | True |  |

| `itemsHidden` | no | bool | 8/25 (32%) | True |  |

| `lootTables` | no | list | 8/25 (32%) |  |  |

| `reqAttune` | no | bool, str | 7/25 (28%) | True, by a spellcaster |  |

| `weight` | no | float, int | 6/25 (24%) | 0.5, 1, 45, 5 |  |

| `miscTags` | no | list | 4/25 (16%) |  |  |

| `focus` | no | list | 3/25 (12%) |  |  |

| `scfType` | no | str | 3/25 (12%) | arcane, druid, holy |  |

| `recharge` | no | str | 2/25 (8%) | dawn |  |

| `ac` | no | int | 1/25 (4%) | 14 |  |

| `baseItem` | no | str | 1/25 (4%) | scale mail\|xphb |  |

| `bonusAc` | no | str | 1/25 (4%) | +1 |  |

| `charges` | no | int | 1/25 (4%) | 5 |  |

| `curse` | no | bool | 1/25 (4%) | True |  |

| `hasRefs` | no | bool | 1/25 (4%) | True |  |

| `rechargeAmount` | no | str | 1/25 (4%) | {@dice 1d4 + 1} |  |

| `reqAttuneTags` | no | list | 1/25 (4%) |  |  |

| `stealth` | no | bool | 1/25 (4%) | True |  |



---

## ./rules/2024/itemMastery.json

Detected entries: **8** (mode: largest-list:itemMastery)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 8/8 (100%) | True |  |

| `entries` | yes | list | 8/8 (100%) |  |  |

| `name` | yes | str | 8/8 (100%) | Cleave, Graze, Nick, Push, Sap, Slow, Topple, Vex |  |

| `page` | yes | int | 8/8 (100%) | 214 |  |

| `source` | yes | str | 8/8 (100%) | XPHB |  |

| `srd52` | yes | bool | 8/8 (100%) | True |  |



---

## ./rules/2024/itemProperty.json

Detected entries: **9** (mode: largest-list:itemProperty)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `abbreviation` | yes | str | 9/9 (100%) | 2H, A, F, H, L, LD, R, T, V |  |

| `basicRules2024` | yes | bool | 9/9 (100%) | True |  |

| `entries` | yes | list | 9/9 (100%) |  |  |

| `page` | yes | int | 9/9 (100%) | 213, 214 |  |

| `source` | yes | str | 9/9 (100%) | XPHB |  |

| `template` | yes | str | 9/9 (100%) | {{prop_name}}, {{prop_name}} (Range {{item.range}} ft.; {{item.ammoType}}), {{prop_name}} ({{item.dmg2}}), {{prop_name}} ({{item.range}} ft.) |  |



---

## ./rules/2024/itemType.json

Detected entries: **22** (mode: largest-list:itemType)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `abbreviation` | yes | str | 22/22 (100%) |  |  |

| `basicRules2024` | yes | bool | 22/22 (100%) | True |  |

| `name` | yes | str | 22/22 (100%) |  |  |

| `page` | yes | int | 22/22 (100%) | 213, 214, 219, 220, 221, 222, 230, 231 |  |

| `source` | yes | str | 22/22 (100%) | XPHB |  |

| `entries` | no | list | 7/22 (32%) |  |  |

| `_copy` | no | dict | 1/22 (5%) |  |  |



---

## ./rules/2024/itemTypeAdditionalEntries.json

Top-level type: **dict**


Top-level keys (sample): `itemTypeAdditionalEntries`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/language.json

Detected entries: **19** (mode: largest-list:language)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 19/19 (100%) | True |  |

| `entries` | yes | list | 19/19 (100%) |  |  |

| `name` | yes | str | 19/19 (100%) | Abyssal, Celestial, Common, Common Sign Language, Deep Speech, Draconic, Druidic, Dwarvish, Elvish, Giant, Gnomish, Goblin, Halfling, Infernal, Orc, Primordial, Sylvan, Thieves' Cant, Undercommon |  |

| `page` | yes | int | 19/19 (100%) | 37 |  |

| `source` | yes | str | 19/19 (100%) | XPHB |  |

| `srd52` | yes | bool | 19/19 (100%) | True |  |

| `type` | yes | str | 19/19 (100%) | rare, standard |  |

| `dialects` | no | list | 1/19 (5%) |  |  |

| `script` | no | str | 1/19 (5%) | Draconic |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `additionalSources`, `basicRules`, `fonts`, `hasFluffImages`, `otherSources`, `reprintedAs`, `srd`, `typicalSpeakers`



---

## ./rules/2024/languageScript.json

Detected entries: **1** (mode: largest-list:languageScript)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `fonts` | yes | list | 1/1 (100%) |  |  |

| `name` | yes | str | 1/1 (100%) | Draconic |  |

| `source` | yes | str | 1/1 (100%) | XPHB |  |



---

## ./rules/2024/legendaryGroup.json

Detected entries: **23** (mode: largest-list:legendaryGroup)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 23/23 (100%) |  |  |

| `page` | yes | int | 23/23 (100%) |  |  |

| `regionalEffects` | yes | list | 23/23 (100%) |  |  |

| `source` | yes | str | 23/23 (100%) | XMM |  |



---

## ./rules/2024/mappings/spell_levels_xphb.json

Top-level type: **dict**


Top-level keys (sample): `Acid Splash`, `Aid`, `Alarm`, `Alter Self`, `Animal Friendship`, `Animal Messenger`, `Animal Shapes`, `Animate Dead`, `Animate Objects`, `Antilife Shell`, `Antimagic Field`, `Antipathy/Sympathy`, `Arcane Eye`, `Arcane Gate`, `Arcane Lock`, `Arcane Vigor`, `Armor of Agathys`, `Arms of Hadar`, `Astral Projection`, `Augury`, `Aura of Life`, `Aura of Purity`, `Aura of Vitality`, `Awaken`, `Bane`, `Banishing Smite`, `Banishment`, `Barkskin`, `Beacon of Hope`, `Beast Sense`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/mappings/spell_to_classes_xphb.json

Top-level type: **dict**


Top-level keys (sample): `Acid Splash`, `Aid`, `Alarm`, `Alter Self`, `Animal Friendship`, `Animal Messenger`, `Animal Shapes`, `Animate Dead`, `Animate Objects`, `Antilife Shell`, `Antimagic Field`, `Antipathy/Sympathy`, `Arcane Eye`, `Arcane Gate`, `Arcane Lock`, `Arcane Vigor`, `Armor of Agathys`, `Arms of Hadar`, `Astral Projection`, `Augury`, `Aura of Life`, `Aura of Purity`, `Aura of Vitality`, `Awaken`, `Bane`, `Banishing Smite`, `Banishment`, `Barkskin`, `Beacon of Hope`, `Beast Sense`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/monster.json

Detected entries: **504** (mode: largest-list:monster)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `ac` | yes | list | 504/504 (100%) |  |  |

| `alignment` | yes | list | 504/504 (100%) |  |  |

| `cha` | yes | int | 504/504 (100%) |  |  |

| `con` | yes | int | 504/504 (100%) |  |  |

| `dex` | yes | int | 504/504 (100%) |  |  |

| `hasFluffImages` | yes | bool | 504/504 (100%) | True |  |

| `hasToken` | yes | bool | 504/504 (100%) | True |  |

| `hp` | yes | dict | 504/504 (100%) |  |  |

| `int` | yes | int | 504/504 (100%) |  |  |

| `name` | yes | str | 504/504 (100%) |  |  |

| `passive` | yes | int | 504/504 (100%) |  |  |

| `size` | yes | list | 504/504 (100%) |  |  |

| `source` | yes | str | 504/504 (100%) | XMM, XPHB |  |

| `speed` | yes | dict | 504/504 (100%) |  |  |

| `str` | yes | int | 504/504 (100%) |  |  |

| `type` | yes | dict, str | 504/504 (100%) | aberration, beast, celestial, construct, dragon, elemental, fey, fiend, giant, humanoid, monstrosity, ooze, plant, undead |  |

| `wis` | yes | int | 504/504 (100%) |  |  |

| `action` | no | list | 503/504 (100%) |  |  |

| `cr` | no | dict, str | 503/504 (100%) |  |  |

| `environment` | no | list | 503/504 (100%) |  |  |

| `hasFluff` | no | bool | 503/504 (100%) | True |  |

| `page` | no | int | 503/504 (100%) |  |  |

| `miscTags` | no | list | 502/504 (100%) |  |  |

| `damageTags` | no | list | 501/504 (99%) |  |  |

| `senses` | no | list | 390/504 (77%) |  |  |

| `senseTags` | no | list | 389/504 (77%) |  |  |

| `soundClip` | no | dict | 373/504 (74%) |  |  |

| `languages` | no | list | 357/504 (71%) |  |  |

| `languageTags` | no | list | 356/504 (71%) |  |  |

| `basicRules2024` | no | bool | 333/504 (66%) | True |  |

| `skill` | no | dict | 333/504 (66%) |  |  |

| `srd52` | no | bool | 332/504 (66%) | True |  |

| `actionTags` | no | list | 329/504 (65%) |  |  |

| `trait` | no | list | 322/504 (64%) |  |  |

| `treasure` | no | list | 299/504 (59%) |  |  |

| `traitTags` | no | list | 249/504 (49%) |  |  |

| `conditionInflict` | no | list | 231/504 (46%) |  |  |

| `savingThrowForced` | no | list | 224/504 (44%) |  |  |

| `save` | no | dict | 197/504 (39%) |  |  |

| `immune` | no | list | 190/504 (38%) |  |  |

| `initiative` | no | dict | 187/504 (37%) |  |  |

| `conditionImmune` | no | list | 180/504 (36%) |  |  |

| `otherSources` | no | list | 179/504 (36%) |  |  |

| `spellcasting` | no | list | 132/504 (26%) |  |  |

| `spellcastingTags` | no | list | 132/504 (26%) |  |  |

| `resist` | no | list | 118/504 (23%) |  |  |

| `group` | no | list | 111/504 (22%) |  |  |

| `bonus` | no | list | 109/504 (22%) |  |  |

| `savingThrowForcedSpell` | no | list | 105/504 (21%) |  |  |

| `conditionInflictSpell` | no | list | 76/504 (15%) |  |  |

| `gear` | no | list | 71/504 (14%) |  |  |

| `damageTagsSpell` | no | list | 70/504 (14%) |  |  |

| `legendary` | no | list | 43/504 (9%) |  |  |

| `dragonAge` | no | str | 41/504 (8%) | adult, ancient, wyrmling, young |  |

| `reaction` | no | list | 41/504 (8%) |  |  |

| `legendaryGroup` | no | dict | 35/504 (7%) |  |  |

| `legendaryActionsLair` | no | int | 34/504 (7%) | 4 |  |

| `familiar` | no | bool | 24/504 (5%) | True |  |

| `savingThrowForcedLegendary` | no | list | 23/504 (5%) |  |  |

| `vulnerable` | no | list | 22/504 (4%) |  |  |

| `_versions` | no | list | 2/504 (0%) |  |  |

| `altArt` | no | list | 2/504 (0%) |  |  |

| `attachedItems` | no | list | 1/504 (0%) |  |  |

| `pbNote` | no | str | 1/504 (0%) | equals your Proficiency Bonus |  |

| `summonedBySpell` | no | str | 1/504 (0%) | Giant Insect\|XPHB |  |

| `summonedBySpellLevel` | no | int | 1/504 (0%) | 4 |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `actionNote`, `alias`, `alignmentPrefix`, `basicRules`, `conditionInflictLegendary`, `damageTagsLegendary`, `dragonCastingColor`, `effects`, `isNamedCreature`, `isNpc`, `legendaryActions`, `legendaryHeader`, `level`, `migrationVersion`, `mythic`, `mythicHeader`, `prototypeToken`, `reactionHeader`, `reprintedAs`, `shortName`, `sizeNote`, `srd`, `summonedByClass`, `tokenCredit`, `variant`



---

## ./rules/2024/monsterFluff.json

Detected entries: **588** (mode: largest-list:monsterFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 588/588 (100%) |  |  |

| `source` | yes | str | 588/588 (100%) | XMM |  |

| `_copy` | no | dict | 340/588 (58%) |  |  |

| `entries` | no | list | 248/588 (42%) |  |  |

| `images` | no | list | 232/588 (39%) |  |  |



---

## ./rules/2024/object.json

Top-level type: **dict**


Top-level keys (sample): `object`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/objectFluff.json

Top-level type: **dict**


Top-level keys (sample): `objectFluff`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/optionalfeature.json

Detected entries: **108** (mode: largest-list:optionalfeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 108/108 (100%) |  |  |

| `source` | yes | str | 108/108 (100%) | XPHB |  |

| `entries` | no | list | 58/108 (54%) |  |  |

| `featureType` | no | list | 58/108 (54%) |  |  |

| `page` | no | int | 58/108 (54%) | 141, 142, 155, 156, 157, 94, 95 |  |

| `migrationVersion` | no | int | 50/108 (46%) | 3 |  |

| `activities` | no | list | 48/108 (44%) |  |  |

| `consumes` | no | dict | 30/108 (28%) |  |  |

| `srd52` | no | bool | 29/108 (27%) | True |  |

| `prerequisite` | no | list | 23/108 (21%) |  |  |

| `effects` | no | list | 19/108 (18%) |  |  |

| `additionalSpells` | no | list | 13/108 (12%) |  |  |

| `featProgression` | no | list | 1/108 (1%) |  |  |

| `senses` | no | list | 1/108 (1%) |  |  |

| `system` | no | dict | 1/108 (1%) |  |  |



---

## ./rules/2024/race.json

Detected entries: **10** (mode: largest-list:race)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `creatureTypes` | yes | list | 10/10 (100%) |  |  |

| `edition` | yes | str | 10/10 (100%) | one |  |

| `entries` | yes | list | 10/10 (100%) |  |  |

| `hasFluff` | yes | bool | 10/10 (100%) | True |  |

| `hasFluffImages` | yes | bool | 10/10 (100%) | True |  |

| `name` | yes | str | 10/10 (100%) | Aasimar, Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, Orc, Tiefling |  |

| `page` | yes | int | 10/10 (100%) | 186, 187, 188, 189, 191, 192, 193, 194, 195, 197 |  |

| `size` | yes | list | 10/10 (100%) |  |  |

| `sizeEntry` | yes | dict | 10/10 (100%) |  |  |

| `soundClip` | yes | dict | 10/10 (100%) |  |  |

| `source` | yes | str | 10/10 (100%) | XPHB |  |

| `speed` | yes | int | 10/10 (100%) | 30, 35 |  |

| `basicRules2024` | no | bool | 9/10 (90%) | True |  |

| `darkvision` | no | int | 7/10 (70%) | 120, 60 |  |

| `srd52` | no | bool | 6/10 (60%) | True |  |

| `_versions` | no | list | 5/10 (50%) |  |  |

| `additionalSpells` | no | list | 3/10 (30%) |  |  |

| `resist` | no | list | 2/10 (20%) |  |  |

| `skillProficiencies` | no | list | 2/10 (20%) |  |  |

| `feats` | no | list | 1/10 (10%) |  |  |

| `traitTags` | no | list | 1/10 (10%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `ability`, `additionalSources`, `age`, `armorProficiencies`, `basicRules`, `blindsight`, `conditionImmune`, `creatureTypeTags`, `entryData`, `heightAndWeight`, `immune`, `languageProficiencies`, `lineage`, `migrationVersion`, `otherSources`, `reprintedAs`, `srd`, `toolProficiencies`, `vulnerable`, `weaponProficiencies`



---

## ./rules/2024/raceFeature.json

Detected entries: **11** (mode: largest-list:raceFeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `migrationVersion` | yes | int | 11/11 (100%) | 3 |  |

| `name` | yes | str | 11/11 (100%) | Adrenaline Rush, Breath Weapon, Celestial Revelation, Draconic Flight, Dwarven Toughness, Healing Hands, Large Form, Luck, Powerful Build, Relentless Endurance, Stonecunning |  |

| `raceName` | yes | str | 11/11 (100%) | Aasimar, Dragonborn, Dwarf, Goliath, Halfling, Orc |  |

| `raceSource` | yes | str | 11/11 (100%) | XPHB |  |

| `source` | yes | str | 11/11 (100%) | XPHB |  |

| `activities` | no | list | 8/11 (73%) |  |  |

| `effects` | no | list | 7/11 (64%) |  |  |

| `system` | no | dict | 3/11 (27%) |  |  |



---

## ./rules/2024/raceFluff.json

Detected entries: **10** (mode: largest-list:raceFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 10/10 (100%) |  |  |

| `images` | yes | list | 10/10 (100%) |  |  |

| `name` | yes | str | 10/10 (100%) | Aasimar, Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, Orc, Tiefling |  |

| `source` | yes | str | 10/10 (100%) | XPHB |  |



---

## ./rules/2024/reward.json

Top-level type: **dict**


Top-level keys (sample): `reward`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/sense.json

Detected entries: **4** (mode: largest-list:sense)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `entries` | yes | list | 4/4 (100%) |  |  |

| `name` | yes | str | 4/4 (100%) | Blindsight, Darkvision, Tremorsense, Truesight |  |

| `page` | yes | int | 4/4 (100%) | 361, 365, 377 |  |

| `source` | yes | str | 4/4 (100%) | XPHB |  |

| `srd52` | yes | bool | 4/4 (100%) | True |  |



---

## ./rules/2024/skill.json

Detected entries: **18** (mode: largest-list:skill)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `ability` | yes | str | 18/18 (100%) | cha, dex, int, str, wis |  |

| `entries` | yes | list | 18/18 (100%) |  |  |

| `name` | yes | str | 18/18 (100%) | Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, Survival |  |

| `page` | yes | int | 18/18 (100%) | 14 |  |

| `source` | yes | str | 18/18 (100%) | XPHB |  |

| `srd52` | yes | bool | 18/18 (100%) | True |  |



---

## ./rules/2024/sources/registry.json

Detected entries: **1** (mode: array)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `aliases` | yes | list | 1/1 (100%) |  |  |

| `category` | yes | str | 1/1 (100%) | official-core |  |

| `default_enabled` | yes | bool | 1/1 (100%) | True |  |

| `id` | yes | str | 1/1 (100%) | XPHB |  |

| `name` | yes | str | 1/1 (100%) | Player's Handbook (2024) |  |

| `publisher` | yes | str | 1/1 (100%) | Wizards of the Coast |  |



---

## ./rules/2024/species.json

Top-level type: **dict**


Top-level keys (sample): `species`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/speciesFeature.json

Top-level type: **dict**


Top-level keys (sample): `speciesFeature`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/speciesFluff.json

Top-level type: **dict**


Top-level keys (sample): `speciesFluff`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/spell.json

Detected entries: **391** (mode: largest-list:spell)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `name` | yes | str | 391/391 (100%) |  |  |

| `source` | yes | str | 391/391 (100%) | XPHB |  |

| `migrationVersion` | no | int | 286/391 (73%) | 3 |  |

| `activities` | no | list | 285/391 (73%) |  |  |

| `effects` | no | list | 170/391 (43%) |  |  |

| `components` | no | dict | 105/391 (27%) |  |  |

| `duration` | no | list | 105/391 (27%) |  |  |

| `entries` | no | list | 105/391 (27%) |  |  |

| `level` | no | int | 105/391 (27%) | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |  |

| `page` | no | int | 105/391 (27%) |  |  |

| `range` | no | dict | 105/391 (27%) |  |  |

| `school` | no | str | 105/391 (27%) | A, C, D, E, I, N, T, V |  |

| `time` | no | list | 105/391 (27%) |  |  |

| `basicRules2024` | no | bool | 99/391 (25%) | True |  |

| `srd52` | no | bool, str | 99/391 (25%) | Arcane Hand, Arcane Sword, Floating Disk, Private Sanctum, Tiny Hut, True |  |

| `miscTags` | no | list | 77/391 (20%) |  |  |

| `areaTags` | no | list | 55/391 (14%) |  |  |

| `entriesHigherLevel` | no | list | 38/391 (10%) |  |  |

| `damageInflict` | no | list | 32/391 (8%) |  |  |

| `system` | no | dict | 31/391 (8%) |  |  |

| `savingThrow` | no | list | 27/391 (7%) |  |  |

| `meta` | no | dict | 15/391 (4%) |  |  |

| `hasFluffImages` | no | bool | 13/391 (3%) | True |  |

| `spellAttack` | no | list | 8/391 (2%) |  |  |

| `abilityCheck` | no | list | 6/391 (2%) |  |  |

| `conditionInflict` | no | list | 6/391 (2%) |  |  |

| `scalingLevelDice` | no | dict | 6/391 (2%) |  |  |

| `affectsCreatureType` | no | list | 4/391 (1%) |  |  |

| `alias` | no | list | 1/391 (0%) |  |  |

| `damageResist` | no | list | 1/391 (0%) |  |  |

| `damageVulnerable` | no | list | 1/391 (0%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `additionalSources`, `basicRules`, `conditionImmune`, `damageImmune`, `hasFluff`, `otherSources`, `reprintedAs`, `srd`



---

## ./rules/2024/spellFluff.json

Detected entries: **61** (mode: largest-list:spellFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `images` | yes | list | 61/61 (100%) |  |  |

| `name` | yes | str | 61/61 (100%) |  |  |

| `source` | yes | str | 61/61 (100%) | XGE, XPHB |  |



---

## ./rules/2024/status.json

Detected entries: **2** (mode: largest-list:status)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 2/2 (100%) | True |  |

| `entries` | yes | list | 2/2 (100%) |  |  |

| `name` | yes | str | 2/2 (100%) | Concentration, Surprised |  |

| `page` | yes | int | 2/2 (100%) | 363, 376 |  |

| `source` | yes | str | 2/2 (100%) | XPHB |  |

| `srd52` | yes | bool | 2/2 (100%) | True |  |



---

## ./rules/2024/subclass.json

Detected entries: **59** (mode: largest-list:subclass)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 59/59 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 59/59 (100%) | XPHB |  |

| `name` | yes | str | 59/59 (100%) |  |  |

| `shortName` | yes | str | 59/59 (100%) |  |  |

| `source` | yes | str | 59/59 (100%) | XPHB |  |

| `edition` | no | str | 48/59 (81%) | one |  |

| `hasFluffImages` | no | bool | 48/59 (81%) | True |  |

| `page` | no | int | 48/59 (81%) |  |  |

| `subclassFeatures` | no | list | 48/59 (81%) |  |  |

| `additionalSpells` | no | list | 33/59 (56%) |  |  |

| `srd52` | no | bool | 12/59 (20%) | True |  |

| `advancement` | no | list | 11/59 (19%) |  |  |

| `basicRules2024` | no | bool | 11/59 (19%) | True |  |

| `migrationVersion` | no | int | 11/59 (19%) | 3 |  |

| `subclassTableGroups` | no | list | 4/59 (7%) |  |  |

| `cantripProgression` | no | list | 2/59 (3%) |  |  |

| `casterProgression` | no | str | 2/59 (3%) | 1/3 |  |

| `preparedSpellsChange` | no | str | 2/59 (3%) | level |  |

| `preparedSpellsProgression` | no | list | 2/59 (3%) |  |  |

| `spellcastingAbility` | no | str | 2/59 (3%) | int |  |

| `featProgression` | no | list | 1/59 (2%) |  |  |

| `optionalfeatureProgression` | no | list | 1/59 (2%) |  |  |



**Differences vs upstream (keys)**


- Present upstream, missing here: `_copy`, `basicRules`, `fluff`, `hasFluff`, `isReprinted`, `otherSources`, `reprintedAs`, `spellsKnownProgression`, `srd`



---

## ./rules/2024/subclassFeature.json

Detected entries: **482** (mode: largest-list:subclassFeature)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 482/482 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 482/482 (100%) | XPHB |  |

| `level` | yes | int | 482/482 (100%) | 10, 11, 13, 14, 15, 17, 18, 20, 3, 6, 7, 9 |  |

| `name` | yes | str | 482/482 (100%) |  |  |

| `source` | yes | str | 482/482 (100%) | XPHB |  |

| `subclassShortName` | yes | str | 482/482 (100%) |  |  |

| `subclassSource` | yes | str | 482/482 (100%) | XPHB |  |

| `entries` | no | list | 309/482 (64%) |  |  |

| `page` | no | int | 309/482 (64%) |  |  |

| `header` | no | int | 229/482 (48%) | 1, 2 |  |

| `migrationVersion` | no | int | 173/482 (36%) | 3 |  |

| `activities` | no | list | 145/482 (30%) |  |  |

| `effects` | no | list | 71/482 (15%) |  |  |

| `srd52` | no | bool | 70/482 (15%) | True |  |

| `basicRules2024` | no | bool | 65/482 (13%) | True |  |

| `consumes` | no | dict | 38/482 (8%) |  |  |

| `system` | no | dict | 19/482 (4%) |  |  |

| `entryData` | no | dict | 14/482 (3%) |  |  |

| `actorTokenMod` | no | dict | 1/482 (0%) |  |  |

| `isIgnored` | no | bool | 1/482 (0%) | True |  |



---

## ./rules/2024/subclassFluff.json

Detected entries: **72** (mode: largest-list:subclassFluff)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `className` | yes | str | 72/72 (100%) | Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard |  |

| `classSource` | yes | str | 72/72 (100%) | PHB, XPHB |  |

| `name` | yes | str | 72/72 (100%) |  |  |

| `shortName` | yes | str | 72/72 (100%) |  |  |

| `source` | yes | str | 72/72 (100%) | XGE, XPHB |  |

| `images` | no | list | 60/72 (83%) |  |  |

| `entries` | no | list | 21/72 (29%) |  |  |



---

## ./rules/2024/table.json

Detected entries: **61** (mode: largest-list:table)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `colStyles` | yes | list | 61/61 (100%) |  |  |

| `name` | yes | str | 61/61 (100%) |  |  |

| `page` | yes | int | 61/61 (100%) |  |  |

| `rows` | yes | list | 61/61 (100%) |  |  |

| `source` | yes | str | 61/61 (100%) | XDMG, XMM, XPHB |  |

| `caption` | no | str | 60/61 (98%) |  |  |

| `chapter` | no | dict | 60/61 (98%) |  |  |

| `colLabels` | no | list | 59/61 (97%) |  |  |

| `basicRules2024` | no | bool | 50/61 (82%) | False, True |  |

| `srd52` | no | bool | 50/61 (82%) | False, True |  |

| `footnotes` | no | list | 3/61 (5%) |  |  |

| `basicRules` | no | bool | 1/61 (2%) | False |  |

| `colLabelRows` | no | list | 1/61 (2%) |  |  |

| `parentEntity` | no | dict | 1/61 (2%) |  |  |

| `srd` | no | bool | 1/61 (2%) | False |  |



---

## ./rules/2024/tableGroup.json

Top-level type: **dict**


Top-level keys (sample): `tableGroup`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./rules/2024/variantrule.json

Detected entries: **117** (mode: largest-list:variantrule)


| key | required | types | coverage | enum candidates | notes |

|---|---|---|---|---|---|

| `basicRules2024` | yes | bool | 117/117 (100%) | True |  |

| `entries` | yes | list | 117/117 (100%) |  |  |

| `name` | yes | str | 117/117 (100%) |  |  |

| `page` | yes | int | 117/117 (100%) | 214, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 376, 377, 44 |  |

| `ruleType` | yes | str | 117/117 (100%) | C |  |

| `source` | yes | str | 117/117 (100%) | XPHB |  |

| `srd52` | yes | bool | 117/117 (100%) | True |  |

| `type` | no | str | 2/117 (2%) | entries, section |  |



---

## ./indexes/2024/_build.json

Top-level type: **dict**


Top-level keys (sample): `baseline`, `counts`, `out`, `source_toggles`, `timestamp`, `tool`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./indexes/2024/feats_by_prereq.json

Top-level type: **dict**


Top-level keys (sample): `CHA>=13`, `CON>=13`, `DEX>=13`, `INT>=13`, `Level>=19`, `Level>=4`, `STR>=13`, `WIS>=13`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./indexes/2024/spells_by_class_level.json

Top-level type: **dict**


Top-level keys (sample): `Bard`, `Cleric`, `Druid`, `Paladin`, `Ranger`, `Sorcerer`, `Warlock`, `Wizard`


*(No per-entry table generated — file does not look like an array of entries.)*


---

## ./indexes/2024/subclass_features_by_level.json

Top-level type: **dict**


Top-level keys (sample): `Barbarian: Berserker`, `Barbarian: Wild Heart`, `Barbarian: World Tree`, `Barbarian: Zealot`, `Bard: Dance`, `Bard: Glamour`, `Bard: Lore`, `Bard: Valor`, `Cleric: Life`, `Cleric: Light`, `Cleric: Trickery`, `Cleric: War`, `Druid: Land`, `Druid: Moon`, `Druid: Sea`, `Druid: Stars`, `Fighter: Battle Master`, `Fighter: Champion`, `Fighter: Eldritch Knight`, `Fighter: Psi Warrior`, `Monk: Elements`, `Monk: Mercy`, `Monk: Open Hand`, `Monk: Shadow`, `Paladin: Ancients`, `Paladin: Devotion`, `Paladin: Glory`, `Paladin: Vengeance`, `Ranger: Beast Master`, `Ranger: Fey Wanderer`


*(No per-entry table generated — file does not look like an array of entries.)*


---
