class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "art_to_poetry",
                "description": "A serene landscape with rolling hills, a shimmering lake, and a golden sunset casting long shadows over the scene."
            },
            "2": {
                "type": "poetry_to_art",
                "poem": "In twilight's embrace, the hills gently sleep,\nA lake of silver whispers secrets deep.\nGolden hues dance as day bids adieu,\nShadows stretch long, painting nature's view."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'art_to_poetry':
            return f"""Your task is to translate the following visual art description into a poem:

Description: {t['description']}

Ensure your poem captures the essence and imagery of the description. Provide your poem in plain text format.

Response format:
Poem: [Your poem]"""
        else:
            return f"""Your task is to translate the following poem into a detailed visual art description:

Poem: {t['poem']}

Ensure your description captures the essence and imagery of the poem. Provide your description in plain text format.

Response format:
Description: [Your detailed visual art description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'art_to_poetry':
            criteria = ["The poem should capture the essence and imagery of the visual art description."]
        else:
            criteria = ["The visual art description should capture the essence and imagery of the poem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
