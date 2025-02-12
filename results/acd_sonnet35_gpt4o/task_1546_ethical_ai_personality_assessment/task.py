import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        personality_theories = [
            "Big Five",
            "Myers-Briggs Type Indicator",
            "Enneagram",
            "Hexaco model",
            "16 Personality Factor Questionnaire"
        ]
        application_domains = [
            "employment screening",
            "mental health diagnosis",
            "dating app matchmaking",
            "educational personalization",
            "criminal justice risk assessment"
        ]
        return {
            "1": {
                "personality_theory": random.choice(personality_theories),
                "application_domain": random.choice(application_domains)
            },
            "2": {
                "personality_theory": random.choice(personality_theories),
                "application_domain": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical AI system for personality assessment based on the {t['personality_theory']} theory, to be applied in the domain of {t['application_domain']}. Your response should include:

1. System Design (250-300 words):
   a) Describe the key components and functioning of your AI personality assessment system.
   b) Explain how it incorporates principles from the {t['personality_theory']} theory.
   c) Detail the data collection methods and analysis techniques used by the system.
   d) Discuss how the system would present results and recommendations.

2. Technical Implementation (200-250 words):
   a) Outline the AI/ML techniques you would use to implement this system (e.g., natural language processing, computer vision, machine learning algorithms).
   b) Explain how these techniques would work together to assess personality.
   c) Discuss any novel or innovative approaches in your implementation.

3. Ethical Analysis (250-300 words):
   a) Identify and analyze at least three potential ethical issues raised by your system.
   b) Discuss how these issues might be particularly relevant in the context of {t['application_domain']}.
   c) Propose safeguards or guidelines to address these ethical concerns.

4. Accuracy and Validity (200-250 words):
   a) Discuss potential challenges in ensuring the accuracy and validity of your system's assessments.
   b) Propose methods for validating the system's results against traditional assessment methods.
   c) Analyze potential biases in your system and how they might be mitigated.

5. Societal Impact (200-250 words):
   a) Analyze potential positive and negative societal impacts of widespread adoption of your system.
   b) Discuss how it might change practices or decision-making in the field of {t['application_domain']}.
   c) Consider long-term implications for privacy, individual autonomy, and social dynamics.

6. Future Developments (150-200 words):
   a) Propose one potential future enhancement or expansion of your system.
   b) Discuss how emerging technologies or new research in psychology might influence the evolution of AI personality assessment systems.

Ensure your response demonstrates a deep understanding of psychological theories, AI technologies, and ethical reasoning. Be creative in your system design while maintaining scientific plausibility and addressing real-world constraints. Use appropriate terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system must be based on the {t['personality_theory']} theory and applied to {t['application_domain']}.",
            "The response must include a clear system design with key components and functioning explained.",
            "Technical implementation details, including AI/ML techniques, must be outlined.",
            "At least three potential ethical issues must be identified and analyzed.",
            "Challenges in ensuring accuracy and validity must be discussed, along with proposed validation methods.",
            "Potential societal impacts of widespread adoption must be analyzed.",
            "A future enhancement or expansion of the system must be proposed.",
            "The response must demonstrate understanding of psychological theories, AI technologies, and ethical reasoning.",
            "The response must be creative while maintaining scientific plausibility.",
            "The response must be formatted with clear headings and adhere to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
