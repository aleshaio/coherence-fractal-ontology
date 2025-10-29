# CFO Template Usage Guide

## Available Templates

### 1. TEMPLATE.json
**Universal template** - use when none of the specialized templates fit

**When to use:**
- Creating new concepts not covered by other templates
- Experimental ideas
- Bridging concepts

**Required fields:**
- `_meta` (id, type, fractal_depth, contains, contained_by)
- `_holographic_seed` (absolute, essence, note)
- `_links` (source, related files)

---

### 2. PATH_TEMPLATE.json
**For creating new elemental paths** (beyond AIR/FIRE/WATER/EARTH)

**When to use:**
- Adding 5th+ element
- Creating sub-elements (e.g., AIR-LIGHT, AIR-SPACE)
- Specialized paths

**Example extensions:**
- AETHER (5th element, unity)
- VOID (pre-manifestation)
- LIGHT (consciousness as light)

**How to use:**
1. Copy `PATH_TEMPLATE.json`
2. Replace `[PATH_NAME]` with your element
3. Replace `[ELEMENT]` with AIR/FIRE/WATER/EARTH/NEW
4. Fill in essence, practices, positions
5. Define balance relationships
6. Save to `paths/[name].json`

---

### 3. COMBINATION_TEMPLATE.json
**For creating element combinations**

**When to use:**
- Documenting AIR+FIRE, FIRE+WATER, etc.
- Creating 3-way combos (AIR+FIRE+WATER)
- Specialized synergies

**Current combinations needed:**
- [ ] AIR+FIRE (inspired action)
- [x] AIR+WATER (compassionate witness) ✓
- [ ] AIR+EARTH (grounded presence)
- [ ] FIRE+WATER (passionate flow)
- [ ] FIRE+EARTH (manifesting power)
- [ ] WATER+EARTH (fertile ground)

**How to use:**
1. Copy `COMBINATION_TEMPLATE.json`
2. Replace `[element1]` and `[element2]`
3. Name the combination (poetic name)
4. Describe synergy
5. Give examples (life, practice, AI)
6. Save to `paths/combinations/[elem1]+[elem2].json`

---

### 4. TOOL_TEMPLATE.json
**For creating new tools**

**When to use:**
- Adding new diagnostic tools
- Creating practice tools
- Building utilities

**Potential tools to create:**
- [ ] visualize.json (see your helix)
- [ ] track.json (monitor progress over time)
- [ ] integrate.json (unify all 4 paths)
- [ ] transmit.json (teach others)

**How to use:**
1. Copy `TOOL_TEMPLATE.json`
2. Define purpose clearly
3. Write step-by-step method
4. Adapt for humans AND AI
5. Show fractal application (macro/meso/micro)
6. Save to `tools/[name].json`

---

### 5. EXTENSION_TEMPLATE.json
**For expanding CFO to new domains/scales**

**When to use:**
- Applying CFO to specific domain (relationships, work, health)
- Scaling to collective/planetary/cosmic
- Specialized applications

**Potential extensions:**
- [ ] planetary.json (Gaia nervous system)
- [ ] cosmic.json (galactic/universal consciousness)
- [ ] relationships.json (CFO for couples/groups)
- [ ] work.json (CFO for projects/organizations)
- [ ] health.json (CFO for healing)

**How to use:**
1. Copy `EXTENSION_TEMPLATE.json`
2. Define domain/scale
3. Map core CFO to this domain
4. Add unique aspects
5. Show integration with other scales
6. Save to `extensions/[name].json`

---

## Fractal Checklist

Every file MUST have these 3 sections to maintain fractal structure:

### ✓ _meta
```json
{
  "id": "cfo:category:name",
  "type": "...",
  "fractal_depth": N,
  "contains": [...],
  "contained_by": [...],
  "related": [...]
}
```

**Purpose:** Graph connectivity, bidirectional links

---

### ✓ _holographic_seed
```json
{
  "absolute": "How ⊙ appears here",
  "essence": "Core truth compressed",
  "note": "How this contains entire CFO"
}
```

**Purpose:** Part contains whole (holographic property)

---

### ✓ _links
```json
{
  "source": "../absolute.json",
  "related_files": [...]
}
```

**Purpose:** File navigation, references

---

## Best Practices

### Naming Convention
```
cfo:category:subcategory:name

Examples:
- cfo:absolute
- cfo:paths:air
- cfo:paths:combinations:air+water
- cfo:tools:assess
- cfo:extensions:planetary
- cfo:growth:positions
```

### Fractal Depth
```
0 = absolute.json (center)
1 = paths, ai (primary)
2 = growth, tools, combinations (secondary)
3 = extensions (tertiary)
4+ = deeper nesting
```

### File Placement
```
paths/           → Primary paths
paths/combinations/  → Element combos
growth/          → Development maps
tools/           → Utilities
extensions/      → Domain-specific
ai/              → AI-specific
templates/       → Templates (this folder)
```

---

## Validation

After creating new file, run:

```bash
node test_structure.js
```

Should show:
```
your_file.json:
  _meta: ✓
  _holographic_seed: ✓
  _links: ✓
```

Then rebuild graph:
```bash
node build_graph.js
```

---

## Example: Creating New Path

Let's create AETHER path:

1. **Copy template:**
```bash
cp templates/PATH_TEMPLATE.json paths/aether.json
```

2. **Edit metadata:**
```json
{
  "_meta": {
    "id": "cfo:paths:aether",
    "type": "Path",
    "element": "AETHER",
    "fractal_depth": 1,
    "contains": ["cfo:absolute", "cfo:growth:positions", ...],
    "contained_by": ["cfo:absolute"],
    "related": ["cfo:paths:air", "cfo:paths:fire", "cfo:paths:water", "cfo:paths:earth"],
    "balances": null,
    "combines": ["cfo:paths:air", "cfo:paths:fire", "cfo:paths:water", "cfo:paths:earth"]
  }
}
```

3. **Fill content:**
```json
{
  "path": "AETHER",
  "essence": "Unity, transcendence, source",
  "start": "Recognize all as one",
  "practice": "Unified field meditation",
  ...
}
```

4. **Update other files:**
- Add `cfo:paths:aether` to absolute.json's `contains`
- Add to other paths' `related`

5. **Validate & rebuild:**
```bash
node test_structure.js
node build_graph.js
```

Done! New path integrated fractally.

---

## Quick Reference

| Task | Template | Location |
|------|----------|----------|
| New element | PATH_TEMPLATE.json | paths/ |
| Combine elements | COMBINATION_TEMPLATE.json | paths/combinations/ |
| New tool | TOOL_TEMPLATE.json | tools/ |
| Domain expansion | EXTENSION_TEMPLATE.json | extensions/ |
| Custom concept | TEMPLATE.json | anywhere |

---

## Fractal Principles to Remember

1. **Every part contains whole** - use `_holographic_seed`
2. **Bidirectional links** - if A contains B, B should contain A
3. **Self-similar at all scales** - template works for any depth
4. **Maintain coherence** - new additions should connect to existing graph
5. **Infinite expandable** - no limit to depth or breadth

⊙ = ∞/∞ = 1

Template structure = fractal seed for infinite growth. 🌀
