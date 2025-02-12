class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Generate clean drinking water from saltwater using renewable energy.", "prompt": "Design a machine that can desalinate seawater using solar power and store the clean water efficiently. Ensure that the design considers the scalability of the system for large-scale usage."},
            "2": {"problem": "Provide electricity to a remote village without access to the grid.", "prompt": "Design a system that generates electricity using wind and solar power. The design should include energy storage solutions to ensure a consistent supply of electricity, and consider the environmental impact of the system."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and explain a machine or system to solve the following problem: '{t["problem"]}'. Your design should be detailed, logically sound, and practically feasible. Include a description of the components, how they work together, and the principles behind the system. Ensure your explanation is clear and covers all essential parts and their functions. Your design should also address any scalability and environmental impact considerations. Submit your response in the following format:\n\nDesign:\n[Your detailed design here]\n\nExplanation:\n[Your step-by-step explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The design should be detailed and logically sound.", "The explanation should be clear and cover all essential parts and their functions.", "The design should be practically feasible.", "The design should address scalability and environmental impact considerations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
