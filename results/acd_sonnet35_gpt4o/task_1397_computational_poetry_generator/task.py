import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        poetry_styles = [
            {
                "language": "English",
                "style": "Shakespearean sonnet",
                "theme": "love"
            },
            {
                "language": "Japanese",
                "style": "haiku",
                "theme": "nature"
            },
            {
                "language": "Arabic",
                "style": "qasida",
                "theme": "nostalgia"
            },
            {
                "language": "Spanish",
                "style": "villancico",
                "theme": "celebration"
            }
        ]
        return {
            "1": random.choice(poetry_styles),
            "2": random.choice(poetry_styles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational system for generating and analyzing poetry in {t['language']}, specifically focusing on the {t['style']} style with the theme of {t['theme']}. Your task has the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your computational poetry system.
   b) Explain how these components interact to generate and analyze poetry.
   c) Discuss any novel algorithms or AI techniques incorporated in your system.
   d) Address how your system handles language-specific challenges and cultural nuances.

2. Poetry Generation Process (250-300 words):
   a) Detail the step-by-step process your system uses to generate a {t['style']} in {t['language']}.
   b) Explain how your system incorporates the theme of {t['theme']} into the generated poetry.
   c) Describe how your system ensures adherence to the specific rules and structure of {t['style']}.
   d) Provide a short example (2-4 lines) of poetry your system might generate, with an English translation if applicable.

3. Literary Device Implementation (200-250 words):
   a) Identify at least three literary devices commonly used in {t['style']}.
   b) Explain how your system implements these devices in the generated poetry.
   c) Discuss any challenges in computationally representing these literary devices.

4. Cultural and Linguistic Considerations (200-250 words):
   a) Analyze how your system accounts for cultural context in {t['language']} poetry.
   b) Explain how linguistic features specific to {t['language']} are handled in your system.
   c) Discuss potential biases or limitations in your system's understanding of {t['language']} and {t['style']}.

5. Poetry Analysis Capabilities (200-250 words):
   a) Describe how your system would analyze an existing {t['style']} poem in {t['language']}.
   b) Explain what metrics or features your system would use to evaluate the quality of a poem.
   c) Discuss how your system might identify themes, emotions, or cultural references in poetry.

6. Ethical and Creative Considerations (150-200 words):
   a) Discuss the ethical implications of AI-generated poetry in the context of {t['language']} and {t['style']}.
   b) Address concerns about cultural appropriation or misrepresentation in AI-generated poetry.
   c) Propose guidelines for the responsible use of AI in poetry generation and analysis.

Ensure your response demonstrates a deep understanding of computational linguistics, poetry structures, and cultural aspects of literature. Use appropriate terminology from both technical and literary fields, providing clear explanations where necessary. Be innovative in your approach while maintaining linguistic and cultural authenticity.

Format your response with clear headings for each section (numbered 1-6) and use lettered subheadings (a, b, c, etc.) within each section as outlined above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of computational linguistics and {t['language']} poetry, specifically {t['style']}.",
            "The proposed system architecture is innovative, detailed, and technically feasible.",
            f"The poetry generation process is well-explained and incorporates the theme of {t['theme']} appropriately.",
            f"The implementation of literary devices common in {t['style']} is clearly described and computationally plausible.",
            f"Cultural and linguistic considerations specific to {t['language']} are thoroughly addressed.",
            "The poetry analysis capabilities are well-thought-out and demonstrate an understanding of literary criticism.",
            "Ethical and creative considerations are discussed thoughtfully and comprehensively.",
            "The response maintains coherence, relevance, and demonstrates creativity throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
