import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "Schadenfreude",
            "Saudade",
            "Hygge",
            "Wabi-sabi",
            "Yugen",
            "Duende"
        ]
        art_styles = [
            "Cubism",
            "Abstract Expressionism",
            "Surrealism",
            "Minimalism",
            "Color Field Painting",
            "Geometric Abstraction"
        ]
        cultures = [
            "Japanese",
            "Brazilian",
            "Egyptian",
            "Finnish",
            "Indian",
            "Maori"
        ]
        tasks = [
            {
                "emotion": random.choice(emotions),
                "art_style": random.choice(art_styles),
                "target_culture": random.choice(cultures)
            },
            {
                "emotion": random.choice(emotions),
                "art_style": random.choice(art_styles),
                "target_culture": random.choice(cultures)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates the complex human emotional state of {t['emotion']} into an abstract art representation in the style of {t['art_style']}, considering the perception and expression of this emotion in {t['target_culture']} culture. Your response should include the following sections, clearly labeled and within the specified word limits:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system processes emotional input and generates abstract art output.
   c) Detail how cultural context is incorporated into the system's decision-making process.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Emotional-Visual Translation Mechanism (200-250 words):
   a) Explain how your system translates {t['emotion']} into visual elements (e.g., color, shape, texture).
   b) Describe how the system incorporates {t['art_style']} principles in its output.
   c) Discuss any novel algorithms or techniques used in this translation process.

3. Cultural Adaptation (200-250 words):
   a) Explain how your system adapts its output to reflect {t['target_culture']} cultural perceptions of {t['emotion']}.
   b) Provide an example of how the output might differ if adapted for a different culture.
   c) Discuss challenges in maintaining emotional authenticity across cultures.

4. Training and Data Considerations (150-200 words):
   a) Describe the type of data your system would need to be trained on.
   b) Explain how you would ensure diverse cultural representation in the training data.
   c) Discuss potential biases and how you would mitigate them.

5. Evaluation Metrics (100-150 words):
   a) Propose methods to evaluate the effectiveness of your system's emotional-to-visual translations.
   b) Describe how you would validate the cultural appropriateness of the generated art.

6. Potential Applications and Ethical Considerations (150-200 words):
   a) Suggest two potential applications of your system beyond art generation.
   b) Discuss ethical implications of translating emotions into visual art across cultures.
   c) Propose guidelines for responsible development and use of emotion-to-art AI systems.

Ensure your response demonstrates a deep understanding of emotional intelligence, art theory, cultural studies, and AI system design. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your response will be evaluated based on the depth of understanding shown, the innovation and plausibility of your proposed system, the thoroughness of your discussion on cultural adaptation and ethical considerations, and the clarity and structure of your writing."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system for translating {t['emotion']} into {t['art_style']} abstract art",
            f"The system demonstrates thoughtful adaptation to {t['target_culture']} cultural context",
            "The response shows interdisciplinary knowledge integration of emotional intelligence, art theory, cultural studies, and AI",
            "The proposed system is innovative yet scientifically plausible",
            "The emotional-visual translation mechanism is clearly explained and incorporates novel techniques",
            "Training data considerations and bias mitigation strategies are thoroughly discussed",
            "Evaluation metrics for both emotional translation and cultural appropriateness are proposed",
            "Ethical considerations and potential applications are thoughtfully addressed",
            "The response is well-structured, clear, and adheres to the specified word limits for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
