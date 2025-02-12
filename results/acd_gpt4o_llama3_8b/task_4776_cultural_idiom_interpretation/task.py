class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "Break the ice", "context": "During the meeting, John decided to tell a joke to break the ice."},
            "2": {"idiom": "Spill the beans", "context": "After weeks of secrecy, Mary finally spilled the beans about the surprise party."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following idiom and explain its meaning in the given context. Ensure that your explanation includes:
1. The literal meaning of the idiom.
2. The figurative meaning of the idiom.
3. A contextual explanation of how the idiom applies to the provided context.

Idiom: {t['idiom']}
Context: {t['context']}

Submit your explanation in the following format:
Literal Meaning: [Your literal interpretation]
Figurative Meaning: [Your figurative interpretation]
Contextual Explanation: [How the idiom applies to the context]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should include both the literal and figurative meanings of the idiom.",
            "The explanation should clearly relate the idiom to the provided context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
