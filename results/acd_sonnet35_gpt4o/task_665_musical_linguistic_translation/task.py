import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "chord progressions",
            "melodic contours",
            "rhythmic patterns",
            "harmonic structures"
        ]
        linguistic_elements = [
            "syntax",
            "morphology",
            "semantics",
            "pragmatics"
        ]
        musical_genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "Folk"
        ]
        
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "linguistic_element": random.choice(linguistic_elements),
                "genre": random.choice(musical_genres)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "linguistic_element": random.choice(linguistic_elements),
                "genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system that translates {t['musical_element']} into linguistic patterns based on {t['linguistic_element']}, then use it to create a 'musical language' and analyze a piece of {t['genre']} music. Your response should include:\n\n" \
               f"1. System Design (250-300 words):\n" \
               f"   a) Explain the core principles of your translation system.\n" \
               f"   b) Describe how {t['musical_element']} are mapped to {t['linguistic_element']}.\n" \
               f"   c) Provide examples of how basic musical structures would be translated into linguistic patterns.\n\n" \
               f"2. Musical Language Creation (200-250 words):\n" \
               f"   a) Using your translation system, create a 'musical language' with its own grammar and vocabulary.\n" \
               f"   b) Provide 3-5 example 'sentences' in your musical language with their musical and linguistic interpretations.\n" \
               f"   c) Explain how your language captures both musical and linguistic properties.\n\n" \
               f"3. Musical Analysis (200-250 words):\n" \
               f"   a) Choose a well-known piece of {t['genre']} music.\n" \
               f"   b) Analyze this piece using your musical language.\n" \
               f"   c) Discuss any insights or patterns revealed through this analysis.\n\n" \
               f"4. Cognitive and Computational Implications (150-200 words):\n" \
               f"   a) Discuss how your system might model or reflect cognitive processes in music perception and language processing.\n" \
               f"   b) Explore potential applications of your system in music education, composition, or AI-driven music analysis.\n\n" \
               f"5. Limitations and Future Directions (100-150 words):\n" \
               f"   a) Identify potential limitations of your translation system.\n" \
               f"   b) Propose ideas for expanding or improving the system.\n\n" \
               f"Ensure your response demonstrates a deep understanding of both music theory and linguistics. Use appropriate terminology from both fields and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section, numbered as above."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both music theory and linguistics, particularly in relation to the specified musical and linguistic elements.",
            "The translation system is clearly explained and logically connects musical structures to linguistic patterns.",
            "The created 'musical language' is coherent, creative, and effectively combines musical and linguistic properties.",
            "The musical analysis using the created language reveals meaningful insights about the chosen piece.",
            "The discussion of cognitive and computational implications is thoughtful and grounded in current understanding of music perception and language processing.",
            "The response identifies valid limitations and proposes plausible ideas for future development."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
