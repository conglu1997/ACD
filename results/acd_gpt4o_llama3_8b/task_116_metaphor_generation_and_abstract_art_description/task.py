class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "ephemeral beauty"},
            "2": {"art": "@@@@@@@@@@@@\n@          @\n@ @@@@@@@@ @\n@ @@    @@ @\n@ @@ @@ @@ @\n@ @@    @@ @\n@ @@@@@@@@ @\n@          @\n@@@@@@@@@@@@\n"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "concept" in t:
            return f"""Generate a metaphor for the following abstract concept:

{t["concept"]}

Ensure that the metaphor is original, creative, and captures the essence of the concept. Submit your response as a plain text string, and ensure it is concise (one or two sentences)."""
        else:
            return f"""Describe the following piece of abstract ASCII art:

{t["art"]}

Provide a detailed description of what it represents. Your description should be clear, accurate, and provide enough detail to convey the essence of the image. Consider the shapes, patterns, and any possible interpretations of the abstract art. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "concept" in t:
            criteria = ["The metaphor should be original and creative.", "The metaphor should capture the essence of the concept."]
        else:
            criteria = ["The description should be clear and accurate.", "The description should convey the essence of the image.", "The description should consider shapes, patterns, and possible interpretations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
