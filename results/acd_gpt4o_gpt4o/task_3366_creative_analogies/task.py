class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Explain how a library is like a garden."},
            "2": {"prompt": "Explain how a computer is like a human brain."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        instructions = f"""Your task is to generate a creative analogy based on the following prompt:

{prompt}

Provide your response in the following format:

Analogy: [Your creative analogy]
Explanation: [Explain the reasoning behind your analogy and how the two concepts are similar]

Example:
Prompt: Explain how a river is like a journey.
Analogy: A river is like a journey because both have a starting point, a path they follow, and an endpoint.
Explanation: Just as a river begins at a source, flows through various terrains, and eventually reaches the sea, a journey begins with a single step, has many experiences along the way, and culminates in a destination."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a creative analogy.",
            "The explanation should clearly describe the similarities between the two concepts.",
            "The analogy should be meaningful, insightful, and logically sound.",
            "The analogy should show a deep understanding of both concepts involved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
