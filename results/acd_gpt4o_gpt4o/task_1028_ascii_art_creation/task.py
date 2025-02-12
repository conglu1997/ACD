class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create an ASCII art representation of a simple house with a door, windows, and a roof.", "requirements": "The art should include at least one door, two windows, and a triangular roof."},
            "2": {"description": "Interpret the following ASCII art and describe what it represents:", "ascii_art": "  /\  \n /  \ \n/____\ \n|    | \n|_[]_|"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "ascii_art" in t:
            instructions = f"""Your task is to interpret the following ASCII art and describe what it represents:

{t['ascii_art']}

Provide your answer in plain text format, clearly and concisely describing the object represented by the ASCII art."""
        else:
            instructions = f"""Your task is to create an ASCII art representation based on the following description:

{t['description']}

Ensure your ASCII art meets the specified requirements and is visually recognizable.

Example format for your ASCII art:

  /\  
 /  \ 
/____\ 
|    | 
|_[]_| 

This is just an example. Ensure your ASCII art is original and fits the given description."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "ascii_art" in t:
            criteria = ["The description should accurately describe the object represented by the ASCII art."]
        else:
            criteria = [
                "The ASCII art should include at least one door.",
                "The ASCII art should include at least two windows.",
                "The ASCII art should include a triangular roof.",
                "The ASCII art should be visually recognizable as a house."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
