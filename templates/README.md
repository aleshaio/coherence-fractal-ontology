# cfo templates

fractal structure templates for extending cfo 2.0

---

## quick start

### automated (recommended)
```bash
node create.js path aether           # new path
node create.js combo air+fire        # combination
node create.js tool visualize        # tool
node create.js extend planetary      # extension
```

### manual
```bash
cp base.json ../category/file.json   # copy template
# edit file, replace [placeholders]
node ../test_structure.js            # validate
node ../build_graph.js               # rebuild graph
```

---

## templates

| file | purpose | output |
|------|---------|--------|
| **base.json** | generic | anywhere |
| **path.json** | elements | `paths/` |
| **combo.json** | combinations | `paths/combinations/` |
| **tool.json** | utilities | `tools/` |
| **extend.json** | extensions | `extensions/` |

---

## required sections

every file must have:

### 1. `_meta`
- id, type, fractal_depth
- contains, contained_by, related

### 2. `_holographic_seed`
- absolute, essence, note

### 3. `_links`
- source, related files

---

## examples

```bash
# new path
node create.js path aether
> element: AETHER
> essence: unity, transcendence
> ✓ created: ../paths/aether.json

# combination
node create.js combo air+fire
> name: inspired action
> ✓ created: ../paths/combinations/air+fire.json

# tool
node create.js tool visualize
> purpose: see your helix
> ✓ created: ../tools/visualize.json
```

---

## validation

```bash
cd ..
node test_structure.js      # check structure
node build_graph.js          # rebuild graph
```

---

## file structure

```
templates/
├── base.json       # generic
├── path.json       # paths
├── combo.json      # combinations
├── tool.json       # tools
├── extend.json     # extensions
├── create.js       # generator
├── guide.md        # detailed guide
└── readme.md       # this file
```

---

## principles

1. part = whole (holographic)
2. bidirectional links
3. self-similar at all scales
4. infinite expandable
5. coherence maintained

⊙ = ∞/∞ = 1

templates = seeds for fractal growth 🌀
