class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "narrative": "Little Red Riding Hood",
                "psych_perspective": "Jungian archetypes",
                "cultural_lens": "Contemporary urban setting"
            },
            "2": {
                "narrative": "The Odyssey",
                "psych_perspective": "Attachment theory",
                "cultural_lens": "Afrofuturism"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and rewrite the narrative '{t['narrative']}' from the psychological perspective of {t['psych_perspective']} and the cultural lens of {t['cultural_lens']}, then create a new story incorporating these insights. Your response should include the following sections:

1. Psychological Analysis (250-300 words):
   a) Briefly explain the key concepts of {t['psych_perspective']}.
   b) Analyze the characters and plot of '{t['narrative']}' using this psychological framework.
   c) Identify at least three specific examples where this perspective offers new insights into the story.

2. Cultural Reinterpretation (250-300 words):
   a) Describe the main characteristics and themes of {t['cultural_lens']}.
   b) Rewrite a key scene from '{t['narrative']}' through this cultural lens.
   c) Explain how this reinterpretation changes the meaning or impact of the story.

3. Narrative Reimagining (400-450 words):
   Rewrite the entire narrative of '{t['narrative']}', incorporating both the psychological perspective and cultural lens. Ensure your reimagined story:
   a) Maintains the core structure and key elements of the original narrative.
   b) Clearly demonstrates the influence of {t['psych_perspective']} in character development and motivations.
   c) Integrates the themes and style of {t['cultural_lens']} throughout the narrative.
   d) Creates a coherent and engaging story that stands on its own.

4. Literary Analysis (200-250 words):
   Analyze your reimagined narrative, discussing:
   a) How the psychological perspective deepens character development and conflict.
   b) How the cultural lens affects the setting, themes, and overall message of the story.
   c) Any new symbols, motifs, or literary devices you've introduced and their significance.

5. Comparative Reflection (150-200 words):
   Compare your reimagined narrative to the original, discussing:
   a) How the core message or moral of the story has changed or evolved.
   b) Any unexpected insights or themes that emerged during the rewriting process.
   c) The potential impact of this new version on different audiences.

6. Creative Extension (250-300 words):
   Create a completely new, original short story (not based on '{t['narrative']}') that incorporates the psychological and cultural insights you've gained from this exercise. Your story should:
   a) Feature at least two distinct characters influenced by {t['psych_perspective']}.
   b) Be set in a world that reflects the themes and style of {t['cultural_lens']}.
   c) Include a clear narrative arc with a beginning, middle, and end.
   d) Demonstrate sophisticated use of literary techniques and devices.

Ensure your response showcases a deep understanding of the chosen psychological perspective, cultural lens, and literary analysis. Be creative and thoughtful in your reinterpretations and new story creation while maintaining logical consistency and narrative coherence.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified psychological perspective and cultural lens.",
            "The narrative reimagining effectively incorporates both the psychological and cultural elements while maintaining the core structure of the original story.",
            "The literary analysis shows insightful connections between the psychological perspective, cultural lens, and narrative elements.",
            "The new original story creatively applies the psychological and cultural insights gained from the exercise.",
            "The writing is clear, engaging, and demonstrates sophisticated use of literary techniques.",
            "The response adheres to the specified word counts and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
