class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "story_outline", "parameters": {"genre": "fantasy", "setting": "a mystical forest", "main_conflict": "a battle against a dark sorcerer"}},
            "2": {"type": "character_profile", "traits": {"name": "Lyria", "role": "warrior", "special_ability": "control over fire", "backstory": "orphaned at a young age, trained by monks"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'story_outline':
            return f"""Your task is to generate a story outline based on the following parameters:

Genre: {t['parameters']['genre']}
Setting: {t['parameters']['setting']}
Main Conflict: {t['parameters']['main_conflict']}

Ensure that your outline includes the main plot points, key characters, and significant events. The outline should be coherent and follow a logical progression. Provide your response in plain text format as a series of bullet points."""
        elif t['type'] == 'character_profile':
            return f"""Your task is to create a character profile based on the following traits:

Name: {t['traits']['name']}
Role: {t['traits']['role']}
Special Ability: {t['traits']['special_ability']}
Backstory: {t['traits']['backstory']}

Ensure that your profile includes a detailed description of the character's appearance, personality, and motivations. The profile should be unique and align with the given traits. Provide your response in plain text format as a descriptive paragraph."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['type'] == 'story_outline':
            criteria.append("The outline should be coherent and follow a logical progression.")
            criteria.append("The outline should include the main plot points, key characters, and significant events.")
        elif t['type'] == 'character_profile':
            criteria.append("The profile should be unique and align with the given traits.")
            criteria.append("The profile should include a detailed description of the character's appearance, personality, and motivations.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
