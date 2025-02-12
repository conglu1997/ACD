class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Time is...", "type": "metaphor"},
            "2": {"prompt": "A computer is to data as...", "type": "analogy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following {t['type']} prompt and explain your reasoning.

Prompt: {t['prompt']}

Your response should include:
1. The completed {t['type']}.
2. An explanation of how the {t['type']} relates to the prompt and why it is appropriate.

Ensure your response is thoughtful, coherent, and demonstrates a clear understanding of the concepts involved. Format your response as follows:

1. Completed {t['type']}:
2. Explanation:"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should complete the prompt meaningfully.",
            "The explanation should clearly relate the completed prompt to the original and justify its appropriateness."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
