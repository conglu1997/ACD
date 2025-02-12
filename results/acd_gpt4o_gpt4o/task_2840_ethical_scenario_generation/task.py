class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parameters": "A medical professional in a small, under-resourced clinic must decide between saving a young child with a rare disease or an elderly patient with a common but severe illness during a medical emergency."},
            "2": {"parameters": "A journalist discovers a major scandal involving a charitable organization that helps thousands of people but is involved in unethical practices. They must decide whether to expose the scandal or protect the organization's beneficiaries."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a complex ethical scenario based on the following parameters:

Parameters: {t['parameters']}

Ensure that the scenario involves a moral dilemma and requires nuanced ethical reasoning. Provide a detailed description of the scenario, including the context, the individuals involved, the moral choices presented, and the potential consequences of each choice. Structure your response as follows:

1. Context: Describe the setting and background of the scenario.
2. Individuals Involved: Identify the key individuals or groups involved in the scenario.
3. Moral Choices: Clearly outline the moral choices or dilemmas faced by the individuals.
4. Potential Consequences: Describe the potential consequences of each moral choice.

Be thorough in your description and ensure the scenario is ethically complex and thought-provoking."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The context should be clearly described.", "The individuals involved should be identified.", "The moral choices should be clearly outlined.", "The potential consequences should be described.", "The scenario should be ethically complex and thought-provoking."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
