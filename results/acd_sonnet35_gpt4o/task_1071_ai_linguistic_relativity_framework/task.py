import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            "Hopi",
            "Guugu Yimithirr",
            "Pirahã",
            "Klingon",
            "Lojban"
        ]
        cognitive_domains = [
            "temporal reasoning",
            "spatial orientation",
            "color perception",
            "logical inference",
            "emotional processing"
        ]
        ai_applications = [
            "natural language processing",
            "computer vision",
            "decision making",
            "creative generation",
            "multi-agent systems"
        ]
        return {
            "1": {
                "language": random.choice(languages),
                "cognitive_domain": random.choice(cognitive_domains),
                "ai_application": random.choice(ai_applications)
            },
            "2": {
                "language": random.choice(languages),
                "cognitive_domain": random.choice(cognitive_domains),
                "ai_application": random.choice(ai_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can dynamically alter its cognitive processes based on the language it operates in, focusing on the language {t['language']}, the cognitive domain of {t['cognitive_domain']}, and the AI application of {t['ai_application']}. Then, analyze the implications for AI development and cross-lingual AI capabilities. Your response should include the following sections:

1. Linguistic Analysis (200-250 words):
   a) Briefly describe the key features of {t['language']} relevant to {t['cognitive_domain']}.
   b) Explain how these features might influence cognition according to the linguistic relativity hypothesis.
   c) Discuss any existing research or examples that support or challenge this influence.

2. AI System Design (300-350 words):
   a) Propose an AI architecture that can adapt its cognitive processes based on the language it operates in.
   b) Explain how your system would alter its {t['cognitive_domain']} processes when using {t['language']}.
   c) Describe the key components and mechanisms that enable this language-dependent cognitive flexibility.
   d) Discuss how this adaptive cognition would be implemented in the context of {t['ai_application']}.

3. Implementation Approach (250-300 words):
   a) Outline the main algorithms or computational techniques you would use in your AI system.
   b) Explain how you would represent and process linguistic features that influence cognition.
   c) Describe how you would measure or evaluate the system's cognitive adaptations.
   d) Provide a short pseudocode snippet (10-15 lines) illustrating a crucial part of your implementation.

4. Implications and Analysis (250-300 words):
   a) Discuss the potential benefits and risks of AI systems with language-dependent cognition.
   b) Analyze how this approach might impact the development of multilingual AI systems.
   c) Explore the ethical considerations of AI systems that may 'think differently' in different languages.
   d) Speculate on how this technology could influence our understanding of human cognition and linguistic relativity.

5. Challenges and Future Directions (200-250 words):
   a) Identify the main technical and theoretical challenges in implementing your proposed system.
   b) Suggest potential solutions or research directions to address these challenges.
   c) Propose two novel experiments or applications that could further explore the implications of your AI system.

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['language']} and its potential influence on {t['cognitive_domain']}.",
            f"The AI system design effectively incorporates language-dependent cognitive adaptations for {t['ai_application']}.",
            "The implementation approach is technically sound and innovative.",
            "The analysis of implications is thorough and considers multiple perspectives.",
            "The response shows creativity and interdisciplinary thinking throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
