class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dialogue": "Person A: Hi! How was your weekend?\nPerson B: It was great! I went hiking in the mountains.\nPerson A: That sounds amazing! Did you see any wildlife?\nPerson B: Yes, I saw a few deer and even a bear from a distance.\nPerson A: Wow, that must have been thrilling! What else did you do?\nPerson B: [Incomplete]"},
            "2": {"dialogue": "Person A: Hey, did you finish the project report?\nPerson B: Not yet, I'm still working on the final section.\nPerson A: We need to submit it by tomorrow.\nPerson B: I know, I'm planning to stay late tonight to get it done.\nPerson A: Do you need any help with it?\nPerson B: [Incomplete]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following dialogue in a coherent and contextually appropriate manner:

Dialogue: {t['dialogue']}

Provide your continuation of the dialogue. Ensure that your response is natural, relevant to the preceding conversation, and maintains the context. Format your response as follows:

Continuation: [Your continuation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The continuation should be coherent and contextually appropriate.", "The response should be natural and relevant to the preceding conversation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
