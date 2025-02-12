class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parameters": "Create a fictional world that is primarily aquatic. Describe its geography, main species, cultural practices, and any unique technologies."},
            "2": {"parameters": "Create a fictional world where technology has advanced to the point of teleportation. Describe its society, main challenges, everyday life, and any unique laws or customs."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed description of a fictional world based on the given parameters. Ensure that your description is coherent, imaginative, and includes all relevant details.

Parameters: {t["parameters"]}

Your response should include:
1. A description of the world's geography.
2. The main species living in this world.
3. Cultural practices and societal norms.
4. Any unique technologies or laws.
5. Any additional details that make the world unique and believable.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a coherent and imaginative description of the world's geography.",
            "The response should describe the main species living in the world.",
            "The response should include cultural practices and societal norms.",
            "The response should mention any unique technologies or laws.",
            "The response should be detailed and unique."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
