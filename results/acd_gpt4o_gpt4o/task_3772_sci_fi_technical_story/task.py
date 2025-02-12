class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concepts": ["quantum entanglement", "artificial intelligence"], "constraints": ["Must include a character who is a scientist.", "Story should be set in a space station.", "The plot must involve a scientific experiment gone wrong."]},
            "2": {"concepts": ["time travel", "genetic engineering"], "constraints": ["Must include a character who is a historian.", "Story should be set in a dystopian future.", "The plot must involve a paradox created by time travel."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concepts = ", ".join(t["concepts"])
        constraints = "\n".join(f"- {constraint}" for constraint in t["constraints"])
        instructions = f"""Your task is to write a short science fiction story that incorporates the following scientific concepts and adheres to the given constraints:

Scientific Concepts: {concepts}

Constraints:
{constraints}

Your story should be creative, engaging, and scientifically plausible. Ensure that you integrate the scientific concepts seamlessly into the narrative and follow all the constraints. The story should be between 500 to 1000 words long. Provide your story in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should incorporate the given scientific concepts.",
            "The story should adhere to all specified constraints.",
            "The story should be creative, engaging, and scientifically plausible.",
            "The story should be coherent and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
