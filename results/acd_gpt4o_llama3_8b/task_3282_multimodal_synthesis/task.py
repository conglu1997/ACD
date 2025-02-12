class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "Design a community garden", "image_description": "An image of an empty plot of land with a few trees around the perimeter, a clear sky, and a small bench."},
            "2": {"text": "Organize an art exhibit", "image_description": "An image of a large, empty hall with white walls, good lighting, and a high ceiling."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        text = t["text"]
        image_description = t["image_description"]
        return f"""Combine the following textual prompt and visual scene description to address the task:

Textual Prompt: '{text}'
Visual Scene Description: '{image_description}'

Provide a detailed solution or description that integrates both the textual and visual information. Use descriptive language to paint a clear picture of your solution. Your response should be comprehensive, logically structured, and demonstrate a clear understanding of how the visual scene complements the textual task. Pay special attention to the feasibility and creativity of your solution.

Submit your response in the following format:
- Introduction: [Brief introduction to the problem and the visual scene]
- Solution/Description: [Detailed solution or description of the work]
- Integration: [Explanation of how the visual scene was integrated with the textual prompt]
- Feasibility: [Discussion of the feasibility of the solution or work]
- Creativity: [Explanation of any creative aspects of your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission must provide a clear and logical introduction to the problem and the visual scene.",
            "The solution or description must be detailed and demonstrate a thorough understanding of both the textual and visual information.",
            "The use of descriptive language to paint a clear picture must be evident.",
            "The integration of the visual scene with the textual prompt must be clearly explained.",
            "The feasibility of the solution or work must be discussed.",
            "The submission must highlight any creative aspects of the solution.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
