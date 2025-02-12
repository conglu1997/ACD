import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_forms = [
            {
                "traditional_art": "Japanese Ukiyo-e woodblock prints",
                "contemporary_medium": "Digital art",
                "cultural_theme": "Urban life in the 21st century"
            },
            {
                "traditional_art": "West African Adinkra symbols",
                "contemporary_medium": "Generative art",
                "cultural_theme": "Global interconnectedness"
            }
        ]
        return {
            "1": random.choice(art_forms),
            "2": random.choice(art_forms)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze, preserve, and innovate traditional art forms from diverse cultures, creating new artistic expressions while respecting cultural heritage. Apply your system to the following scenario:

Traditional Art Form: {t['traditional_art']}
Contemporary Medium: {t['contemporary_medium']}
Cultural Theme to Explore: {t['cultural_theme']}

Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for analyzing and synthesizing art.
   b) Explain how your system integrates knowledge of traditional art forms, cultural contexts, and contemporary artistic techniques.
   c) Detail the AI techniques used for artistic analysis, generation, and evaluation.
   d) Discuss how your system ensures cultural sensitivity and authenticity in its creations.

2. Traditional Art Analysis (200-250 words):
   a) Explain how your AI system analyzes and understands the traditional art form.
   b) Describe the key features, techniques, and cultural significance it would identify.
   c) Discuss how the system preserves and represents this knowledge.

3. Artistic Synthesis Process (250-300 words):
   a) Detail the step-by-step process your AI uses to create new art.
   b) Explain how it combines traditional elements with the contemporary medium.
   c) Describe how the system incorporates the specified cultural theme.
   d) Provide an example of a potential artistic output from your system.

4. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of using AI to innovate traditional art forms.
   b) Address issues of cultural appropriation, authenticity, and artistic ownership.
   c) Propose guidelines for responsible AI art creation that respects cultural heritage.

5. Evaluation and Feedback (150-200 words):
   a) Describe how your system evaluates the quality and cultural authenticity of its creations.
   b) Explain how feedback from artists, cultural experts, and audiences could be incorporated.
   c) Discuss potential methods for continuous learning and improvement of the AI system.

6. Societal Impact and Applications (150-200 words):
   a) Explore potential applications of your AI system in art education, cultural preservation, or cross-cultural understanding.
   b) Discuss how this technology might influence the future of art and cultural expression.
   c) Consider potential risks or challenges of widespread adoption of AI in traditional arts.

Ensure your response demonstrates a deep understanding of the specified art forms, cultural sensitivity, and AI technologies. Be creative and innovative in your approach while maintaining respect for cultural traditions. Use appropriate terminology from both art and AI domains, providing clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['traditional_art']} and its cultural significance.",
            f"The AI system effectively integrates {t['traditional_art']} with {t['contemporary_medium']} while exploring the theme of {t['cultural_theme']}.",
            "The approach shows creativity and innovation while maintaining respect for cultural traditions.",
            "The ethical considerations are thoroughly addressed, including issues of cultural appropriation and authenticity.",
            "The response provides a clear and technically sound explanation of the AI system's architecture and processes.",
            "The potential societal impacts and applications of the AI system are thoughtfully explored."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
