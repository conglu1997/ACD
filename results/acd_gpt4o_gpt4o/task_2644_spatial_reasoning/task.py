class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "assemble", "parts": ["base", "pole", "lamp head", "light bulb", "screw"], "instructions": "Assemble a simple lamp using the given parts. Describe the process step by step."},
            "2": {"task": "navigate", "maze": ["start at the entrance", "go left", "go straight", "turn right", "go straight", "turn left", "exit"], "instructions": "Navigate through a simple maze based on the given directions. Describe your path step by step."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "assemble":
            parts = ", ".join(t["parts"])
            return f"Your task is to assemble a simple object using the following parts: {parts}. Describe the process step by step. Ensure your description is clear, logical, and follows the correct order of assembly. Provide your response in plain text format, with each step numbered."
        elif t["task"] == "navigate":
            return f"Your task is to navigate through a simple maze based on the following directions: {', '.join(t['maze'])}. Describe your path step by step. Ensure your description is clear, logical, and correctly follows the given directions. Provide your response in plain text format, with each step numbered."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "assemble":
            criteria = [
                "The description should clearly explain the assembly process step by step.",
                "The description should include all given parts in the correct order of assembly."]
        elif t["task"] == "navigate":
            criteria = [
                "The description should clearly explain the navigation through the maze step by step.",
                "The description should correctly follow the given directions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
