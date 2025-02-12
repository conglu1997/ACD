class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Design a new type of public park that maximizes green space while also providing recreational areas and facilities for community events.",
                "constraints": [
                    "The park must fit within a 5-acre area.",
                    "At least 60% of the park must be green space.",
                    "There must be at least one playground, one sports field, and one community event area.",
                    "All facilities must be accessible to people with disabilities."
                ]
            },
            "2": {
                "problem": "Create a new type of classroom layout that enhances student engagement and collaboration.",
                "constraints": [
                    "The classroom must accommodate 30 students.",
                    "There must be space for both individual and group work.",
                    "The layout must include a central area for the teacher to give instructions.",
                    "All students must have a clear view of the central area."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints_str = '\n'.join(t['constraints'])
        return f"""Generate a creative solution to the following problem while adhering to the given constraints. Ensure that your solution is detailed and addresses all aspects of the problem. Here is the problem:

{t['problem']}

Here are the constraints:
{constraints_str}

Submit your solution in the following format:

Problem: [Your detailed solution]

Ensure your response is coherent and logically structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution must address the problem stated.",
            "The solution must adhere to all given constraints.",
            "The response should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
