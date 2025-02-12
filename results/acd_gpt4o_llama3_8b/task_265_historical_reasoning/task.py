class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Imagine that the Industrial Revolution had never occurred in Europe. Discuss the potential implications for global development and technological progress.",
                "constraints": [
                    "Consider the impact on economic systems, societal structures, and technological advancements.",
                    "Account for alternative historical developments that may have arisen in the absence of the Industrial Revolution."]
            },
            "2": {
                "scenario": "Consider a scenario where the Roman Empire never fell. Discuss the potential implications for European history and global geopolitics.",
                "constraints": [
                    "Consider the impact on cultural, political, and technological developments in Europe and beyond.",
                    "Account for the interactions between the Roman Empire and other civilizations."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        constraints = "\n".join(t["constraints"])
        return f"""Analyze the following historical scenario and explain the potential outcomes or significance of these events. The scenario is: {scenario}\n
Here are the constraints:\n{constraints}\n
Submit your analysis and explanation as a plain text string in the following format: 'Analysis: [Your analysis]\nExplanation: [Your explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should be historically plausible.", "The explanation should logically follow from the scenario and constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
