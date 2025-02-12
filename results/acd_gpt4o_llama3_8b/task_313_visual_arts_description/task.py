class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A surreal painting featuring a clock melting over the edge of a table, with a barren, desolate landscape in the background. The clock's numbers are distorted, and there is a lone tree with no leaves on the right side of the painting. The sky is a mix of orange and purple hues, giving a sense of twilight. In the foreground, there is a cracked mirror reflecting a distorted image of the clock.",
                "instructions": "Describe the visual elements of the painting and interpret its possible meaning. Your description should include details about the objects, their arrangement, and the use of color. Additionally, provide an interpretation of what the painting might represent. Submit your response as a plain text string in the following format: \nDescription: [Your description] \nInterpretation: [Your interpretation]"
            },
            "2": {
                "data": "A vibrant abstract painting filled with geometric shapes of various colors. Circles, squares, and triangles are scattered across the canvas, overlapping and intersecting. The background is a gradient of blue and green, with splashes of red and yellow adding contrast. The painting exudes a sense of chaos and energy. In the center of the canvas, there is a large red circle with a smaller blue square inside it, creating a focal point.",
                "instructions": "Describe the visual elements of the painting and interpret its possible meaning. Your description should include details about the objects, their arrangement, and the use of color. Additionally, provide an interpretation of what the painting might represent. Submit your response as a plain text string in the following format: \nDescription: [Your description] \nInterpretation: [Your interpretation]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the visual elements of the painting and interpret its possible meaning. Your description should include details about the objects, their arrangement, and the use of color. Additionally, provide an interpretation of what the painting might represent. Here is the description of the painting:\n\n{t['data']}\n\nSubmit your response as a plain text string in the following format:\nDescription: [Your description] \nInterpretation: [Your interpretation]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately capture the visual elements described.",
            "The interpretation should be coherent and plausible based on the description of the painting."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
