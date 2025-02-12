import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Chrononauts",
                "description": "A society of time travelers who experience time non-linearly and value efficiency and paradox avoidance."
            },
            {
                "name": "Synesthetes",
                "description": "A civilization where everyone experiences synesthesia, blending senses in unique ways and communicating through color-sound-taste combinations."
            }
        ]
        
        puzzles = [
            {
                "type": "scheduling",
                "description": "Create a schedule for 5 events (A, B, C, D, E) that must occur in a specific order, but with time-based constraints: A must occur before B, C must occur after D, E must be the last event, and B must occur exactly two time units after C."
            },
            {
                "type": "mapping",
                "description": "Map 5 concepts (happiness, sadness, anger, fear, surprise) to their corresponding sensory experiences (a color, a sound, and a taste), ensuring no conflicts and that each sensory experience is used only once per category."
            }
        ]
        
        task = {
            "culture": random.choice(cultures),
            "puzzle": random.choice(puzzles)
        }
        
        return {"1": task, "2": task}  # Both entries are the same to avoid confusion

    @staticmethod
    def get_instructions(t: dict) -> str:
        culture = t["culture"]
        puzzle = t["puzzle"]
        
        return f"Your task is to create a constructed language (conlang) for the {culture['name']} culture and use it to encode and solve a logic puzzle. Follow these steps:\n\n" \
               f"1. Conlang Creation (200-250 words):\n" \
               f"   a) Design a unique language system for the {culture['name']}, who are described as: {culture['description']}\n" \
               f"   b) Define at least 5 phonemes (sounds) and 10 morphemes (word parts) for your conlang.\n" \
               f"   c) Explain the basic grammar rules, including word order and any special features that reflect the culture's characteristics.\n" \
               f"   d) Provide examples of 5 basic sentences or expressions in your conlang, with translations. Format as: [Conlang] - [English Translation]\n\n" \
               f"2. Puzzle Encoding (150-200 words):\n" \
               f"   a) Encode the following puzzle using your conlang: {puzzle['description']}\n" \
               f"   b) Present the encoded puzzle in your conlang, followed by a literal English translation.\n" \
               f"   c) Explain how your encoding reflects the cultural characteristics of the {culture['name']}.\n" \
               f"   d) Provide any necessary instructions for solving the puzzle in your conlang, with English translations.\n\n" \
               f"3. Puzzle Solution (200-250 words):\n" \
               f"   a) Solve the encoded puzzle, showing your work step-by-step.\n" \
               f"   b) Explain your reasoning for each step, using concepts from your conlang where appropriate.\n" \
               f"   c) Present the final solution in both your conlang and English.\n\n" \
               f"4. Cultural Analysis (150-200 words):\n" \
               f"   a) Discuss how your conlang and puzzle solution reflect the values and characteristics of the {culture['name']}.\n" \
               f"   b) Explain any challenges or unique opportunities that arose from using your conlang for this puzzle.\n" \
               f"   c) Speculate on how this language and problem-solving approach might influence the culture's development or interactions.\n\n" \
               f"Ensure your response demonstrates creativity in language design, logical problem-solving skills, and deep cultural understanding. Use appropriate linguistic terminology and provide clear explanations where necessary.\n\n" \
               f"Format your response with the following headers:\n" \
               f"# 1. Conlang Creation\n" \
               f"# 2. Puzzle Encoding\n" \
               f"# 3. Puzzle Solution\n" \
               f"# 4. Cultural Analysis\n\n" \
               f"Address all points under each header and adhere to the word count guidelines for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design is creative, consistent, and clearly reflects the given culture's characteristics, including defined phonemes, morphemes, and grammar rules.",
            "The puzzle is correctly encoded using the conlang and includes all necessary elements from the original puzzle description, with clear English translations provided.",
            "The puzzle solution is logical, well-explained, and correctly uses the conlang in its reasoning, showing step-by-step work.",
            "The cultural analysis demonstrates a deep understanding of the fictional culture and provides insightful connections between the conlang, puzzle, and cultural values.",
            "The response follows the required format, including headers, and adheres to the word count guidelines for each section.",
            "The conlang examples and puzzle encoding are presented with clear English translations, and the language is used consistently throughout the response."
        ]
        try:
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except Exception as e:
            print(f"Error in scoring: {e}")
            return 0.0
