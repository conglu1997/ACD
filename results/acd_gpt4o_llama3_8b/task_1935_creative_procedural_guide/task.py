class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "process": "Building a miniature fairy garden",
                "criteria": [
                    "Use materials that can be found in a household or garden.",
                    "Include at least three different types of plants.",
                    "Incorporate miniature furniture or decorations."]
            },
            "2": {
                "process": "Creating a themed escape room at home",
                "criteria": [
                    "Design a storyline based on a pirate treasure hunt.",
                    "Include at least three different puzzles or challenges.",
                    "Use items commonly found around the house for props and clues."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed, step-by-step guide for the following process: {t['process']}.

Ensure your guide meets the following criteria:
""" + '\n'.join([f"- {criterion}" for criterion in t['criteria']]) + """

Your guide should be clear, logically organized, and include all necessary steps and materials. Submit your guide as a plain text string with the following sections:

1. Introduction: [Brief introduction to the process]
2. Materials: [List of materials needed]
3. Steps: [Detailed, step-by-step instructions for the process]
4. Conclusion: [Any additional tips or final thoughts]

Each section should be detailed and clearly written to ensure the process can be followed accurately. Use bullet points or numbered lists where appropriate to enhance clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The guide includes a brief introduction to the process.",
            "The guide lists all necessary materials.",
            "The guide provides detailed, step-by-step instructions.",
            "The guide includes a conclusion with additional tips or final thoughts.",
            "The guide meets all specified criteria for the process.",
            "The guide is clear, logically organized, and easy to follow."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
