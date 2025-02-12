class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a fictional story about a mission to Mars that must overcome unexpected technical challenges using engineering solutions."},
            "2": {"prompt": "Create a fictional narrative about a future society that uses quantum computing to solve global problems."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "Mars" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Your story should include:
1. A clear description of the mission and its objectives.
2. The unexpected technical challenges faced during the mission.
3. The engineering solutions devised to overcome these challenges.
4. A coherent and engaging narrative that accurately incorporates scientific and engineering principles.

Ensure your story is creative, technically accurate, and coherent. Submit your response as a plain text string in paragraph format."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Your story should include:
1. A clear description of the future society and its characteristics.
2. The role of quantum computing in addressing global problems.
3. Specific examples of problems solved using quantum computing.
4. A coherent and engaging narrative that accurately incorporates scientific and technical concepts.

Ensure your story is creative, technically accurate, and coherent. Submit your response as a plain text string in paragraph format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "Mars" in t["prompt"]:
            criteria = ["The story should include a clear mission description, unexpected technical challenges, and engineering solutions.", "The narrative should be creative, technically accurate, and coherent."]
        else:
            criteria = ["The story should include a clear description of the future society, the role of quantum computing, and specific examples of problems solved.", "The narrative should be creative, technically accurate, and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
