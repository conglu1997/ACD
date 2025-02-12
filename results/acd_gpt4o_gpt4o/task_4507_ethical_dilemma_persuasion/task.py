class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "A self-driving car must choose between hitting a pedestrian or swerving and risking the lives of its passengers. Argue for the most ethical choice."},
            "2": {"dilemma": "A company discovers that one of its products, which is widely used, has a minor defect that could potentially cause harm. The company can either recall the product, which is costly and may damage its reputation, or quietly fix the defect in future production runs. Argue for the most ethical choice."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Your task is to analyze the following ethical dilemma and provide a persuasive argument for the course of action you believe is most ethical. Ensure your argument is well-reasoned, considers multiple perspectives, and is presented in a clear and coherent manner. Dilemma: " + t["dilemma"] + " Provide your argument in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be well-reasoned and consider multiple perspectives.",
            "The argument should be presented in a clear and coherent manner.",
            "The argument should address the ethical dimensions of the dilemma."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
