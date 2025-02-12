class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Explain the forces acting on a static block on an inclined plane."},
            "2": {"scenario": "Describe and illustrate the electric field lines around a positive and a negative charge."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to generate a diagram and accompanying description based on the following scenario:

Scenario: {0}

Ensure that your diagram accurately represents the physical phenomena described in the scenario. Your description should clearly explain the elements of the diagram and the principles involved. Provide your response in the following format:

1. Diagram: [Your diagram description]
2. Description: [Your detailed description]

Example (different scenario):
Scenario: Illustrate the forces acting on a falling object with air resistance.
Diagram: A diagram showing a falling object with arrows representing the gravitational force and the air resistance force.
Description: The diagram depicts a falling object experiencing two forces: gravitational force acting downward and air resistance acting upward, opposing the motion. The length of the arrows indicates the relative magnitudes of the forces.""".format(t["scenario"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The diagram should accurately represent the physical phenomena described in the scenario.",
            "The description should clearly explain the elements of the diagram and the principles involved.",
            "The response should be scientifically accurate and understandable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
