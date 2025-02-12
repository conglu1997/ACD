class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"form": "sonnet", "theme": "love", "constraint": "Include the phrase 'eternal flame'.", "word_count": "14 lines"},
            "2": {"form": "haiku", "theme": "nature", "constraint": "Mention a specific animal."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        form = t["form"]
        theme = t["theme"]
        constraint = t["constraint"]
        word_count = t.get("word_count", "")
        if form == "sonnet":
            structure = "A sonnet is a 14-line poem with a specific rhyme scheme (typically ABABCDCDEFEFGG) and a metrical pattern (usually iambic pentameter)."
        elif form == "haiku":
            structure = "A haiku is a 3-line poem with a syllable pattern of 5-7-5."
        else:
            structure = ""
        return f"""Compose a poem based on the following requirements:

Form: {form}
Theme: {theme}
Constraint: {constraint}
{structure}
{word_count}

Ensure that your poem adheres to the specified form's structure and rules. Your poem should be creative, engaging, and clearly incorporate the given theme and constraint. Submit your poem as a plain text string in the following format:

[Your Poem]

Example Format:
For a sonnet:
Line 1: [text]
Line 2: [text]
...
Line 14: [text]
For a haiku:
Line 1: [text]
Line 2: [text]
Line 3: [text]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the specified form's structure and rules.", 
            "The poem should creatively and clearly incorporate the given theme.", 
            "The poem should meet the additional constraint provided.",
            "The poem should be engaging and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
