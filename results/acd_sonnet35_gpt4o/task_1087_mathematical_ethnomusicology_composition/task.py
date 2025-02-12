import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        number_sequences = [
            "Fibonacci sequence",
            "Prime numbers",
            "Pi digits",
            "Golden ratio"
        ]
        cultural_narratives = [
            "Polynesian voyaging traditions",
            "Aztec creation myth",
            "Aboriginal Dreamtime stories",
            "Norse Ragnarök"
        ]
        tasks = {
            "1": {
                "number_sequence": random.choice(number_sequences),
                "cultural_narrative": random.choice(cultural_narratives)
            },
            "2": {
                "number_sequence": random.choice(number_sequences),
                "cultural_narrative": random.choice(cultural_narratives)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a mathematical music system based on the {t['number_sequence']}, then use it to compose a piece representing the {t['cultural_narrative']}. Your response should include:

1. Mathematical Music System (200-250 words):
   a) Explain how you will use the {t['number_sequence']} to create a musical scale or rhythm system.
   b) Describe the mathematical rules for composing melodies or harmonies in your system.
   c) Discuss how your system differs from traditional Western music theory.

2. Cultural Narrative Analysis (150-200 words):
   a) Briefly describe the key elements of the {t['cultural_narrative']}.
   b) Identify at least three specific aspects of the narrative that you will represent musically.
   c) Explain how these aspects relate to the cultural context and significance of the narrative.

3. Composition Process (250-300 words):
   a) Describe how you will use your mathematical music system to represent each aspect of the narrative.
   b) Explain any challenges in mapping the narrative to your music system and how you resolved them.
   c) Discuss how you balance mathematical precision with artistic expression in your composition.

4. Notational System (100-150 words):
   a) Propose a notational system for your composition that incorporates both mathematical and musical elements.
   b) Provide a short example of your notation system in ASCII or Unicode characters.

5. Cultural and Mathematical Implications (200-250 words):
   a) Discuss how your composition might be perceived by members of the culture whose narrative you're representing.
   b) Explain how your system could be used to analyze or create music from other cultural traditions.
   c) Propose a mathematical or musical insight that could be gained from your system.

Ensure your response demonstrates a deep understanding of music theory, mathematics, and cultural anthropology. Be innovative in your approach while maintaining scientific and cultural accuracy. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all five requested sections with appropriate content for each.",
            "The mathematical music system should be clearly explained and logically connected to the specified number sequence.",
            "The cultural narrative analysis should demonstrate understanding and respect for the chosen culture.",
            "The composition process should show a clear connection between the mathematical system, the cultural narrative, and music theory.",
            "The notational system should be innovative yet comprehensible, with a clear example provided.",
            "The discussion of implications should show depth of thought and potential for broader application.",
            "The overall response should demonstrate creativity, interdisciplinary knowledge, and analytical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
