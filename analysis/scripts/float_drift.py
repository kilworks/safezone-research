"""Section 8.3: where binary64 code disagrees with the exact rule (Python and JavaScript).

For every multiplier the wiki states, compares the exact rational result with what
a programmer would get writing round(x * m) in IEEE 754 binary64, over the whole
domain of the quantity. Runs the same expressions in Node.js and checks that both
languages agree with each other (they must: both use binary64).

Writes analysis/results/float_drift.json. Usage: py -3 analysis/scripts/float_drift.py
"""
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# name, float multiplier as code would write it, exact multiplier, rounding, domain, what it is
CASES = [
    ("kick_attack_bonus", "1.1", Fraction(11, 10), "floor", range(0, 501), "attacker live on Kick: +10%, rounded down (damage)"),
    ("kick_defense", "0.9", Fraction(9, 10), "floor", range(0, 501), "defender live on Kick, reading A of U-0001 (damage)"),
    ("protection_nuke", "0.5", Fraction(1, 2), "floor", range(0, 501), "Protection takes 50% less from a nuke (damage)"),
    ("protection_potion", "0.5", Fraction(1, 2), "floor", range(0, 221), "Protection potions heal 50% less (heal; rounding not stated)"),
    ("piety_potion", "1.15", Fraction(115, 100), "floor", range(0, 401), "Piety potions heal 15% more, rounded down (heal)"),
    ("ingenuity_price", "1.1", Fraction(11, 10), "ceil", range(0, 1001), "Ingenuity pays 10% more, rounded up (blood tokens)"),
    ("eddie_gain", "0.5", Fraction(1, 2), "floor", range(80, 221), "Eddie's potion heals 50% of max HP (rounding not stated)"),
    ("eddie_loss", "0.3", Fraction(3, 10), "floor", range(80, 221), "Eddie's potion loses 30% of max HP (rounding not stated)"),
    ("eddie_loss_ceil", "0.3", Fraction(3, 10), "ceil", range(80, 221), "same, if rounded up"),
    ("death_rob_heal", "0.05", Fraction(5, 100), "floor", range(80, 221), "Death robs a grave: heal 5% of max HP (rounding not stated)"),
    ("death_cap", "0.6", Fraction(6, 10), "floor", range(80, 221), "Death heal cap: 60% of max HP (rounding not stated)"),
    ("death_alive_threshold", "0.2", Fraction(2, 10), "floor", range(1, 1001), "20% of contestants alive (count; rounding not stated)"),
    ("crown_bonus", "0.2", Fraction(2, 10), "floor", range(0, 100001), "viewer crown kill: 20% of purchase price (Cx-Bucks; rounding not stated)"),
    ("bandage_protection", "1.1", Fraction(11, 10), "ceil", range(0, 7201), "Protection bandages last 1.1x as long (seconds, if rounded up)"),
]
ROUND = {"floor": math.floor, "ceil": math.ceil}


def python_side():
    out = {}
    for name, mf, mx, rnd, dom, _ in CASES:
        f = ROUND[rnd]
        out[name] = [x for x in dom if f(x * float(mf)) != f(x * mx)]
    return out


def node_side():
    js = "const C=" + json.dumps([[n, mf, mx.numerator, mx.denominator, r, dom.start, dom.stop]
                                  for n, mf, mx, r, dom, _ in CASES]) + r""";
const out={};
for (const [n,mf,num,den,r,a,b] of C){
  const f=Math[r], m=Number(mf), bad=[];
  for (let x=a;x<b;x++){
    // exact: integer division on BigInt, floor or ceil of x*num/den
    const p=BigInt(x)*BigInt(num), q=BigInt(den);
    const fl=p/q, ex = (r==='floor'||p%q===0n) ? fl : fl+1n;
    if (BigInt(f(x*m))!==ex) bad.push(x);
  }
  out[n]=bad;
}
console.log(JSON.stringify(out));"""
    return json.loads(subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout)


def main():
    py, nd = python_side(), node_side()
    assert py == nd, "Python and Node.js disagree: binary64 should be identical"
    rows = []
    for name, mf, mx, rnd, dom, what in CASES:
        bad = py[name]
        rows.append({"name": name, "code": f"Math.{rnd}(x * {mf})", "exact": f"{rnd}(x * {mx.numerator}/{mx.denominator})",
                     "domain": [dom.start, dom.stop - 1], "what": what, "disagreements": len(bad), "values": bad[:40]})
        print(f"{name:22s} {rnd}(x*{mf:5s}) domain {dom.start}..{dom.stop - 1}: {len(bad)} disagreements {bad[:12]}")
    out = ROOT / "analysis" / "results" / "float_drift.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"python_equals_node": True, "cases": rows}, indent=1) + "\n", "utf-8", newline="\n")


if __name__ == "__main__":
    main()
