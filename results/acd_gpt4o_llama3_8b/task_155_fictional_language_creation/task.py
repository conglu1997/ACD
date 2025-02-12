class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Create a fictional language with basic grammar rules (including word order, verb conjugation, and noun-adjective agreement). Translate the following sentence into your fictional language: 'The quick brown fox jumps over the lazy dog.'"
            },
            "2": {
                "requirements": "Create a fictional language with basic grammar rules (including word order, verb conjugation, and noun-adjective agreement). Translate the following sentence into your fictional language: 'She sells seashells by the seashore.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional language with basic grammar rules and translate the given sentence into that language.

Requirements:
{t['requirements']}

Ensure that your fictional language includes the following components:
1. Basic grammar rules (word order, verb conjugation, noun-adjective agreement).
2. Examples for each grammar rule.
3. A consistent application of these rules in the translation.

Submit your response in the following format:
1. Grammar Rules: [Your grammar rules with examples]
2. Translation: [Your translation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The fictional language must include basic grammar rules with examples.", "The translation must be consistent with the provided grammar rules."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
