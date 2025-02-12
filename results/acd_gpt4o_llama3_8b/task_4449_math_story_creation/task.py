class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"math_element": "solve x + 3 = 7"},
            "2": {"math_element": "a triangle with sides of lengths 3, 4, and 5"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given mathematical element:

Mathematical Element: {t['math_element']}

Generate a creative story that incorporates the given mathematical element. The story should be engaging, coherent, and seamlessly integrate the mathematical concept or problem into the narrative. Ensure that the mathematical element is accurately represented and plays a significant role in the story.

Submit your response as a plain text string in the following format:
Story: [Your story]

Example Response:
Story: In a small village, there lived a wise old man who always carried a mysterious box. One day, he challenged the villagers to solve the riddle of the box. 'Inside this box,' he said, 'lies the answer to x + 3 = 7.' The villagers pondered for days until a young girl named Lily realized that x must be 4. When she opened the box, she found a map leading to a hidden treasure."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be engaging and coherent.",
            "The mathematical element should be accurately represented.",
            "The mathematical element should play a significant role in the story.",
            "The story should demonstrate creative integration of the mathematical concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
