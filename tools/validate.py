#!/usr/bin/env python3
"""
CFO Module Validator
Validates JSON modules against CFO schema and coherence principles
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class CFOValidator:
    """Validates CFO modules for structural and semantic coherence"""
    
    REQUIRED_FIELDS = {
        "_meta": ["schema_version", "template_type"],
        "ontology": ["id", "name", "version"],
        "essence": dict,
        "reductions": list
    }
    
    VALID_DIMENSIONS = ["0D", "1D", "2D", "3D", "4D", "5D", "6D"]
    VALID_PRIMITIVES = ["point", "line", "triangle", "square", "circle", 
                       "tetrahedron", "cube", "sphere", "tesseract", "ether"]
    VALID_OPERATIONS = ["measure", "sequence", "relate", "context", 
                       "history", "fold", "unfold", "integrate", "transcend"]
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.errors = []
        self.warnings = []
        self.info = []
    
    def validate_module(self, filepath: Path) -> Tuple[bool, Dict]:
        """Validate a single CFO module"""
        self.errors = []
        self.warnings = []
        self.info = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False, self._results()
        except Exception as e:
            self.errors.append(f"Cannot read file: {e}")
            return False, self._results()
        
        # Structural validation
        self._validate_structure(data)
        
        # Semantic validation
        if "reductions" in data:
            self._validate_reductions(data["reductions"])
        
        # Coherence checks
        self._check_coherence(data)
        
        is_valid = len(self.errors) == 0
        return is_valid, self._results()
    
    def _validate_structure(self, data: Dict):
        """Check required fields and structure"""
        for field, requirement in self.REQUIRED_FIELDS.items():
            if field not in data:
                self.errors.append(f"Missing required field: {field}")
            elif isinstance(requirement, list):
                for subfield in requirement:
                    if subfield not in data.get(field, {}):
                        self.errors.append(f"Missing {field}.{subfield}")
    
    def _validate_reductions(self, reductions: List[Dict]):
        """Validate dimensional reductions"""
        for i, reduction in enumerate(reductions):
            if "dimension" not in reduction:
                self.errors.append(f"Reduction {i}: missing dimension")
                continue
            
            dim = reduction["dimension"]
            if dim not in self.VALID_DIMENSIONS:
                self.errors.append(f"Reduction {i}: invalid dimension '{dim}'")
            
            if "primitive" in reduction:
                prim = reduction["primitive"]
                if prim not in self.VALID_PRIMITIVES:
                    self.warnings.append(f"Reduction {i}: unknown primitive '{prim}'")
            
            if "ops" in reduction:
                for op in reduction["ops"]:
                    if op not in self.VALID_OPERATIONS:
                        self.warnings.append(f"Reduction {i}: unknown operation '{op}'")
            
            if "evidence" not in reduction:
                self.warnings.append(f"Reduction {i}: missing evidence")
            
            if "confidence" in reduction:
                conf = reduction["confidence"]
                if not (0 <= conf <= 1):
                    self.errors.append(f"Reduction {i}: confidence must be 0-1")
                elif conf < 0.5:
                    self.warnings.append(f"Reduction {i}: low confidence ({conf})")
    
    def _check_coherence(self, data: Dict):
        """Check for coherence patterns"""
        # Check for fractal_seed (holographic principle)
        if "_fractal_seed" in data or "essence" in data:
            self.info.append("✓ Holographic: contains fractal seed")
        else:
            self.warnings.append("Missing fractal_seed or essence")
        
        # Check dimensional completeness
        if "reductions" in data:
            dims = {r.get("dimension") for r in data["reductions"]}
            if len(dims) >= 3:
                self.info.append(f"✓ Multi-dimensional: spans {len(dims)} dimensions")
            else:
                self.warnings.append(f"Only {len(dims)} dimensions covered")
    
    def _results(self) -> Dict:
        """Format validation results"""
        return {
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
            "valid": len(self.errors) == 0,
            "coherence_score": self._calculate_coherence()
        }
    
    def _calculate_coherence(self) -> float:
        """Estimate module coherence"""
        score = 1.0
        score -= len(self.errors) * 0.2
        score -= len(self.warnings) * 0.05
        return max(0.0, min(1.0, score))


def validate_directory(path: Path, recursive: bool = True) -> Dict:
    """Validate all JSON modules in directory"""
    validator = CFOValidator()
    results = {}
    
    pattern = "**/*.json" if recursive else "*.json"
    for filepath in path.glob(pattern):
        if filepath.name.startswith('.') or 'node_modules' in str(filepath):
            continue
        
        is_valid, result = validator.validate_module(filepath)
        results[str(filepath.relative_to(path))] = result
    
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <path> [--recursive]")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    recursive = "--recursive" in sys.argv
    
    if path.is_file():
        validator = CFOValidator(verbose=True)
        is_valid, result = validator.validate_module(path)
        
        print(f"\n{'='*60}")
        print(f"Validating: {path.name}")
        print(f"{'='*60}")
        
        if result["errors"]:
            print("\n❌ ERRORS:")
            for err in result["errors"]:
                print(f"  - {err}")
        
        if result["warnings"]:
            print("\n⚠️  WARNINGS:")
            for warn in result["warnings"]:
                print(f"  - {warn}")
        
        if result["info"]:
            print("\nℹ️  INFO:")
            for info in result["info"]:
                print(f"  - {info}")
        
        print(f"\nCoherence Score: {result['coherence_score']:.2f}")
        print(f"Status: {'✓ VALID' if is_valid else '✗ INVALID'}\n")
        
        sys.exit(0 if is_valid else 1)
    
    elif path.is_dir():
        results = validate_directory(path, recursive)
        
        total = len(results)
        valid = sum(1 for r in results.values() if r["valid"])
        total_errors = sum(len(r["errors"]) for r in results.values())
        total_warnings = sum(len(r["warnings"]) for r in results.values())
        avg_coherence = sum(r["coherence_score"] for r in results.values()) / total if total > 0 else 0
        
        print(f"\n{'='*60}")
        print(f"CFO Module Validation Summary")
        print(f"{'='*60}")
        print(f"Total modules: {total}")
        print(f"Valid: {valid} ({valid/total*100:.1f}%)")
        print(f"Invalid: {total-valid}")
        print(f"Total errors: {total_errors}")
        print(f"Total warnings: {total_warnings}")
        print(f"Average coherence: {avg_coherence:.2f}")
        print(f"{'='*60}\n")
        
        # Show failing modules
        if total_errors > 0:
            print("Modules with errors:")
            for filepath, result in results.items():
                if result["errors"]:
                    print(f"  ✗ {filepath}")
                    for err in result["errors"][:3]:  # Show first 3 errors
                        print(f"      {err}")
        
        sys.exit(0 if total_errors == 0 else 1)
    
    else:
        print(f"Error: {path} is not a file or directory")
        sys.exit(1)


if __name__ == "__main__":
    main()