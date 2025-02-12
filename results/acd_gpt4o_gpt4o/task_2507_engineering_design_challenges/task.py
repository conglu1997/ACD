class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Design a bridge to span a 500-meter-wide river, capable of supporting both vehicular and pedestrian traffic.", "constraints": "Must withstand high winds, support at least 10,000 vehicles per day, and include pedestrian walkways."},
            "2": {"problem": "Develop a water filtration system for a small rural community with limited access to clean water.", "constraints": "System must be low-cost, easy to maintain, and capable of filtering at least 500 liters of water per day."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        constraints = t["constraints"]
        instructions = f"""Your task is to propose a detailed solution to the following engineering problem:

Problem: {problem}

Constraints: {constraints}

Your solution should include the following components:
1. Conceptual design: Describe the overall design and how it addresses the problem.
2. Technical details: Provide technical specifications and considerations for your design.
3. Materials and resources: List the materials and resources needed, and explain why they were chosen.
4. Feasibility: Discuss the feasibility of your design, considering the given constraints.

Ensure that your proposal is clear, detailed, and technically sound. Provide your response in plain text format with sections for each component mentioned above."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conceptual design should clearly address the problem.",
            "The technical details should be accurate and logically sound.",
            "The materials and resources should be appropriate and justified.",
            "The feasibility discussion should consider the constraints and provide a realistic assessment."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
