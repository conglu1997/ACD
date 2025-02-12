class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "story": [
                    {"text": "You find yourself in a dark forest. There are paths to the north and south.", "choices": {"north": 1, "south": 2}},
                    {"text": "You encounter a wild beast blocking your path. Do you fight or run?", "choices": {"fight": 3, "run": 4}},
                    {"text": "You reach a tranquil lake. Do you rest or continue walking?", "choices": {"rest": 5, "continue": 6}},
                    {"text": "You fight bravely and defeat the beast. You find a treasure chest. Congratulations!", "choices": {}},
                    {"text": "You run back and safely return home. The adventure ends here.", "choices": {}},
                    {"text": "You rest by the lake and regain your strength. You continue your journey and find a hidden village. Congratulations!", "choices": {}},
                    {"text": "You continue walking and get lost in the forest. The adventure ends here.", "choices": {}}
                ]
            },
            "2": {
                "story": [
                    {"text": "You wake up in a mysterious cave. There are exits to the east and west.", "choices": {"east": 1, "west": 2}},
                    {"text": "You find a river blocking your path. Do you swim across or build a raft?", "choices": {"swim": 3, "raft": 4}},
                    {"text": "You encounter a wise sage. Do you ask for help or continue on your own?", "choices": {"ask": 5, "continue": 6}},
                    {"text": "You swim across the river safely and find a hidden treasure. Congratulations!", "choices": {}},
                    {"text": "You build a raft and float down the river to freedom. Congratulations!", "choices": {}},
                    {"text": "The sage provides you with a map leading to a treasure. Congratulations!", "choices": {}},
                    {"text": "You continue on your own and get lost in the cave. The adventure ends here.", "choices": {}}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to navigate through the following text-based adventure game by making sequential choices. Read each part of the story and make your decision based on the given choices. Your goal is to successfully complete the adventure. Provide your response as a series of choices in plain text format, separated by commas. For example: 'north, fight'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_id = 0
        try:
            choices = submission.split(', ')
            for choice in choices:
                task_id = t['story'][task_id]['choices'][choice]
            # Check if the final story text contains 'Congratulations!'
            if 'Congratulations!' in t['story'][task_id]['text']:
                return 1.0
        except (KeyError, IndexError):
            return 0.0
        return 0.0
