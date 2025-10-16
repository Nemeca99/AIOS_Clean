#!/usr/bin/env python3
"""
Luna Linguistic Calculus
Interrogative operators for consciousness reasoning compression

Converts natural language questions into graph operations:
- Why → causal edges
- How → mechanism chains
- What → type classification
- Where/When → context binding
- Who → agent aggregation

Integrates with Luna's response generator for prompt compression and arbiter scoring.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Iterable
from collections import defaultdict
import uuid

Edge = Tuple[str, str, str]  # (src, label, dst)


@dataclass
class ExperienceState:
    """Graph state for linguistic experience accumulation"""
    nodes: Dict[str, Dict[str, float]] = field(default_factory=lambda: defaultdict(dict))
    edges: List[Edge] = field(default_factory=list)

    def add_edge(self, src: str, label: str, dst: str):
        self.edges.append((src, label, dst))

    def add_feat(self, node: str, feat: str, val: float = 1.0):
        self.nodes[node][feat] = self.nodes[node].get(feat, 0.0) + val

    def strengthen(self, src: str, label: str, dst: str, w: float = 1.0):
        # simple strengthening: add a weight feature to a virtual edge-node key
        key = f"{src}|{label}|{dst}"
        self.add_feat(key, "edge_weight", w)


@dataclass
class CalcResult:
    """Result of linguistic operation"""
    updated: ExperienceState
    derivations: List[str]
    summary: str
    depth_score: int = 0
    compress_gain: float = 0.0


class LinguaCalc:
    """Linguistic Calculus Engine - converts interrogatives to graph operations"""
    
    def __init__(self):
        pass

    # ---------- Primitive ops ----------
    
    def op_why(self, st: ExperienceState, cause: str, effect: str) -> CalcResult:
        """Why operator: introduce/strengthen causal edge"""
        st.add_edge(cause, "CAUSES", effect)
        st.strengthen(cause, "CAUSES", effect, 1.0)
        return CalcResult(
            st, 
            [f"WHY: {cause} -> {effect}"], 
            summary=f"Hypothesis: {cause} causes {effect}"
        )

    def op_how(self, st: ExperienceState, src: str, dst: str, steps: Optional[List[str]] = None) -> CalcResult:
        """How operator: introduce mechanism chain"""
        m = f"mechanism:{uuid.uuid4().hex[:8]}"
        st.add_edge(src, "MECHANISM", m)
        st.add_edge(m, "MECHANISM_TO", dst)
        depth = 0
        
        if steps:
            last = src
            for s in steps:
                st.add_edge(last, "STEP_TO", s)
                last = s
                depth += 1
            st.add_edge(last, "STEP_TO", dst)
            depth += 1
        
        return CalcResult(
            st, 
            [f"HOW: {src} => {dst} via {steps or [m]}"], 
            summary=f"Mechanism linking {src} to {dst}", 
            depth_score=depth
        )

    def op_what(self, st: ExperienceState, ent: str, typ: str) -> CalcResult:
        """What operator: type/classify entity"""
        st.add_edge(ent, "IS_A", typ)
        st.strengthen(ent, "IS_A", typ, 0.5)
        return CalcResult(
            st, 
            [f"WHAT: {ent} is a {typ}"], 
            summary=f"Classified {ent} as {typ}", 
            compress_gain=0.1
        )

    def op_where(self, st: ExperienceState, ent: str, loc: str) -> CalcResult:
        """Where operator: spatial context binding (monoidal - last write wins)"""
        # Remove previous LOCATED_IN edges for this entity (idempotent behavior)
        st.edges = [(s, l, d) for s, l, d in st.edges 
                    if not (s == ent and l == "LOCATED_IN")]
        st.add_edge(ent, "LOCATED_IN", loc)
        return CalcResult(
            st, 
            [f"WHERE: {ent} @ {loc}"], 
            summary=f"Bound {ent} to location {loc}"
        )

    def op_when(self, st: ExperienceState, ent: str, t: str) -> CalcResult:
        """When operator: temporal context binding (monoidal - last write wins)"""
        # Remove previous OCCURS_AT edges for this entity (idempotent behavior)
        st.edges = [(s, l, d) for s, l, d in st.edges 
                    if not (s == ent and l == "OCCURS_AT")]
        st.add_edge(ent, "OCCURS_AT", t)
        return CalcResult(
            st, 
            [f"WHEN: {ent} @ {t}"], 
            summary=f"Bound {ent} to time {t}"
        )

    def op_who(self, st: ExperienceState, target: str, agents: Iterable[str]) -> CalcResult:
        """Who operator: agent aggregation (mean/typical)"""
        agents = list(agents)
        if not agents:
            return CalcResult(st, [], summary="WHO: no agents")
        
        # μ-agent: pick most frequent or first; can swap for proper aggregator
        mu = agents[0]
        st.add_edge(mu, "TYPICAL_AGENT_OF", target)
        return CalcResult(
            st, 
            [f"WHO: μ({agents}) -> {mu}"], 
            summary=f"Typical agent {mu} for {target}"
        )

    # ---------- Rewrite rules ----------
    
    def combine_two_whys_into_how(
        self, 
        st: ExperienceState, 
        cause1: str, 
        cause2: str, 
        effect: str
    ) -> CalcResult:
        """
        Rewrite rule: Why + Why → How
        Collapse parallel causes into mechanism spine
        """
        steps = [cause1, cause2]
        res_how = self.op_how(st, src="∅", dst=effect, steps=steps)
        
        # Record each cause explicitly
        self.op_why(res_how.updated, cause1, effect)
        self.op_why(res_how.updated, cause2, effect)
        
        res_how.derivations.append(f"RULE: WHY+WHY⇒HOW for {effect}")
        res_how.summary = f"Two causes merged into mechanism for {effect}"
        res_how.compress_gain += 0.2
        
        return res_how
    
    def combine_why_how_into_what(
        self, 
        st: ExperienceState,
        cause: str,
        effect: str,
        mechanism_steps: Optional[List[str]] = None
    ) -> CalcResult:
        """
        Rewrite rule: Why + How → What
        Assign type/regularity τ = "process class" learned from mechanism
        
        Collapse causal hypothesis + mechanism chain into type classification
        """
        # First apply Why
        why_res = self.op_why(st, cause, effect)
        
        # Then apply How
        how_res = self.op_how(why_res.updated, cause, effect, mechanism_steps or [])
        
        # Synthesize process class from mechanism
        process_type = f"process_class:{cause}_to_{effect}"
        what_res = self.op_what(how_res.updated, effect, process_type)
        
        what_res.derivations.append(f"RULE: WHY+HOW⇒WHAT for {effect}")
        what_res.summary = f"Classified {effect} as {process_type} via mechanism"
        what_res.compress_gain += 0.3  # Higher gain than just Why+Why
        what_res.depth_score = how_res.depth_score  # Inherit depth from mechanism
        
        return what_res

    # ---------- Safe division as recursion-depth ----------
    
    def safe_division_depth(self, a: int, b: int) -> Optional[int]:
        """
        Division as recursion depth counter
        Returns: max k such that b can be recursively subtracted from a
        """
        if b == 0:
            return None  # ⊥ undefined
        
        k = 0
        r = a
        while r >= b:
            r -= b
            k += 1
        
        return k  # "how many expansions of b fit in a"

    # ---------- NL parser (pattern-based, extend as needed) ----------
    
    def parse_and_apply(self, st: ExperienceState, text: str) -> CalcResult:
        """
        Parse natural language question and apply appropriate operator
        
        Toy patterns - replace with embeddings/router later
        """
        t = text.strip().lower()
        
        # Why pattern
        if t.startswith("why "):
            if " cause " in t and "?" in t:
                mid = t.split("why ")[1].split("?")[0]
                if " cause " in mid:
                    left, right = mid.split(" cause ", 1)
                    cause = left.replace("does", "").replace("do", "").strip()
                    effect = right.strip()
                    return self.op_why(st, cause, effect)
            return CalcResult(st, [], "WHY: parsed but no cause/effect found")
        
        # How pattern
        if t.startswith("how "):
            if " to " in t:
                mid = t.split("how ")[1].split("?")[0]
                parts = mid.split(" to ")
                if len(parts) >= 2:
                    src = parts[0].replace("does", "").replace("do", "").replace("lead", "").strip() or "∅"
                    dst = parts[-1].strip()
                    return self.op_how(st, src, dst)
            return CalcResult(st, [], "HOW: parsed but no src/dst found")
        
        # What pattern
        if t.startswith("what "):
            if " what is " in " " + t + " ":
                ent = t.split("what is", 1)[1].strip(" ?.")
                return self.op_what(st, ent, "concept")
            return CalcResult(st, [], "WHAT: default classification")
        
        # Where pattern
        if t.startswith("where "):
            ent = t.split("where is", 1)[1].strip(" ?.") if "where is" in t else "unknown"
            return self.op_where(st, ent, "unknown_location")
        
        # When pattern
        if t.startswith("when "):
            ent = t.split("when does", 1)[1].strip(" ?.") if "when does" in t else "unknown"
            return self.op_when(st, ent, "unknown_time")
        
        # Who pattern
        if t.startswith("who "):
            tgt = t.split("who ", 1)[1].strip(" ?.")
            return self.op_who(st, tgt, agents=["human_crowd"])
        
        # Fallback: no-op
        return CalcResult(st, [], "No operator matched")


# ---------- Demo/Test ----------

def _demo():
    """Sanity test for linguistic calculus"""
    lc = LinguaCalc()
    s = ExperienceState()
    
    # Build reasoning chain
    r1 = lc.op_why(s, "heat", "expansion")
    r2 = lc.op_why(r1.updated, "pressure", "expansion")
    r3 = lc.combine_two_whys_into_how(r2.updated, "heat", "pressure", "expansion")
    r4 = lc.op_what(r3.updated, "expansion", "thermodynamic_response")
    
    print("=== Linguistic Calculus Demo ===")
    print("\nEdges created:")
    for e in r4.updated.edges[:10]:
        print(f"  {e}")
    
    print(f"\nDepth: {r3.depth_score}")
    print(f"Compression gain: {r3.compress_gain}")
    print(f"Summary: {r4.summary}")
    
    # Test safe division
    print("\n=== Division as Recursion Depth ===")
    print(f"10 ÷ 3 = {lc.safe_division_depth(10, 3)} steps")
    print(f"15 ÷ 5 = {lc.safe_division_depth(15, 5)} steps")
    print(f"7 ÷ 0 = {lc.safe_division_depth(7, 0)} (None = undefined)")


if __name__ == "__main__":
    _demo()

