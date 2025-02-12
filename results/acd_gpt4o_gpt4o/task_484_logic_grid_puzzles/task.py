class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Alice, Bob, and Carol each have a different pet: a cat, a dog, and a rabbit. Use the clues to determine who has which pet.",
                "clues": [
                    "Alice does not have the dog.",
                    "Bob has the rabbit.",
                    "Carol does not have a cat."
                ],
                "solution": {
                    "Alice": "cat",
                    "Bob": "rabbit",
                    "Carol": "dog"
                }
            },
            "2": {
                "puzzle": "Three friends – Eve, Frank, and Grace – each ride a different type of vehicle: a bicycle, a scooter, and a skateboard. Use the clues to determine who rides which vehicle.",
                "clues": [
                    "Eve does not ride a scooter.",
                    "Frank rides a skateboard.",
                    "Grace does not ride a bicycle."
                ],
                "solution": {
                    "Eve": "bicycle",
                    "Frank": "skateboard",
                    "Grace": "scooter"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logic grid puzzle using the given clues.

Puzzle: {t['puzzle']}
Clues: {', '.join(t['clues'])}

Provide your solution in the format: 'Name: Pet/Vehicle'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution must correctly match each person with their pet or vehicle.",
            "The solution must be provided in the format: 'Name: Pet/Vehicle'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
