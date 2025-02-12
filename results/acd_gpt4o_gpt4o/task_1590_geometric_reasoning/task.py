class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "complex_polygon", "parameters": {"sides": 7, "angles": [120, 150, 140, 110, 90, 100, 150], "lengths": [5, 6, 7, 5, 6, 7, 8]}, "expected_result": "A detailed description of the shape's properties and structure."},
            "2": {"puzzle": "A triangle has angles of 65° and 85°, and one side of length 10 units. Calculate the missing angle, the type of triangle, and the lengths of the other sides.", "expected_result": "A clear explanation, correct missing angle, and accurate side lengths."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "shape" in t:
            return f"""Generate a detailed description of the following geometric shape based on the given parameters:

Shape: {t['shape']}
Parameters: Sides - {t['parameters']['sides']}, Angles - {', '.join(map(str, t['parameters']['angles']))}, Lengths - {', '.join(map(str, t['parameters']['lengths']))}

Provide the description in a clear, coherent format, ensuring it includes all relevant geometric properties and structural details. The description should be in plain text format and at least 100 words. Mention the type of polygon, the sum of angles, and any symmetry properties.
"""
        else:
            return f"""Solve the following geometric puzzle and provide a detailed explanation of your solution:

Puzzle: {t['puzzle']}

Ensure your explanation is clear and includes all necessary steps to arrive at the correct solution. Provide your answer in plain text format with the following details:
1. The missing angle
2. The type of triangle (acute, right, or obtuse)
3. The lengths of the other sides
4. A step-by-step explanation of how you arrived at the solution
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "shape" in t:
            criteria = ["The description should be detailed, coherent, and accurately reflect the given parameters."]
        else:
            criteria = ["The solution should be correct, and the explanation should clearly outline the steps to determine the missing angle, type of triangle, and side lengths."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
