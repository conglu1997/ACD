class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "In a forest ecosystem, a sudden increase in the population of deer is observed. The primary predators of deer in this ecosystem are wolves. Additionally, deer feed on various plant species, including young trees and shrubs. Predict the potential short-term and long-term effects on the ecosystem."},
            "2": {"scenario": "In a coral reef ecosystem, a significant bleaching event has occurred, affecting the coral colonies. Coral reefs are home to many marine species, including fish, crustaceans, and algae. Explain the potential impacts of the bleaching event on the reef ecosystem and its inhabitants."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following ecological scenario and provide your insights or predictions:

{t["scenario"]}

Your response should include:
1. An explanation of the immediate effects based on the given scenario.
2. Predictions of the long-term impacts on the ecosystem and its various components.

Provide your analysis in a clear and concise manner as a plain text string in the following format:

Immediate Effects: [Your explanation]
Long-Term Impacts: [Your predictions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should accurately reflect ecological principles.", "The predictions should be logical and based on the given scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
