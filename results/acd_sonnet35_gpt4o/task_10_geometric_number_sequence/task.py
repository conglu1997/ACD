import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        shapes = [
            {"name": "circle", "params": {"radius": random.randint(3, 7)}},
            {"name": "square", "params": {"side_length": random.randint(4, 8)}},
            {"name": "equilateral_triangle", "params": {"side_length": random.randint(5, 9)}},
            {"name": "spiral", "params": {"turns": random.randint(2, 4)}}
        ]
        return {
            "1": random.choice(shapes),
            "2": random.choice(shapes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        shape = t["name"]
        params = t["params"]
        
        instructions = f"Create a sequence of at least 20 integer coordinate pairs (x, y) that, when plotted on a coordinate plane, form an approximation of a {shape}. "
        
        if shape == "circle":
            instructions += f"The circle should have a radius of approximately {params['radius']} units and be centered at the origin (0, 0)."
        elif shape == "square":
            instructions += f"The square should have a side length of approximately {params['side_length']} units and be centered at the origin (0, 0)."
        elif shape == "equilateral_triangle":
            instructions += f"The equilateral triangle should have a side length of approximately {params['side_length']} units and be centered at the origin (0, 0)."
        elif shape == "spiral":
            instructions += f"The spiral should make approximately {params['turns']} turns around the origin (0, 0), starting close to the origin and moving outward."
        
        instructions += "\n\nApproach:\n"
        instructions += "1. Consider the mathematical properties of the shape and how they relate to coordinates.\n"
        instructions += "2. Use integer approximations where necessary to create the shape.\n"
        instructions += "3. Ensure the sequence of points, when connected, forms a recognizable approximation of the shape.\n"
        
        instructions += "\nRules:\n"
        instructions += "1. All coordinates must be integers.\n"
        instructions += "2. The sequence should form a recognizable approximation of the specified shape.\n"
        instructions += "3. Provide at least 20 coordinate pairs.\n"
        instructions += "4. The shape should be centered around the origin (0, 0) unless otherwise specified.\n"
        
        instructions += "\nProvide your answer in the following format:\n"
        instructions += "Coordinates: [(x1, y1), (x2, y2), ..., (xn, yn)]\n"
        instructions += "Explanation: A brief explanation of your approach and how the coordinates approximate the required shape."
        
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The sequence forms a recognizable approximation of a {t['name']} when plotted.",
            "All coordinates are integers.",
            "The sequence contains at least 20 coordinate pairs.",
            f"The {t['name']} approximately matches the specified parameters: {t['params']}.",
            "The solution demonstrates creativity in generating the sequence while adhering to the constraints.",
            "The explanation provides insight into the approach used to generate the coordinates."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
