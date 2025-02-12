class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "You see a runaway trolley moving towards five people tied up on the tracks. You are standing next to a lever that can divert the trolley onto another track, where there is one person tied up. Do you pull the lever to save the five people at the expense of the one person?"},
            "2": {"dilemma": "A research lab is working on a potential cure for a deadly disease. They have limited resources and can either continue their current project, which has a 50% chance of success and would save 100 lives, or switch to a new project with a 90% chance of success but would only save 50 lives. Should they switch projects?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Evaluate the following ethical dilemma and provide a reasoned decision. Consider various ethical principles such as utilitarianism, deontology, and virtue ethics, and explain your reasoning clearly.

Dilemma: {t['dilemma']}

Your response should include:
1. A clear decision on what action to take.
2. An explanation of multiple ethical principles considered.
3. A detailed reasoning for your decision, demonstrating a deep understanding of ethical concepts.

Provide your response in plain text format, structured as follows:

Decision: [Your decision]
Ethical Principles: [Ethical principles considered]
Reasoning: [Detailed reasoning]

Ensure that your response is comprehensive, logically sound, and considers multiple ethical perspectives."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The decision should be clear and directly address the dilemma.",
            "The ethical principles considered should be relevant and appropriately applied, demonstrating an understanding of multiple perspectives.",
            "The reasoning should be detailed and logical, demonstrating a deep understanding of ethical concepts and multiple perspectives."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
