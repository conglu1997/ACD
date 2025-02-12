class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"specification": "Design a simple pulley system to lift a 50 kg weight with minimal effort."},
            "2": {"specification": "Design a basic wind-powered device to generate electricity for a small household."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        specification = t["specification"]
        return f"""Design a mechanical system based on the following specification:

Specification: {specification}

Your design should include a detailed description of the components, how they work together, and the principles behind the system. Provide a step-by-step explanation of how the system operates and achieves the specified goal. Ensure that your description covers all essential parts and their functions, and that your explanation is clear, logically sound, and practically feasible. Emphasize the practicality of your design in real-world applications. Submit your response in the following format:

Design:
[Your detailed design here]

Explanation:
[Your step-by-step explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The design should meet the given specification.", "The explanation should be clear and logically sound.", "The principles behind the system should be accurately described.", "The practical feasibility of the design should be considered and emphasized."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
