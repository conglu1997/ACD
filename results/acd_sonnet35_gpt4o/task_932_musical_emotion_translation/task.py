import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_narratives = [
            {
                "narrative": "A sudden realization of love amidst chaos",
                "musical_elements": ["tempo", "key", "dynamics"]
            },
            {
                "narrative": "The bittersweet nostalgia of childhood memories",
                "musical_elements": ["melody", "harmony", "rhythm"]
            },
            {
                "narrative": "Overcoming fear and embracing the unknown",
                "musical_elements": ["instrumentation", "texture", "form"]
            }
        ]
        return {str(i+1): narrative for i, narrative in enumerate(random.sample(emotional_narratives, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the emotional content of the following narrative into musical elements, then compose a short musical piece based on this translation.

Emotional Narrative: {t['narrative']}
Musical Elements to focus on: {', '.join(t['musical_elements'])}

Your task has three parts:

1. Emotional Translation (150-200 words):
   a) Analyze the emotional content of the given narrative.
   b) Translate this emotional content into musical terms, focusing on the specified musical elements.
   c) Explain your choices and how they reflect the emotional narrative.

2. Musical Composition (200-250 words):
   a) Compose a short musical piece (about 16-32 measures) based on your emotional translation.
   b) Describe your composition in detail, including how you've used the specified musical elements.
   c) Explain how your composition reflects the emotional journey of the narrative.

3. Reflection and Analysis (150-200 words):
   a) Discuss the challenges you faced in translating emotions between language and music.
   b) Analyze the effectiveness of your composition in conveying the original emotional narrative.
   c) Suggest how this exercise might inform our understanding of the relationship between music, language, and emotion.

Ensure your response demonstrates a deep understanding of music theory, emotional expression, and the relationship between language and music. Be creative in your approach while maintaining logical connections between the narrative and your musical choices.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear analysis of the emotional content in the given narrative",
            "The musical translation should logically connect to the emotional narrative",
            "The musical composition should be described in detail, using appropriate music theory terminology",
            "The reflection should demonstrate understanding of the challenges in translating between emotions, language, and music",
            "The response should be creative while maintaining coherence with the original narrative"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
