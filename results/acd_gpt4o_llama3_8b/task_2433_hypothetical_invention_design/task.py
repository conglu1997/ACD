class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem_statement": "Design an invention that can help reduce food waste in households."
            },
            "2": {
                "problem_statement": "Design an invention that can help people with mobility impairments navigate urban environments more easily."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical invention or innovation to solve the following problem: {t['problem_statement']}

Your design should include the following sections:
1. Introduction: Briefly describe the problem and the significance of solving it.
2. Invention Overview: Provide a high-level description of your invention, including its main features and how it works.
3. Technical Details: Explain the technical aspects of your invention, including any relevant diagrams or schematics.
4. Benefits: Describe the benefits of your invention and how it addresses the problem.
5. Potential Challenges: Identify any potential challenges or limitations of your invention and suggest possible solutions.

The description should be clear, well-structured, and comprehensive. Use plain text for your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be clear and well-structured.",
            "The invention should address the given problem effectively.",
            "The technical details should be logically sound and feasible.",
            "The benefits and potential challenges should be clearly articulated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
