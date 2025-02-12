class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_piece": "A swirling mass of colors that blend from dark blues and purples to bright oranges and yellows, with jagged black lines cutting through the chaos. Small, intermittent dots of bright green are scattered throughout.", "questions": ["What emotions does this piece evoke?", "What might the artist be trying to convey?", "How do the colors and shapes contribute to the overall impact of the piece?"]},
            "2": {"prompts": ["Theme: Conflict between nature and technology", "Emotions: Melancholy and hope", "Elements: Use of geometric shapes and organic forms"], "expected_result": "A vivid and evocative description of an abstract art piece that captures the given theme, emotions, and elements."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "art_piece" in t:
            return f"""Interpret the following abstract art piece and answer the questions below:

Art Piece Description: {t['art_piece']}

Questions: {', '.join(t['questions'])}

Provide your answers in plain text format."""
        else:
            return f"""Create a description of an abstract art piece based on the following prompts:

Prompts: {', '.join(t['prompts'])}

Your description should be vivid and evocative, capturing the essence of the given theme, emotions, and elements. Provide your description in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "art_piece" in t:
            criteria = ["The interpretation should reflect a deep understanding of the art piece and address all the questions accurately."]
        else:
            criteria = ["The description should be vivid, evocative, and accurately capture the given theme, emotions, and elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
