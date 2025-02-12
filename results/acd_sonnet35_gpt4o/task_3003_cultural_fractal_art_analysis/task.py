import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                'name': 'Mayan',
                'pattern': 'Step pyramid',
                'fractal_type': 'Sierpinski triangle',
                'cultural_significance': 'Represents the layers of the universe and the journey to enlightenment'
            },
            {
                'name': 'Celtic',
                'pattern': 'Spiral',
                'fractal_type': 'Koch snowflake',
                'cultural_significance': 'Symbolizes the cycles of life, death, and rebirth'
            },
            {
                'name': 'Japanese',
                'pattern': 'Wave',
                'fractal_type': 'Mandelbrot set',
                'cultural_significance': 'Represents the power and beauty of nature, particularly the ocean'
            },
            {
                'name': 'Aboriginal Australian',
                'pattern': 'Dot painting',
                'fractal_type': 'Cantor set',
                'cultural_significance': 'Depicts Dreamtime stories and connection to the land'
            },
            {
                'name': 'Islamic',
                'pattern': 'Geometric tessellation',
                'fractal_type': 'Apollonian gasket',
                'cultural_significance': 'Symbolizes the infinite nature of Allah and the complexity of creation'
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f'''Create and analyze a fractal art piece based on the cultural pattern of {t['name']} culture. A fractal is a geometric figure that repeats its pattern at different scales, creating complex, never-ending patterns. Your task has five parts:

1. Fractal Design (250-300 words):
   a) Describe how you would create a fractal art piece that combines the {t['pattern']} pattern with the {t['fractal_type']} fractal.
   b) Explain the mathematical principles behind your chosen fractal and how they relate to the cultural pattern.
   c) Describe the visual elements of your artwork (e.g., colors, shapes, composition) and how they reflect the culture.
   d) Provide a text-based representation or detailed description of your fractal artwork (e.g., ASCII art or a step-by-step description of the pattern's development).

2. Cultural Analysis (150-200 words):
   a) Analyze the cultural significance of the {t['pattern']} pattern in {t['name']} culture.
   b) Explain how your fractal interpretation enhances or transforms the original cultural meaning.
   c) Discuss any challenges in representing cultural symbols through mathematical fractals.

3. Mathematical-Artistic Integration (150-200 words):
   a) Explain how your design balances mathematical precision with artistic expression.
   b) Describe any modifications you made to the standard {t['fractal_type']} to better represent the cultural pattern.
   c) Discuss how the fractal nature of the artwork might reveal new insights about the cultural pattern.

4. Symbolic Interpretation (100-150 words):
   a) Interpret the symbolic meaning of your fractal artwork in the context of {t['name']} culture.
   b) Explain how the infinite nature of fractals relates to the cultural significance: {t['cultural_significance']}.

5. Cross-Cultural Comparison (150-200 words):
   a) Compare your fractal interpretation of {t['name']} {t['pattern']} with a similar concept from a different culture.
   b) Analyze how the mathematical representation highlights similarities or differences between cultures.
   c) Discuss the potential of fractal art as a tool for cross-cultural understanding.

Ensure your response demonstrates a deep understanding of fractal mathematics, artistic principles, and cultural anthropology. Use appropriate terminology from each field and provide clear explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and mathematical accuracy.

Format your response with clear headings for each section. Your total response should be between 800-1050 words.'''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of fractal mathematics and its application to art.",
            "The cultural analysis shows insight into the significance of the pattern in the given culture.",
            "The fractal design creatively integrates mathematical principles with cultural symbolism.",
            "A text-based representation or detailed description of the fractal artwork is provided.",
            "The symbolic interpretation thoughtfully connects the fractal nature of the artwork to cultural meanings.",
            "The cross-cultural comparison provides meaningful insights and demonstrates broad cultural knowledge.",
            "The response is well-structured, following the specified format with clear headings for each section.",
            "The total word count is between 800-1050 words, as specified in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
