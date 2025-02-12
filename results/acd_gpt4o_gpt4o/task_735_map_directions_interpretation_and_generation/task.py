class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "interpretation", "directions": "Start at Main Street, go straight for 2 blocks, turn left at Pine Avenue, go straight for 1 block, then turn right at Oak Street, and your destination is the second building on the left."},
            "2": {"type": "generation", "start": "Central Park", "end": "Museum of Art"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'interpretation':
            return f"""Your task is to interpret the given map directions and describe the route clearly.

Directions: {t['directions']}

Your response should include:
1. A detailed description of the route.
2. The key turns and landmarks mentioned.
3. The final destination.

Provide your response in plain text format.

Example:
Directions: Start at Elm Street, go straight for 3 blocks, turn right at Oak Avenue, go straight for 2 blocks, and your destination is the first house on the left.
1. The route starts at Elm Street and goes straight for 3 blocks.
2. Then, turn right at Oak Avenue and continue straight for 2 blocks.
3. The final destination is the first house on the left."""
        elif t['type'] == 'generation':
            return f"""Your task is to generate map directions from the given start location to the given end location.

Start Location: {t['start']}
End Location: {t['end']}

Your response should include:
1. Clear and coherent directions from the start location to the end location.
2. Key turns and landmarks to help navigate the route.
3. Ensure the directions are logical and easy to follow.

Provide your response in plain text format.

Example:
Start Location: Library
End Location: Coffee Shop
1. Start at the Library, go straight for 2 blocks on Maple Street.
2. Turn left at Birch Avenue and go straight for 1 block.
3. The Coffee Shop is the second building on the right."""
        else:
            raise ValueError("Unknown task type.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'interpretation':
            criteria = [
                "The description of the route should be detailed and accurate.",
                "The key turns and landmarks should be correctly identified.",
                "The final destination should be correctly stated."
            ]
        elif t['type'] == 'generation':
            criteria = [
                "The generated directions should be clear and coherent.",
                "The key turns and landmarks should be logically placed.",
                "The directions should lead correctly from the start location to the end location."
            ]
        else:
            raise ValueError("Unknown task type.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
