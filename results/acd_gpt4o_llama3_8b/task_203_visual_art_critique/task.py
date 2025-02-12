class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A surreal painting featuring a melting clock draped over a tree branch, with a distorted landscape in the background."},
            "2": {"description": "A realistic portrait of an elderly woman sitting by a window, with soft sunlight illuminating her face and a serene expression."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given description:

Artwork Description: {t['description']}

Analyze and critique the described artwork. Your response should include:
1. An analysis of the visual elements and composition.
2. An interpretation of the possible meaning or message of the artwork.
3. A critique of the overall impact and effectiveness of the artwork.

Ensure that your critique is well-reasoned, coherent, and demonstrates a deep understanding of visual art principles. Submit your response as a plain text string with clearly labeled sections for 'Analysis', 'Interpretation', and 'Critique'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include an analysis of the visual elements and composition.", "The response should include an interpretation of the possible meaning or message of the artwork.", "The response should include a critique of the overall impact and effectiveness of the artwork.", "The critique should be well-reasoned, coherent, and demonstrate a deep understanding of visual art principles."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
