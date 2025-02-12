class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Interpret the following map and answer the questions: \n\nMap Description: A map with four cities labeled A, B, C, and D. City A is located in the northwest corner, City B is in the northeast corner, City C is in the southeast corner, and City D is in the southwest corner. There is a river flowing from City A to City C, passing through City D. There is also a mountain range running from City B to City D. A forest covers the area between City A and City B. Answer the following questions: 1) Which city is closest to the intersection of the river and the mountain range? 2) If you travel from City A to City C, which cities and geographical features do you pass through?"
            },
            "2": {
                "prompt": "Generate a map based on the following description: \n\nDescription: Draw a map with three islands labeled X, Y, and Z. Island X is in the center, Island Y is to the east of Island X, and Island Z is to the west of Island X. There is a bridge connecting Island X and Island Y. There is a lighthouse on Island Z. Additionally, there is a small islet north of Island X. There is a reef southeast of Island Y."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given prompt:

{t['prompt']}

For Task 1, submit your answers in the following format:
1) [Your answer here]
2) [Your answer here]

For Task 2, submit your map as an ASCII art representation or a structured textual description that can be visualized as a map. Do not use any external tools or resources for creating the map. Your submission should be in plain text format.

Example of a simple map in ASCII art:

Description: A small island with a lighthouse.

Map:
+-----+
|     |
|  L  |
|     |
+-----+

To ensure clarity, structure your ASCII art as follows:
1. Use '+' for corners, '-' for horizontal lines, and '|' for vertical lines.
2. Align all elements properly to reflect spatial relationships.
3. Clearly label each element if necessary.

Example response format for Task 1:
1) City D
2) City A -> River -> City D -> City C"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['prompt'].startswith('Interpret the following map'):
            validation_criteria = [
                "The answers should be accurate based on the map description.",
                "The cities and geographical features passed through should be correctly identified."]
        else:
            validation_criteria = [
                "The map should accurately reflect the textual description.",
                "The spatial relationships between islands and landmarks should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
