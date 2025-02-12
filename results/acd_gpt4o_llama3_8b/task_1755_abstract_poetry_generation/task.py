class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Time and Memory",
                "constraints": "The poem should be at least 8 lines long and should not explicitly mention 'time' or 'memory'."
            },
            "2": {
                "theme": "Dreams and Reality",
                "constraints": "The poem should be at least 8 lines long and should not explicitly mention 'dreams' or 'reality'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an abstract poem based on the given theme and constraints.

Theme: {t['theme']}

Constraints: {t['constraints']}

Ensure that the poem is creative, evocative, and adheres to the given constraints. Submit your response as a plain text string in the format: 'Poem: [Your poem]'. Use metaphor, imagery, and abstract language to convey the theme without explicitly mentioning the forbidden words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The poem must adhere to the given theme.",
            "The poem must follow the constraints provided.",
            "The poem should be creative and evocative.",
            "The poem should use metaphor, imagery, and abstract language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
