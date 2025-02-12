class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a short story about a journey through a magical forest.",
                "constraints": "The story must include a talking animal, a hidden treasure, and must end with a moral lesson. The style should mimic a fairy tale." 
            },
            "2": {
                "prompt": "Write a poem about the change of seasons.",
                "constraints": "The poem must be at least 12 lines long, include personification, and follow an ABAB rhyme scheme." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a creative piece of writing based on the given prompt and constraints.

Prompt: {t['prompt']}

Constraints: {t['constraints']}

Your response should be coherent, creative, and adhere to the specified constraints. Submit your response as a plain text string in the following format:

For Task 1 (Short Story):
- Title: [Title of your story]
- Story: [Your story here]

For Task 2 (Poem):
- Title: [Title of your poem]
- Poem: [Your poem here]

Example for Task 1:
- Title: The Enchanted Forest Adventure
- Story: Once upon a time, in a magical forest, there lived a talking rabbit named Thumper. Thumper discovered a hidden treasure beneath an ancient oak tree. With the help of his forest friends, he learned that the true treasure was the friendships he made along the way. And thus, Thumper and his friends lived happily ever after, always remembering the moral lesson that true wealth lies in the bonds we share.

Example for Task 2:
- Title: Seasons' Dance
- Poem: Winter whispers through the trees,
Spring arrives with gentle breeze,
Summer shouts with vibrant hues,
Autumn dons its golden shoes.

Make sure to follow the specified format exactly and provide a comprehensive, creative piece of writing."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should adhere to the given prompt and constraints.",
            "The writing should be coherent and creative.",
            "The story or poem should follow the specified style and structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
