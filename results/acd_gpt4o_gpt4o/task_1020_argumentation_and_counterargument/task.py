class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Should social media platforms be regulated by the government? Provide a thorough argument and counterargument."},
            "2": {"topic": "Is climate change the most pressing global issue today? Provide a thorough argument and counterargument."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to construct a well-reasoned argument on the following topic:

Topic: {t['topic']}

Provide a detailed argument supporting your position, ensuring it is at least 150 words long. After that, generate a coherent counterargument that addresses the points made in your initial argument, which should also be at least 150 words long. Your response should be structured as follows:

Argument: [Your argument]
Counterargument: [Your counterargument]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import re
        from src.eval_helper import eval_with_llm_judge

        def extract_argument_and_counterargument(submission: str) -> tuple[str, str]:
            match = re.search(r"Argument:\s*(.*?)\s*Counterargument:\s*(.*)", submission, re.DOTALL)
            if match:
                return match.group(1).strip(), match.group(2).strip()
            return "", ""

        instructions = TaskFamily.get_instructions(t)
        argument, counterargument = extract_argument_and_counterargument(submission)

        criteria = [
            "The argument should be well-reasoned, coherent, and at least 150 words long.",
            "The counterargument should directly address the points made in the initial argument and be at least 150 words long.",
            "Both the argument and counterargument should be logically sound and demonstrate critical thinking."
        ]

        # Evaluate the argument and counterargument with LLM judge
        argument_correct = eval_with_llm_judge(instructions, argument, criteria)
        counterargument_correct = eval_with_llm_judge(instructions, counterargument, criteria)

        return 1.0 if argument_correct and counterargument_correct else 0.0
