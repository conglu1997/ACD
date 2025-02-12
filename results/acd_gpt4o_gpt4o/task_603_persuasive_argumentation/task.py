class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Should schools implement a year-round education system?", "role": "pro"},
            "2": {"topic": "Is social media beneficial for society?", "role": "con"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a persuasive argument on the given topic. Your role is to argue {'in favor of' if t['role'] == 'pro' else 'against'} the topic. Ensure that your argument is logically coherent, rhetorically effective, and persuasive.\n\nTopic: {t['topic']}\n\nYour response should include:\n1. A clear thesis statement.\n2. Supporting points with evidence or reasoning.\n3. A counterargument and your response to it.\n4. A conclusion that reinforces your thesis.\n\nStructure your response as follows:\n- Thesis statement: [Your thesis statement]\n- Supporting points: [Your supporting points with evidence or reasoning]\n- Counterargument: [Address a counterargument and provide your response to it]\n- Conclusion: [Your conclusion that reinforces your thesis]\n\nFormat your response in plain text without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear thesis statement.",
            "The response should provide supporting points with evidence or reasoning.",
            "The response should address a counterargument and provide a response to it.",
            "The response should have a conclusion that reinforces the thesis.",
            "The argument should be logically coherent, rhetorically effective, and persuasive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
