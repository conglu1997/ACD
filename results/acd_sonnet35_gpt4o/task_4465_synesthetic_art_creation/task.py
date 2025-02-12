import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "input_modality": "sound",
                "output_modality": "color",
                "input_description": "The sound of ocean waves crashing on a rocky shore",
                "emotion": "serenity",
                "constraint": "Use only primary and secondary colors"
            },
            "2": {
                "input_modality": "taste",
                "output_modality": "shape",
                "input_description": "The taste of a ripe, juicy strawberry",
                "emotion": "joy",
                "constraint": "Use only geometric shapes"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate a synesthetic experience by translating the given {t['input_modality']} input into a {t['output_modality']} experience, then create an artistic piece based on this synesthetic translation. Your task has four parts:

1. Synesthetic Translation (200-250 words):
   a) Describe in detail how you would translate the given {t['input_modality']} input ("{t['input_description']}") into a {t['output_modality']} experience.
   b) Explain the reasoning behind your translation, drawing on principles of sensory perception and potential neurological connections.
   c) Describe the emotional qualities of both the input and your synesthetic translation, focusing on the emotion of {t['emotion']}.

2. Artistic Conceptualization (200-250 words):
   a) Based on your synesthetic translation, conceptualize an artistic piece (visual art, music, poetry, dance choreography, etc.).
   b) Explain how your artistic concept incorporates both the original {t['input_modality']} input and the synesthetic {t['output_modality']} experience.
   c) Describe how your artistic piece will convey the emotion of {t['emotion']}.
   d) Explain how you will incorporate the constraint: {t['constraint']}.

3. Artistic Creation (350-400 words):
   a) Create your artistic piece. Depending on the medium, provide one of the following:
      - Visual art: A detailed textual description of the artwork, including composition, colors, shapes, and textures.
      - Music: A textual representation of the musical score, including tempo, key, instruments, and notable motifs.
      - Poetry: The full text of the poem.
      - Dance: A detailed description of the choreography, including movements, rhythm, and use of space.
   b) Explain the key elements of your creation and how they relate to the synesthetic experience and emotional content.
   c) Describe how you've incorporated the constraint: {t['constraint']}.

4. Reflection and Analysis (200-250 words):
   a) Analyze how effectively your artistic piece captures the synesthetic experience and conveys the intended emotion.
   b) Discuss any challenges you faced in translating between sensory modalities and expressing this through art.
   c) Reflect on how this exercise in synesthetic art creation might enhance our understanding of sensory perception, emotional expression, and creativity.
   d) Discuss how the constraint ({t['constraint']}) affected your creative process and the final artwork.

Ensure your response demonstrates creativity, emotional intelligence, and a deep understanding of sensory experiences and artistic expression. Use appropriate terminology from neuroscience, psychology, and art theory where relevant.

Format your response with clear headings for each section. Your total response should be between 950-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a creative and plausible translation from {t['input_modality']} to {t['output_modality']}.",
            f"The artistic piece effectively incorporates both the original input and the synesthetic experience.",
            f"The creation convincingly conveys the emotion of {t['emotion']}.",
            f"The artistic piece adheres to the constraint: {t['constraint']}.",
            "The reflection shows deep understanding of synesthesia, sensory perception, and artistic expression.",
            "The overall response is creative, emotionally intelligent, and demonstrates understanding of cross-modal sensory experiences.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
