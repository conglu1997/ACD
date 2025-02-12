import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            {
                'concept': 'Fibonacci sequence',
                'description': 'A sequence where each number is the sum of the two preceding ones',
                'cognitive_aspect': 'pattern recognition'
            },
            {
                'concept': 'Fractals',
                'description': 'Geometric shapes that can be split into parts, each of which is a reduced-size copy of the whole',
                'cognitive_aspect': 'spatial reasoning'
            },
            {
                'concept': 'Chaos theory',
                'description': 'The study of systems that are highly sensitive to initial conditions',
                'cognitive_aspect': 'predictive analysis'
            },
            {
                'concept': 'Prime numbers',
                'description': 'Natural numbers greater than 1 that are only divisible by 1 and themselves',
                'cognitive_aspect': 'logical reasoning'
            }
        ]
        
        return {str(i+1): random.choice(math_concepts) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the mathematical concept of {t['concept']} into a musical composition, and analyze its potential cognitive and emotional effects. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your math-to-music translation system.
   b) Explain in detail how your system converts {t['concept']} into musical elements (e.g., rhythm, melody, harmony, timbre, dynamics).
   c) Provide a specific example of how three distinct features of {t['concept']} would be represented musically.
   d) Include a simple diagram or pseudocode snippet illustrating a key aspect of your system.

2. Musical Composition Analysis (250-300 words):
   a) Describe the expected characteristics of the resulting musical composition.
   b) Explain how these characteristics reflect the mathematical properties of {t['concept']}.
   c) Discuss how your composition might differ from traditional music in structure or sound.
   d) Provide a hypothetical 8-bar musical score or a detailed description of a short musical phrase that demonstrates your system's output.

3. Cognitive and Emotional Impact (250-300 words):
   a) Analyze how listening to this mathematical music might affect {t['cognitive_aspect']}.
   b) Hypothesize potential emotional responses to the composition, citing relevant psychological theories.
   c) Propose a detailed experiment to test the cognitive or emotional effects of your mathematical music, including methodology and expected outcomes.

4. Applications and Implications (200-250 words):
   a) Suggest three potential applications of your math-to-music translation system in different fields.
   b) Discuss how this system might enhance understanding or appreciation of mathematics.
   c) Consider any ethical implications of using such mathematically-derived music, including potential misuse.

5. Comparative Analysis (150-200 words):
   a) Compare your approach to two existing methods of representing mathematical concepts through sound or music.
   b) Discuss the unique advantages and potential limitations of your system.
   c) Propose one way to address a limitation you've identified.

Ensure your response demonstrates a deep understanding of mathematics, music theory, and cognitive science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and theoretical plausibility.

Format your response using the following structure:

1. System Design
   [Your response here]

2. Musical Composition Analysis
   [Your response here]

3. Cognitive and Emotional Impact
   [Your response here]

4. Applications and Implications
   [Your response here]

5. Comparative Analysis
   [Your response here]

Your entire response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['concept']} and provides a detailed explanation of how it is translated into multiple musical elements.",
            "The system design is creative, well-explained, and theoretically plausible, with clear examples and a relevant diagram or pseudocode.",
            f"The analysis of cognitive and emotional impact, particularly regarding {t['cognitive_aspect']}, is thoughtful, grounded in cognitive science principles, and includes a well-designed experiment.",
            "The proposed applications are diverse and insightful, and the ethical considerations are well-reasoned and thorough.",
            "The comparative analysis shows a good understanding of existing methods in the field and proposes a plausible improvement to the system.",
            "The response adheres to the specified format and word count, and demonstrates appropriate use of technical terminology from mathematics, music theory, and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
