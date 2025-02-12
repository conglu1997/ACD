class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"fields": ["medicine", "computer science"], "problem": "Design a wearable device to monitor and analyze a patient's vital signs in real-time."},
            "2": {"fields": ["art", "physics"], "problem": "Create a sculpture that visually represents the concept of gravitational waves."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        fields = t["fields"]
        problem = t["problem"]
        return f"""Combine knowledge from the fields of {fields[0]} and {fields[1]} to address the following problem: '{problem}'. Provide a detailed solution or description that demonstrates a clear understanding of both fields and how they integrate to solve the problem. Your response should be comprehensive, logically structured, and feasible.

Submit your response in the following format:
- Introduction: [Brief introduction to the problem and the fields involved]
- Solution/Description: [Detailed solution or description of the work]
- Integration: [Explanation of how knowledge from both fields was integrated]
- Feasibility: [Discussion of the feasibility of the solution or work]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission must provide a clear and logical introduction to the problem and fields involved.",
            "The solution or description must be detailed and demonstrate a thorough understanding of both fields.",
            "The integration of knowledge from both fields must be clearly explained.",
            "The feasibility of the solution or work must be discussed.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
