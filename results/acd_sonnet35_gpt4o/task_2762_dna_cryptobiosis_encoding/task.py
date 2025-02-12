import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        encoding_methods = [
            "Base64-inspired nucleotide encoding",
            "Codon-based encryption",
            "DNA origami steganography",
            "Epigenetic markers as encryption keys"
        ]
        data_types = [
            "Text document",
            "Image file",
            "Audio recording",
            "Software code"
        ]
        biological_constraints = [
            "Avoiding start/stop codons",
            "Maintaining GC content balance",
            "Preventing unintended protein expression",
            "Ensuring DNA stability"
        ]
        return {
            "1": {
                "encoding_method": random.choice(encoding_methods),
                "data_type": random.choice(data_types),
                "biological_constraint": random.choice(biological_constraints)
            },
            "2": {
                "encoding_method": random.choice(encoding_methods),
                "data_type": random.choice(data_types),
                "biological_constraint": random.choice(biological_constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for encoding and decoding complex information in synthetic DNA sequences, considering biological constraints and cryptographic principles. Your task involves the following specifics:

Encoding method: {t['encoding_method']}
Data type to encode: {t['data_type']}
Biological constraint to address: {t['biological_constraint']}

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your DNA encoding/decoding system.
   b) Explain how your system incorporates the specified encoding method.
   c) Discuss how your approach addresses the given biological constraint.
   d) Provide a high-level diagram or pseudocode illustrating your system's workflow.

2. Encoding Process (200-250 words):
   a) Detail the step-by-step process of encoding the specified data type into DNA.
   b) Explain any preprocessing or compression techniques used.
   c) Describe how your system ensures data integrity and error correction.

3. Decoding Mechanism (200-250 words):
   a) Explain the process of retrieving and decoding information from the synthetic DNA.
   b) Discuss how your system handles potential errors or mutations in the DNA sequence.
   c) Describe any security measures to prevent unauthorized decoding.

4. Biological Implementation (150-200 words):
   a) Propose a method for synthesizing and storing the encoded DNA sequences.
   b) Discuss potential challenges in maintaining data stability over time.
   c) Suggest how your system could be integrated into living organisms as a data storage mechanism.

5. Cryptographic Analysis (150-200 words):
   a) Analyze the security of your encoding system from a cryptographic perspective.
   b) Discuss potential vulnerabilities and how they might be addressed.
   c) Compare your approach to traditional digital encryption methods.

6. Ethical and Societal Implications (200-250 words):
   a) Discuss the potential benefits and risks of DNA-based data storage.
   b) Analyze the ethical considerations of creating synthetic DNA sequences carrying complex information.
   c) Explore the potential impact on privacy, data security, and synthetic biology.

7. Future Directions (150-200 words):
   a) Propose two potential applications or extensions of your DNA cryptobiosis system.
   b) Suggest areas for further research or improvement in DNA-based data encoding.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and cryptography. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specified encoding method: {t['encoding_method']}.",
            f"The system should be designed to encode and decode the data type: {t['data_type']}.",
            f"The proposed solution must address the biological constraint: {t['biological_constraint']}.",
            "The response must include all seven required sections: System Architecture, Encoding Process, Decoding Mechanism, Biological Implementation, Cryptographic Analysis, Ethical and Societal Implications, and Future Directions.",
            "The system design should demonstrate a clear integration of principles from molecular biology, information theory, and cryptography.",
            "The encoding and decoding processes should be logically explained and scientifically plausible.",
            "The response should include thoughtful analysis of ethical implications and potential societal impacts.",
            "The proposed future directions should be innovative and relevant to the field of DNA-based data storage and synthetic biology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
