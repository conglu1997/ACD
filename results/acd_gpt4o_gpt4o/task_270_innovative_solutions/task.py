class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Design a sustainable urban farming solution that can be implemented in a densely populated city."},
            "2": {"problem": "Develop an innovative method to reduce plastic waste in the oceans."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to design an innovative solution to the following real-world problem:

Problem: {problem}

Your solution should be detailed and feasible, incorporating elements from various disciplines (e.g., engineering, environmental science, urban planning). Start your solution with a brief summary (1-2 sentences) outlining the main idea. Provide your solution in plain text format, ensuring that it is clear, well-structured, and includes all necessary details to understand and implement the solution."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should include a brief summary at the beginning.",
            "The solution should be innovative and feasible.",
            "The solution should incorporate elements from various disciplines.",
            "The solution should be detailed and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
