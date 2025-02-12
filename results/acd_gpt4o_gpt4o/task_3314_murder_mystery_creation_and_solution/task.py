class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "elements": {
                    "victim": "a wealthy businessman",
                    "location": "a secluded mansion",
                    "weapon": "a candlestick",
                    "suspects": ["the butler", "the business partner", "the estranged wife"]
                }
            },
            "2": {
                "elements": {
                    "victim": "a famous actress",
                    "location": "a beach house",
                    "weapon": "a poisoned drink",
                    "suspects": ["the jealous co-star", "the personal assistant", "the ex-boyfriend"]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a murder mystery story based on the following elements and provide a logical solution to the mystery:

Victim: {t['elements']['victim']}
Location: {t['elements']['location']}
Weapon: {t['elements']['weapon']}
Suspects: {', '.join(t['elements']['suspects'])}

Ensure the story is engaging, coherent, and includes clues that lead to the logical identification of the murderer. Provide the story and its solution in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be engaging and coherent.", "The story should include clues that lead to the logical identification of the murderer.", "The solution should be logical and consistent with the clues provided in the story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
