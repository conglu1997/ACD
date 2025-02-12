class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "The beauty of a sunset", "constraints": "Use vivid imagery and at least one metaphor."},
            "2": {"poem": "The sky so vast, a canvas blue,\nWith stars that twinkle, a wondrous view.\nThe moonlight dances on the sea,\nA night so calm, where dreams run free.", "criteria": ["Use of imagery", "Coherence", "Emotional impact"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            return f"""Your task is to generate a poem based on the following theme and constraints:

Theme: {t['theme']}

Constraints:
{t['constraints']}

Provide your poem in plain text format."""
        elif "poem" in t:
            return f"""Your task is to critique the following poem based on the given criteria:

Poem:
{t['poem']}

Criteria: {', '.join(t['criteria'])}

Provide your critique in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theme" in t:
            criteria = [
                "The poem should use vivid imagery.",
                "The poem should include at least one metaphor.",
                "The poem should be creative and coherent."
            ]
        else:
            criteria = [
                "The critique should address the use of imagery.",
                "The critique should address the coherence of the poem.",
                "The critique should assess the emotional impact of the poem."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
