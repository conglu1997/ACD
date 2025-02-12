class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Consider the philosophical question: 'If a tree falls in a forest and no one is around to hear it, does it make a sound?' Provide a reasoned argument that either supports or refutes the idea that the tree makes a sound."},
            "2": {"scenario": "Discuss the philosophical implications of the 'Trolley Problem' where you must decide whether to pull a lever to divert a runaway trolley onto a track where it will kill one person instead of five. Provide a reasoned argument for your decision and discuss any moral principles involved."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following philosophical scenario and generate a reasoned argument based on it. Ensure that your argument is coherent, logically sound, and well-structured. Here is the scenario:\n\n{t['scenario']}\n\nSubmit your argument in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The argument should be coherent and logically sound.", "The argument should be well-structured and articulate.", "The argument should directly address the philosophical scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
