class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "identify",
                "scenario": "A forest fire destroyed many homes in the area."
            },
            "2": {
                "task_type": "generate",
                "cause_or_effect": "Due to heavy rains, the river overflowed."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'identify':
            return f"""Identify the cause or effect in the following scenario and explain your reasoning:

Scenario: {t['scenario']}

Submit your response as a plain text string in the following format:

Cause/Effect: [Your identified cause or effect]
Reasoning: [Your explanation for why this is the cause or effect]

Ensure your reasoning is clear and logically connects the cause or effect to the scenario provided."""
        else:
            return f"""Generate a plausible scenario given the following cause or effect and explain your reasoning:

Cause/Effect: {t['cause_or_effect']}

Submit your response as a plain text string in the following format:

Scenario: [Your generated scenario]
Reasoning: [Your explanation for why this scenario is plausible given the cause or effect]

Ensure your generated scenario is coherent and logically follows from the given cause or effect."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'identify':
            validation_criteria = ["The identified cause or effect should be relevant to the scenario.", "The reasoning should clearly explain why the identified element is the cause or effect.", "The explanation should logically connect the cause or effect to the scenario."]
        else:
            validation_criteria = ["The generated scenario should be plausible given the cause or effect.", "The reasoning should clearly explain why the scenario is plausible.", "The scenario should be coherent and logically follow from the given cause or effect."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
