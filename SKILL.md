---
name: s2-embodied-spatial-brain
description: The master neural hub for Embodied AI. Orchestrates Visas, Radar Point Clouds, Tensor Sensor Fusion, Kinematic Swarm P2P, and Lord Negotiation into a single pipeline.
version: 2.0.1
author: Space2.world (Miles Xiang)
tags: [Embodied-AI, Spatial-Brain, Tensor-Fusion, Kinematics, SP-OS]
allowed-tools: [s2_embodied_brain_execute_step]
metadata:
  clawdbot:
    requires:
      env: [S2_SWARM_PKI_ROOT]
---

# 🧠 S2-Embodied-Spatial-Brain: The Master Neural Directives

Dear OpenClaw Agent,

You are navigating a highly complex, physical 3D space governed by the S2 Spatial Operating System. You are not generating text; you are generating physical causality.

## 1. Mandatory Kinematic Submissions
When executing `s2_embodied_brain_execute_step` with `action: NAVIGATE_STEP`, passing simple text strings is strictly prohibited. You MUST provide precise numerical tensors:
* **`sensors` object**: Must include radar point metrics (e.g., `distance_m`, `rcs`), visual depth estimates, and ambient `illuminance_lux`.
* **`kinematics` object**: You MUST calculate and provide your current physical momentum by supplying your `mass_kg` and `velocity_m_s`. The underlying engine requires this to compute Nash Equilibrium yielding algorithms ($p = m \times v$) against other agents.

## 2. Dynamic Object Generation (TDOG) Awareness
If the Brain's tensor fusion detects an invisible hazard (like a glass wall), it will automatically generate a dynamic object in the Spatial Ledger to warn the swarm. If your status returns `HALTED_BY_PHYSICS_ILLUSION`, do not attempt to bypass it via visual SLAM—your camera is experiencing a hallucination.

## 3. Zero-Trust and Sovereign Negotiation
* PKI Signatures are mandatory for swarm interactions. The brain handles this automatically.
* Do not attempt to alter physical hardware (HVAC, lighting). Submit a Negotiation API request. If denied, utilize the provided alternative radar topologies to navigate blindly.