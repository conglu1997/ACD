import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "time",
            "love",
            "power",
            "knowledge",
            "life",
            "death"
        ]
        cultures = [
            "Western",
            "East Asian",
            "Middle Eastern",
            "African",
            "South Asian",
            "Latin American"
        ]
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice([c for c in cultures if c != cultures[-1]])
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice([c for c in cultures if c != cultures[-1]])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and generates conceptual metaphors across different cultures, then use it to translate the abstract concept of {t['concept']} from {t['source_culture']} culture to {t['target_culture']} culture. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the components of your AI system for analyzing and generating cross-cultural conceptual metaphors.
   b) Explain how the system processes and represents cultural knowledge.
   c) Detail the method for identifying and extracting conceptual metaphors from cultural data.
   d) Discuss how the system generates new conceptual metaphors appropriate to a target culture.

2. Conceptual Metaphor Analysis (200-250 words):
   a) Analyze common conceptual metaphors for {t['concept']} in {t['source_culture']} culture.
   b) Explain how these metaphors reflect the cultural values, beliefs, or experiences of the {t['source_culture']} culture.
   c) Discuss any challenges in computationally representing these metaphors.
   d) Provide at least two specific examples of conceptual metaphors for {t['concept']} in {t['source_culture']} culture.

3. Cross-Cultural Translation (250-300 words):
   a) Using your AI system, generate at least three conceptual metaphors for {t['concept']} appropriate to the {t['target_culture']} culture.
   b) Explain how these generated metaphors capture the essence of the concept while being culturally appropriate.
   c) Discuss any adaptations or transformations made to the original metaphors during the translation process.
   d) Provide a step-by-step explanation of how your system arrived at one of the generated metaphors.

4. Cognitive Linguistic Analysis (200-250 words):
   a) Compare and contrast the conceptual metaphors from the source and target cultures.
   b) Analyze how differences in these metaphors might reflect differences in cognitive patterns or worldviews.
   c) Discuss the implications of these differences for cross-cultural communication and understanding.
   d) Propose a hypothesis about how these metaphorical differences might influence behavior or decision-making in each culture.

5. Evaluation and Ethical Considerations (200-250 words):
   a) Propose a method for evaluating the cultural authenticity and effectiveness of your system's generated metaphors.
   b) Discuss potential biases or limitations in your system and how they might be addressed.
   c) Explore ethical considerations in using AI to analyze and generate cultural metaphors.
   d) Suggest guidelines for the responsible development and use of cross-cultural AI systems.

Ensure your response demonstrates a deep understanding of cognitive linguistics, cultural anthropology, and AI technologies. Be innovative in your approach while maintaining scientific and cultural sensitivity. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual metaphors and their cultural significance",
            "The proposed AI system is innovative and scientifically plausible",
            f"The analysis of conceptual metaphors for {t['concept']} in {t['source_culture']} culture is thorough and insightful, with at least two specific examples provided",
            f"At least three appropriate conceptual metaphors for {t['concept']} are generated for the {t['target_culture']} culture, with a step-by-step explanation for one",
            "The cognitive linguistic analysis effectively compares and contrasts the metaphors from different cultures, including a hypothesis about behavioral implications",
            "The evaluation method and ethical considerations are well-thought-out and relevant, including suggested guidelines for responsible AI development",
            "The response shows cultural sensitivity and awareness throughout",
            "The response is well-structured, following the numbered format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
