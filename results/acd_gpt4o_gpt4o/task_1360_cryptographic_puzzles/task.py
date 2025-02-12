class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"cipher_text": "Uifsf jt b tfdsfu nfttbhf uibu zpv offe up efdpef", "cipher_type": "caesar", "shift": 1},
            "2": {"cipher_text": "Gsv jfrxp yildm ulc qfnkh levi gsrh rh z wvxlwvmg kilwvh!", "cipher_type": "atbash"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['cipher_type'] == 'caesar':
            return f"""Your task is to decipher the following message encoded with a Caesar cipher. The cipher uses a shift of {t['shift']}.

Encoded Message: {t['cipher_text']}

Provide the decoded message in plain text format."""
        elif t['cipher_type'] == 'atbash':
            return f"""Your task is to decipher the following message encoded with an Atbash cipher.

Encoded Message: {t['cipher_text']}

Provide the decoded message in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Provide expected answers for the criteria
        if t['cipher_type'] == 'caesar':
            expected_answer = "There is a secret message that you need to decode"
        elif t['cipher_type'] == 'atbash':
            expected_answer = "The quick brown fox jumps over the lazy dog"
        return 1.0 if eval_with_llm_judge(instructions, submission, [expected_answer]) else 0.0
