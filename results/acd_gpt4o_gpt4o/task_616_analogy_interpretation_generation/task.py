class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"analogy": "Life is like a box of chocolates."},
            "2": {"analogy": "Time is a thief."}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the meaning of the given analogy and create a new analogy with an explanation:

Analogy: {t['analogy']}

1. Interpret the given analogy and explain its meaning in your own words. Ensure your explanation is clear, accurate, and contextually appropriate.
2. Create a new analogy and provide an explanation of its meaning and context. The new analogy should be original, coherent, and culturally appropriate.

Provide your response in the following format:

Interpretation: [Your interpretation]
New Analogy: [Your new analogy]
Explanation: [Explanation of your new analogy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
