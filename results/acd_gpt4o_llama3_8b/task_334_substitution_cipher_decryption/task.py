class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ciphered_text": "Tfd jefsq mfu gjsjodf pg uif lfwfm rvfoult.", "shift": 1},
            "2": {"ciphered_text": "Uijt jt b tjnqmf tfof fpg b dbftbs djqifs.", "shift": 1}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ciphered_text = t['ciphered_text']
        shift = t['shift']
        return f"""You are given a text that has been encrypted using a simple Caesar cipher with a shift of {shift}. Your task is to decrypt the text and provide the original message. Note that the shift value is the same for all characters. Here is the encrypted text:

{ciphered_text}

Submit your decrypted message as a plain text string. Ensure that the decrypted message makes sense and is grammatically correct."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The decrypted message should make sense and be grammatically correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
