class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"project": "Design a small, portable wind turbine that can be used to charge electronic devices in remote areas.", "constraints": "The turbine must be lightweight, have a power output of at least 10W, and be able to operate in wind speeds as low as 5 mph."},
            "2": {"project": "Design a water filtration system for use in disaster-stricken areas.", "constraints": "The system must be able to filter at least 100 liters of water per day, remove 99.9% of bacteria and viruses, and be easy to transport and set up."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a conceptual design for the following engineering project based on the given requirements and constraints:

Project: {t['project']}

Constraints: {t['constraints']}

Your design should include a description of the key components, their functions, and how they work together to meet the project requirements. Ensure that your design is coherent, innovative, and feasible. Submit your response as a plain text string in the following format:

Design Concept: [Your design concept here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design should include a description of the key components.",
            "The design should explain the functions of the components.",
            "The design should detail how the components work together to meet the project requirements.",
            "The design should be coherent, innovative, and feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
