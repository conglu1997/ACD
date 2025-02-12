import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_sequences = [
            {"name": "Fibonacci sequence", "first_terms": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]},
            {"name": "Prime numbers", "first_terms": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]}
        ]
        musical_traditions = [
            {"name": "Indian classical", "scale": "Raga Yaman", "description": "A system of melodic modes used in Indian classical music"},
            {"name": "West African", "rhythm": "Polyrhythmic", "description": "Complex rhythms that combine two or more different rhythms simultaneously"},
            {"name": "Chinese traditional", "scale": "Pentatonic", "description": "A five-note scale commonly used in traditional Chinese music"}
        ]
        tasks = {}
        for i in range(2):
            sequence = random.choice(mathematical_sequences)
            tradition = random.choice(musical_traditions)
            tasks[str(i+1)] = {
                "sequence": sequence,
                "tradition": tradition
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical composition that fuses mathematical patterns with cultural musical traditions. Your task has several parts:

1. Composition (250-300 words):
   a) Create a musical piece based on the {t['sequence']['name']} ({', '.join(map(str, t['sequence']['first_terms']))}, ...) and the {t['tradition']['name']} musical tradition ({t['tradition']['description']}).
   b) Explain how you incorporated the mathematical sequence into your composition (e.g., note duration, pitch selection, rhythm).
   c) Describe how you integrated elements of the {t['tradition']['name']} tradition (e.g., {t['tradition'].get('scale', t['tradition'].get('rhythm', 'specific instruments or techniques'))})
   d) Provide a detailed textual representation of your composition (e.g., musical notation, tablature, or a comprehensive description of the piece's structure, melody, and rhythm).

2. Structural Analysis (200-250 words):
   a) Analyze the mathematical properties of your composition.
   b) Explain how the structure of the piece reflects both the sequence and the musical tradition.
   c) Discuss any interesting patterns or properties that emerged from this fusion.

3. Cultural Significance (200-250 words):
   a) Explain the cultural significance of the {t['tradition']['name']} elements in your composition.
   b) Discuss how the integration of mathematical patterns might be perceived within the context of this musical tradition.
   c) Explore potential reactions to this fusion from both mathematicians and traditional musicians.

4. Comparative Analysis (150-200 words):
   a) Compare your composition to a traditional piece from the {t['tradition']['name']} tradition.
   b) Discuss how the incorporation of the {t['sequence']['name']} has altered the traditional structure or feel of the music.

5. Emotional and Cognitive Impact (150-200 words):
   a) Describe the potential emotional impact of your composition on listeners.
   b) Discuss how engaging with this type of mathematical-musical fusion might affect cognitive processes or mathematical thinking.

Ensure your response demonstrates a deep understanding of music theory, mathematical sequences, and the chosen cultural tradition. Be creative in your approach while maintaining musical and cultural authenticity.

Format your response with clear headings for each section, numbered as above. Your total response should be between 950-1200 words. Use appropriate musical and mathematical terminology throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The composition must incorporate the {t['sequence']['name']} and elements of {t['tradition']['name']} music",
            "The response must include all five required sections: Composition, Structural Analysis, Cultural Significance, Comparative Analysis, and Emotional and Cognitive Impact",
            "The analysis should demonstrate understanding of both mathematical and musical concepts",
            "The response should show creativity in fusing mathematical and musical elements",
            "The cultural analysis should be respectful and well-informed",
            "The response should use appropriate musical and mathematical terminology",
            "The composition should be described in sufficient detail to understand its structure, melody, and rhythm",
            "The response should adhere to the specified word count for each section",
            "The analysis should consider both the mathematical and cultural aspects of the composition",
            "The emotional and cognitive impact analysis should be insightful and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
