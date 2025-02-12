class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"work": "Pride and Prejudice", "author": "Jane Austen", "parody_length": 300},
            "2": {"work": "Moby Dick", "author": "Herman Melville", "parody_length": 300}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        work = t["work"]
        author = t["author"]
        parody_length = t["parody_length"]
        instructions = f"""Your task is to create a parody of the following well-known literary work:

Title: {work}
Author: {author}

Your parody should be humorous or satirical, while maintaining the original style of the work. The length of the parody should be approximately {parody_length} words. Ensure that your parody captures the essence of the original work but introduces elements of humor or satire.

Provide your response in the following format:

Parody: [Your parody text]

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The parody should be humorous or satirical.",
            "The parody should maintain the original style of the work.",
            "The parody should capture the essence of the original work."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
