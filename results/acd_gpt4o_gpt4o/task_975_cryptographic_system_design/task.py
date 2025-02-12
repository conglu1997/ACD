class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Design a secure encryption system for transmitting confidential messages over the internet. Ensure it includes key generation, encryption, and decryption processes.", "additional_criteria": ["The system should use asymmetric cryptography.", "The design should include a detailed explanation of each process."]},
            "2": {"cryptographic_system": "A system that uses a simple substitution cipher for encryption. Each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.", "additional_criteria": ["Analyze the security of the provided cryptographic system.", "Suggest improvements to enhance its security.", "Provide a detailed explanation of your analysis and suggestions."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "requirements" in t:
            instructions = f"""Your task is to design a secure cryptographic system based on the following requirements:

{t['requirements']}

Ensure your design meets the following criteria:
{', '.join(t['additional_criteria'])}

Provide a detailed explanation of each process involved in the system.

Response format:
1. Key Generation: [Detailed explanation of key generation process]
2. Encryption: [Detailed explanation of encryption process]
3. Decryption: [Detailed explanation of decryption process]"""
        else:
            instructions = f"""Your task is to analyze the security of the following cryptographic system:

{t['cryptographic_system']}

Ensure your analysis meets the following criteria:
{', '.join(t['additional_criteria'])}

Provide a detailed explanation of your analysis and suggestions.

Response format:
1. Security Analysis: [Detailed explanation of the security analysis]
2. Suggested Improvements: [Detailed suggestions for improving the security]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get('additional_criteria', [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
