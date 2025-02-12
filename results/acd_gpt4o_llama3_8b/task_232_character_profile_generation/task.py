class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "name": "Elara",
                "age": "28",
                "occupation": "Space Explorer",
                "setting": "A futuristic world where space travel is common"
            },
            "2": {
                "name": "Kai",
                "age": "35",
                "occupation": "Detective",
                "setting": "A bustling modern city with a dark underbelly"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed character profile for the character with the following criteria:

Name: {t['name']}
Age: {t['age']}
Occupation: {t['occupation']}
Setting: {t['setting']}

Your profile should include the following sections:
1. Physical Appearance: Describe the character's physical traits.
2. Personality: Outline the character's key personality traits.
3. Background: Provide a brief background or history of the character.
4. Motivations: Explain the character's main motivations and goals within their setting.

Ensure each section is well-developed and coherent. The entire profile should be engaging and suitable for use in a fictional narrative. Submit your profile as a plain text string in the following format:

Physical Appearance: [Your description]
Personality: [Your description]
Background: [Your description]
Motivations: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The profile should include well-developed sections for Physical Appearance, Personality, Background, and Motivations.",
            "The profile should be coherent and engaging.",
            "Each section should be relevant to the character's given criteria."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
