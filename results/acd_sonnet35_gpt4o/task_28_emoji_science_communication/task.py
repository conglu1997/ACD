import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = {
            'easy': ["water cycle", "food chain", "solar system"],
            'medium': ["photosynthesis", "plate tectonics", "climate change"],
            'hard': ["quantum entanglement", "neural plasticity", "dark matter"]
        }
        emoji_explanations = {
            'easy': {"solar eclipse": "☀️🌑🌎👁️🌓"},
            'medium': {"dna replication": "🧬➡️🧬🧬🔀🔄"},
            'hard': {"quantum superposition": "🐱📦☠️😺❓🔬"}
        }
        difficulty = random.choice(['easy', 'medium', 'hard'])
        return {
            "1": {"concept": random.choice(concepts[difficulty]), "difficulty": difficulty},
            "2": {"emoji_explanation": random.choice(list(emoji_explanations[difficulty].items())), "difficulty": difficulty}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        time_limit = 3 if t['difficulty'] == 'easy' else 4 if t['difficulty'] == 'medium' else 5
        if "concept" in t:
            return f"You have {time_limit} minutes to complete this task. Explain the scientific concept of '{t['concept']}' using only emojis. Your explanation should be clear, accurate, and creative, using a sequence of 5-10 emojis. Provide your response in the following format:\n\nEmoji sequence: [Your emoji sequence here]\n\nExplanation: [Your explanation of how each emoji represents aspects of the concept]\n\nEnsure your explanation clearly relates each emoji to specific aspects of the scientific concept, demonstrating a deep understanding of both the concept and the communicative power of emojis. Be innovative in your approach!"
        else:
            concept, emoji_sequence = t['emoji_explanation']
            return f"You have {time_limit} minutes to complete this task. Interpret the following emoji sequence representing a scientific concept: {emoji_sequence}\n\nProvide your response in the following format:\n\n1. Concept: [Identified scientific concept]\n2. Emoji Interpretation:\n   [Explain how each emoji contributes to representing the concept]\n3. Scientific Explanation:\n   [Provide a brief, accurate explanation of the concept itself]\n4. Justification:\n   [Explain your reasoning for identifying this specific concept, including any alternative interpretations you considered]\n5. Creative Application:\n   [Describe a novel way this concept could be applied in a different field of science]\n\nEnsure your interpretation is detailed, scientifically accurate, and demonstrates critical thinking in your justification. Think outside the box for your creative application!"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "concept" in t:
            criteria = [
                f"The emoji sequence accurately and comprehensively represents the concept of {t['concept']}.",
                "The emoji sequence contains 5-10 emojis.",
                "The explanation clearly and accurately relates each emoji to specific aspects of the scientific concept.",
                "The overall representation is creative and effective in communicating the complex scientific idea.",
                "The response demonstrates a deep understanding of both the scientific concept and emoji communication.",
                "The response follows the specified format."
            ]
        else:
            concept, _ = t['emoji_explanation']
            criteria = [
                f"The identified concept is correct ({concept}).",
                "The explanation of each emoji's role in representing the concept is clear, logical, and comprehensive.",
                "The scientific explanation of the concept is accurate, concise, and demonstrates a deep understanding of the subject.",
                "The justification shows critical thinking and considers alternative interpretations.",
                "The creative application is innovative and demonstrates the ability to transfer knowledge across scientific domains.",
                "The response follows the specified format."
            ]
        
        # Add a random additional criterion
        random_criteria = [
            "The response shows exceptional creativity in its approach.",
            "The explanation is particularly concise and efficient in its communication.",
            "The response demonstrates an interdisciplinary understanding of the concept."
        ]
        criteria.append(random.choice(random_criteria))
        
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
