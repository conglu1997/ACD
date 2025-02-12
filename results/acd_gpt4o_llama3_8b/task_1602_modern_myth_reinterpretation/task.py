class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story": "The story of Icarus", "summary": "Icarus and his father Daedalus attempt to escape from Crete using wings made of feathers and wax. Icarus flies too close to the sun, causing the wax to melt, and he falls into the sea and drowns."},
            "2": {"story": "The tale of Little Red Riding Hood", "summary": "A young girl, Little Red Riding Hood, goes to visit her grandmother. A wolf disguises itself as her grandmother and attempts to eat her."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reinterpret the following classical myth or fairy tale in a modern context. Preserve the core themes and characters while updating the setting and circumstances to fit contemporary times.

Story: {t["story"]}

Summary: {t["summary"]}

Your reinterpretation should include:
1. A modern setting and context.
2. Updated character roles and professions.
3. Contemporary challenges and themes that mirror the original story.

Submit your response as a plain text string in the following format:

Modern Reinterpretation: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The reinterpretation should preserve the core themes and characters.", "The setting and context should be updated to modern times.", "The story should adapt character roles and professions to fit contemporary scenarios.", "The challenges and themes should reflect modern-day issues while mirroring the original story.", "The reinterpretation should be coherent and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
