# -*- coding: utf-8 -*-
"""Personal Agent Visceral Adiposity Index Metabolic Skill.

Zero-dependency Amato Visceral Adiposity Index (VAI) calculator, Lipid Accumulation Product (LAP) modeler,
and visceral adipose tissue (VAT) ectopic dysfunction risk evaluator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentVisceralAdiposityIndexMetabolic:
    """Quantitative visceral adipose tissue (VAT) dysfunction and cardiometabolic risk engine
    based on the clinical Visceral Adiposity Index (VAI) formula by Amato et al."""

    def calculate_visceral_adiposity_index(
        self,
        waist_circumference_cm: float = 88.0,
        bmi: float = 24.5,
        triglycerides_mg_dl: float = 110.0,
        hdl_mg_dl: float = 52.0,
        sex: str = "male"
    ) -> Dict[str, Any]:
        """Calculates sex-specific Visceral Adiposity Index (VAI), Lipid Accumulation Product (LAP),
        and cardiometabolic ectopic fat risk tier."""
        wc = max(50.0, float(waist_circumference_cm))
        b = max(15.0, float(bmi))
        tg_mg = max(30.0, float(triglycerides_mg_dl))
        hdl_mg = max(15.0, float(hdl_mg_dl))
        gender = "female" if sex.lower().startswith("f") else "male"

        # Unit conversions from mg/dL to mmol/L:
        # TG: mg/dL * 0.01129 = mmol/L
        # HDL: mg/dL * 0.02586 = mmol/L
        tg_mmol = tg_mg * 0.01129
        hdl_mmol = hdl_mg * 0.02586

        # Amato et al. sex-specific VAI equation:
        if gender == "male":
            wc_denominator = 39.68 + (1.88 * b)
            tg_factor = tg_mmol / 1.03
            hdl_factor = 1.31 / hdl_mmol
            vai = (wc / wc_denominator) * tg_factor * hdl_factor
            lap = max(0.0, (wc - 65.0) * tg_mmol)
        else:
            wc_denominator = 36.58 + (1.89 * b)
            tg_factor = tg_mmol / 0.81
            hdl_factor = 1.52 / hdl_mmol
            vai = (wc / wc_denominator) * tg_factor * hdl_factor
            lap = max(0.0, (wc - 58.0) * tg_mmol)

        vai_rounded = round(max(0.2, vai), 2)
        lap_rounded = round(lap, 1)

        # Clinical VAI Risk Stratification (Amato et al. reference):
        # VAI = 1.0 represents normal visceral adipose function in healthy non-obese individuals
        if vai_rounded <= 1.5:
            risk_tier = "Optimal / Healthy Visceral Adipose Tissue Function"
            clinical_status = "Minimal ectopic fat accumulation; intact insulin sensitivity"
        elif vai_rounded <= 2.5:
            risk_tier = "Mild Visceral Adipose Tissue Dysfunction"
            clinical_status = "Sub-clinical ectopic lipid deposition; early adipokine dysregulation"
        elif vai_rounded <= 3.9:
            risk_tier = "Moderate Visceral Adiposity Dysfunction"
            clinical_status = "Elevated hepatic fat content; increased risk of NAFLD / MASLD"
        else:
            risk_tier = "Severe Visceral Adiposity & High Cardiometabolic Risk"
            clinical_status = "Significant visceral adipose inflammation, atherogenic dyslipidemia, and metabolic syndrome"

        return {
            "sex": gender,
            "waist_circumference_cm": wc,
            "bmi": b,
            "triglycerides_mg_dl": tg_mg,
            "hdl_cholesterol_mg_dl": hdl_mg,
            "visceral_adiposity_index_vai": vai_rounded,
            "lipid_accumulation_product_lap": lap_rounded,
            "visceral_fat_risk_tier": risk_tier,
            "metabolic_dysfunction_assessment": clinical_status,
            "reference_population_baseline": 1.0,
            "adipose_dysfunction_fold_elevation": round(vai_rounded / 1.0, 2)
        }

    def prescribe_visceral_fat_mobilization_protocol(
        self,
        vai_score: float,
        current_fasting_window_hours: float = 12.0
    ) -> Dict[str, Any]:
        """Prescribes evidence-based nutrition and exercise interventions to deplete visceral fat depots."""
        vai = max(0.2, float(vai_score))
        f_hours = max(8.0, float(current_fasting_window_hours))

        if vai >= 3.0:
            recommended_fasting = max(16.0, f_hours + 2.0)
            aerobic_target = "180 min/week Zone 2 aerobic base + 1 weekly sprint interval session"
            dietary_rule = "Strict elimination of liquid sucrose/fructose, refined seed oils, and ultra-processed carbohydrates."
        elif vai >= 1.8:
            recommended_fasting = 14.0
            aerobic_target = "150 min/week Zone 2 aerobic exercise"
            dietary_rule = "Cap refined carbohydrates < 100g/day; focus on high-polyphenol Mediterranean fat profile (extra virgin olive oil, avocado)."
        else:
            recommended_fasting = 12.0
            aerobic_target = "120-150 min/week general aerobic maintenance"
            dietary_rule = "Preserve current balanced dietary habits and caloric equilibrium."

        return {
            "current_vai_score": vai,
            "recommended_intermittent_fasting_window_hours": recommended_fasting,
            "prescribed_cardiorespiratory_protocol": aerobic_target,
            "nutritional_strategy": dietary_rule,
            "biochemical_rationale": "Visceral adipose tissue has higher beta-adrenoceptor density and lipolytic sensitivity to catecholamines during fasted Zone 2 exercise."
        }
