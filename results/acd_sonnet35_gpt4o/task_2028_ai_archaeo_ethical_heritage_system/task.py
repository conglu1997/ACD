import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artifact_types = [
            "Ancient manuscripts",
            "Prehistoric cave paintings",
            "Indigenous oral traditions",
            "Historical architectural sites"
        ]
        ai_techniques = [
            "Computer vision",
            "Natural language processing",
            "3D reconstruction",
            "Knowledge graph construction"
        ]
        ethical_considerations = [
            "Cultural ownership and repatriation",
            "Privacy of indigenous knowledge",
            "Bias in AI interpretations",
            "Accessibility and democratization of knowledge"
        ]
        return {
            "1": {
                "artifact": random.choice(artifact_types),
                "ai_technique": random.choice(ai_techniques),
                "ethical_issue": random.choice(ethical_considerations)
            },
            "2": {
                "artifact": random.choice(artifact_types),
                "ai_technique": random.choice(ai_techniques),
                "ethical_issue": random.choice(ethical_considerations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for preserving and interpreting {t['artifact']}, using {t['ai_technique']} as a key component. Address the ethical consideration of {t['ethical_issue']} in your design. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system for cultural heritage preservation and interpretation.
   b) Explain how {t['ai_technique']} is integrated into the system and its role in analyzing {t['artifact']}.
   c) Detail other AI or computational techniques used in your system and their functions.
   d) Discuss how your system ensures the accuracy and reliability of its interpretations.

2. Archaeological Integration (200-250 words):
   a) Explain how your AI system incorporates established archaeological principles and methodologies.
   b) Describe how the system would interact with or assist human archaeologists.
   c) Discuss any novel approaches your system brings to the field of archaeology.
   d) Address potential challenges in applying AI to {t['artifact']} and how your system overcomes them.

3. Ethical Framework (200-250 words):
   a) Propose a comprehensive ethical framework for your AI system, with particular focus on {t['ethical_issue']}.
   b) Discuss how your system balances the benefits of AI-driven interpretation with respect for cultural sensitivities.
   c) Describe safeguards or oversight mechanisms to prevent misuse or misinterpretation of cultural heritage.
   d) Explain how your system addresses issues of data ownership, privacy, and access.

4. Cultural Sensitivity and Bias Mitigation (150-200 words):
   a) Describe how your AI system is designed to be culturally sensitive and respectful.
   b) Explain techniques used to identify and mitigate potential biases in the AI's interpretations.
   c) Discuss how the system incorporates diverse cultural perspectives in its analysis.

5. Practical Application (150-200 words):
   a) Provide a specific example of how your system would be applied to a real-world scenario involving {t['artifact']}.
   b) Describe the potential impact of your system on the field of archaeology and cultural heritage preservation.
   c) Discuss any limitations of your approach and areas for future development.

Ensure your response demonstrates a deep understanding of AI technologies, archaeological principles, and ethical considerations in cultural heritage preservation. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and ethical integrity.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system architecture that effectively incorporates {t['ai_technique']} for analyzing {t['artifact']}.",
            "The system demonstrates a strong integration of archaeological principles with AI technologies.",
            f"The ethical framework comprehensively addresses {t['ethical_issue']} and other relevant ethical considerations.",
            "The response shows a nuanced understanding of cultural sensitivity and bias mitigation in AI systems.",
            "The practical application example is relevant and demonstrates the potential impact of the system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
