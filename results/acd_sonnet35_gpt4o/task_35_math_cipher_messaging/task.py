import random
import string
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        operations = [
            {"name": "add", "symbol": "+"},
            {"name": "subtract", "symbol": "-"},
            {"name": "multiply", "symbol": "*"},
            {"name": "divide", "symbol": "/"}
        ]
        topics = ["space exploration", "renewable energy", "artificial intelligence", "ocean conservation"]
        
        tasks = {}
        for i in range(1, 3):
            operation = random.choice(operations)
            key = random.randint(2, 9)
            if operation['name'] == 'divide':
                # Ensure key is coprime with 26 for division
                while math.gcd(key, 26) != 1:
                    key = random.randint(2, 9)
            task = {
                "operation": operation,
                "key": key,
                "topic": random.choice(topics)
            }
            tasks[str(i)] = task
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task involves creating and decoding messages using a custom mathematical cipher. Follow these steps:

1. Create a short message (1 sentence, maximum 15 words) related to the topic of {t['topic']}.

2. Encode your message using the following cipher:
   - Convert each letter to its position in the alphabet (A=1, B=2, ..., Z=26).
   - {t['operation']['name'].capitalize()} {t['key']} to each number.
   - If the result is greater than 26, subtract 26 until it's in the range 1-26.
   - If the result is less than 1, add 26 until it's in the range 1-26.
   - Convert the numbers back to letters.
   - For division, round down to the nearest integer before converting back to a letter.

Example: If the operation is 'add' and the key is 3:
'HELLO' would become 'KHOOR' because:
H(8) + 3 = 11 -> K
E(5) + 3 = 8 -> H
L(12) + 3 = 15 -> O
L(12) + 3 = 15 -> O
O(15) + 3 = 18 -> R

3. Provide your original message and the encoded message.

4. Now, decode this message using the same cipher in reverse:
   [Encoded message will be provided here]

Provide your answer in the following format:

Original message: [Your message here]
Encoded message: [Your encoded message here]
Decoded message: [The decoded message provided]

Ensure your original message is relevant to the given topic and that your encoding follows the cipher rules exactly. Spaces and punctuation should remain unchanged in the encoding process. The cipher is case-insensitive, so you may use uppercase or lowercase letters.

NOTE: Strictly adhere to the format provided above. Your response will be automatically evaluated, so exact formatting is crucial for a correct assessment."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        
        # Generate a random encoded message for decoding
        alphabet = string.ascii_uppercase
        message = ' '.join([''.join(random.choices(alphabet, k=5)) for _ in range(2)])
        encoded_message = TaskFamily.encode_message(message, t['operation'], t['key'])
        
        # Insert the encoded message into the instructions
        instructions = instructions.replace('[Encoded message will be provided here]', encoded_message)
        
        criteria = [
            f"The original message is 1 sentence long (maximum 15 words) and relevant to the topic of {t['topic']}.",
            "The encoded message applies the given cipher to the original message with no more than one minor error.",
            f"The decoded message correctly deciphers '{encoded_message}' using the given cipher in reverse with no more than one minor error.",
            "The response follows the format specified in the instructions.",
            "Spaces and punctuation remain unchanged in the encoding process."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

    @staticmethod
    def encode_message(message: str, operation: dict, key: int) -> str:
        alphabet = string.ascii_uppercase
        encoded = []
        for char in message.upper():
            if char in alphabet:
                num = alphabet.index(char) + 1
                if operation['name'] == 'add':
                    num = ((num + key - 1) % 26) + 1
                elif operation['name'] == 'subtract':
                    num = ((num - key - 1) % 26) + 1
                elif operation['name'] == 'multiply':
                    num = ((num * key - 1) % 26) + 1
                elif operation['name'] == 'divide':
                    num = ((num * pow(key, -1, 26) - 1) % 26) + 1
                encoded.append(alphabet[num - 1])
            else:
                encoded.append(char)
        return ''.join(encoded)
