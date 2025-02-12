class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "Explain how a rainbow is formed."},
            "2": {"problem": "Design a simple machine that can lift a heavy object (e.g., 100 kg) using basic principles of physics."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "phenomenon" in t:
            return f"Your task is to explain the scientific phenomenon described below:\n\n{t['phenomenon']}\n\nProvide a detailed explanation that includes the relevant scientific principles and processes involved. Ensure your explanation is clear, accurate, and thorough. Structure your response as follows:\n\n1. Introduction: [Brief introduction]\n2. Scientific Principles: [Describe the scientific principles involved]\n3. Process: [Explain the process in detail]\n4. Conclusion: [Summarize your explanation]"
        elif "problem" in t:
            return f"Your task is to solve the practical problem described below using scientific principles:\n\n{t['problem']}\n\nProvide a detailed solution that includes the relevant scientific concepts and a step-by-step explanation of how to implement your solution. Ensure your solution is feasible and well-explained. Structure your response as follows:\n\n1. Problem Restatement: [Restate the problem in your own words]\n2. Scientific Concepts: [Describe the scientific concepts involved]\n3. Solution Steps: [Detail the steps to implement the solution]\n4. Feasibility: [Explain the feasibility of your solution]\n5. Conclusion: [Summarize your solution]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "phenomenon" in t:
            criteria = [
                "The explanation should accurately describe the scientific phenomenon.",
                "The explanation should include relevant scientific principles.",
                "The explanation should be clear and thorough.",
                "The explanation should follow the structured format provided."]
        elif "problem" in t:
            criteria = [
                "The solution should be based on scientific principles.",
                "The solution should be feasible and practical.",
                "The explanation should be detailed and clear.",
                "The solution should follow the structured format provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0