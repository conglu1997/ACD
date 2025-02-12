class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature", "form": "sonnet", "rhyme_scheme": "ABABCDCDEFEFGG"},
            "2": {"theme": "love", "form": "haiku", "rhyme_scheme": ""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        form = t["form"]
        rhyme_scheme = t.get("rhyme_scheme", "")
        instructions = f"""Your task is to generate a poem based on the given theme and form. Ensure that your poem adheres to the specified structure and rhyme scheme (if provided). The poem should evoke the emotions and imagery associated with the theme.

Theme: {theme}
Form: {form}
Rhyme Scheme: {rhyme_scheme if rhyme_scheme else 'N/A'}

Provide your poem in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the specified form.",
            "The poem should follow the given rhyme scheme (if applicable).",
            "The poem should evoke the emotions and imagery associated with the theme.",
            "The poem should be coherent and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
