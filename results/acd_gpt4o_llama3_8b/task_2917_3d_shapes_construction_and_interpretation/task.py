class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Construct a 3x3x3 cube using the following blocks: 1 red block at (0,0,0), 1 blue block at (1,1,1), and 1 green block at (2,2,2). Fill the remaining blocks with yellow." 
            },
            "2": {
                "structure": "A tower with 3 layers. The first layer has a 3x3 base of red blocks, the second layer has a 2x2 base of blue blocks centered on the red blocks, and the top layer is a single green block centered on the blue blocks."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "description" in t:
            return f"""Construct a 3D shape based on the following description: {t['description']}. Represent the 3D shape as a series of layers from bottom to top, with each layer represented by a 3x3 grid of blocks. Use 'R' for red, 'B' for blue, 'G' for green, and 'Y' for yellow. Submit your response as a plain text string with each layer separated by a blank line.

Example format:
Layer 1:
Y Y Y
Y R Y
Y Y Y

Layer 2:
Y Y Y
Y B Y
Y Y Y

Layer 3:
Y Y Y
Y Y G
Y Y Y"""
        else:
            return f"""Interpret the following 3D structure description and represent it as a series of layers from bottom to top, with each layer represented by a 3x3 grid of blocks. Use 'R' for red, 'B' for blue, and 'G' for green. Submit your response as a plain text string with each layer separated by a blank line.

Description: {t['structure']}

Example format:
Layer 1:
R R R
R R R
R R R

Layer 2:
R R R
R B R
R R R

Layer 3:
Y Y Y
Y Y G
Y Y Y"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The 3D shape should be correctly represented as a series of layers.",
            "Each layer should be a 3x3 grid of blocks with appropriate colors.",
            "The layers should be correctly ordered from bottom to top.",
            "The colors of the blocks should match the description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
