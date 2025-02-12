class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate an analogy to explain the concept of photosynthesis to a child. Use simple language and relatable examples."
            },
            "2": {
                "prompt": "Create an analogy that explains the relationship between a neuron and a neural network, relating it to a familiar system like a city or a computer network."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an analogy that demonstrates an understanding of relationships between concepts in the following domain:

{t["prompt"]}

Your response should be clear, creative, and accurately capture the relationship between the concepts. A good analogy should draw a parallel between the unfamiliar concept and something familiar to the intended audience. The response should be at least 50 words long. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analogy should be clear and easy to understand.",
            "The analogy should accurately capture the relationship between the concepts.",
            "The analogy should be creative and engaging.",
            "The response should be at least 50 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
