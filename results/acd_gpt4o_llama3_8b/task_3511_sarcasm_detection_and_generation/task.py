class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "Oh great, another meeting that could have been an email."},
            "2": {"context": "Your friend tells you they got yet another parking ticket."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'statement' in t:
            return f"""You are given a statement. Your task is to determine if the statement is sarcastic. Respond with 'Sarcastic' or 'Not Sarcastic'.

Statement: {t['statement']}

Submit your response as a plain text string in the following format:
Response: [Your answer]"""
        elif 'context' in t:
            return f"""You are given a context. Your task is to generate a sarcastic response that fits the given context. Ensure that your response is witty, relevant, and clearly conveys sarcasm.

Context: {t['context']}

Submit your response as a plain text string in the following format:
Sarcastic Response: [Your response]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'statement' in t:
            criteria = [
                "The response should correctly identify the statement as Sarcastic or Not Sarcastic."]
        else:
            criteria = [
                "The response should be sarcastic.",
                "The response should be relevant to the given context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
