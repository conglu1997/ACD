import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sequences = [
            {
                "name": "Fibonacci",
                "rule": "Each number is the sum of the two preceding ones",
                "example": "0, 1, 1, 2, 3, 5, 8, 13, ..."
            },
            {
                "name": "Prime",
                "rule": "Each number is only divisible by 1 and itself",
                "example": "2, 3, 5, 7, 11, 13, 17, 19, ..."
            }
        ]
        poem_structures = [
            {
                "name": "Haiku",
                "rules": [
                    "Three lines",
                    "5-7-5 syllable pattern",
                    "Nature theme"
                ]
            },
            {
                "name": "Sonnet",
                "rules": [
                    "14 lines",
                    "10 syllables per line",
                    "Specific rhyme scheme (e.g., ABAB CDCD EFEF GG)"
                ]
            }
        ]
        return {
            "1": {
                "sequence": random.choice(sequences),
                "poem": random.choice(poem_structures)
            },
            "2": {
                "sequence": random.choice(sequences),
                "poem": random.choice(poem_structures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a fractal poem based on the {t['sequence']['name']} sequence and the structure of a {t['poem']['name']}. Follow these steps:\n\n1. Create a {t['poem']['name']} that adheres to its traditional rules:\n   {', '.join(t['poem']['rules'])}\n\n2. Incorporate the {t['sequence']['name']} sequence ({t['sequence']['rule']}) into your poem's structure. You must use at least two of the following methods:\n   - Use the sequence to determine the number of words in each line\n   - Use the sequence to determine the number of syllables in specific words\n   - Use the sequence to create a pattern of stressed syllables\n   - Use the sequence to determine the number of lines in each stanza (for longer poems)\n\n3. Ensure that the poem's content reflects the mathematical nature of the sequence, either explicitly or metaphorically. The connection should be clear and creative.\n\n4. Explain how you incorporated the {t['sequence']['name']} sequence into your poem's structure (3-4 sentences). Be specific about which methods you used from step 2.\n\n5. Analyze how the mathematical sequence influences the poem's rhythm, meaning, or overall effect (3-4 sentences). Include at least one specific example from your poem.\n\nProvide your response in the following format:\n\nPoem:\n[Your fractal poem here]\n\nSequence Incorporation:\n[Your explanation here]\n\nAnalysis:\n[Your analysis here]\n\nNote: Originality and creativity in your approach will be highly valued."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The poem strictly adheres to the traditional rules of a {t['poem']['name']}",
            f"The {t['sequence']['name']} sequence is clearly and creatively incorporated into the poem's structure using at least two of the suggested methods",
            "The poem's content reflects the mathematical nature of the sequence in a clear and original way, either explicitly or metaphorically",
            "The explanation of sequence incorporation is detailed, accurate, and covers at least two specific methods used",
            "The analysis demonstrates a deep understanding of how the mathematical sequence influences the poem, with at least one specific example from the poem",
            "The overall response shows high levels of creativity and originality in approach"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
