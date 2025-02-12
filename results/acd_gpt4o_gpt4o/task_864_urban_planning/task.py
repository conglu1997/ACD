class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Design a small urban park in a densely populated area. The park should include green spaces, recreational areas, and facilities for community activities. Consider the environmental impact and accessibility for all age groups.", "criteria": {"area_size": "2 acres", "facilities": ["playground", "walking trails", "community garden", "benches"], "age_groups": ["children", "adults", "seniors"]}},
            "2": {"scenario": "Plan a residential neighborhood for a growing city. The neighborhood should have a mix of housing types, public transportation access, and essential services like schools and grocery stores. Ensure the design promotes sustainability and fosters a sense of community.", "criteria": {"housing_types": ["apartments", "townhouses", "single-family homes"], "services": ["school", "grocery store", "public transportation"], "sustainability_features": ["solar panels", "green roofs", "electric vehicle charging stations"]}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an urban area based on the following scenario and criteria:

Scenario: {t['scenario']}

Criteria:
- Area size: {t['criteria'].get('area_size', 'N/A')}
- Facilities: {', '.join(t['criteria'].get('facilities', []))}
- Housing types: {', '.join(t['criteria'].get('housing_types', []))}
- Services: {', '.join(t['criteria'].get('services', []))}
- Age Groups: {', '.join(t['criteria'].get('age_groups', []))}
- Sustainability Features: {', '.join(t['criteria'].get('sustainability_features', []))}

Provide a detailed plan for the urban area, including:

1. A description of the layout and key features.
2. Justification for your design choices, considering community needs, environmental impact, and sustainability.
3. Any additional considerations to ensure the area is practical and beneficial for residents.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The design should be practical and detailed.", "The design should consider community needs, environmental impact, and sustainability.", "The justification should be well-articulated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
