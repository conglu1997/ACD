class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "decipher",
                "encoded_message": "GSRH RH Z HVXIVG",
                "cipher": {"A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"}
            },
            "2": {
                "task_type": "encode",
                "message": "HELLO WORLD",
                "cipher": {"A": "M", "B": "N", "C": "B", "D": "V", "E": "C", "F": "X", "G": "Z", "H": "L", "I": "K", "J": "J", "K": "H", "L": "G", "M": "F", "N": "D", "O": "S", "P": "A", "Q": "P", "R": "O", "S": "I", "T": "U", "U": "Y", "V": "T", "W": "R", "X": "E", "Y": "W", "Z": "Q"}
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'decipher':
            return f"""Your task is to decipher the following encoded message using the given substitution cipher:

Encoded Message: {t['encoded_message']}

Cipher: {t['cipher']}

Each letter in the encoded message is substituted with another letter according to the given cipher. For example, if the cipher is {{"A": "B", "B": "C"}}, then an encoded message "A" would be decoded to "B", and "B" would be decoded to "C".

Provide the decoded message in plain text format.

Expected format:
Decoded Message: [Your decoded message]
"""
        elif t['task_type'] == 'encode':
            return f"""Your task is to encode the following message using the given substitution cipher:

Message: {t['message']}

Cipher: {t['cipher']}

Each letter in the message should be substituted with another letter according to the given cipher. For example, if the cipher is {{"A": "B", "B": "C"}}, then a message "A" would be encoded to "B", and "B" would be encoded to "C".

Provide the encoded message in plain text format.

Expected format:
Encoded Message: [Your encoded message]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'decipher':
            criteria = ["The decoded message should be 'THIS IS A SECRET'."]
        elif t['task_type'] == 'encode':
            criteria = ["The encoded message should be 'LCSGG SRSGC'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
