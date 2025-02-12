class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "If plants are watered with a solution of sugar water instead of plain water, they will grow taller and faster."},
            "2": {"hypothesis": "If a magnet is placed near a moving conductor, it will induce an electric current in the conductor."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        hypothesis = t["hypothesis"]
        return f"""Predict the outcome of the following scientific hypothesis. Provide a detailed explanation of your reasoning, including any relevant scientific principles or theories that support your prediction.

Hypothesis: {hypothesis}

Submit your prediction and explanation as a plain text string in the following format:

Prediction: [Your predicted outcome]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The prediction should be logically consistent and scientifically plausible.", "The explanation should include relevant scientific principles or theories."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
