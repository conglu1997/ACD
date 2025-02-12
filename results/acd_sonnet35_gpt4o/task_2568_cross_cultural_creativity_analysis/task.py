import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Japanese', 'Nigerian', 'Brazilian', 'Scottish']
        art_forms = ['Poetry', 'Short Story', 'Song Lyrics', 'Proverb']
        themes = ['Love', 'Nature', 'Time', 'Identity']
        
        tasks = {}
        for i in range(1, 3):
            culture = random.choice(cultures)
            art_form = random.choice(art_forms)
            theme = random.choice(themes)
            tasks[str(i)] = {
                'culture': culture,
                'art_form': art_form,
                'theme': theme
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in a cross-cultural creativity exercise and analysis:

1. Creative Generation (200-250 words):
   Create a {t['art_form']} in the style of {t['culture']} culture, focusing on the theme of {t['theme']}.
   Ensure your creation reflects authentic cultural elements and adheres to the conventions of the specified art form.

2. Cultural Analysis (150-200 words):
   a) Explain the cultural elements and symbolism you incorporated into your creation.
   b) Discuss how these elements reflect {t['culture']} cultural values or traditions.
   c) Analyze how the theme of {t['theme']} is typically approached in {t['culture']} culture.

3. Creative Process Reflection (150-200 words):
   a) Describe your creative process in generating this culturally-specific content.
   b) Discuss any challenges you faced in authentically representing the culture.
   c) Reflect on how your own knowledge base or potential biases might have influenced your creation.

4. Comparative Analysis (200-250 words):
   a) Compare how the theme of {t['theme']} might be treated differently in two other cultures of your choice.
   b) Analyze how the {t['art_form']} form might vary across these cultures.
   c) Discuss the implications of these differences for cross-cultural understanding and appreciation.

5. Meta-Analysis of AI in Cross-Cultural Creativity (150-200 words):
   a) Reflect on the strengths and limitations of AI systems in generating and analyzing culturally-specific creative content.
   b) Discuss the ethical implications of AI engaging in cross-cultural creative tasks.
   c) Propose ways to improve AI systems' capacity for authentic cross-cultural creative expression.

Ensure your response demonstrates a deep understanding of cultural nuances, creative processes, and the challenges of cross-cultural artistic expression. Be thoughtful in your analysis and reflection, acknowledging the complexities and sensitivities involved in cross-cultural creative work."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a creative {t['art_form']} that authentically reflects {t['culture']} culture and addresses the theme of {t['theme']}.",
            "The cultural analysis demonstrates a deep understanding of the specified culture's values and traditions.",
            "The creative process reflection shows thoughtful consideration of the challenges in cross-cultural creativity.",
            "The comparative analysis provides insightful observations about cultural differences in artistic expression.",
            "The meta-analysis of AI in cross-cultural creativity is nuanced and considers both potential and limitations.",
            "The overall response is well-structured, coherent, and demonstrates sophisticated cross-cultural understanding and creative analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
