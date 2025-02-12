class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Machine Learning", "example_questions": ["What is Machine Learning?", "What are the types of Machine Learning?"]},
            "2": {"topic": "Climate Change", "example_questions": ["What is Climate Change?", "What are the causes of Climate Change?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a structured FAQ document based on the following topic: '{t["topic"]}'. The document should include at least 5 questions and answers. Ensure the questions are relevant to the topic and the answers are clear and accurate. Submit your FAQ document as a plain text string in the following format:

Question 1: [Your question]
Answer 1: [Your answer]

Question 2: [Your question]
Answer 2: [Your answer]

..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
