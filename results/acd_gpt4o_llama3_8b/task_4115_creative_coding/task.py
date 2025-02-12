class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "output_type": "art",
                "criteria": "Generate a piece of procedural art that consists of a grid of colorful circles with varying sizes and colors. The circles should be arranged in a visually appealing pattern."
            },
            "2": {
                "output_type": "music",
                "criteria": "Generate a short piece of music using a sine wave oscillator. The music should have a duration of 30 seconds and include at least three different frequencies."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write code to generate the following creative output based on the criteria:

Output Type: {t['output_type']}

Criteria: {t['criteria']}

Ensure the code is written in Python and uses appropriate libraries for the task (e.g., matplotlib for art, numpy and sounddevice for music). Submit your code as a plain text string in the following format:

Code: <Your code here>

Ensure the code is well-commented and explain how it meets the criteria."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The code should be syntactically correct and runnable.",
            "The code should generate an output that meets the given criteria.",
            "The code should be written in Python and use appropriate libraries for the task.",
            "The output should be creative and visually or aurally appealing.",
            "The code should be well-commented and explain how it meets the criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
