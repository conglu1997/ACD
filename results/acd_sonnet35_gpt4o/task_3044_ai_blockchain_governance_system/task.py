import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        governance_aspects = [
            "Decision-making processes",
            "Resource allocation",
            "Conflict resolution",
            "Policy implementation",
            "Citizen participation"
        ]
        societal_challenges = [
            "Economic inequality",
            "Environmental sustainability",
            "Technological unemployment",
            "Privacy and data rights",
            "Global cooperation"
        ]
        return {
            "1": {"aspect": random.choice(governance_aspects), "challenge": random.choice(societal_challenges)},
            "2": {"aspect": random.choice(governance_aspects), "challenge": random.choice(societal_challenges)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a novel governance system using advanced AI and blockchain technology for a future society, focusing on the aspect of {t['aspect']}. Then, propose solutions to address the societal challenge of {t['challenge']}. Your response should include:

1. Governance System Design (300-350 words):
   a) Describe the overall structure and key components of your AI-blockchain governance system.
   b) Explain how AI and blockchain technologies are integrated to handle {t['aspect']}.
   c) Detail the mechanisms for ensuring transparency, security, and fairness in the system.
   d) Discuss how your system balances automation with human oversight and input.

2. Technical Implementation (250-300 words):
   a) Outline the specific AI algorithms or models used in your governance system.
   b) Describe the blockchain architecture and consensus mechanism employed.
   c) Explain how data is collected, processed, and stored in your system.
   d) Address potential technical challenges and propose solutions.

3. Societal Impact Analysis (200-250 words):
   a) Analyze the potential positive and negative impacts of your governance system on society.
   b) Discuss how it might affect existing power structures and social dynamics.
   c) Explain how your system promotes or challenges democratic values.

4. Ethical Considerations (200-250 words):
   a) Identify three key ethical issues raised by your governance system.
   b) Analyze these issues using one ethical framework (e.g., utilitarianism, deontology, virtue ethics).
   c) Propose safeguards or guidelines to address these ethical concerns.

5. Addressing {t['challenge']} (250-300 words):
   a) Explain how your governance system could be applied to address the challenge of {t['challenge']}.
   b) Propose a specific policy or initiative using your system to tackle this issue.
   c) Discuss potential obstacles in implementing your solution and how to overcome them.

6. Future Implications and Adaptability (150-200 words):
   a) Discuss how your governance system might evolve over time.
   b) Explain how it could adapt to unforeseen future challenges.
   c) Propose a method for evaluating and improving the system's effectiveness.

Ensure your response demonstrates a deep understanding of AI, blockchain technology, political systems, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering practical implications and potential consequences.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI and blockchain technologies and their potential applications in governance.",
            f"The governance system design effectively addresses the aspect of {t['aspect']} using AI and blockchain.",
            "The technical implementation is well-explained and addresses potential challenges.",
            "The societal impact analysis is thoughtful and considers both positive and negative consequences.",
            "The ethical analysis is thorough and proposes meaningful safeguards or guidelines.",
            f"The proposed solution for addressing {t['challenge']} is innovative and well-reasoned.",
            "The response shows creativity and interdisciplinary knowledge integration throughout.",
            "The writing is clear, well-structured, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
