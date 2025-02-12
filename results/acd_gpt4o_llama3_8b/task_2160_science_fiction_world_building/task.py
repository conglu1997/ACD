class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"fictional_world": "A planet with floating islands that move across the sky.", "synthetic_examples": ["A world where plants can communicate with each other through bioluminescent signals.", "A planet with oceans of liquid methane."]},
            "2": {"fictional_world": "A civilization that has harnessed the power of black holes for energy.", "synthetic_examples": ["An ecosystem where all life forms are based on silicon instead of carbon.", "A world where the atmosphere is composed mostly of neon."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        return f"""Create a scientifically plausible explanation for the following fictional world or phenomenon. Your explanation should be clear, coherent, and demonstrate an understanding of relevant scientific principles.

Fictional World: {t['fictional_world']}

Additional examples:
{examples}

Submit your response as a plain text string in the following format:

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should provide a scientifically plausible explanation for the fictional world: {t['fictional_world']}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
