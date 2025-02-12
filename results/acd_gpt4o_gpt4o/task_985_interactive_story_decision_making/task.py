class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "story": "You are an adventurer exploring an ancient temple. As you enter the main hall, you see three doors: one to the left, one to the right, and one straight ahead. Each door has a unique symbol: a lion, an eagle, and a snake. Which door do you choose?",
                "choices": ["lion", "eagle", "snake"],
                "consequences": {
                    "lion": "The door leads to a room filled with gold, but a trap is triggered. You must choose whether to disarm the trap or take the gold and run.",
                    "eagle": "The door opens to a library filled with ancient texts. You can spend time reading or search for a hidden passage.",
                    "snake": "The door leads to a dark tunnel. You hear hissing sounds. You can either proceed cautiously or retreat and choose another door."
                },
                "expected_result": "A coherent continuation of the story based on the chosen path, maintaining logical progression."
            },
            "2": {
                "story": "You are a detective investigating a series of mysterious disappearances in a small town. As you gather clues, you find three potential leads: a suspicious neighbor, a hidden diary, and a strange artifact. Which lead do you follow?",
                "choices": ["neighbor", "diary", "artifact"],
                "consequences": {
                    "neighbor": "The neighbor is defensive and evasive. You can either press for more information or search their house while they are distracted.",
                    "diary": "The diary contains cryptic entries. You can spend time decoding them or visit the places mentioned in the entries.",
                    "artifact": "The artifact is linked to an ancient legend. You can research its history or take it to a local expert for examination."
                },
                "expected_result": "A coherent continuation of the story based on the chosen path, maintaining logical progression."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are about to engage in an interactive story. Read the initial scenario and make a decision based on the given options. Your decision will influence the next part of the story. Ensure that your continuation is coherent and logically follows from the choice you made.

Initial Scenario: {t['story']}

Choices: {', '.join(t['choices'])}

Provide your decision and the continuation of the story in a clear and coherent format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The continuation should be coherent, maintain logical progression, and follow from the chosen path."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
