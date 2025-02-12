class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "A group of plants in an experimental garden showed varied growth rates when exposed to different amounts of sunlight. Group A received 2 hours of sunlight daily, Group B received 4 hours, and Group C received 6 hours. Group A grew 10 cm on average, Group B grew 15 cm, and Group C grew 20 cm.", "constraints": "Formulate a hypothesis explaining the relationship between sunlight exposure and plant growth. Provide reasoning for your hypothesis based on the given data.", "domain": "botany"},
            "2": {"data": "In a lab experiment, two different chemicals were tested for their effect on bacterial growth. Chemical X was added to a bacterial culture, resulting in a 50% reduction in bacterial colonies. Chemical Y was added to another culture, leading to a 70% reduction in colonies.", "constraints": "Formulate a hypothesis explaining the effect of the two chemicals on bacterial growth. Provide reasoning for your hypothesis based on the given data.", "domain": "microbiology"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        data = t["data"]
        constraints = t["constraints"]
        domain = t["domain"]
        instructions = f"""Your task involves two parts:\n\n1. Hypothesis Formulation: Based on the following data and constraints, formulate a scientific hypothesis.\n\nData: {data}\n\nConstraints: {constraints}\n\n2. Hypothesis Reasoning: Provide a detailed explanation of the reasoning behind your hypothesis, including how the data supports your hypothesis and any underlying scientific principles.\n\nEnsure that your hypothesis is coherent, scientifically plausible, and adheres to the given constraints. Your reasoning should demonstrate an understanding of the scientific process and the relationship between the data and the hypothesis.\n\nResponse Format:\nHypothesis: <Your hypothesis>\nReasoning: <Your reasoning>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be scientifically plausible.",
            "The hypothesis should be based on the given data.",
            "The reasoning should explain how the data supports the hypothesis.",
            "The reasoning should demonstrate an understanding of the underlying scientific principles."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
