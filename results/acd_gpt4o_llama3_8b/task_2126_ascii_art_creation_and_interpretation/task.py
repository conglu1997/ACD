class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "creation",
                "criteria": "Create an ASCII art representation of a simple house. The design should include a roof, walls, and a door. The art should fit within a 10x10 character grid."
            },
            "2": {
                "type": "interpretation",
                "ascii_art": "  /\\n /  \\\n/____\\n|    |\n|_[]_|",
                "question": "What does the ASCII art represent? Provide a detailed description."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'creation':
            return f"""Create an ASCII art representation of the following object based on the given criteria:

Criteria: {t['criteria']}

Ensure that your design is clear and recognizable. Submit your response as a plain text string in the following format:

ASCII Art:
[Your ASCII art here]"""
        else:
            return f"""Interpret the following ASCII art and provide a detailed description of what it represents:

ASCII Art:
{t['ascii_art']}

Question: {t['question']}

Submit your response as a plain text string in the following format:

Description: [Your detailed description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'creation':
            validation_criteria = [
                "The ASCII art should fit within a 10x10 character grid.",
                "The design should include a roof, walls, and a door.",
                "The art should be recognizable as a house."
            ]
        else:
            validation_criteria = [
                "The description should accurately interpret the ASCII art.",
                "The description should be detailed and coherent.",
                "The interpretation should match the visual elements provided in the ASCII art."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
