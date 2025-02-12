import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_theories = [
            {"name": "Conceptual Metaphor Theory", "proponent": "Lakoff and Johnson"},
            {"name": "Frame Semantics", "proponent": "Charles J. Fillmore"},
            {"name": "Construction Grammar", "proponent": "Adele Goldberg"},
            {"name": "Cognitive Grammar", "proponent": "Ronald Langacker"},
            {"name": "Mental Spaces Theory", "proponent": "Gilles Fauconnier"}
        ]
        ai_applications = [
            "Natural Language Understanding",
            "Machine Translation",
            "Sentiment Analysis",
            "Dialogue Systems",
            "Knowledge Representation"
        ]
        return {
            "1": {"theory": random.choice(cognitive_theories), "application": random.choice(ai_applications)},
            "2": {"theory": random.choice(cognitive_theories), "application": random.choice(ai_applications)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI architecture inspired by the cognitive linguistics theory of {t['theory']['name']} (proposed by {t['theory']['proponent']}) and analyze its potential impact on {t['application']} and artificial general intelligence (AGI). Your response should include:

1. Theoretical Foundation (200-250 words):
   a) Explain the key principles of {t['theory']['name']}.
   b) Discuss how this theory relates to human cognition and language processing.
   c) Identify aspects of the theory that could be particularly relevant to AI development.

2. AI Architecture Design (300-350 words):
   a) Propose an AI architecture that incorporates the principles of {t['theory']['name']}.
   b) Describe the key components of your architecture and their functions.
   c) Explain how your design mimics or adapts cognitive processes suggested by the theory.
   d) Discuss how this architecture could be implemented using current AI technologies.

3. Application to {t['application']} (250-300 words):
   a) Explain how your AI architecture could improve or revolutionize {t['application']}.
   b) Provide a specific example or use case demonstrating the potential advantages of your approach.
   c) Discuss any challenges or limitations in applying your architecture to this domain.

4. Implications for AGI (200-250 words):
   a) Analyze how your cognitive linguistics-inspired architecture might contribute to the development of AGI.
   b) Discuss potential advantages and limitations of this approach compared to current AGI strategies.
   c) Speculate on how this architecture might handle general problem-solving and learning tasks.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical implications or risks associated with your proposed AI architecture.
   b) Suggest guidelines or safeguards for responsible development and deployment of such systems.
   c) Discuss how this approach might impact our understanding of machine consciousness or intelligence.

6. Future Research Directions (150-200 words):
   a) Propose two specific research questions or experiments to further explore the potential of your architecture.
   b) Suggest potential collaborations between cognitive linguists and AI researchers that could advance this field.

Ensure your response demonstrates a deep understanding of both cognitive linguistics and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing potential limitations or challenges.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of {t['theory']['name']} and its relevance to AI development.",
            f"The proposed AI architecture should creatively incorporate principles from {t['theory']['name']}.",
            f"The application to {t['application']} should be well-explained with specific examples or use cases.",
            "The implications for AGI should be thoughtfully analyzed, considering both potential advantages and limitations.",
            "Ethical considerations and future research directions should be addressed comprehensively.",
            "The overall response should be well-structured, coherent, and demonstrate interdisciplinary knowledge synthesis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
