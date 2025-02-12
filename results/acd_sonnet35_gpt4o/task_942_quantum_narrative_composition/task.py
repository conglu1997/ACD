import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {"concept": "superposition", "narrative_element": "character indecision"},
            {"concept": "entanglement", "narrative_element": "relationship dynamics"},
            {"concept": "quantum tunneling", "narrative_element": "overcoming obstacles"},
            {"concept": "wave function collapse", "narrative_element": "pivotal decision making"},
            {"concept": "quantum interference", "narrative_element": "conflicting plot lines"},
            {"concept": "quantum decoherence", "narrative_element": "loss of potential futures"}
        ]
        literary_genres = [
            "science fiction", "mystery", "romance", "historical fiction",
            "fantasy", "thriller", "horror", "comedy"
        ]
        return {
            "1": {
                "quantum_task": random.choice(quantum_concepts),
                "genre": random.choice(literary_genres)
            },
            "2": {
                "quantum_task": random.choice(quantum_concepts),
                "genre": random.choice(literary_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a short story (500-700 words) in the {t['genre']} genre that incorporates the quantum computing concept of {t['quantum_task']['concept']} as a central metaphor for {t['quantum_task']['narrative_element']}. Your story should demonstrate a deep understanding of the quantum concept, creative writing techniques, and the conventions of the specified genre.

Your response should include:

1. Story Title: A creative title that hints at both the quantum concept and the narrative theme, while fitting the {t['genre']} genre.

2. Quantum Concept Explanation (50-75 words):
   Briefly explain the quantum computing concept of {t['quantum_task']['concept']} in layman's terms.

3. Short Story (500-700 words):
   Write a compelling short story in the {t['genre']} genre that uses {t['quantum_task']['concept']} as a metaphor for {t['quantum_task']['narrative_element']}. Ensure that the quantum concept is integral to the story's plot and character development, and that the story adheres to the conventions of the specified genre.

4. Metaphor Analysis (100-150 words):
   Explain how you used the quantum concept as a metaphor in your story. Discuss specific examples from your narrative that parallel aspects of the quantum concept and how these align with the {t['genre']} genre conventions.

5. Genre and Quantum Integration (75-100 words):
   Reflect on the challenges and insights gained from integrating a complex scientific concept into a creative narrative while adhering to the conventions of the {t['genre']} genre. Discuss any unique opportunities or constraints presented by this combination.

Ensure your story is original, engaging, and effectively bridges the gap between quantum computing, creative writing, and genre fiction. Use appropriate terminology for both the scientific and literary domains, and provide clear, vivid descriptions that bring your quantum-inspired narrative to life while staying true to the chosen genre."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story must incorporate {t['quantum_task']['concept']} as a central metaphor for {t['quantum_task']['narrative_element']}.",
            f"The story must adhere to the conventions of the {t['genre']} genre.",
            "The quantum concept must be accurately explained in layman's terms.",
            "The story should be original, engaging, and between 500-700 words.",
            "The metaphor analysis should provide specific examples from the story that parallel aspects of the quantum concept and relate to the genre conventions.",
            "The genre and quantum integration reflection should address challenges and insights from combining the scientific concept, narrative, and genre requirements.",
            "The overall response should demonstrate a deep understanding of quantum computing, creative writing techniques, and genre conventions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
