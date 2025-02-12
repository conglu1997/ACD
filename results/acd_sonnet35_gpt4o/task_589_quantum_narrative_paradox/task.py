import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "quantum superposition",
            "quantum entanglement",
            "wave-particle duality",
            "quantum tunneling",
            "Schrödinger's cat thought experiment"
        ]
        philosophical_paradoxes = [
            "the ship of Theseus",
            "the grandfather paradox",
            "Zeno's paradox",
            "the simulation hypothesis",
            "the omnipotence paradox"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "philosophical_paradox": random.choice(philosophical_paradoxes)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "philosophical_paradox": random.choice(philosophical_paradoxes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story (400-500 words) that incorporates the quantum physics concept of {t['quantum_concept']} and explores the philosophical paradox known as {t['philosophical_paradox']}. Your story should demonstrate a deep understanding of both the scientific concept and the philosophical issue, weaving them together in a compelling narrative.

After writing the story, provide an analysis (300-400 words) that addresses the following points:

1. Explain how you incorporated the quantum physics concept into your story and how it relates to the plot or characters.
2. Discuss how the philosophical paradox is explored in your narrative and its significance to the story's themes.
3. Analyze the potential implications of combining these ideas, both for scientific understanding and philosophical inquiry.
4. Reflect on how the narrative format allows for a unique exploration of these complex concepts.

Ensure your response demonstrates a thorough understanding of the quantum physics concept, a nuanced exploration of the philosophical paradox, and creative storytelling skills. Use appropriate scientific and philosophical terminology throughout your response.

Format your answer as follows:

Story:
[Your short story here]

Analysis:
[Your analysis here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately incorporates the quantum physics concept of {t['quantum_concept']}.",
            f"The narrative effectively explores the philosophical paradox known as {t['philosophical_paradox']}.",
            "The story demonstrates creativity and engaging storytelling.",
            "The analysis shows a deep understanding of both the quantum concept and the philosophical paradox.",
            "The response reflects on the implications of combining these ideas in a narrative format.",
            "Appropriate scientific and philosophical terminology is used throughout the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
