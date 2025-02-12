class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sender": "Sherlock Holmes",
                "receiver": "Dr. John Watson",
                "context": "Holmes is writing to Watson to inform him about a new case involving a stolen artifact from the British Museum."
            },
            "2": {
                "sender": "Harry Potter",
                "receiver": "Hermione Granger",
                "context": "Harry is writing to Hermione to thank her for her help in their recent adventure and to discuss plans for the upcoming school year at Hogwarts."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a fictional letter based on the given context:

Sender: {t['sender']}
Receiver: {t['receiver']}
Context: {t['context']}

Ensure that the letter captures the personality and writing style of the sender, and is coherent and engaging. Submit your letter as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The letter should capture the personality and writing style of the sender.",
            "The letter should be coherent and engaging.",
            "The letter should adhere to the given context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
