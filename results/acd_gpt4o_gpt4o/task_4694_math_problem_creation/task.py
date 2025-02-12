class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "geometry", "constraint": "involving circles and triangles"},
            "2": {"topic": "number theory", "constraint": "involving prime numbers and divisibility"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        constraint = t["constraint"]
        instructions = f"""Your task is to create a novel and interesting mathematical problem based on the given topic and constraint.

Topic: {topic}
Constraint: {constraint}

Describe the problem clearly and ensure it is solvable. Provide your response in the following format:

Problem:
[Your problem description]

Solution:
[Solution to the problem]

Example:
Problem:
Given a triangle with sides of length 3, 4, and 5, inscribe a circle within the triangle. Calculate the radius of the inscribed circle.

Solution:
The radius of the inscribed circle in a triangle with sides 3, 4, and 5 can be calculated using the formula r = A/s, where A is the area and s is the semi-perimeter. The area A = 6 and the semi-perimeter s = 6, so the radius r = 1.

Make sure the problem adheres strictly to the given topic and constraint, and the solution is correct and well-explained."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The problem should be clear and understandable.", "The problem should adhere to the given topic and constraint.", "The problem should be novel and interesting.", "The solution should be correct and well-explained."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
