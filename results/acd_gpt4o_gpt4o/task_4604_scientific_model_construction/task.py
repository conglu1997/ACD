class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"principles": "Newton's laws of motion", "phenomenon": "How a rocket launches into space, overcoming Earth's gravity."},
            "2": {"principles": "Photosynthesis", "phenomenon": "How plants convert sunlight into energy, producing oxygen as a byproduct."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to construct a scientific model based on the given principles and use it to explain the following phenomenon:

Principles: {t['principles']}
Phenomenon: {t['phenomenon']}

Your response should include:
1. A clear and concise explanation of the principles involved.
2. The construction of a scientific model that incorporates these principles.
3. A detailed explanation of how the model explains the given phenomenon.

Provide your response in plain text format as follows:

Principles Explanation:
[Explanation of the principles]

Scientific Model:
[Description of the model]

Phenomenon Explanation:
[Explanation of how the model explains the phenomenon]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and concise explanation of the principles involved.",
            "The response should include the construction of a scientific model that incorporates these principles.",
            "The explanation should clearly describe how the model explains the given phenomenon."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
