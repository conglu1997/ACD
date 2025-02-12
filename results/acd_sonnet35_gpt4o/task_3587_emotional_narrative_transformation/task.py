import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        narratives = [
            "As the sun set, Sarah walked along the beach, remembering the times she spent here with her grandfather. The sound of the waves brought a sense of peace she hadn't felt in months.",
            "Tom stared at the rejection letter, his hands shaking. Years of hard work seemed to crumble before his eyes. He took a deep breath and reached for his phone to call his mentor."
        ]
        emotion_sets = [
            ["joy", "excitement", "anticipation"],
            ["anger", "frustration", "determination"],
            ["fear", "anxiety", "hope"],
            ["sadness", "nostalgia", "acceptance"]
        ]
        tasks = [
            {
                'narrative': random.choice(narratives),
                'target_emotions': random.choice(emotion_sets)
            },
            {
                'narrative': random.choice(narratives),
                'target_emotions': random.choice(emotion_sets)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the emotional content of the following narrative, then rewrite it to convey a different set of emotions while preserving the core plot elements.

Original Narrative:
{t['narrative']}

Target Emotions: {', '.join(t['target_emotions'])}

Your task:

1. Emotional Analysis (100-150 words):
   - Identify and explain the primary emotions conveyed in the original narrative.
   - Discuss how specific words, phrases, or narrative elements contribute to these emotions.

2. Emotional Transformation Strategy (150-200 words):
   - Explain your strategy for transforming the narrative to convey the target emotions.
   - Discuss which elements of the original narrative you will keep, modify, or replace.
   - Explain how you will incorporate the target emotions while maintaining the core plot.

3. Rewritten Narrative (100-150 words):
   - Provide a rewritten version of the narrative that conveys the target emotions.
   - Ensure that the core plot elements and characters are preserved.

4. Analysis of Transformation (150-200 words):
   - Explain how your rewritten narrative conveys the target emotions.
   - Compare and contrast the emotional impact of the original and rewritten narratives.
   - Discuss any challenges you encountered in the transformation process.

5. Psychological Implications (100-150 words):
   - Discuss the potential psychological impact of the emotional shift on readers.
   - Explain how changing the emotional content might affect the interpretation of the narrative.

Ensure your response demonstrates a deep understanding of emotional intelligence, narrative structure, and the psychological aspects of storytelling. Use appropriate terminology from psychology and literary analysis. Be creative in your narrative transformation while maintaining coherence and plausibility.

Format your response with clear headings for each section. Your total response should be between 600-850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a thorough emotional analysis of the original narrative.",
            "The rewritten narrative effectively conveys the target emotions while preserving core plot elements.",
            "The analysis of the transformation process is insightful and well-explained.",
            "The discussion of psychological implications demonstrates understanding of emotional impact on readers.",
            "The overall response shows creativity, emotional intelligence, and strong narrative skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
