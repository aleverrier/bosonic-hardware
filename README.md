# Bosonic hardware lab

Interactive superconducting circuit models with electrical schematics and adjustable parameters:

- LC resonator: resonance and ring-down.
- Storage and buffer: linear excitation exchange and damping.
- Transmon and readout: charge-basis spectrum and dispersive response.
- ATS: flux-dependent potential and nonlinear conversion estimates.
- Cat stabilization: single-mode Lindblad evolution, Wigner function, photon number, parity and purity.

## Open the lab

Open `index.html` in a browser. An internet connection is required to load D3 from its pinned CDN URL. There is no backend or account requirement.

For a local server, run `python3 -m http.server 8000` in this directory, then open http://localhost:8000.

## Edit and rebuild

Edit `src/circuit-lab.html`, then run `python3 tools/build.py`. Commit the updated `index.html` together with the source. The standalone schematic gallery is in `src/circuit-schematics.html`.

## Model scope

Schematics are simplified lumped-element representations. A 50-ohm termination represents an external microwave environment. Flux-pump arrows are magnetic control, not wires. The transmon model uses charge-basis diagonalization. ATS estimates assume an ideal inductive shunt and weak pump. The cat simulation uses an effective single-mode master equation after eliminating the buffer; it does not explicitly simulate the entire drawn circuit. Parasitic modes, pump-induced heating and detailed fabrication effects are omitted.

JavaScript syntax and schematic wiring to the controls were checked for this version. Earlier numerical checks covered excitation accounting, transmon diagonalization, ATS cancellation, and trace/positivity/parity in cat evolution. Browser rendering has not been visually verified in the current environment.

## References

- Blais et al., *Circuit quantum electrodynamics*, Rev. Mod. Phys. 93, 025005 (2021): https://arxiv.org/abs/2005.12667
- Lescanne et al., *Exponential suppression of bit-flips in a qubit encoded in an oscillator*, Nature Physics 16, 509–513 (2020): https://doi.org/10.1038/s41567-020-0824-x
- Berdou et al., *One hundred second bit-flip time in a two-photon dissipative oscillator*: https://arxiv.org/abs/2203.03222

## GitHub Pages

For a stable hosted URL, enable GitHub Pages in repository Settings → Pages, selecting the `main` branch and `/ (root)`. Availability depends on repository visibility and account plan. The expected URL is https://aleverrier.github.io/bosonic-hardware/ once deployment succeeds.
