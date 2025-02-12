import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture': 'Ancient Egyptian',
                'art_form': 'symbolic narrative',
                'theme': 'the afterlife',
                'elements': ['Anubis', 'scarab beetle', 'lotus flower']
            },
            {
                'culture': 'Edo period Japanese',
                'art_form': 'haiku',
                'theme': 'impermanence',
                'elements': ['cherry blossoms', 'samurai', 'tea ceremony']
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As an AI with expertise in computational creativity and cultural studies, your task is to generate and analyze a culturally-specific creative work based on the following parameters:

Culture: {t['culture']}
Art Form: {t['art_form']}
Theme: {t['theme']}
Required Elements: {', '.join(t['elements'])}

1. Creation (200-250 words):
   Generate a {t['art_form']} in the style of {t['culture']} culture, incorporating the theme of {t['theme']} and including all the required elements. 
   - For a symbolic narrative, describe a series of symbolic images and their arrangement, as if describing a painted scene.
   - For a haiku, provide the haiku in English, following the 5-7-5 syllable structure.
   Provide a brief explanation of how your creation reflects the specified cultural context and artistic traditions.

2. Cultural Analysis (200-250 words):
   Analyze your created work in the context of {t['culture']} culture. Discuss how it reflects cultural values, beliefs, and artistic conventions of the time. Explain the significance of the theme and required elements within this cultural framework.

3. Comparative Perspective (150-200 words):
   Compare and contrast your created work with a similar art form from a different culture. Discuss how the theme of {t['theme']} might be treated differently in another cultural context.

4. Modern Interpretation (150-200 words):
   Propose a modern reinterpretation of your created work that maintains its cultural essence while making it relevant to a contemporary global audience. Explain your creative choices and how they bridge traditional and modern perspectives.

5. AI and Cultural Creativity (100-150 words):
   Reflect on the challenges and ethical considerations of using AI to generate culturally-specific creative works. Discuss potential benefits and risks of this approach to cultural preservation and artistic expression.

Ensure your response demonstrates a deep understanding of the specified culture, art form, and creative processes. Use appropriate terminology and provide clear explanations for cultural references. Be creative in your approach while maintaining cultural authenticity and sensitivity.

Format your response with clear headings for each section, numbered as above. Your total response should be between 800-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a culturally appropriate {t['art_form']} (200-250 words) incorporating the theme and all required elements.",
            f"The cultural analysis (200-250 words) demonstrates a deep understanding of {t['culture']} culture and artistic traditions.",
            "The comparative perspective (150-200 words) offers meaningful insights into cultural differences in artistic expression.",
            "The modern reinterpretation (150-200 words) successfully bridges traditional and contemporary perspectives.",
            "The reflection on AI and cultural creativity (100-150 words) addresses relevant ethical considerations.",
            "The overall response shows creativity, cultural sensitivity, and analytical depth.",
            "The response follows the specified format with clear headings and word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
