class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "Analyze Artwork",
                "artwork_description": "A painting by Vincent van Gogh depicting a starry night over a quiet village with swirling blue and yellow skies."
            },
            "2": {
                "title": "Generate Art Description",
                "theme": "Surrealist Dreamscape",
                "constraints": "Include elements like melting clocks, floating islands, and an ethereal color palette."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['title'] == "Analyze Artwork":
            instructions = f"""Your task is to analyze the given artwork based on its description.

Artwork Description: {t['artwork_description']}

Your analysis should include:
1. The artist's potential intent or message behind the artwork.
2. A detailed description of the visual elements and their significance.
3. The historical and cultural context of the artwork.
4. Any notable techniques or styles used by the artist.

Provide your response in plain text format, structured in paragraphs."""
        elif t['title'] == "Generate Art Description":
            instructions = f"""Your task is to generate a creative description of an artwork based on the provided theme and constraints.

Theme: {t['theme']}
Constraints: {t['constraints']}

Your description should be vivid and imaginative, adhering to the given constraints. Describe the visual elements in detail and create a compelling narrative around the artwork. Provide your response in plain text format, structured in paragraphs."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['title'] == "Analyze Artwork":
            criteria = [
                "The analysis should provide a plausible interpretation of the artist's intent or message.",
                "The analysis should include a detailed description of the visual elements and their significance.",
                "The analysis should mention the historical and cultural context of the artwork.",
                "The analysis should note any notable techniques or styles used by the artist."
            ]
        elif t['title'] == "Generate Art Description":
            criteria = [
                "The description should be vivid and imaginative.",
                "The description should adhere to the given theme and constraints.",
                "The description should include detailed visual elements.",
                "The description should create a compelling narrative around the artwork."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
