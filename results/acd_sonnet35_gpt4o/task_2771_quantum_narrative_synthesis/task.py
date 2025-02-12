import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Quantum Superposition",
            "Quantum Entanglement",
            "Quantum Tunneling",
            "Quantum Decoherence"
        ]
        story_themes = [
            "Time Travel",
            "Parallel Universes",
            "Artificial Intelligence",
            "Consciousness Transfer"
        ]
        return {
            "1": {"concept": random.choice(quantum_concepts), "theme": random.choice(story_themes)},
            "2": {"concept": random.choice(quantum_concepts), "theme": random.choice(story_themes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story that incorporates the quantum computing concept of {t['concept']} and explores its implications through a narrative lens focused on the theme of {t['theme']}. Then, analyze the story's scientific accuracy and literary merit. Follow these steps:

1. Short Story (400-500 words):
   Write a creative short story that integrates {t['concept']} into a narrative exploring {t['theme']}. Your story should:
   a) Accurately represent the quantum concept.
   b) Explore its implications within the given theme.
   c) Engage the reader with a compelling narrative.
   d) Maintain scientific plausibility while allowing for speculative elements.

2. Scientific Analysis (200-250 words):
   a) Explain how {t['concept']} is represented in your story.
   b) Assess the scientific accuracy of your depiction.
   c) Discuss any liberties taken for narrative purposes and their potential impact on scientific understanding.
   d) Propose a hypothetical experiment or technology that could emerge from the ideas in your story.

3. Literary Analysis (200-250 words):
   a) Analyze the narrative structure and character development in your story.
   b) Discuss how the quantum concept enhances or challenges the chosen theme.
   c) Explain any symbolism or metaphors used to convey scientific ideas.
   d) Reflect on the challenges and opportunities of integrating complex scientific concepts into fiction.

4. Interdisciplinary Implications (150-200 words):
   a) Discuss how your story might impact public understanding of quantum computing.
   b) Explore potential ethical considerations raised by your narrative.
   c) Propose an educational application of your story in teaching quantum concepts.

Ensure your response demonstrates a deep understanding of both quantum computing and narrative techniques. Be creative in your storytelling while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately incorporates the quantum concept of {t['concept']}.",
            f"The narrative effectively explores the theme of {t['theme']}.",
            "The scientific analysis demonstrates a deep understanding of the quantum concept.",
            "The literary analysis provides insightful commentary on the story's structure and themes.",
            "The interdisciplinary implications are thoughtfully considered and explained.",
            "The response maintains a balance between scientific accuracy and creative storytelling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
