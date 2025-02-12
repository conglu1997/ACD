class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "start": "The main gate of the university",
                "end": "The library",
                "details": "The main gate is located at the east end of the campus. The library is a three-story building with a clock tower on the north side of the campus. There are several key landmarks along the route, including the central fountain, the science building, and the student union."
            },
            "2": {
                "start": "The entrance of the park",
                "end": "The central fountain",
                "details": "The entrance of the park is located at the south end, marked by a large archway. The central fountain is located in the middle of the park, surrounded by flower beds and benches. Key landmarks along the route include the playground, the rose garden, and the pond."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate detailed directions for navigating from the following point to the destination point. Ensure the directions are clear, logical, and use recognizable landmarks or features as provided in the details.

Start: {t['start']}
End: {t['end']}
Details: {t['details']}

Submit your response as a plain text string in the following format:
Step 1: [Your direction]
Step 2: [Your direction]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The directions should be clear and logically structured.",
            "The directions should correctly lead from the start point to the end point.",
            "The directions should use recognizable landmarks or features as provided in the details."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
