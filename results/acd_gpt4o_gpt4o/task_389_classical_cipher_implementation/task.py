class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"cipher": "caesar", "shift": 3, "message": "HELLO WORLD"},
            "2": {"cipher": "vigenere", "key": "KEY", "message": "ATTACKATDAWN"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['cipher'] == 'caesar':
            return f"""Your task is to implement the Caesar cipher to encrypt the following message. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.

Message: {t['message']}
Shift: {t['shift']}

Provide the encrypted message as your response in plain text format."""
        elif t['cipher'] == 'vigenere':
            return f"""Your task is to implement the Vigenère cipher to encrypt the following message. The Vigenère cipher uses a keyword to shift letters in the plaintext.

Message: {t['message']}
Key: {t['key']}

Provide the encrypted message as your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)

        def caesar_cipher_encrypt(message: str, shift: int) -> str:
            encrypted = []
            for char in message:
                if char.isalpha():
                    shift_base = ord('A') if char.isupper() else ord('a')
                    encrypted.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
                else:
                    encrypted.append(char)
            return ''.join(encrypted)

        def vigenere_cipher_encrypt(message: str, key: str) -> str:
            key = (key * (len(message) // len(key)) + key[:len(message) % len(key)]).upper()
            encrypted = []
            for i, char in enumerate(message):
                if char.isalpha():
                    shift_base = ord('A')
                    encrypted.append(chr((ord(char) - shift_base + ord(key[i]) - shift_base) % 26 + shift_base))
                else:
                    encrypted.append(char)
            return ''.join(encrypted)

        if t['cipher'] == 'caesar':
            expected_output = caesar_cipher_encrypt(t['message'], t['shift'])
        elif t['cipher'] == 'vigenere':
            expected_output = vigenere_cipher_encrypt(t['message'], t['key'])
        else:
            return 0.0

        return 1.0 if eval_with_llm_judge(instructions, submission, [f"The encrypted message should be: {expected_output}"]) else 0.0
