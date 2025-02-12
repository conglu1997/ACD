class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Discuss how the concept of entropy in thermodynamics can be related to the theme of chaos in abstract art."
            },
            "2": {
                "prompt": "Analyze how the Fibonacci sequence is used in both nature (e.g., the arrangement of leaves) and in classical music compositions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Synthesize information from both scientific and artistic domains to generate a coherent and insightful response to the following prompt:

{t["prompt"]}

Your response should demonstrate a deep understanding of both fields and provide a meaningful connection between them. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should demonstrate a deep understanding of both scientific and artistic domains.",
            "The response should provide a meaningful connection between the two fields.",
            "The response should be coherent and insightful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
