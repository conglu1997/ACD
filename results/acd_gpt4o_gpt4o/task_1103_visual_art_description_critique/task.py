class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A surrealist painting featuring a melting clock draped over a tree branch, with a distorted landscape in the background. The colors are muted, with shades of blue and grey dominating the scene.", "theme": "surrealism", "style": "painting"},
            "2": {"description": "A modern sculpture made of intertwined metal rods, forming an abstract shape that resembles a human figure in motion. The sculpture is placed in an open space, allowing light and shadow to interact with its form.", "theme": "modern", "style": "sculpture"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        theme = t["theme"]
        style = t["style"]
        instructions = f"""Your task involves two parts:\n\n1. Interpretation and Critique: Interpret and critique the following visual art piece based on its description:\n\nDescription: {description}\n\n2. Generation: Create a description for a hypothetical art piece based on the given theme and style:\n\nTheme: {theme}\nStyle: {style}\n\nYour interpretation and critique should be insightful and address the main elements, emotions, and potential meanings conveyed by the art piece. Your generated description should be creative and adhere to the given theme and style, demonstrating an understanding of visual art concepts.\n\nResponse Format:\nInterpretation and Critique: <Your interpretation and critique>\nGenerated Description: <Your description>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation and critique should address the main elements, emotions, and potential meanings conveyed by the art piece.",
            "The generated description should adhere to the given theme and style.",
            "The generated description should demonstrate creativity and understanding of visual art concepts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
