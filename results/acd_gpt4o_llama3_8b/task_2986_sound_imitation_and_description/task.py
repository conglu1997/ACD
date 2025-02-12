class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sound_scenario": "A busy city street during rush hour, with honking cars, people talking, distant construction noises, ambulance sirens, the occasional sound of a bike bell, and street musicians playing."
            },
            "2": {
                "sound_scenario": "A serene forest at dawn, with birds chirping, a gentle stream flowing, leaves rustling in the wind, the distant howl of a wolf, the sound of a woodpecker pecking a tree, and a deer drinking from the stream."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an onomatopoeic representation and a detailed description of the following sound scenario: {t['sound_scenario']}.

Your response should include:
1. An onomatopoeic representation of the sounds involved in the scenario. Use creative language to convey the sounds as accurately as possible. Each sound should be represented distinctly.
2. A detailed description of the sounds, including any sensory details that help convey the atmosphere. Describe the quality, volume, and any notable characteristics of each sound individually.
3. An explanation of why each sound is significant to the scenario.

Submit your response as a plain text string in the following format:

Onomatopoeia: [Your onomatopoeic representation]
Description: [Your detailed description]
Significance: [Your explanation of the significance of each sound]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The onomatopoeic representation should be relevant and creatively convey the essence of the sound scenario.",
            "Each sound should be represented distinctly in the onomatopoeic representation.",
            "The detailed description should accurately describe the sounds and include sensory details.",
            "The description should cover the quality, volume, and notable characteristics of each sound individually.",
            "The significance of each sound in the scenario should be explained clearly.",
            "The onomatopoeic representation, description, and significance explanation should be clearly separated in the submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
