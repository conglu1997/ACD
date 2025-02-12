class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_piece": "A swirling mix of vibrant colors, predominantly blue and green, with hints of yellow and red. The patterns are chaotic yet harmonious, resembling waves in a turbulent sea."},
            "2": {"art_piece": "A geometric composition with sharp angles and contrasting colors. Dominant shapes include triangles and rectangles in shades of black, white, and red. The overall feel is one of tension and balance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        art_piece = t["art_piece"]
        instructions = f"""Your task is to interpret the following abstract art piece and create an imaginative narrative based on it.\n\nArt Piece Description: {art_piece}\n\nYour narrative should include:\n1. A setting that matches the mood and elements of the art piece.\n2. At least one character who interacts with the setting.\n3. A plot that unfolds in this setting.\n\nEnsure that your narrative is between 300 and 500 words long, vividly describes the setting, and creatively incorporates elements of the art piece. Provide your response in plain text format.\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative includes a setting that matches the mood and elements of the art piece.",
            "The narrative includes at least one character who interacts with the setting.",
            "The narrative has a plot that unfolds in the setting.",
            "The response is between 300 and 500 words long.",
            "The narrative vividly describes the setting and creatively incorporates elements of the art piece."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
