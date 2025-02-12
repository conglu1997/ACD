import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language": "Japanese",
                "visual_focus": "spatial relationships",
                "scene_type": "urban landscape"
            },
            {
                "language": "Hopi",
                "visual_focus": "temporal aspects",
                "scene_type": "natural environment"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that maps between visual scenes and linguistic descriptions in {t['language']}, focusing on how this language encodes {t['visual_focus']} in a {t['scene_type']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your visual-linguistic mapping system.
   b) Explain how these components interact to process visual information and generate linguistic descriptions.
   c) Detail any novel algorithms or techniques used in your design.
   d) Discuss how your system accounts for the unique features of {t['language']} in encoding {t['visual_focus']}.

2. Visual Scene Analysis (250-300 words):
   a) Explain how your system processes and analyzes {t['scene_type']} images.
   b) Describe the methods used to identify and categorize {t['visual_focus']} within the scene.
   c) Discuss any challenges specific to analyzing {t['visual_focus']} in {t['scene_type']} and how your system addresses them.

3. Linguistic Encoding (250-300 words):
   a) Detail how your system generates linguistic descriptions of the analyzed visual scenes in {t['language']}.
   b) Explain how it captures the nuances of {t['visual_focus']} expression in {t['language']}.
   c) Provide an example of how a specific visual element would be described, highlighting unique features of {t['language']}.

4. Cross-lingual Comparison (200-250 words):
   a) Compare how your system's approach for {t['language']} differs from encoding similar information in English.
   b) Discuss any insights this comparison provides about the relationship between language and visual perception.
   c) Explain how these differences might impact machine translation or cross-cultural communication.

5. Evaluation and Testing (200-250 words):
   a) Propose methods to evaluate the accuracy and cultural authenticity of your system's visual-linguistic mappings.
   b) Describe experiments to test the system's performance with native speakers of {t['language']}.
   c) Discuss potential biases or limitations in your evaluation approach and how you'd address them.

6. Applications and Implications (150-200 words):
   a) Suggest potential applications of your system in fields such as education, cross-cultural communication, or artificial intelligence.
   b) Discuss the implications of your system for our understanding of language, culture, and visual perception.
   c) Explore any ethical considerations related to encoding cultural perspectives on visual information.

Ensure your response demonstrates a deep understanding of linguistics, computer vision, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of {t['language']} and how it encodes {t['visual_focus']}.",
            f"The system design should effectively integrate visual processing of {t['scene_type']} with linguistic encoding in {t['language']}.",
            "The cross-lingual comparison should provide insightful analysis of differences between the specified language and English.",
            "The proposed evaluation methods should be culturally sensitive and scientifically rigorous.",
            "The response should be creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
