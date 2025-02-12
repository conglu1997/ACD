class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Nature", "constraints": "4 lines, AABB rhyme scheme, include at least one metaphor"},
            "2": {"poem": "The sky is dark, the stars are bright,\nA silver moon casts gentle light.\nThe night is calm, the world at rest,\nIn this stillness, we are blessed."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            return f"""Your task is to generate a poem based on the given theme and constraints.

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure your poem adheres to the specified theme and follows the given constraints. Provide your response in plain text format.

Example Response:
Poem: The sun is a golden coin in the sky,\nBirds sing sweet songs as they fly by.\nTrees whisper secrets in the breeze,\nNature's symphony puts the mind at ease."""
        else:
            return f"""Your task is to interpret the following poem and explain its meaning and stylistic elements.

Poem: {t['poem']}

Provide your response in plain text format and include:
1. An explanation of the poem's meaning.
2. Identification of any notable stylistic elements (e.g., rhyme scheme, meter, imagery).

Example Response:
Explanation: This poem describes a peaceful night scene. The darkness of the sky contrasts with the brightness of the stars and the moon, creating a sense of calm and tranquility. The poem suggests that this stillness is a blessing.
Stylistic Elements: The poem uses an AABB rhyme scheme, simple meter, and imagery to create a vivid picture of the night."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theme" in t:
            criteria = [
                "The poem should adhere to the given theme.",
                "The poem should follow the specified constraints (e.g., rhyme scheme, line count, use of metaphor)."
            ]
        else:
            criteria = [
                "The explanation should accurately interpret the poem's meaning.",
                "The response should correctly identify notable stylistic elements."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
