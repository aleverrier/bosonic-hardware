# Bosonic hardware lab

[Open the interactive lab](https://aleverrier.github.io/bosonic-hardware/)

**Publication pending:** the link above becomes active after GitHub Pages is enabled. See [publishing instructions](docs/publishing.md).

An interactive lab for building intuition about superconducting circuits, bosonic modes, nonlinear conversion and dissipative cat stabilization.

| Experiment | What to explore |
|---|---|
| LC resonator | Resonance, linewidth, ring-down, impedance and thermal occupation |
| Storage + buffer | Excitation exchange, avoided crossings and damping |
| Transmon + readout | Energy levels, anharmonicity, charge sensitivity and dispersive readout |
| ATS | Flux-dependent potential, junction mismatch and pair-conversion estimates |
| Quantum cat | Photon number, parity, purity, even-cat fidelity and Wigner distribution |

Each experiment includes an electrical schematic, adjustable parameters and live plots.

## Use the lab

Use the web link above once publication is active. For a local copy, download `index.html` and open it in a browser. Clicking the file on GitHub displays its source.

An internet connection is required for the pinned D3 dependency. The circuit calculations run in your browser.

## Repository layout

| Path | Purpose |
|---|---|
| `index.html` | Generated standalone webpage and GitHub Pages entry point |
| `src/circuit-lab.html` | Editable interface, schematics and simulation source |
| `src/circuit-schematics.html` | Separate schematic gallery source |
| `tools/build.py` | Rebuilds the standalone webpage using Python's standard library |
| `tools/*-template.html` | Standalone wrapper and theme templates |
| `docs/models.md` | Model scope, conventions, limitations and references |
| `docs/publishing.md` | GitHub Pages setup and updates |
| `.nojekyll` | Serves the page as plain static HTML |

## Edit and rebuild

Edit `src/circuit-lab.html`, then run:

```sh
python3 tools/build.py
```

Commit both the source and the regenerated `index.html`. See [model notes](docs/models.md) before interpreting simulation results.
