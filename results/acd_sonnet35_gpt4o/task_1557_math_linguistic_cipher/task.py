import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sequences = [
            {
                'name': 'Fibonacci',
                'rule': lambda n: 1 if n <= 1 else TaskFamily.fibonacci(n-1) + TaskFamily.fibonacci(n-2)
            },
            {
                'name': 'Prime',
                'rule': lambda n: TaskFamily.nth_prime(n)
            }
        ]
        return {str(i+1): seq for i, seq in enumerate(random.sample(sequences, 2))}

    @staticmethod
    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def nth_prime(n: int) -> int:
        count = 0
        num = 2
        while count < n:
            if TaskFamily.is_prime(num):
                count += 1
            if count == n:
                return num
            num += 1

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a cipher using the {t['name']} sequence and linguistic features, then encode and decode a message. Follow these steps:

1. Cipher Creation (200-250 words):
   a) Describe a cipher that uses the {t['name']} sequence to determine letter shifts or substitutions.
   b) Incorporate at least two linguistic features (e.g., parts of speech, syllable count) into your cipher rules.
   c) Explain how your cipher works, providing examples for clarity.

2. Message Encoding (100-150 words):
   a) Create a short message (1-2 sentences, 15-25 words) related to artificial intelligence or language processing.
   b) Encode your message using the cipher you created.
   c) Show your work, explaining each step of the encoding process.

3. Message Decoding (100-150 words):
   a) Decode the following message using your cipher: [ENCODED_MESSAGE]
   b) Explain your decoding process step by step.
   c) Present the decoded message.

4. Cipher Analysis (150-200 words):
   a) Discuss the strengths and weaknesses of your cipher.
   b) Analyze how the mathematical sequence and linguistic features interact in your cipher.
   c) Suggest one way to improve or expand your cipher.

Ensure your response demonstrates creativity, mathematical reasoning, and linguistic understanding. Use clear, concise language and provide examples where necessary.

Format your response with numbered sections and clear headings. Your total response should be between 550-750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the chosen mathematical sequence and its application in the cipher.",
            "The cipher incorporates at least two linguistic features in a creative and logical manner.",
            "The encoding and decoding processes are explained clearly and correctly.",
            "The analysis of the cipher's strengths and weaknesses is insightful and well-reasoned.",
            "The overall response shows creativity, mathematical reasoning, and linguistic understanding."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
