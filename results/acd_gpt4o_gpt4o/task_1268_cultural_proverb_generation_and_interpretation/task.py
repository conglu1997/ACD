class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"proverb": "Actions speak louder than words.", "additional_criteria": ["Provide the meaning of the proverb.", "Explain the cultural context and significance of the proverb.", "Include examples demonstrating the proverb in real-life situations."]},
            "2": {"theme": "Perseverance", "culture": "Japanese", "additional_criteria": ["Generate a culturally relevant proverb based on the given theme.", "Explain the cultural significance of the generated proverb.", "Provide a hypothetical scenario where the proverb can be applied."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "proverb" in t:
            instructions = f"""Your task is to interpret the following proverb:

{t['proverb']}

Ensure your interpretation meets the following criteria:
{', '.join(t['additional_criteria'])}

Provide a detailed explanation of the proverb's meaning, its cultural context, and significance. Also, include examples demonstrating the proverb in real-life situations.

Response format:
1. Meaning: [Detailed explanation of the proverb's meaning]
2. Cultural Context: [Explanation of the cultural context and significance]
3. Real-life Examples: [Examples demonstrating the proverb in real-life situations]"""
        else:
            instructions = f"""Your task is to generate a culturally relevant proverb based on the following theme and culture:

Theme: {t['theme']}
Culture: {t['culture']}

Ensure your generated proverb meets the following criteria:
{', '.join(t['additional_criteria'])}

Provide the generated proverb, explain its cultural significance, and provide a hypothetical scenario where the proverb can be applied.

Response format:
1. Proverb: [Generated proverb]
2. Cultural Significance: [Explanation of the cultural significance]
3. Hypothetical Scenario: [Hypothetical scenario where the proverb can be applied]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get('additional_criteria', [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
