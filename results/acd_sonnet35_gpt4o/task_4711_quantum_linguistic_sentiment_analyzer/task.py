import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_media_platforms = [
            "Twitter",
            "Facebook",
            "Instagram",
            "TikTok",
            "LinkedIn"
        ]
        linguistic_features = [
            "Semantic Entanglement",
            "Lexical Superposition",
            "Syntactic Interference",
            "Pragmatic Decoherence",
            "Morphological Tunneling"
        ]
        return {
            "1": {
                "platform": random.choice(social_media_platforms),
                "feature": random.choice(linguistic_features),
                "time_span": random.randint(1, 5)
            },
            "2": {
                "platform": random.choice(social_media_platforms),
                "feature": random.choice(linguistic_features),
                "time_span": random.randint(1, 5)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        feature_explanations = {
            "Semantic Entanglement": "the interdependence of meaning between words or phrases",
            "Lexical Superposition": "the simultaneous existence of multiple meanings for a word",
            "Syntactic Interference": "the interaction between different sentence structures",
            "Pragmatic Decoherence": "the loss of contextual meaning in communication",
            "Morphological Tunneling": "the unexpected formation of new words or meanings"
        }
        return f"""Design a quantum-inspired AI system that analyzes and predicts sentiment evolution on {t['platform']} over a period of {t['time_span']} years, focusing on the quantum linguistic feature of {t['feature']} ({feature_explanations[t['feature']]}). Your response should include:

1. Quantum Linguistic Framework (250-300 words):
   a) Explain how you interpret and apply the concept of {t['feature']} in the context of sentiment analysis.
   b) Describe how this quantum linguistic feature can be modeled mathematically.
   c) Discuss how this approach differs from classical linguistic analysis.
   d) Provide a specific example of how {t['feature']} might manifest in social media text.

2. System Architecture (300-350 words):
   a) Outline the key components of your quantum-inspired sentiment analysis system.
   b) Explain how these components integrate quantum computing principles with NLP techniques.
   c) Describe how your system processes and analyzes social media data from {t['platform']}.
   d) Include a high-level diagram or pseudocode illustrating your system's architecture.

3. Sentiment Evolution Algorithm (250-300 words):
   a) Detail your algorithm for modeling sentiment evolution using quantum linguistic principles.
   b) Explain how your algorithm incorporates the specific feature of {t['feature']}.
   c) Provide a mathematical formulation or equation representing a key aspect of your sentiment evolution model.
   d) Discuss how your algorithm handles the temporal aspect of sentiment change over {t['time_span']} years.

4. Predictive Modeling (200-250 words):
   a) Describe how your system generates predictions about future sentiment trends.
   b) Explain the advantages of your quantum-inspired approach over classical predictive models.
   c) Discuss any limitations or potential biases in your predictive modeling approach.
   d) Provide a concrete example of how your system would analyze and predict sentiment for a specific topic or event on {t['platform']}.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical concerns related to quantum-inspired sentiment analysis on social media.
   b) Discuss the potential societal impact of accurate long-term sentiment prediction.
   c) Propose guidelines for responsible development and use of such systems.

6. Future Developments (150-200 words):
   a) Suggest potential improvements or extensions to your system.
   b) Discuss how your approach could be adapted to other areas of linguistic analysis or social media research.
   c) Propose a novel research direction that could emerge from your work on quantum linguistic sentiment analysis.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and social media dynamics. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and their application to linguistics and sentiment analysis.",
            "The system architecture and algorithms are clearly explained and incorporate both quantum and linguistic concepts in a novel way.",
            "The approach to sentiment evolution modeling and prediction is innovative and scientifically plausible.",
            "Concrete examples are provided for the quantum linguistic feature and sentiment analysis on the given platform.",
            "Ethical considerations and societal impacts are thoughtfully discussed.",
            "The response is well-structured, within the specified word count, and uses appropriate terminology from all relevant fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
