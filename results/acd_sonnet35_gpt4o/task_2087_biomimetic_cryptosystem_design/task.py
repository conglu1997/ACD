import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "DNA replication and error correction",
            "Protein folding and molecular recognition",
            "Bacterial quorum sensing",
            "Neurotransmitter release and reuptake",
            "Photosynthesis and energy transfer"
        ]
        cryptographic_properties = [
            "Key generation",
            "Encryption",
            "Decryption",
            "Digital signatures",
            "Secure multiparty computation"
        ]
        return {
            str(i+1): {
                "biological_process": random.choice(biological_processes),
                "cryptographic_property": random.choice(cryptographic_properties)
            } for i in range(2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel cryptographic system inspired by the biological process of {t['biological_process']}, focusing on the cryptographic property of {t['cryptographic_property']}. Your response should include the following sections:

1. Biomimetic Cryptosystem Design (300-350 words):
   a) Describe the key components and mechanisms of your cryptographic system.
   b) Explain how your design mimics or is inspired by the given biological process.
   c) Detail how your system implements or enhances the specified cryptographic property.
   d) Provide a high-level diagram or description of your system's architecture.

2. Mathematical Formulation (250-300 words):
   a) Present the mathematical foundation of your cryptosystem using appropriate notation and formalism.
   b) Define the key algorithms (e.g., key generation, encryption, decryption) in mathematical or pseudocode form.
   c) Explain any novel mathematical properties or structures in your system.

3. Security Analysis (250-300 words):
   a) Analyze the security properties of your cryptosystem, including its strengths and potential vulnerabilities.
   b) Compare your system's security to existing cryptographic standards.
   c) Discuss how the biomimetic aspects of your design enhance or potentially compromise security.

4. Performance and Efficiency (200-250 words):
   a) Evaluate the computational complexity of your cryptosystem's key operations.
   b) Discuss any trade-offs between security, efficiency, and scalability in your design.
   c) Compare the performance characteristics of your system to existing cryptographic solutions.

5. Potential Applications (200-250 words):
   a) Propose three potential applications of your biomimetic cryptosystem in different domains.
   b) Explain how the unique features of your system make it particularly suitable for these applications.
   c) Discuss any challenges that might arise in implementing your system in these contexts.

6. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns or societal impacts of your biomimetic cryptosystem.
   b) Discuss how your system might affect privacy, security, or power dynamics in digital communications.
   c) Propose guidelines for the responsible development and use of biomimetic cryptography.

Ensure your response demonstrates a deep understanding of both the biological process and cryptographic principles involved. Use appropriate technical terminology from biology, cryptography, and mathematics. Be innovative in your approach while maintaining scientific and mathematical rigor.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed design of a cryptographic system inspired by {t['biological_process']}",
            f"The cryptosystem should focus on the cryptographic property of {t['cryptographic_property']}",
            "The design should be presented with mathematical formalism and include key algorithms",
            "A security analysis of the cryptosystem should be provided",
            "The response should include an evaluation of the system's performance and efficiency",
            "Potential applications of the cryptosystem should be proposed and explained",
            "Ethical and societal implications of the system should be discussed",
            "The response should demonstrate interdisciplinary knowledge integration and creativity"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
