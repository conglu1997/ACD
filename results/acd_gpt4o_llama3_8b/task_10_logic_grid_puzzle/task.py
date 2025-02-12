class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clues": [
                    "1. The person who likes apples is not Bob.",
                    "2. Charlie likes bananas.",
                    "3. The person who likes cherries is either Alice or Bob.",
                    "4. Alice does not like bananas."
                ],
                "variables": {
                    "names": ["Alice", "Bob", "Charlie"],
                    "fruits": ["apples", "bananas", "cherries"]
                }
            },
            "2": {
                "clues": [
                    "1. The red house is to the left of the green house.",
                    "2. The blue house is not on the far right.",
                    "3. The person in the green house drinks coffee.",
                    "4. The person in the red house drinks tea.",
                    "5. The person in the middle house drinks milk."
                ],
                "variables": {
                    "houses": ["red", "green", "blue"],
                    "drinks": ["tea", "coffee", "milk"]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        clues = t["clues"]
        return "Solve the logic grid puzzle based on the given clues. Assign the correct relationships between entities. Ensure that the solution is logically consistent with all the provided clues.\n\nClues:\n" + "\n".join(clues) + "\n\nSubmit your solution as a JSON object. For example, {'Alice': 'apples', 'Bob': 'bananas', 'Charlie': 'cherries'}."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import json
        from src.eval_helper import eval_with_llm_judge
        try:
            parsed_submission = json.loads(submission)
        except json.JSONDecodeError:
            return 0.0

        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution must be logically consistent with all the provided clues."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
