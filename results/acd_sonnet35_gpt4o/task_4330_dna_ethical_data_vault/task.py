import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        data_types = [
            "personal medical records",
            "government classified documents",
            "corporate trade secrets",
            "historical archives",
            "genetic engineering protocols"
        ]
        ethical_concerns = [
            "privacy protection",
            "data integrity",
            "access control",
            "long-term stability",
            "potential for misuse"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "data_type": random.choice(data_types),
                "ethical_concern": random.choice(ethical_concerns)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a DNA-based data storage system with built-in ethical safeguards for storing and protecting sensitive information. Your system should specifically address the storage of {t['data_type']} while focusing on the ethical concern of {t['ethical_concern']}. Your response should include the following sections:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your DNA-based data storage system.\n   b) Explain how your system encodes and stores information using DNA.\n   c) Detail the mechanisms for data retrieval and decoding.\n   d) Discuss how your system addresses the specified ethical concern.\n\n2. DNA Encoding Schema (250-300 words):\n   a) Present your method for encoding digital information into DNA sequences.\n   b) Explain how your encoding ensures data integrity and error correction.\n   c) Discuss any novel approaches or optimizations in your encoding method.\n   d) Provide a small example of how a piece of data would be encoded (using ASCII art if necessary).\n\n3. Ethical Safeguards (250-300 words):\n   a) Describe the specific ethical safeguards built into your system.\n   b) Explain how these safeguards address the given ethical concern.\n   c) Discuss any potential ethical dilemmas that may arise from your system and how you propose to resolve them.\n   d) Consider the long-term ethical implications of DNA-based data storage.\n\n4. Security and Access Control (200-250 words):\n   a) Detail the security measures implemented in your system.\n   b) Explain your approach to access control and user authentication.\n   c) Discuss how your system protects against unauthorized access or tampering.\n   d) Address potential vulnerabilities and how they are mitigated.\n\n5. Practical Implementation (200-250 words):\n   a) Describe the laboratory processes required for writing and reading data in your system.\n   b) Discuss scalability and cost considerations for practical deployment.\n   c) Address challenges in long-term storage and preservation of DNA-encoded data.\n   d) Propose a method for indexing and quickly accessing specific data within the DNA storage system.\n\n6. Future Implications and Research Directions (150-200 words):\n   a) Discuss potential applications and impacts of your DNA-based data storage system.\n   b) Propose two future research directions to enhance or expand your system.\n   c) Consider potential societal and ethical impacts of widespread adoption of DNA data storage.\n\nEnsure your response demonstrates a deep understanding of molecular biology, information theory, cryptography, and bioethics. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words. Include at least one citation or reference to support your design, using a consistent citation format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of DNA-based data storage systems and their potential for storing {t['data_type']}",
            f"The proposed system effectively addresses the ethical concern of {t['ethical_concern']}",
            "The DNA encoding schema is well-explained and scientifically plausible",
            "The ethical safeguards are thoughtfully designed and address potential issues comprehensively",
            "The security and access control measures are robust and well-considered",
            "The practical implementation details are realistic and address key challenges",
            "The discussion of future implications and research directions is insightful and forward-thinking",
            "The response includes at least one relevant citation or reference to support the design",
            "The proposed solution demonstrates originality and innovation in its approach",
            "The response meets the required word count of 1350-1650 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
