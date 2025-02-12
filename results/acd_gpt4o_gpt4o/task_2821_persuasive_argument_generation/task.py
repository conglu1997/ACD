class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "The use of animal testing in medical research should be banned.", "position": "against", "context": "Many medical breakthroughs have been achieved through animal testing, but it raises ethical concerns about the treatment of animals."},
            "2": {"topic": "Social media platforms should ban political advertisements.", "position": "in favor", "context": "Political ads on social media can spread misinformation and affect the outcome of elections. However, they are also a source of revenue for these platforms."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to generate a persuasive argument to support the given position on a controversial topic. Here are the details:

Topic: {0}
Position: {1}
Context: {2}

Ensure that your argument is:
1. Logically structured
2. Rhetorically effective
3. Addresses potential counterarguments
4. Supported by facts or reasoning

Provide your response in plain text format as follows:

Argument: [Your argument here]
""".format(t["topic"], t["position"], t["context"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be logically structured.",
            "The argument should be rhetorically effective.",
            "The argument should address potential counterarguments.",
            "The argument should be supported by facts or reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
