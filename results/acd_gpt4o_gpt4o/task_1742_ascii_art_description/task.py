class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ascii_art": ""
                        "  /\ \n"
                        " /  \ \n"
                        "/____\ \n"
                        "|    | \n"
                        "|____| \n"
                        ""},
            "2": {"ascii_art": ""
                        "  \   /\n"
                        "   o o\n"
                        "    ~\n"
                        "\_____/\n"
                        ""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed description or narrative based on the given piece of ASCII art. Use your creativity to describe what the art represents, and provide a coherent and engaging narrative or description that matches the visual elements.

ASCII Art:
{t['ascii_art']}

Provide your description or narrative in plain text format. Ensure that your response is detailed and provides a clear representation of the ASCII art."

Response Format:
Description/Narrative: [Your detailed description or narrative]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description or narrative should accurately represent the elements present in the ASCII art.",
            "The narrative should be coherent, engaging, and creatively written.",
            "The description should be detailed and provide a clear representation of the ASCII art."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
