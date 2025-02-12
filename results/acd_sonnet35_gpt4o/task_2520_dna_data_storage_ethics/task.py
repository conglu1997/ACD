import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        data_types = [
            "medical records",
            "financial information",
            "personal memories",
            "biometric data"
        ]
        ethical_concerns = [
            "privacy and data protection",
            "consent and ownership",
            "long-term stability and access",
            "potential for misuse or weaponization"
        ]
        return {
            "1": {
                "data_type": random.choice(data_types),
                "ethical_concern": random.choice(ethical_concerns)
            },
            "2": {
                "data_type": random.choice(data_types),
                "ethical_concern": random.choice(ethical_concerns)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a DNA-based information storage system for {t['data_type']} and analyze its ethical implications, focusing on the concern of {t['ethical_concern']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your DNA-based storage system.
   b) Explain the encoding method for converting {t['data_type']} into DNA sequences.
   c) Discuss data retrieval and error correction mechanisms.
   d) Address how your system ensures data integrity and security.
   e) Provide a specific example of how a piece of {t['data_type']} would be encoded and stored in your system.

2. Molecular Biology Principles (200-250 words):
   a) Explain the relevant principles of DNA structure and replication.
   b) Discuss how your system leverages or mimics natural biological processes.
   c) Address potential biological constraints or limitations.
   d) Describe at least one novel approach to overcome a biological limitation.

3. Information Theory Analysis (200-250 words):
   a) Analyze the information density and capacity of your DNA storage system.
   b) Compare its efficiency to traditional digital storage methods.
   c) Discuss error rates and data longevity considerations.
   d) Provide a quantitative comparison of storage density between your system and current electronic storage.

4. Ethical Implications (250-300 words):
   a) Analyze the ethical concerns related to {t['ethical_concern']} in the context of DNA-based storage of {t['data_type']}.
   b) Discuss potential societal impacts and legal considerations.
   c) Propose ethical guidelines for the development and use of this technology.
   d) Present a case study illustrating a potential ethical dilemma and your proposed resolution.

5. Security and Privacy Measures (200-250 words):
   a) Describe encryption or obfuscation techniques for protecting the stored data.
   b) Discuss access control mechanisms and potential vulnerabilities.
   c) Address concerns about unauthorized DNA sequencing or data extraction.
   d) Propose a novel security measure specifically designed for DNA-based data storage.

6. Future Implications and Challenges (150-200 words):
   a) Speculate on potential future applications or advancements in DNA-based data storage.
   b) Discuss challenges that need to be overcome for widespread adoption.
   c) Consider long-term societal and evolutionary implications of storing human data in biological substrates.
   d) Propose a research agenda to address the most critical challenges you've identified.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and bioethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of DNA structure and molecular biology principles, including a novel approach to overcome a biological limitation.",
            "The proposed DNA-based storage system is innovative yet scientifically plausible, with a specific example of data encoding provided.",
            "The information theory analysis is thorough, includes a quantitative comparison, and compares the system to traditional storage methods.",
            f"The ethical implications, particularly regarding {t['ethical_concern']}, are thoroughly analyzed with a relevant case study.",
            "The security and privacy measures are well-thought-out, address potential vulnerabilities, and include a novel security measure specific to DNA-based storage.",
            "The response shows interdisciplinary knowledge integration across biology, information theory, and ethics, with a proposed research agenda for future challenges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
