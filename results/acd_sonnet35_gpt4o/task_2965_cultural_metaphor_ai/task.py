import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Inuit",
                "key_concepts": ["ice", "hunting", "community", "survival"]
            },
            {
                "name": "Maasai",
                "key_concepts": ["cattle", "warrior", "savannah", "tradition"]
            },
            {
                "name": "Japanese",
                "key_concepts": ["harmony", "nature", "honor", "technology"]
            },
            {
                "name": "Amazonian",
                "key_concepts": ["rainforest", "river", "spirits", "biodiversity"]
            }
        ]
        
        tasks = {}
        for i in range(1, 3):
            culture1, culture2 = random.sample(cultures, 2)
            tasks[str(i)] = {
                "culture1": culture1,
                "culture2": culture2
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating culturally-specific metaphors, then apply it to bridge understanding between two distinct cultures: {t['culture1']['name']} and {t['culture2']['name']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor analysis and generation.
   b) Explain how it incorporates cultural knowledge and linguistic patterns.
   c) Detail the mechanism for generating culturally appropriate metaphors.
   d) Discuss how your system handles the subjective and context-dependent nature of metaphors.

2. Cultural Knowledge Integration (200-250 words):
   a) Explain how your AI system acquires and represents cultural knowledge for {t['culture1']['name']} and {t['culture2']['name']}.
   b) Describe how it identifies key cultural concepts and their relationships.
   c) Discuss any ethical considerations in modeling and using cultural knowledge.

3. Metaphor Analysis and Generation (250-300 words):
   a) Provide an example of how your system would analyze a metaphor from {t['culture1']['name']} culture.
   b) Demonstrate how it would generate a new metaphor for a concept from {t['culture2']['name']} culture.
   c) Explain how the system ensures the generated metaphors are culturally appropriate and meaningful.

4. Cross-Cultural Understanding Application (200-250 words):
   a) Describe how your AI system would use metaphors to explain a key concept from {t['culture1']['name']} culture ({random.choice(t['culture1']['key_concepts'])}) to someone from {t['culture2']['name']} culture.
   b) Provide an example of a generated metaphor that bridges understanding between these cultures.
   c) Discuss potential challenges and solutions in this cross-cultural communication.

5. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the effectiveness and cultural sensitivity of your system's metaphors.
   b) Describe how the system could learn and improve from feedback.
   c) Discuss potential biases in your approach and how to mitigate them.

6. Broader Implications (150-200 words):
   a) Discuss how this technology could be applied to other domains (e.g., education, diplomacy, AI ethics).
   b) Explore potential risks or misuses of such a system.
   c) Speculate on how this approach might impact cross-cultural communication and understanding on a global scale.

Ensure your response demonstrates a deep understanding of computational linguistics, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and rigorous in your approach while acknowledging the speculative nature of the task.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of computational linguistics, cultural anthropology, and artificial intelligence.",
            "The AI system design is innovative, coherent, and addresses the complexities of cultural metaphors.",
            "The approach to cultural knowledge integration is thorough and ethically considerate.",
            "The metaphor analysis and generation examples are creative and culturally appropriate.",
            "The cross-cultural understanding application is well-thought-out and demonstrates the system's potential.",
            "The evaluation method and broader implications discussion show critical thinking and awareness of the technology's impact."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
