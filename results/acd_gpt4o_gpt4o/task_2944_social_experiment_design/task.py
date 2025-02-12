class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "People are more likely to help others when they are in a good mood.", "scenario": "A person drops their books in a busy hallway."},
            "2": {"hypothesis": "Social media usage decreases face-to-face interactions.", "scenario": "A group of friends at a cafe, some using phones and some not."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a social experiment to test the given hypothesis and analyze the ethical considerations involved.

Hypothesis: {t['hypothesis']}

Scenario: {t['scenario']}

Provide your experimental design in the following format:

1. Experimental Design: [Describe your experiment, including independent and dependent variables, controls, and methodology. Specify how you will measure outcomes.]
2. Ethical Considerations: [Discuss the ethical implications of your experiment, including informed consent, potential harm, and how you would address them.]

Ensure that your response is clear and comprehensive.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The experimental design should be logical and coherent.", "The ethical considerations should be well-addressed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
