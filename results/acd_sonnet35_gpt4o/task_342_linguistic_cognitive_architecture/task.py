import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "ergative-absolutive alignment",
            "evidentiality markers",
            "logographic writing system",
            "tonal phonology",
            "polysynthetic morphology"
        ]
        cognitive_domains = [
            "spatial reasoning",
            "temporal cognition",
            "social intelligence",
            "causal inference",
            "metaphorical thinking"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_domain": random.choice(cognitive_domains)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_domain": random.choice(cognitive_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical cognitive architecture for an AI system based on the linguistic feature of {t['linguistic_feature']} and focused on the cognitive domain of {t['cognitive_domain']}. Your response should include:

1. Linguistic Feature Analysis (150-200 words):
   a) Explain the given linguistic feature and its significance in human languages.
   b) Discuss how this feature might influence cognition in speakers of languages that have it.

2. Cognitive Domain Overview (150-200 words):
   a) Describe the specified cognitive domain and its importance in human intelligence.
   b) Explain how this domain is typically implemented in traditional AI systems.

3. Cognitive Architecture Design (250-300 words):
   a) Propose a novel cognitive architecture that integrates the linguistic feature into the specified cognitive domain.
   b) Describe the key components and processes of your architecture.
   c) Explain how your design differs from traditional AI approaches to this cognitive domain.

4. Operational Example (200-250 words):
   a) Provide a specific example of how your cognitive architecture would process information or solve a problem.
   b) Walk through the steps of operation, highlighting how the linguistic feature influences the cognitive process.

5. Implications for AI Development (200-250 words):
   a) Discuss potential advantages of your architecture for AI systems in terms of performance, adaptability, or capabilities.
   b) Analyze possible challenges or limitations in implementing your architecture.
   c) Propose a research agenda to further explore and develop your ideas.

6. Broader Impact Analysis (150-200 words):
   a) Speculate on how widespread adoption of your cognitive architecture might influence AI research and development.
   b) Discuss potential ethical considerations or societal impacts of AI systems using your architecture.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cognitive architecture must be based on the linguistic feature of {t['linguistic_feature']} and focused on the cognitive domain of {t['cognitive_domain']}.",
            "The response must include a clear analysis of the given linguistic feature and its potential influence on cognition.",
            "An overview of the specified cognitive domain and its implementation in traditional AI systems must be provided.",
            "The proposed cognitive architecture must integrate the linguistic feature into the cognitive domain in a novel and plausible way.",
            "A specific operational example of the cognitive architecture must be provided, demonstrating how it processes information or solves a problem.",
            "The implications for AI development, including potential advantages and challenges, must be discussed.",
            "A broader impact analysis, including potential ethical considerations and societal impacts, must be included.",
            "The response must demonstrate a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The response must be creative while maintaining scientific plausibility.",
            "The response must be formatted with clear headings for each section and numbered paragraphs within each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
