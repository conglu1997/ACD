class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "The benefits of space exploration."},
            "2": {"argument": "Social media has more negative impacts than positive effects on society."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'topic' in t:
            return f"""Your task is to generate a persuasive argument for the following topic:

Topic: {t['topic']}

Your argument should be well-structured, logically sound, and compelling. Ensure that you provide evidence and reasoning to support your points.

Format your response in plain text as follows:

Argument: [Your argument here]"""
        else:
            return f"""Your task is to provide a counterargument to the following argument:

Argument: {t['argument']}

Your counterargument should address the points raised in the argument, provide counter-evidence, and present a coherent and logical rebuttal.

Format your response in plain text as follows:

Counterargument: [Your counterargument here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument or counterargument should be well-structured and logically sound.",
            "The submission should provide evidence and reasoning to support the points made.",
            "The submission should be persuasive and compelling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
