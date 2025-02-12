class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clues": [
                    "A wealthy businessman is found dead in his study.",
                    "The room was locked from the inside.",
                    "A broken window is found on the ground floor.",
                    "A ladder is missing from the garden shed.",
                    "A neighbor reported seeing a shadowy figure in the garden late at night."
                ]
            },
            "2": {
                "clues": [
                    "A famous painting is stolen from a museum.",
                    "The security cameras were disabled.",
                    "A guard was found unconscious near the entrance.",
                    "A van was seen speeding away from the museum around the time of the theft.",
                    "A note was left at the scene: 'Art is priceless.'"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        clues = "\n".join(f"- {clue}" for clue in t["clues"])
        return f"""Analyze the given clues from the fictional mystery and generate a plausible solution with a detailed explanation. Here are the clues:\n{clues}\n\nSubmit your solution and explanation as a plain text string in the following format: 'Solution: [Your solution]\nExplanation: [Your detailed explanation]'. Ensure your explanation covers all the clues provided and is coherent and logically consistent with them."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should logically follow from the clues.", "The explanation should be detailed, cover all the clues, and be consistent with them."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
