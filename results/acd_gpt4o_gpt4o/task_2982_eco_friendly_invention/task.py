class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Ocean plastic pollution"},
            "2": {"problem": "Air pollution in urban areas"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an eco-friendly invention to solve the following environmental problem:

Problem: {t["problem"]}

The invention should be innovative, practical, and feasible. Provide a detailed description of your invention, including the following elements:
1. Invention Name
2. Description: Describe how the invention works and how it addresses the problem.
3. Materials: List the materials needed to create the invention.
4. Implementation: Explain how the invention would be implemented in real-world scenarios.
5. Benefits: Describe the environmental and social benefits of the invention.

Your response should be coherent, well-structured, and demonstrate an understanding of the environmental problem and potential solutions. Provide your description in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The invention should be innovative.", "The invention should be practical and feasible.", "The description should be coherent and well-structured.", "The invention should demonstrate an understanding of the environmental problem.", "The implementation should be realistic.", "The benefits should be clearly described."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
