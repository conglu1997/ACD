class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The benefits of renewable energy sources",
                "argument": "Renewable energy sources are a waste of investment because they are not as reliable as fossil fuels."
            },
            "2": {
                "topic": "The importance of a balanced diet",
                "argument": "A balanced diet is overrated. People should just eat what they like and enjoy their food without worrying about balance."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Task 1: Generate a persuasive argument on the following topic: {t['topic']}.

Task 2: Critique the provided argument for logical consistency and effectiveness.

Provided Argument: {t['argument']}

Submit your responses in the following format:

1. Persuasive Argument:
[Your persuasive argument here]

2. Critique:
[Your critique here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The persuasive argument should be coherent, logically structured, and effectively support the given topic.",
            "The critique should accurately identify logical inconsistencies or weaknesses in the provided argument and suggest improvements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
