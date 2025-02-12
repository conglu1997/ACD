class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Create an analogy:", "concept1": "Time", "concept2": "River"},
            "2": {"task": "Create a metaphor:", "concept1": "Life", "concept2": "Journey"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a creative and insightful analogy or metaphor based on the provided concepts. Ensure that your response clearly illustrates the relationship between the concepts and is expressed in a meaningful way. Here are examples to guide you:

Analogy Example: "Time is like a river, always flowing forward and never going back."
Metaphor Example: "Life is a journey, with its twists and turns, highs and lows."

Concept 1: {t['concept1']}
Concept 2: {t['concept2']}

Provide your analogy or metaphor below in plain text format:"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should clearly illustrate the relationship between the concepts.", "The response should be creative and meaningful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
