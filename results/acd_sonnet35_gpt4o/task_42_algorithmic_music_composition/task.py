import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_scales = ['major', 'minor', 'pentatonic', 'chromatic']
        mathematical_sequences = ['Fibonacci', 'prime numbers', 'powers of 2', 'triangular numbers']
        compositional_elements = ['rhythm', 'harmony', 'melody', 'dynamics']
        musical_techniques = ['counterpoint', 'modulation', 'ostinato', 'polyrhythm']
        musical_genres = ['baroque', 'classical', 'romantic', 'jazz', 'minimalism']
        
        return {
            "1": {
                "scale": random.choice(musical_scales),
                "sequence": random.choice(mathematical_sequences),
                "element": random.choice(compositional_elements),
                "technique": random.choice(musical_techniques),
                "genre": random.choice(musical_genres)
            },
            "2": {
                "scale": random.choice(musical_scales),
                "sequence": random.choice(mathematical_sequences),
                "element": random.choice(compositional_elements),
                "technique": random.choice(musical_techniques),
                "genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an algorithmic music composition based on the following constraints:\n\n1. Use the {t['scale']} scale as the basis for your composition.\n2. Incorporate the {t['sequence']} sequence into your algorithm to determine the {t['element']} of your composition.\n3. Include the technique of {t['technique']} in your algorithm.\n4. Describe your algorithm in 4-5 sentences, explaining how it integrates the given musical scale, mathematical sequence, and musical technique. Include at least one specific musical example in your description.\n5. Provide a short example (4-8 measures) of the musical output your algorithm would generate, using standard music notation or a clear textual representation. Ensure this example clearly demonstrates the use of the given scale, sequence, and technique.\n6. Analyze the potential musical implications of your algorithm, discussing its strengths and limitations (2-3 sentences). Include at least one potential limitation and one unexpected benefit.\n7. Explain how you would adapt your algorithm to compose in the style of {t['genre']} music (2-3 sentences). Provide at least two specific changes you would make to your algorithm.\n8. Compare your algorithmic approach to the style of a well-known composer or a specific musical period of your choice (2-3 sentences). Identify at least one similarity and one difference.\n\nFormat your response as follows:\n\nAlgorithm Description:\n[Your description here]\n\nExample Output:\n[Your example here]\n\nAnalysis:\n[Your analysis here]\n\nGenre Adaptation:\n[Your explanation here]\n\nStyleistic Comparison:\n[Your comparison here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The algorithm correctly incorporates the {t['scale']} scale, with at least one specific example of its use.",
            f"The {t['sequence']} sequence is effectively used to determine the {t['element']} of the composition, with a clear explanation of how it's applied.",
            f"The technique of {t['technique']} is properly integrated into the algorithm, with a demonstration of how it affects the composition.",
            "The algorithm description is clear, demonstrates understanding of musical, mathematical, and technical concepts, and includes at least one specific musical example.",
            f"The example output is consistent with the described algorithm, uses appropriate notation, and clearly demonstrates the use of the {t['scale']} scale, {t['sequence']} sequence, and {t['technique']} technique.",
            "The analysis provides insightful commentary on the algorithm's musical implications, including at least one potential limitation and one unexpected benefit.",
            f"The explanation of adapting the algorithm to {t['genre']} music is plausible, demonstrates understanding of the genre, and includes at least two specific changes to the algorithm.",
            "The stylistic comparison shows a good understanding of musical history and compositional techniques, identifying at least one similarity and one difference with the chosen composer or period.",
            "The response demonstrates creativity and originality in the algorithmic approach to music composition.",
            "The overall response shows a cohesive understanding of the relationships between mathematics, music theory, and compositional techniques."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
