class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ecosystem": "Amazon Rainforest", "additional_criteria": ["Describe the key characteristics of the ecosystem.", "Identify major threats to biodiversity in this ecosystem.", "Propose detailed and feasible measures to protect biodiversity.", "Consider the socio-economic factors impacting biodiversity conservation in this ecosystem."]},
            "2": {"ecosystem": "Great Barrier Reef", "additional_criteria": ["Describe the key characteristics of the ecosystem.", "Identify major threats to biodiversity in this ecosystem.", "Propose detailed and feasible measures to protect biodiversity.", "Consider the socio-economic factors impacting biodiversity conservation in this ecosystem."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the following ecosystem and propose measures to protect its biodiversity:

Ecosystem: {t['ecosystem']}

Ensure your analysis meets the following criteria:
{', '.join(t['additional_criteria'])}

Provide a detailed description of the ecosystem's key characteristics, identify major threats to biodiversity, and propose effective measures to protect biodiversity. Additionally, consider socio-economic factors impacting conservation efforts.

Response format:
1. Key Characteristics: [Detailed description of the ecosystem's key characteristics]
2. Major Threats: [Identification of major threats to biodiversity]
3. Protection Measures: [Detailed and feasible measures to protect biodiversity]
4. Socio-economic Factors: [Consideration of socio-economic factors impacting conservation efforts]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get('additional_criteria', [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
