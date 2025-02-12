class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_prompt": "A young boy finds a mysterious key in the attic.", "additional_prompts": ["The key starts glowing when he touches it.", "He hears a whisper telling him to find the hidden door.", "The door leads to an ancient library full of magical books."]},
            "2": {"initial_prompt": "A spaceship lands in the middle of a bustling city.", "additional_prompts": ["An alien steps out and speaks in an unknown language.", "The alien points to a nearby building and gestures urgently.", "Inside the building, they find a device that could save the alien's planet."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with an initial prompt to start a story. Your task is to generate an ongoing story based on the initial prompt and integrate additional elements as new prompts are given to you. Ensure that the story remains coherent and that each new element is incorporated smoothly into the narrative.

Initial Prompt: {t['initial_prompt']}

You will be given additional prompts one by one. Continue the story by integrating each new prompt seamlessly.

Example response format:
1. Initial Story: [Your story based on the initial prompt]
2. Continued Story: [Your story with the first additional prompt integrated]
3. Continued Story: [Your story with the second additional prompt integrated]
4. Continued Story: [Your story with the third additional prompt integrated]

Example:
Initial Prompt: 'A young boy finds a mysterious key in the attic.'
1. Initial Story: The young boy was exploring the dusty attic when his eyes caught a glimmer. He curiously approached the source and found an old, ornate key hidden among the cobwebs.
2. Continued Story: As he picked up the key, it started glowing with a soft, golden light. The boy's eyes widened in astonishment, and he felt a strange warmth spreading through his hand.
3. Continued Story: Suddenly, he heard a whisper, though no one was around. 'Find the hidden door,' the voice said. The boy felt a shiver down his spine but decided to follow the mysterious command.
4. Continued Story: After searching the attic, he found a hidden door behind an old bookshelf. With trembling hands, he used the key to unlock it. The door creaked open to reveal an ancient library filled with magical books, each glowing with enchantment. He stepped inside, ready for an adventure of a lifetime.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should maintain narrative coherence throughout.",
            "Each additional prompt should be integrated smoothly and logically into the story.",
            "The overall story should be engaging and creative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
