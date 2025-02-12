import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        encryption_methods = [
            "Symmetric key",
            "Public key",
            "Homomorphic",
            "Quantum-resistant"
        ]
        dna_storage_techniques = [
            "In vitro",
            "In vivo",
            "Cell-free",
            "Synthetic organelles"
        ]
        extreme_environments = [
            "Deep sea",
            "Space vacuum",
            "Radioactive zones",
            "Extreme temperature"
        ]
        data_types = [
            "Text",
            "Images",
            "Audio",
            "Executable code"
        ]
        
        tasks = {}
        for i in range(2):
            encryption = random.choice(encryption_methods)
            storage = random.choice(dna_storage_techniques)
            environment = random.choice(extreme_environments)
            data = random.choice(data_types)
            
            tasks[str(i+1)] = {
                "encryption": encryption,
                "storage": storage,
                "environment": environment,
                "data": data
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical system for encoding and encrypting {t['data']} in synthetic DNA sequences using {t['encryption']} encryption, then analyze its potential for long-term data storage using {t['storage']} techniques and secure communication in {t['environment']} environments. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your DNA-based cryptosystem.
   b) Explain how you encode {t['data']} into DNA sequences.
   c) Detail your {t['encryption']} encryption method for DNA-encoded data.
   d) Discuss how your system integrates with {t['storage']} storage techniques.

2. Encoding and Encryption Process (200-250 words):
   a) Provide a step-by-step explanation of your encoding and encryption process.
   b) Discuss any novel algorithms or techniques you've developed.
   c) Explain how your system ensures data integrity and security.

3. Storage and Retrieval (200-250 words):
   a) Describe how your system stores encrypted DNA sequences using {t['storage']} techniques.
   b) Explain the process of retrieving and decrypting the stored information.
   c) Discuss how your system maintains data stability over long periods.

4. Environmental Adaptation (150-200 words):
   a) Analyze how your system would function in {t['environment']} environments.
   b) Discuss any special adaptations or protective measures required.
   c) Explain potential advantages of DNA-based storage in these conditions.

5. Security Analysis (200-250 words):
   a) Assess the security of your system against known cryptographic attacks.
   b) Discuss potential vulnerabilities specific to DNA-based encryption.
   c) Propose methods to enhance the security of your system.

6. Practical Applications (150-200 words):
   a) Suggest three potential applications of your DNA cryptosystem.
   b) Discuss how these applications could impact fields such as data archiving, secure communication, or biotechnology.
   c) Address any ethical considerations related to these applications.

7. Future Directions and Challenges (150-200 words):
   a) Identify key challenges in implementing your system.
   b) Propose areas for future research and development.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of synthetic biology, information theory, and cryptography. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of synthetic biology, information theory, and cryptography, especially as they relate to {t['encryption']} encryption and {t['storage']} storage techniques",
            f"The proposed system effectively encodes and encrypts {t['data']} in synthetic DNA sequences",
            f"The storage and retrieval process is well-explained and accounts for long-term stability",
            f"The system's adaptation to {t['environment']} environments is thoroughly analyzed",
            "The security analysis is comprehensive and addresses DNA-specific vulnerabilities",
            "The proposed applications are innovative and their potential impacts are well-discussed",
            "The response follows the required format and falls within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
