class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Should governments implement universal basic income (UBI)?", "position": "for"},
            "2": {"topic": "Is it ethical to use animals for scientific research?", "position": "against"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write an argumentative essay on the given topic. You should take the specified position on the topic and support your argument with evidence and reasoning.\n\nTopic: {t['topic']}\nPosition: {t['position']}\n\nYour essay should include:\n1. An introduction that presents the topic and states your position clearly.\n2. Body paragraphs that support your position with evidence, examples, and logical reasoning.\n3. Counterarguments that present and refute opposing viewpoints.\n4. A conclusion that summarizes your argument and reinforces your position.\n\nThe essay should be approximately 500 words in length.\n\nEnsure that your essay is coherent, logically structured, and persuasive. Format your response in plain text without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an introduction that presents the topic and states the position clearly.",
            "The body paragraphs should support the position with evidence, examples, and logical reasoning.",
            "The counterarguments should present and refute opposing viewpoints.",
            "The conclusion should summarize the argument and reinforce the position.",
            "The response should be coherent, logically structured, and persuasive.",
            "The essay should be approximately 500 words in length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
