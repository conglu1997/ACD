class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "generation",
                "scenario": "A group of friends planning a surprise birthday party for another friend, Dave, who is known for being punctual and loves outdoor activities.",
                "characters": ["Alice (the organizer)", "Bob (the cautious one)", "Charlie (always enthusiastic)", "Dana (the creative one)", "Eve (the practical one)", "Frank (the quiet observer)", "Gina (the distractor)", "Henry (the detail-focused)", "Irene (the conflict resolver)", "Jack (the joker)"],
                "prompt": "Generate a dialogue where the friends discuss the details of the party, including the venue, time, surprise elements, and potential issues that might arise. Ensure each character has a distinct personality and voice, and that the dialogue reflects their traits."
            },
            "2": {
                "type": "interpretation",
                "dialogue": "Alice: We should have the party at the park.\nBob: That sounds great, but what if it rains?\nCharlie: Maybe we can have a backup plan at my place just in case.\nDana: We should also think of some fun outdoor activities.\nEve: That's a good idea, but we need to make sure everything is practical.\nFrank: I can help with setting up.\nGina: Let's make sure Dave doesn't find out!\nHenry: I'll handle the details for the backup plan.\nIrene: If there's any disagreement, we can resolve it calmly.\nJack: And I'll bring the jokes to keep everyone entertained!",
                "question": "Describe the personalities and roles of each character based on the dialogue."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'generation':
            return f"""Generate a dialogue based on the following scenario and prompt:

Scenario: {t['scenario']}
Characters: {', '.join(t['characters'])}

Prompt: {t['prompt']}

Ensure that each character's lines are distinct and reflect their personalities. Submit your response as a plain text string in the following format:

Dialogue:
[Your dialogue here]"""
        else:
            return f"""Interpret the following dialogue and provide a detailed description of the characters' personalities and roles:

Dialogue:
{t['dialogue']}

Question: {t['question']}

Submit your response as a plain text string in the following format:

Character Descriptions:
[Your descriptions here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'generation':
            validation_criteria = [
                "The dialogue should reflect the scenario and prompt.",
                "Each character should have a distinct personality and voice.",
                "The dialogue should be coherent and engaging.",
                "The dialogue should include discussions about the venue, time, surprise elements, and potential issues."
            ]
        else:
            validation_criteria = [
                "The descriptions should accurately reflect the personalities and roles of the characters.",
                "The interpretation should be detailed and coherent.",
                "The descriptions should align with the dialogue provided.",
                "Each character's role and personality should be distinctly identified."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
