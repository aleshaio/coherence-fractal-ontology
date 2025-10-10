#!/usr/bin/env python3
"""
CFO Example Generator
Generates rich reduction examples across diverse domains
"""

import json
from dataclasses import dataclass, asdict
from typing import List, Dict

@dataclass
class Reduction:
    dimension: str
    primitive: str
    planes: List[str]
    ops: List[str]
    evidence: str
    confidence: float

@dataclass
class Example:
    id: str
    domain: str
    raw: str
    reductions: List[Dict]
    
    def to_jsonl(self) -> str:
        return json.dumps({
            "id": self.id,
            "domain": self.domain,
            "raw": self.raw,
            "reduction": [asdict(r) for r in self.reductions]
        })


# Advanced examples covering gaps in current set
EXAMPLES = [
    # Quantum mechanics
    Example(
        id="physics:superposition",
        domain="quantum",
        raw="Electron in superposition before measurement",
        reductions=[
            Reduction("2D", "circle", ["XY"], ["relate"], 
                     "Wave function = probabilistic field over configuration space", 0.85),
            Reduction("5D", "ether", ["ZV", "WV"], ["fold"],
                     "Superposition = all states unified before collapse", 0.75)
        ]
    ),
    
    # Consciousness
    Example(
        id="consciousness:meditation",
        domain="psychology",
        raw="Deep meditation - dissolution of subject-object boundary",
        reductions=[
            Reduction("3D", "sphere", ["XY", "YZ", "XZ"], ["integrate"],
                     "Unified field of awareness before differentiation", 0.80),
            Reduction("5D", "ether", ["XV", "YV", "ZV", "WV"], ["fold", "transcend"],
                     "Non-dual awareness - ∞/∞ = 1", 0.70)
        ]
    ),
    
    # AI Architecture
    Example(
        id="ai:transformer",
        domain="computer_science",
        raw="Transformer neural network with attention mechanism",
        reductions=[
            Reduction("2D", "triangle", ["YW"], ["relate", "map"],
                     "Attention = dynamic relational graph between tokens", 0.90),
            Reduction("4D", "tesseract", ["XW", "YW", "ZW"], ["history", "context"],
                     "Complete context window = 4D memory structure", 0.85)
        ]
    ),
    
    # Emergence
    Example(
        id="complexity:emergence",
        domain="systems",
        raw="Murmuration - flock of birds moving as unified whole",
        reductions=[
            Reduction("0D", "point", ["XY"], ["measure"],
                     "Each bird = discrete agent", 0.95),
            Reduction("2D", "triangle", ["XY", "YW"], ["relate"],
                     "Local interaction rules between neighbors", 0.90),
            Reduction("3D", "sphere", ["XY", "XZ", "YZ"], ["integrate"],
                     "Emergent global pattern from local rules", 0.85),
            Reduction("5D", "ether", ["ZV"], ["fold"],
                     "Collective consciousness - swarm as single organism", 0.60)
        ]
    ),
    
    # Mythology - deeper
    Example(
        id="myth:ouroboros",
        domain="symbols",
        raw="Ouroboros - serpent eating its own tail",
        reductions=[
            Reduction("1D", "line", ["XW"], ["sequence"],
                     "Linear time - beginning to end", 0.75),
            Reduction("2D", "circle", ["XY"], ["relate"],
                     "Cycle closing on itself - eternal return", 0.90),
            Reduction("5D", "ether", ["WV"], ["fold"],
                     "Self-reference - system consuming/creating itself = unity", 0.85)
        ]
    ),
    
    # Mathematics
    Example(
        id="math:mandelbrot",
        domain="mathematics",
        raw="Mandelbrot set - fractal with infinite detail",
        reductions=[
            Reduction("2D", "circle", ["XY"], ["relate", "pattern"],
                     "Complex plane mapping z → z² + c", 0.95),
            Reduction("6D", "point", ["XV", "YV"], ["self_reference", "fractal_recurse"],
                     "Self-similar at all scales - fractal dimension", 0.90)
        ]
    ),
    
    # Biology
    Example(
        id="biology:dna",
        domain="biology",
        raw="DNA double helix encoding genetic information",
        reductions=[
            Reduction("1D", "line", ["XW"], ["sequence"],
                     "Linear sequence of base pairs A-T-G-C", 0.95),
            Reduction("2D", "triangle", ["XZ"], ["relate"],
                     "Double helix = two strands in complementary relation", 0.90),
            Reduction("4D", "tesseract", ["ZW"], ["history", "context"],
                     "Genetic memory - evolutionary history encoded", 0.85)
        ]
    ),
    
    # Sociology
    Example(
        id="society:revolution",
        domain="sociology",
        raw="Social revolution - rapid transformation of power structures",
        reductions=[
            Reduction("2D", "square", ["YW"], ["relate"],
                     "Old hierarchical structure (stable grid)", 0.85),
            Reduction("1D", "line", ["XW"], ["sequence"],
                     "Crisis trajectory - rapid change vector", 0.80),
            Reduction("3D", "cube", ["YW", "ZW"], ["context", "transform"],
                     "New integrated system emerging from chaos", 0.75)
        ]
    ),
    
    # Language
    Example(
        id="language:metaphor",
        domain="linguistics",
        raw="'Time is money' - conceptual metaphor",
        reductions=[
            Reduction("2D", "triangle", ["YW"], ["relate", "map"],
                     "Mapping structure from source domain (money) to target (time)", 0.85),
            Reduction("5D", "ether", ["ZV"], ["fold"],
                     "Unity of abstract concepts - time ≡ money in cultural field", 0.70)
        ]
    ),
    
    # Technology
    Example(
        id="tech:blockchain",
        domain="technology",
        raw="Blockchain - distributed ledger with consensus",
        reductions=[
            Reduction("0D", "point", ["XY"], ["measure"],
                     "Each transaction = discrete event", 0.95),
            Reduction("1D", "line", ["XW"], ["sequence"],
                     "Chain of blocks in temporal order", 0.95),
            Reduction("2D", "square", ["YW"], ["relate", "tessellate"],
                     "Network of nodes maintaining consensus", 0.85),
            Reduction("4D", "tesseract", ["XW", "YW", "ZW"], ["history", "context"],
                     "Complete immutable history = 4D ledger", 0.90)
        ]
    ),
    
    # Economics
    Example(
        id="economics:market",
        domain="economics",
        raw="Free market - supply and demand equilibrium",
        reductions=[
            Reduction("2D", "triangle", ["YW"], ["relate"],
                     "Buyers-sellers-goods triangular relation", 0.85),
            Reduction("3D", "sphere", ["YW", "ZW"], ["context", "integrate"],
                     "Market as self-regulating field finding equilibrium", 0.80)
        ]
    ),
    
    # Phenomenology
    Example(
        id="phenomenology:dasein",
        domain="philosophy",
        raw="Dasein - being-in-the-world (Heidegger)",
        reductions=[
            Reduction("3D", "cube", ["XY", "XZ", "YZ"], ["context"],
                     "Being embedded in spatial world", 0.80),
            Reduction("4D", "tesseract", ["XW", "YW", "ZW"], ["history", "context"],
                     "Temporality - being-toward-death, thrownness, project", 0.85),
            Reduction("5D", "ether", ["ZV", "WV"], ["fold"],
                     "Being-as-such - ontological unity", 0.70)
        ]
    ),
    
    # Art
    Example(
        id="art:symphony",
        domain="music",
        raw="Beethoven's 5th Symphony - complete work",
        reductions=[
            Reduction("1D", "line", ["XW"], ["sequence"],
                     "Temporal unfolding of musical phrases", 0.90),
            Reduction("2D", "triangle", ["XY", "YW"], ["relate"],
                     "Harmonic relationships and thematic development", 0.85),
            Reduction("3D", "cube", ["YW", "ZW"], ["integrate", "context"],
                     "Multi-instrumental integration and emotional field", 0.85),
            Reduction("5D", "ether", ["ZV", "WV"], ["fold", "transcend"],
                     "Universal archetype - triumph over fate", 0.75)
        ]
    ),
    
    # Cosmology
    Example(
        id="cosmology:bigbang",
        domain="astronomy",
        raw="Big Bang - universe emergence from singularity",
        reductions=[
            Reduction("0D", "point", [], ["measure"],
                     "Initial singularity - infinite density, zero extent", 0.90),
            Reduction("1D", "line", ["XW"], ["sequence", "unfold"],
                     "Expansion vector - universe unfolding in time", 0.90),
            Reduction("3D", "sphere", ["XY", "XZ", "YZ"], ["integrate"],
                     "3D space emerging and inflating", 0.85),
            Reduction("5D", "ether", ["XV", "YV", "ZV", "WV"], ["unfold"],
                     "Point (•) unfolding to infinity (∞) - • → ∞", 0.80)
        ]
    ),
    
    # Chemistry
    Example(
        id="chemistry:catalysis",
        domain="chemistry",
        raw="Enzyme catalysis - lowering activation energy",
        reductions=[
            Reduction("2D", "triangle", ["XY"], ["relate"],
                     "Enzyme-substrate-product triangular reaction", 0.90),
            Reduction("3D", "cube", ["XZ"], ["context"],
                     "Active site = 3D geometric pocket", 0.85),
            Reduction("1D", "line", ["XW"], ["sequence"],
                     "Reaction pathway over time", 0.85)
        ]
    ),
    
    # Ecology
    Example(
        id="ecology:ecosystem",
        domain="ecology",
        raw="Rainforest ecosystem - integrated web of life",
        reductions=[
            Reduction("0D", "point", ["XY"], ["measure"],
                     "Individual organism = discrete entity", 0.90),
            Reduction("2D", "triangle", ["YW"], ["relate"],
                     "Food web - predator-prey-decomposer relations", 0.90),
            Reduction("3D", "sphere", ["XY", "XZ", "YZ"], ["integrate", "context"],
                     "Complete ecosystem - spatial integration", 0.85),
            Reduction("4D", "tesseract", ["ZW"], ["history"],
                     "Ecological succession - long-term evolution", 0.80)
        ]
    ),
    
    # Neuroscience
    Example(
        id="neuro:plasticity",
        domain="neuroscience",
        raw="Neuroplasticity - brain rewiring through learning",
        reductions=[
            Reduction("2D", "square", ["YW"], ["relate", "tessellate"],
                     "Neural network - nodes and connections", 0.90),
            Reduction("4D", "tesseract", ["XW", "YW"], ["history", "transform"],
                     "Synaptic strengthening over time = learning", 0.85)
        ]
    ),
    
    # Ritual
    Example(
        id="ritual:pilgrimage",
        domain="anthropology",
        raw="Pilgrimage - sacred journey to holy site",
        reductions=[
            Reduction("1D", "line", ["XW", "XZ"], ["sequence"],
                     "Physical journey path in space-time", 0.85),
            Reduction("4D", "tesseract", ["XW", "YW", "ZW"], ["history", "relate", "transform"],
                     "Inner transformation through temporal-relational process", 0.80),
            Reduction("5D", "ether", ["XV", "ZV"], ["fold", "transcend"],
                     "Return to origin - sacred = point of unity", 0.75)
        ]
    ),
    
    # Disease
    Example(
        id="medicine:pandemic",
        domain="epidemiology",
        raw="COVID-19 pandemic - global disease spread",
        reductions=[
            Reduction("0D", "point", ["XW"], ["measure"],
                     "Patient zero - initial case", 0.95),
            Reduction("1D", "line", ["XW"], ["sequence"],
                     "Transmission chains over time", 0.90),
            Reduction("2D", "triangle", ["YW"], ["relate"],
                     "Social network spread - person-to-person", 0.90),
            Reduction("3D", "sphere", ["XY", "XZ", "YZ"], ["integrate"],
                     "Global geographic spread", 0.85)
        ]
    ),
    
    # Architecture
    Example(
        id="architecture:cathedral",
        domain="architecture",
        raw="Gothic cathedral - soaring vertical sacred space",
        reductions=[
            Reduction("1D", "line", ["XZ"], ["sequence"],
                     "Vertical ascent - reaching toward heaven", 0.85),
            Reduction("3D", "cube", ["XY", "XZ", "YZ"], ["context", "contain"],
                     "Sacred space - container for ritual", 0.90),
            Reduction("5D", "ether", ["ZV"], ["fold", "transcend"],
                     "Architecture as frozen music - material pointing to transcendent", 0.75)
        ]
    ),
    
    # Game Theory
    Example(
        id="gametheory:nash",
        domain="mathematics",
        raw="Nash equilibrium - stable strategy profile",
        reductions=[
            Reduction("0D", "point", ["YW"], ["measure"],
                     "Equilibrium = fixed point in strategy space", 0.90),
            Reduction("2D", "triangle", ["YW"], ["relate"],
                     "Multi-player strategic interactions", 0.85)
        ]
    )
]


def generate_examples_file(output_path: str = "reduction-examples-extended.jsonl"):
    """Generate extended examples file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        for example in EXAMPLES:
            f.write(example.to_jsonl() + '\n')
    
    print(f"Generated {len(EXAMPLES)} examples → {output_path}")
    
    # Statistics
    domains = {}
    dimensions = {}
    for ex in EXAMPLES:
        domains[ex.domain] = domains.get(ex.domain, 0) + 1
        for r in ex.reductions:
            dimensions[r.dimension] = dimensions.get(r.dimension, 0) + 1
    
    print(f"\nDomain coverage:")
    for domain, count in sorted(domains.items(), key=lambda x: -x[1]):
        print(f"  {domain}: {count}")
    
    print(f"\nDimensional coverage:")
    for dim, count in sorted(dimensions.items()):
        print(f"  {dim}: {count}")


if __name__ == "__main__":
    generate_examples_file()