import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "name": "Entropy",
                "description": "A measure of the average amount of information contained in a message.",
                "additional_concept": "Mutual Information"
            },
            {
                "name": "Channel Capacity",
                "description": "The maximum rate at which information can be transmitted over a communication channel.",
                "additional_concept": "Signal-to-Noise Ratio"
            }
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a new form of scientific communication based on the information theory concept of {t['name']}. Your task is to create a detailed proposal for this communication system and analyze its potential impact on scientific discourse. Additionally, you must incorporate the concept of {t['additional_concept']} into your design. Include the following in your response:\n\n1. System Design (250-300 words):\n   a) Explain how you will use {t['name']} and {t['additional_concept']} to create a new form of scientific communication.\n   b) Describe the key features and structure of your communication system.\n   c) Explain how your system differs from traditional scientific communication methods.\n   d) Propose a specific encoding method that optimizes information transfer based on these concepts.\n\n2. Information Theory Analysis (200-250 words):\n   a) Provide a detailed explanation of how your system incorporates {t['name']} and {t['additional_concept']}.\n   b) Include at least two formulas or equations that demonstrate the information theory principles behind your system.\n   c) Discuss how your system optimizes information transfer in scientific communication.\n   d) Analyze the theoretical limits and efficiency of your proposed system.\n\n3. Linguistic Aspects (150-200 words):\n   a) Describe the linguistic features of your communication system.\n   b) Explain how these features enhance scientific discourse.\n   c) Discuss any challenges in adopting this system across different languages or scientific disciplines.\n   d) Propose a method for translating between your system and traditional scientific language.\n\n4. Example Usage (100-150 words):\n   Provide a brief example of how a complex scientific concept would be communicated using your system. Choose a concept from quantum mechanics or molecular biology and demonstrate how it would be expressed.\n\n5. Potential Impact (200-250 words):\n   a) Analyze how your communication system might influence scientific research and collaboration.\n   b) Discuss potential advantages and challenges in implementing this system.\n   c) Explore possible long-term effects on scientific education and public understanding of science.\n   d) Predict how this system might evolve over time with advancements in information theory.\n\n6. Ethical Considerations (100-150 words):\n   a) Identify at least three ethical concerns raised by this new form of scientific communication.\n   b) Propose guidelines for responsible development and use of this system.\n   c) Discuss potential misuse scenarios and how they could be mitigated.\n\nEnsure your response demonstrates a deep understanding of information theory, linguistics, and scientific communication. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology throughout your answer.\n\nFormat your response with clear headings for each section. Your total response should be between 1000-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['name']} and {t['additional_concept']}, and their application to scientific communication.",
            "The proposed communication system is innovative, well-structured, and scientifically plausible.",
            "The information theory analysis includes at least two relevant formulas or equations and a clear explanation of how the system optimizes information transfer.",
            "The linguistic aspects of the system are well-considered and enhance scientific discourse.",
            "The example usage effectively demonstrates how the system would work in practice with a complex scientific concept.",
            "The potential impact analysis is comprehensive, considering both advantages and challenges, and includes predictions for future evolution.",
            "Ethical considerations are thoughtfully addressed with appropriate guidelines proposed and potential misuse scenarios discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
