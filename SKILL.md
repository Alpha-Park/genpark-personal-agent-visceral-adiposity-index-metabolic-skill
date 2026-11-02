---
name: genpark-personal-agent-visceral-adiposity-index-metabolic-skill
version: "1.0.0"
description: "Zero-dependency Amato Visceral Adiposity Index (VAI) calculator, Lipid Accumulation Product (LAP) modeler, and visceral adipose tissue (VAT) ectopic dysfunction risk evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Visceral Adiposity Index Metabolic Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to evaluate visceral adipose tissue (VAT) endocrine dysfunction, compute sex-specific Visceral Adiposity Index ($VAI$) and Lipid Accumulation Product ($LAP$), and prescribe targeted catecholamine-mediated visceral lipolysis protocols.

## Agent In-Context Capabilities

- **Amato Mathematical Formulation**: Synthesizes anthropometric (Waist Circumference, BMI) and metabolic (Triglycerides, HDL) biomarkers into a validated surrogate for visceral adiposity.
- **Ectopic Fat Risk Stratification**: Identifies occult visceral fat accumulation in normal-BMI individuals (Normal Weight Obese phenotype).
- **Targeted Lipolysis Prescriptions**: Tailors fasted Zone 2 cardio and intermittent fasting protocols to exploit the high $\beta_1/\beta_2$-adrenoceptor density of visceral depots.

## Tools Summary

1. `calculate_visceral_adiposity_index`: Computes VAI, LAP, fold elevation over baseline, and risk tier.
2. `prescribe_visceral_fat_mobilization_protocol`: Recommends fasting window, cardiorespiratory volume, and dietary strategies.
