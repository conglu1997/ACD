class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A repeating pattern of equilateral triangles forming a hexagon.", "constraints": "Each side of the triangles should be 5 units long."},
            "2": {"description": "A pattern of concentric circles with alternating colors.", "constraints": "The radius of the smallest circle should be 2 units, and each subsequent circle should have an additional radius of 2 units."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        constraints = t["constraints"]
        return f"""Generate a detailed description of how to create the following geometric pattern, adhering to the given constraints.\nPattern: {description}\nConstraints: {constraints}\nEnsure your description is clear and includes step-by-step instructions for drawing the pattern. The steps should be detailed enough for someone to follow and recreate the pattern accurately. Pay special attention to the constraints provided to ensure accuracy. Submit your response as a plain text string. For example:\n1. Draw a line of 5 units.\n2. Draw another line of 5 units at a 60-degree angle to the first line.\n3. Continue drawing lines of 5 units to form an equilateral triangle.\n4. Repeat the process to form a hexagon made up of equilateral triangles.\n...\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately follow the geometric constraints.", "The steps should be clear and detailed.", "The final pattern should match the described pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
