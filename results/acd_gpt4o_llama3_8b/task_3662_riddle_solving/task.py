class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
            },
            "2": {
                "riddle": "I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following riddle by providing a logical and coherent explanation of your answer: {t['riddle']}.

Your response should include:
1. The riddle restated.
2. Your answer to the riddle.
3. A detailed explanation of how you arrived at the answer.

For example:
Riddle: I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, and I can drown. What am I?
Answer: Fire
Explanation: Fire is not a living being, but it 'grows' when it spreads. It needs oxygen to sustain itself, though it doesn't have lungs. It can be extinguished (drowned) by water."

Ensure your explanation is clear, logical, and directly addresses the riddle."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The answer should directly address the riddle.",
            "The explanation should be logical and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
