class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "The use of artificial intelligence in military applications"},
            "2": {"topic": "The legalization of recreational drugs"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a debate on the following controversial topic:

{t['topic']}

Present well-developed arguments both for and against the topic. Ensure that the arguments are clear, logical, and persuasive. Provide a conclusion that fairly summarizes both sides of the debate. The debate should be structured as follows:

1. Introduction: Briefly introduce the topic.
2. Argument For: Present substantial arguments in favor of the topic.
3. Argument Against: Present substantial arguments against the topic.
4. Conclusion: Summarize both sides and provide a balanced conclusion.

Your response should be coherent, well-structured, and demonstrate an understanding of the complexities of the topic. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an introduction, substantial arguments for and against the topic, and a conclusion.",
            "The arguments should be clear, logical, and persuasive.",
            "The conclusion should fairly summarize both sides of the debate.",
            "The response should be coherent and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
