class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "I told my computer I needed a break, and now it won't stop sending me Kit-Kat ads.", "context": "Write a joke about a cat and a vacuum cleaner."},
            "2": {"statement": "Parallel lines have so much in common. It’s a shame they’ll never meet.", "context": "Write a funny story about a day in the life of a penguin."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        statement = t["statement"]
        context = t["context"]
        return f"""This task involves two parts:

1. Humor Detection:
Determine if the following statement is humorous. Respond with 'Humorous' or 'Not Humorous'.

Statement: {statement}

2. Humor Generation:
Generate humorous content based on the given context. Ensure that the content is original, creative, and makes use of the context provided. Avoid using cliches or common jokes.

Context: {context}

Submit your responses in the following format:

Response:
Humor Detection: [Your answer]
Humor Generation: [Your humorous content]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The humor detection should accurately determine if the statement is humorous.",
            "The humorous content should be original, creative, and relevant to the given context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
