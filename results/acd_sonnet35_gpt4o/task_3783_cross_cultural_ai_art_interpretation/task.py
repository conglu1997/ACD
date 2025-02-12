import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture1': 'Japanese',
                'culture2': 'Mexican',
                'art_style': 'Surrealism'
            },
            {
                'culture1': 'Indian',
                'culture2': 'Nigerian',
                'art_style': 'Abstract Expressionism'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can interpret and generate visual art based on cultural contexts, then use it to analyze and create artworks that bridge {t['culture1']} and {t['culture2']} cultures in the style of {t['art_style']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cultural art interpretation and generation.
   b) Explain how your system integrates cultural knowledge, art history, and visual processing.
   c) Detail how your system generates new artworks that combine elements from different cultures.
   d) Provide a diagram or flowchart of your system's architecture (describe it textually).

2. Cultural Art Analysis (250-300 words):
   a) Explain how your system would analyze and interpret artworks from {t['culture1']} and {t['culture2']} cultures.
   b) Discuss the key visual elements, symbols, and themes your system would identify in each culture's art.
   c) Describe how your system recognizes and interprets the characteristics of {t['art_style']}.

3. Cross-Cultural Art Generation (250-300 words):
   a) Detail the process your AI system would use to create a new artwork that combines elements from {t['culture1']} and {t['culture2']} cultures in the style of {t['art_style']}.
   b) Explain how your system ensures cultural authenticity while creating a novel piece.
   c) Describe a hypothetical artwork your system might generate, including its visual elements and symbolic meaning.

4. Ethical and Cultural Considerations (200-250 words):
   a) Discuss potential ethical issues in AI-generated art that combines elements from different cultures.
   b) Explain how your system addresses concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of AI in cross-cultural art creation.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the cultural accuracy and artistic quality of your system's outputs.
   b) Describe how you would measure the system's ability to meaningfully combine different cultural elements.
   c) Discuss the challenges in evaluating AI-generated cross-cultural art and how you'd address them.

6. Future Applications and Research Directions (150-200 words):
   a) Suggest two potential applications of your system in fields such as education, cultural preservation, or creative industries.
   b) Propose a related research question that could further explore the intersection of AI, art, and cultural understanding.

Ensure your response demonstrates a deep understanding of art history, cultural symbolism, and AI-based image generation techniques. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of art history, cultural symbolism, and AI-based image generation techniques.",
            "The system architecture is well-explained and effectively integrates cultural knowledge, art history, and visual processing.",
            "The cultural art analysis and cross-cultural art generation processes are thoroughly described and culturally sensitive.",
            "Ethical and cultural considerations are comprehensively discussed with insightful guidelines proposed.",
            "The evaluation and validation methods are well-reasoned and address the challenges of assessing AI-generated cross-cultural art.",
            "Future applications and research directions are creative and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
