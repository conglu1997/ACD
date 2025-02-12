class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "Number Theory"
            },
            "2": {
                "topic": "Geometry"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a novel mathematical problem or puzzle in the following topic: {t['topic']}.

Once you have generated the problem, provide a detailed solution to it. Ensure that your problem is original, non-trivial, and solvable. Additionally, include a brief explanation of why your problem is novel and challenging. Your solution should be logically structured and demonstrate a clear understanding of the mathematical principles involved. Submit both the problem and the solution as a plain text string in the following format:

Problem: [Your problem]
Solution: [Your solution]
Explanation: [Why your problem is novel and challenging]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The problem should be novel and non-trivial.",
            "The problem should be solvable based on the provided solution.",
            "The solution should be logically structured and correct.",
            "The explanation should justify both the novelty and challenge of the problem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
