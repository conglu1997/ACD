import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        legal_systems = [
            "Common Law",
            "Civil Law",
            "Religious Law",
            "Customary Law"
        ]
        ethical_principles = [
            "Utilitarianism",
            "Deontology",
            "Virtue Ethics",
            "Care Ethics"
        ]
        return {
            "1": {"legal_system": random.choice(legal_systems), "ethical_principle": random.choice(ethical_principles)},
            "2": {"legal_system": random.choice(legal_systems), "ethical_principle": random.choice(ethical_principles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze legal language, predict judicial decisions, and evaluate ethical implications in the context of the {t['legal_system']} system, while considering the ethical framework of {t['ethical_principle']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for analyzing legal language and predicting judicial decisions.
   b) Explain how your system incorporates cultural and linguistic nuances specific to the given legal system.
   c) Detail how the system integrates the specified ethical framework into its analysis and decision-making processes.

2. Legal Language Analysis (200-250 words):
   a) Explain how your AI system processes and interprets legal texts and precedents.
   b) Describe any novel NLP techniques your system uses to handle the complexities of legal language.
   c) Discuss how your system accounts for cultural context and linguistic variations in legal terminology.

3. Judicial Decision Prediction (200-250 words):
   a) Detail the approach your AI uses to predict judicial decisions based on case information and legal precedents.
   b) Explain how your system handles uncertainty and conflicting precedents.
   c) Describe a method for evaluating the accuracy and fairness of your system's predictions.

4. Ethical Evaluation (200-250 words):
   a) Explain how your system applies the given ethical framework to evaluate the implications of legal decisions.
   b) Describe how your AI identifies and analyzes potential ethical dilemmas in legal cases.
   c) Discuss how your system balances legal precedent with ethical considerations.

5. Cross-cultural Application (150-200 words):
   a) Explain how your system could be adapted to work across different legal systems and cultures.
   b) Discuss potential challenges in applying your system globally and how they might be addressed.

6. Limitations and Safeguards (150-200 words):
   a) Identify potential biases or limitations in your AI system.
   b) Propose safeguards to ensure the ethical use of your system in real-world legal contexts.
   c) Discuss the implications of using AI in legal decision-making processes.

Ensure your response demonstrates a deep understanding of legal systems, linguistic analysis, ethical frameworks, and AI technologies. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and legal plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly address the {t['legal_system']} system and incorporate the ethical framework of {t['ethical_principle']}.",
            "The proposed AI system should demonstrate a novel approach to legal language analysis and judicial decision prediction.",
            "The response should show a deep understanding of the complexities and cultural nuances in legal systems.",
            "The ethical evaluation component should be well-integrated and thoughtfully considered.",
            "The response should address all six requested sections adequately.",
            "The proposed system should have clear practical applications while acknowledging limitations and ethical concerns."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
