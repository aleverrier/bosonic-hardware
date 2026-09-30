# Models and interpretation

The lab is an educational model of selected circuit degrees of freedom. It is not a general electrical circuit simulator: the schematic illustrates each experiment's physical realization, while the calculation uses that experiment's effective model.

## Conventions

Frequencies shown as GHz or MHz are ordinary frequencies. Rates explicitly labelled κ / 2π or g / 2π use angular-rate conventions. For photon loss κ D[a], energy decays as exp(−κt), while field amplitude decays as exp(−κt/2). The energy lifetime is 1/κ, and Q = ω / κ.

The electrical drawings use lumped-element equivalents. Crosses denote Josephson junctions; coils denote inductors; parallel plates denote capacitors. Ground symbols share a reference. The 50-ohm termination represents an external microwave environment. Dashed flux-control arrows are not electrical wires.

## LC resonator

Uses ω = 1/√(LC), impedance √(L/C), a Lorentzian driven response and exponential ring-down. Thermal occupation follows the Bose distribution. The oscillator is linear and single-mode; the model omits frequency-dependent material loss and unwanted modes.

## Storage and buffer

Uses a linear coupling between two damped modes. The plotted excitation accounting includes the emitted population. The avoided-crossing plot is a lossless reference, separate from the damped time evolution.

This experiment demonstrates linear exchange, not two-photon cat stabilization.

## Transmon and readout

Diagonalizes the charge-basis Hamiltonian 4EC(n−ng)² − EJ cos φ with a charge cutoff from −18 to 18. Anharmonicity is f12−f01 and is normally negative in the transmon regime.

The readout uses a weak dispersive approximation and is suppressed near resonances where that approximation is unreliable. It is not a simulation of the full driven transmon–readout system. The displayed critical photon number is a two-level estimate.

## ATS

Uses an ideal quadratic inductive shunt and a flux-dependent Josephson potential, allowing a phenomenological junction mismatch. It estimates local harmonic frequency and nonlinear coefficients near a static potential minimum.

Pair conversion is estimated from a weak flux pump and a low-order expansion. The inferred two-photon rate uses fast-buffer elimination, κ2 ≈ 4|g2|² / κb. That estimate requires the buffer to relax faster than the relevant conversion dynamics. It does not imply correction becomes faster when κb is increased at fixed g2.

Parasitic modes, inductive-shunt nonlinearities, flux-line calibration and pump-induced heating are omitted.

## Cat stabilization

Evolves a truncated single-mode Lindblad model with engineered two-photon stabilization and ordinary single-photon loss. The buffer is eliminated; the simulation does not evolve the full storage–ATS–buffer circuit shown in the drawing.

The displayed metrics include mean photon number, photon parity, purity and overlap with the target even cat. Even-cat fidelity is not a measure of preservation of an arbitrary encoded qubit. The Wigner plot is a distribution in the storage mode's phase space.

The interface reports trace error and population near the Fock cutoff. Increase the dimension when the cutoff population is appreciable. Results outside the elimination regime need a two-mode model.

## Verification status

JavaScript syntax and deterministic reconstruction of the standalone page were checked. Earlier numerical checks covered linear excitation accounting, transmon diagonalization, ATS cancellation, and trace, positivity, parity and the coherent-state Wigner reference. Visual browser verification remains incomplete in this environment.

## References

- Blais et al., *Circuit quantum electrodynamics*, Rev. Mod. Phys. 93, 025005 (2021): https://arxiv.org/abs/2005.12667
- Lescanne et al., *Exponential suppression of bit-flips in a qubit encoded in an oscillator*, Nature Physics 16, 509–513 (2020): https://doi.org/10.1038/s41567-020-0824-x
- Berdou et al., *One hundred second bit-flip time in a two-photon dissipative oscillator*: https://arxiv.org/abs/2203.03222
