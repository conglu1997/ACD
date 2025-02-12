import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Navajo",
                "features": "tonal language with complex verb structure"
            },
            {
                "name": "Finnish",
                "features": "agglutinative language with extensive case system"
            },
            {
                "name": "Arabic",
                "features": "root-based morphology with non-concatenative inflection"
            },
            {
                "name": "Chinese",
                "features": "tonal language with logographic writing system"
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cryptographic system based on the linguistic features of {t['name']} ({t['features']}). Your task is to create a unique encryption method that leverages the specific characteristics of this language to secure messages.

Follow these steps:

1. Analyze the given language features and explain how they can be used for cryptographic purposes (2-3 sentences).

2. Design your cryptosystem by describing:
   a) The encryption process (2-3 sentences)
   b) The decryption process (2-3 sentences)
   c) The key generation method (1-2 sentences)

3. Provide an example of how your cryptosystem works:
   a) Generate a sample key
   b) Encrypt the message: "Meet me at sunset"
   c) Show the decryption process for the encrypted message

4. Analyze the strengths and potential vulnerabilities of your cryptosystem (2-3 sentences).

5. Explain how your cryptosystem satisfies the following cryptographic principles:
   a) Confusion
   b) Diffusion

6. Discuss how this linguistic-based cryptosystem could potentially impact the field of cryptography or linguistics (2-3 sentences).

Format your response as follows:

Language Analysis:
[Your analysis here]

Cryptosystem Design:
1. Encryption Process: [Your description]
2. Decryption Process: [Your description]
3. Key Generation: [Your description]

Example:
1. Sample Key: [Your key]
2. Encrypted Message: [Your encrypted message]
3. Decryption Process: [Your decryption explanation]

Strengths and Vulnerabilities:
[Your analysis here]

Cryptographic Principles:
1. Confusion: [Your explanation]
2. Diffusion: [Your explanation]

Potential Impact:
[Your discussion here]

Ensure that your cryptosystem is innovative, grounded in the linguistic features of the given language, and demonstrates a clear understanding of both linguistic and cryptographic principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cryptosystem should be based on the linguistic features of {t['name']} ({t['features']})",
            "The response should include all required sections: Language Analysis, Cryptosystem Design, Example, Strengths and Vulnerabilities, Cryptographic Principles, and Potential Impact",
            "The cryptosystem design should be innovative and logically consistent",
            "The example should demonstrate a working encryption and decryption process",
            "The analysis of strengths, vulnerabilities, and cryptographic principles should be thoughtful and accurate",
            "The response should demonstrate interdisciplinary knowledge of linguistics and cryptography"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
