class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the following paradox and explain its nature: 'This statement is false.'"},
            "2": {"prompt": "Generate a new logical paradox and explain why it is paradoxical."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Complete the following task based on the given prompt:\n\n{prompt}\n\nSubmit your response as a plain text string. Your response should be structured as follows:\n\n1. Analysis: [Detailed analysis here]\n2. Paradox: [Generated paradox here]\n3. Explanation: [Explanation of why the paradox is paradoxical here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should demonstrate a clear understanding of the paradox and its inherent contradiction.",
            "The generated paradox should be original and logically contradictory.",
            "The explanation should clearly articulate why the statement is paradoxical.",
            "The response should follow the given format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
