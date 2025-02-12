import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy",
            "sorrow",
            "anger",
            "fear",
            "surprise",
            "disgust",
            "anticipation",
            "trust"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre",
            "dynamics",
            "texture"
        ]
        tasks = [
            {
                "emotion": random.choice(emotions),
                "musical_focus": random.choice(musical_elements),
                "synaesthetic_sense": random.choice(["color", "taste", "smell", "texture"])
            } for _ in range(2)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the emotional state of {t['emotion']} into a musical composition, focusing primarily on the musical element of {t['musical_focus']}. Then, describe this composition using synaesthetic language related to {t['synaesthetic_sense']}.

Synaesthesia is a perceptual phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway. In this task, you'll be creating a form of artificial synaesthesia between music and {t['synaesthetic_sense']}.

Your response should include:

1. Emotional-Musical Translation (200-250 words):
   a) Explain how your system would represent {t['emotion']} using musical elements, with a focus on {t['musical_focus']}.
   b) Describe the key features of the resulting composition.
   c) Justify your choices based on psychological or neuroscientific understanding of emotion and music perception.

2. Synaesthetic Description (150-200 words):
   a) Provide a vivid description of the composition using language related to {t['synaesthetic_sense']}.
   b) Explain how specific musical features correspond to particular {t['synaesthetic_sense']} experiences.
   c) Discuss how this synaesthetic description enhances understanding of the emotional content.

3. System Architecture (200-250 words):
   a) Outline the components of your emotion-to-music-to-language system.
   b) Explain how these components interact to produce the final output.
   c) Discuss any machine learning or AI techniques you would incorporate.

4. Cross-modal Integration Analysis (150-200 words):
   a) Analyze how your system integrates information across emotional, musical, and linguistic domains.
   b) Discuss potential challenges in this integration and how you address them.
   c) Explain how this integration might mirror or differ from human cognitive processes.

5. Potential Applications and Implications (100-150 words):
   a) Propose two potential applications of your system in fields such as therapy, art, or human-computer interaction.
   b) Discuss the implications of your system for our understanding of emotion, music, and language processing.

6. Reflection (100-150 words):
   a) Discuss any insights you gained about the relationships between emotion, music, and language while completing this task.
   b) Reflect on how this task might reveal strengths or limitations of AI language models in processing cross-modal information.

Ensure your response demonstrates a deep understanding of music theory, emotional processing, and synaesthetic language use. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section and adhere to the specified word limits. Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively translates {t['emotion']} into musical elements, focusing on {t['musical_focus']}.",
            f"The synaesthetic description vividly represents the composition using {t['synaesthetic_sense']}-related language.",
            "The system architecture is well-explained and incorporates relevant AI or machine learning techniques.",
            "The cross-modal integration analysis is insightful and addresses potential challenges.",
            "The proposed applications and implications are innovative and well-reasoned.",
            "The reflection demonstrates deep thinking about the relationships between emotion, music, and language.",
            "The response demonstrates a deep understanding of music theory, emotional processing, and synaesthetic language use.",
            "The approach is creative while maintaining scientific plausibility.",
            "The response adheres to the specified word limits and formatting guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
