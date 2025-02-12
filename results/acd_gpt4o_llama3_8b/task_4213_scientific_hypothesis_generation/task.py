class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "observations": "In a remote forest area, scientists have observed that the population of a certain species of bird has been declining over the past decade. The forest area has also seen an increase in industrial activities and deforestation during the same period.",
                "task_type": "generate"
            },
            "2": {
                "hypothesis": "The decline in the bird population is primarily due to the increase in industrial activities and deforestation in the forest area.",
                "task_type": "validate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            return f"""Based on the following observations, generate a plausible scientific hypothesis. Your hypothesis should be clear, concise, and logically derived from the observations. Additionally, explain the reasoning behind your hypothesis and how it connects to the observations.

Observations:
{t['observations']}

Submit your hypothesis and reasoning as a plain text string in the following format:

Hypothesis: [Your hypothesis]
Reasoning: [Your reasoning]"""
        elif t["task_type"] == "validate":
            return f"""Validate the following scientific hypothesis using logical reasoning and scientific principles. Your validation should include supporting evidence, potential counterarguments, and a conclusion on whether the hypothesis is likely to be true or false based on the provided information.

Hypothesis:
{t['hypothesis']}

Submit your validation as a plain text string in the following format:

Validation: [Your validation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generate":
            validation_criteria = ["The hypothesis should be clear and logically derived from the observations.", "The reasoning should explain how the hypothesis connects to the observations."]
        elif t["task_type"] == "validate":
            validation_criteria = ["The validation should use logical reasoning and scientific principles.", "The validation should include supporting evidence and address potential counterarguments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
