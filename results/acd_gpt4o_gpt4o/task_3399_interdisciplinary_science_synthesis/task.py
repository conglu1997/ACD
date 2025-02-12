class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concepts": ["photosynthesis", "electromagnetic spectrum", "energy conservation"], "instruction": "Explain how the given concepts are interrelated and apply them to describe the process of photosynthesis in plants. Provide your response in plain text format, including a detailed and coherent explanation."},
            "2": {"concepts": ["chemical bonding", "cell membrane structure", "diffusion"], "instruction": "Explain the process of nutrient uptake in cells by integrating the given concepts. Provide your response in plain text format, including a detailed and coherent explanation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to synthesize the following scientific concepts to explain a phenomenon or solve a problem:

Concepts: {', '.join(t['concepts'])}

Instruction: {t['instruction']}

Ensure that your explanation accurately integrates the given concepts and is detailed and coherent. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should accurately integrate the given concepts.",
            "The explanation should be detailed and coherent.",
            "The explanation should correctly describe the phenomenon or solve the problem as instructed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
