This Python script performs a **molecular dynamics (MD) simulation** workflow using the OpenMM library for a protein system (apoCezanne2). It includes restrained equilibration followed by unrestrained production simulation.

**Key Components:**

- System Setup: Loads CHARMM PSF and PDB files, applies periodic boundary conditions, and creates the system with PME electrostatics, a 1.2 nm cutoff, and hydrogen bond constraints. Custom van der Waals switching is applied.

- Restraints: Defines a harmonic restraint force on heavy atoms (N, C, O, CA) with an initial force constant of 500 kcal/mol/nm².

- Integrator and Platform: Uses Langevin dynamics at 310.15 K with 2 fs timesteps, running on CUDA (GPU).

**Simulation Phases:**

_Minimization:_ Energy minimization for up to 5000 iterations.

_Equilibration:_ NVT (constant volume/temperature) for 50,000 steps.
NPT (constant pressure/temperature) for 50,000 steps with Monte Carlo barostat at 1 atm.

_Production:_ Loads equilibrated state, removes restraints, and runs for 500,000,000 steps.

_Output:_ Saves trajectories (DCD), energy data (CSV), checkpoints, and states at various stages.

The script is designed for GPU-accelerated MD simulation of protein dynamics, suitable for studying conformational changes or stability. Total runtime is measured and printed.

