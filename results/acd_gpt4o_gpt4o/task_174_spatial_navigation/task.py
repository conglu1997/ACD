class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate", "start": "entrance", "end": "cafeteria", "map": "entrance -> hallway -> left -> stairs -> right -> cafeteria"},
            "2": {"type": "interpret", "instructions": "Go straight from the entrance, take the first left, then go up the stairs, take a right and the cafeteria will be on your left.", "map": "entrance -> hallway -> left -> stairs -> right -> cafeteria"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate":
            start = t["start"]
            end = t["end"]
            map = t["map"]
            instructions = f"""Your task is to generate spatial instructions for navigating from the {start} to the {end}.

Map: {map}

Ensure the instructions are clear, concise, and accurately reflect the map. Provide the instructions in a step-by-step plain text format."""
        elif t["type"] == "interpret":
            instructions = t["instructions"]
            map = t["map"]
            instructions = f"""Your task is to interpret the following spatial instructions and verify if they correctly describe the given map.

Instructions: {instructions}
Map: {map}

Provide your response as 'Correct' or 'Incorrect' along with an explanation if it is incorrect. Ensure your explanation details which part of the instructions does not match the map."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate":
            criteria = [
                "The generated instructions should be clear and concise.",
                "The instructions should accurately reflect the provided map.",
                "The start and end points should be correctly identified.",
                "The instructions must be in a step-by-step format."
            ]
        elif t["type"] == "interpret":
            criteria = [
                "The interpretation should correctly identify if the instructions match the map.",
                "If identified as incorrect, the explanation should be accurate and clear, detailing which part of the instructions does not match the map."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
