# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Visceral Adiposity Index Metabolic Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentVisceralAdiposityIndexMetabolic

mcp = FastMCP("PersonalAgentVisceralAdiposityIndexMetabolic")
client = PersonalAgentVisceralAdiposityIndexMetabolic()

@mcp.tool()
def calculate_visceral_adiposity_index(
    waist_circumference_cm: float = 88.0,
    bmi: float = 24.5,
    triglycerides_mg_dl: float = 110.0,
    hdl_mg_dl: float = 52.0,
    sex: str = "male"
) -> str:
    """Calculates sex-specific Visceral Adiposity Index (VAI), Lipid Accumulation Product (LAP), and risk tier."""
    import json
    return json.dumps(client.calculate_visceral_adiposity_index(
        waist_circumference_cm, bmi, triglycerides_mg_dl, hdl_mg_dl, sex
    ), indent=2)

@mcp.tool()
def prescribe_visceral_fat_mobilization_protocol(
    vai_score: float = 2.2,
    current_fasting_window_hours: float = 12.0
) -> str:
    """Prescribes fasting window and Zone 2 exercise protocol to mobilize ectopic visceral adipose tissue."""
    import json
    return json.dumps(client.prescribe_visceral_fat_mobilization_protocol(
        vai_score, current_fasting_window_hours
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
