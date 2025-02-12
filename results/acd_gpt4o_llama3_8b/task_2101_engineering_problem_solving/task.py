class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Design a bridge to span a 50-meter wide river with minimal environmental impact.", "constraints": "Use sustainable materials and ensure the design can support both pedestrian and light vehicle traffic. Include considerations for environmental impacts such as reducing construction footprint and protecting local wildlife."},
            "2": {"scenario": "Create a solar-powered irrigation system for a small farm.", "constraints": "The system should be cost-effective, easy to maintain, and capable of irrigating 2 hectares of land. Ensure the design includes a water distribution mechanism that operates efficiently with solar power."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a solution for the following engineering challenge based on the given scenario and constraints:

Scenario: {t["scenario"]}
Constraints: {t["constraints"]}

Ensure that your solution is practical, feasible, and adheres to the specified constraints. Provide a detailed description of your solution, including any relevant diagrams or calculations. If diagrams or calculations are necessary, describe them in text form. Format your response with clear sections and use bullet points or numbered lists where applicable. Submit your response as a plain text string.

Example:
For the scenario 'Design a bridge to span a 50-meter wide river' with the constraints 'Use sustainable materials and ensure the design can support both pedestrian and light vehicle traffic. Include considerations for environmental impacts such as reducing construction footprint and protecting local wildlife,' a suitable solution could be 'A suspension bridge using bamboo and recycled steel cables, with a wooden deck reinforced with fiberglass to support the weight of pedestrians and light vehicles. The construction footprint is minimized by using pre-fabricated components, and measures are taken to protect the local fish population during construction.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be practical and feasible.",
            "The solution should adhere to the specified constraints.",
            "The solution should demonstrate an understanding of engineering principles.",
            "The solution should include clear sections and be well-organized.",
            "If relevant, the solution should include any necessary diagrams or calculations described in text form."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
