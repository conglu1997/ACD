class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "characters": [
                    {"name": "Alice", "traits": "curious, adventurous, optimistic"},
                    {"name": "Bob", "traits": "cautious, logical, skeptical"}
                ],
                "scenario": "Alice and Bob are exploring an ancient, mysterious temple. They encounter a puzzle that needs to be solved to proceed further. The puzzle involves deciphering ancient symbols that are hidden in different parts of the temple and avoiding traps that are triggered by wrong moves."
            },
            "2": {
                "characters": [
                    {"name": "Eve", "traits": "sarcastic, witty, impatient"},
                    {"name": "Mallory", "traits": "calm, methodical, patient"}
                ],
                "scenario": "Eve and Mallory are on a space mission to repair a malfunctioning satellite. They need to work together to fix the issue, despite their differing approaches and a looming deadline. The satellite's control system is malfunctioning, requiring them to manually align the satellite's antennas and recalibrate the system."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        characters = ", ".join([f"{char['name']} ({char['traits']})" for char in t['characters']])
        return f"""Generate a fictional dialogue based on the following character profiles and scenario:

Characters:
{characters}

Scenario:
{t['scenario']}

Ensure the dialogue is engaging, coherent, and maintains the consistency of each character's traits. The dialogue should be contextually appropriate and advance the scenario. The characters' language styles should consistently reflect their traits. The dialogue should be at least 15 exchanges long.

Submit your response as a plain text string formatted as a dialogue.

Example format:
Alice: [Alice's dialogue]
Bob: [Bob's dialogue]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue should be engaging and coherent.",
            "The characters' traits should be consistently maintained.",
            "The dialogue should be contextually appropriate for the scenario.",
            "The characters' language styles should reflect their traits.",
            "The dialogue should advance the scenario.",
            "The dialogue should be at least 15 exchanges long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
