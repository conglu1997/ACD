class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"answers": ["time", "shadow", "echo"], "example_riddle": "I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, and I can drown. What am I?", "example_answer": "fire"},
            "2": {"answers": ["mirror", "key", "fire"], "example_riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "example_answer": "echo"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        answers = ", ".join(t["answers"])
        example_riddle = t["example_riddle"]
        example_answer = t["example_answer"]
        instructions = f"""Your task is to perform two activities related to riddles.

1. Generate creative and challenging riddles for the following answers:
Answers: {answers}

Example Riddle: {example_riddle}

Please provide your riddles in the following format:
- Answer: [Given answer]
- Riddle: [Your riddle]

2. Solve the following riddle and provide the answer:
Example Riddle: {example_riddle}

Ensure that your generated riddles are creative, clear, and logically lead to the given answers. Provide the answer to the example riddle in plain text format as follows:
- Answer: [Your answer]

Your response should include both the generated riddles and the answer to the example riddle."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated riddles should be creative, clear, and logically lead to the given answers.",
            "The answer to the example riddle should be accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
