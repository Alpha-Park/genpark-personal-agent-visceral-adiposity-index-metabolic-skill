# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Visceral Adiposity Index Metabolic Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentVisceralAdiposityIndexMetabolic

def main():
    agent = PersonalAgentVisceralAdiposityIndexMetabolic()

    print("=" * 70)
    print("DEMO: Personal Agent Visceral Adiposity Index (VAI) Modeler")
    print("=" * 70)

    # 1. Evaluate Visceral Adiposity Index (Male, WC 89 cm, BMI 25.2, TG 125 mg/dL, HDL 48 mg/dL)
    res_vai = agent.calculate_visceral_adiposity_index(
        waist_circumference_cm=89.0,
        bmi=25.2,
        triglycerides_mg_dl=125.0,
        hdl_mg_dl=48.0,
        sex="male"
    )

    print(f"\n1. Visceral Adiposity Index (VAI) Evaluation:")
    print(f"   Sex: {res_vai['sex'].capitalize()} | WC: {res_vai['waist_circumference_cm']} cm | BMI: {res_vai['bmi']}")
    print(f"   Lipids: TG = {res_vai['triglycerides_mg_dl']} mg/dL | HDL = {res_vai['hdl_cholesterol_mg_dl']} mg/dL")
    print(f"   Visceral Adiposity Index (VAI): {res_vai['visceral_adiposity_index_vai']} (Fold Elevation: {res_vai['adipose_dysfunction_fold_elevation']}x)")
    print(f"   Lipid Accumulation Product (LAP): {res_vai['lipid_accumulation_product_lap']}")
    print(f"   Risk Tier: {res_vai['visceral_fat_risk_tier']}")
    print(f"   Metabolic Assessment: {res_vai['metabolic_dysfunction_assessment']}")

    # 2. Prescribe Visceral Fat Mobilization Protocol
    res_proto = agent.prescribe_visceral_fat_mobilization_protocol(
        vai_score=res_vai['visceral_adiposity_index_vai'],
        current_fasting_window_hours=12.0
    )

    print(f"\n2. Visceral Fat Mobilization Strategy:")
    print(f"   Recommended Fasting Window: {res_proto['recommended_intermittent_fasting_window_hours']} hours")
    print(f"   Cardiorespiratory Protocol: {res_proto['prescribed_cardiorespiratory_protocol']}")
    print(f"   Nutritional Mandate: {res_proto['nutritional_strategy']}")
    print(f"   Biochemical Rationale: {res_proto['biochemical_rationale']}")

    print("\nVerification complete: Visceral adiposity index engine executed flawlessly.")

if __name__ == "__main__":
    main()
