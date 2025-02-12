class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "How many distinct ways can 5 people be seated around a circular table? Remember that rotations of the same arrangement are considered identical."
            },
            "2": {
                "problem": "Consider a graph with 6 vertices where each vertex is connected to every other vertex. How many edges does this graph have? Provide a general formula for any complete graph with n vertices."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following discrete mathematics problem:

{t['problem']}

Provide a detailed explanation of your solution, including any relevant formulas or theorems used. Clearly state the final answer. Submit your solution as a plain text string in the following format:

Answer: [your final answer]
Explanation: [detailed explanation of your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should include a detailed explanation of the steps taken.",
            "The solution should use appropriate formulas or theorems relevant to the problem.",
            "The final answer should be correct and clearly stated.",
            "The explanation should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
