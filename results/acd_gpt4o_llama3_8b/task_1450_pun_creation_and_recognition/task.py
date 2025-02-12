class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a pun involving a fruit."
            },
            "2": {
                "sentence": "I used to be a baker, but I couldn't make enough dough."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            return f"Create a pun based on the following prompt:\n\nPrompt:\n{t['prompt']}"
        else:
            return f"Identify the pun in the following sentence and explain the wordplay:\n\nSentence:\n{t['sentence']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The response should include a pun.",
                "The pun should be based on the given prompt.",
                "The pun should be humorous or clever."
            ]
        else:
            criteria = [
                "The response should correctly identify the pun in the sentence.",
                "The explanation should accurately describe the wordplay involved in the pun."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
