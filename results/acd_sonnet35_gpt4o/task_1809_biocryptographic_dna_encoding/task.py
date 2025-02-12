import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        encryption_methods = [
            {
                "name": "DNA Substitution Cipher",
                "description": "Replace each character with a specific DNA codon sequence."
            },
            {
                "name": "DNA Transposition Cipher",
                "description": "Rearrange the order of nucleotides based on a key."
            },
            {
                "name": "DNA Folding Cipher",
                "description": "Encrypt information based on the 3D folding patterns of DNA molecules."
            },
            {
                "name": "DNA Hybridization Cipher",
                "description": "Use complementary base pairing for encryption and decryption."
            }
        ]
        
        applications = [
            {
                "name": "Secure Communication",
                "problem": "Encode and encrypt a sensitive message for transmission through a biological medium."
            },
            {
                "name": "Data Storage",
                "problem": "Design a system to store and retrieve large amounts of data in synthesized DNA sequences."
            },
            {
                "name": "Biomarker Encryption",
                "problem": "Develop a method to encrypt patient-specific biomarker information in DNA sequences."
            },
            {
                "name": "Synthetic Biology Security",
                "problem": "Create a DNA-based authentication system for genetically engineered organisms."
            }
        ]
        
        return {
            "1": {
                "encryption": random.choice(encryption_methods),
                "application": random.choice(applications)
            },
            "2": {
                "encryption": random.choice(encryption_methods),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biocryptographic system using DNA sequences for information encoding and encryption, focusing on the {t['encryption']['name']} method. Then, apply your system to the following problem: {t['application']['problem']}

Your response should include:

1. Biocryptographic System Design (300-350 words):
   a) Describe your DNA-based encryption system in detail, explaining how it incorporates the {t['encryption']['name']} method.
   b) Explain the encoding process for converting information into DNA sequences.
   c) Detail the encryption and decryption processes, including any necessary biological or chemical operations.
   d) Discuss potential advantages of your system over classical cryptographic methods.

2. Information Theory Analysis (200-250 words):
   a) Analyze the information capacity of your DNA-based encryption system.
   b) Discuss the error rates and error correction mechanisms in your system.
   c) Compare the efficiency of your system to traditional digital encryption methods.

3. Application to the Problem (250-300 words):
   a) Apply your biocryptographic system to solve the problem: {t['application']['problem']}
   b) Provide a step-by-step explanation of how your system would be used in this context.
   c) Discuss any challenges specific to this application and how your system addresses them.

4. Security Analysis (200-250 words):
   a) Analyze the security strengths of your biocryptographic system.
   b) Identify potential vulnerabilities and propose ways to mitigate them.
   c) Discuss how quantum computing might affect the security of your system.

5. Ethical and Practical Considerations (150-200 words):
   a) Discuss ethical implications of using biological systems for cryptography.
   b) Address potential dual-use concerns of your technology.
   c) Propose guidelines for responsible development and use of biocryptographic systems.

Ensure your response demonstrates a deep understanding of synthetic biology, information theory, and cryptography. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The biocryptographic system design is coherent, creative, and clearly incorporates the specified encryption method using DNA sequences.",
            "The proposed system demonstrates novelty and innovation in its approach to DNA-based cryptography.",
            "The information theory analysis demonstrates a solid understanding of information capacity, error rates, and efficiency in the context of DNA-based systems.",
            "The application of the biocryptographic system to the given problem is well-explained and addresses the specific challenges of the application.",
            "The security analysis is thorough, identifying both strengths and potential vulnerabilities of the system.",
            "The response addresses ethical and practical considerations of biocryptographic systems thoughtfully.",
            "The overall response demonstrates a deep understanding of synthetic biology, information theory, and cryptography, using appropriate terminology and providing clear explanations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
