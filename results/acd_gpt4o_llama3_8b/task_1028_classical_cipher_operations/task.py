class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "Encode the following message using the Caesar cipher with a shift of 3: 'HELLO WORLD'. Provide the encoded message."
            },
            "2": {
                "task": "Decode the following message using the Vigenère cipher with the key 'LEMON': 'LXFOPVEFRNHR'. Provide the decoded message."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform the following task:

{t['task']}

Ensure that your response follows the specified cipher method and provides the correct encoded or decoded message. Submit your response as a plain text string in the following format:

Response: [Your encoded or decoded message]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        def caesar_cipher_encode(text: str, shift: int) -> str:
            encoded_text = []
            for char in text:
                if char.isalpha():
                    shift_base = 65 if char.isupper() else 97
                    encoded_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
                else:
                    encoded_text.append(char)
            return ''.join(encoded_text)

        def vigenere_cipher_decode(text: str, key: str) -> str:
            key = key.upper()
            decoded_text = []
            key_index = 0
            for char in text:
                if char.isalpha():
                    shift = ord(key[key_index]) - 65
                    decoded_char = chr((ord(char) - 65 - shift) % 26 + 65)
                    decoded_text.append(decoded_char)
                    key_index = (key_index + 1) % len(key)
                else:
                    decoded_text.append(char)
            return ''.join(decoded_text)

        expected_responses = {
            "1": caesar_cipher_encode('HELLO WORLD', 3),
            "2": vigenere_cipher_decode('LXFOPVEFRNHR', 'LEMON')
        }

        task_id = "1" if 'Caesar' in t['task'] else "2"
        return 1.0 if submission.strip() == expected_responses[task_id] else 0.0
