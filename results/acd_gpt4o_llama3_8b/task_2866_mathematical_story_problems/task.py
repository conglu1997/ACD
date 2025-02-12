class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem_type": "basic arithmetic",
                "story_elements": "a farmer, a market, and a certain number of apples"
            },
            "2": {
                "problem_type": "geometry",
                "story_elements": "a painter, a canvas, and the dimensions of shapes"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story that includes a mathematical problem of the type specified below and provide the solution to that problem.

Problem Type:
{t['problem_type']}

Story Elements:
{t['story_elements']}

Your story should be between 100 and 200 words long. Clearly state the mathematical problem within the narrative and ensure your story is coherent and engaging. After the story, provide a step-by-step solution to the mathematical problem.

Example:
Story: Once upon a time, there was a farmer who went to the market with 10 apples. He sold 3 apples and then bought 5 more. How many apples does he have now?
Solution: The farmer had 10 apples, sold 3 (10 - 3 = 7), and bought 5 more (7 + 5 = 12). So, he has 12 apples now.

Submit your response in the following format:

Story: [Your story]
Solution: [Your step-by-step solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should include the specified mathematical problem type.",
            "The story should incorporate the given story elements.",
            "The solution should be correct and clearly explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
