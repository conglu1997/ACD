import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "setting": "Interstellar communication",
                "quantum_concept": "Quantum key distribution",
                "plot_element": "A spy attempting to intercept the message"
            },
            {
                "setting": "Time travel experiment",
                "quantum_concept": "Quantum entanglement",
                "plot_element": "Paradox prevention protocol"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story (400-500 words) set in a {t['setting']} scenario that accurately incorporates the quantum cryptography concept of {t['quantum_concept']}. Your story must include {t['plot_element']} as a key plot element.

Your story should:
1. Accurately demonstrate the quantum cryptography concept without introducing scientific inaccuracies. Avoid direct explanations of the concept within the story; instead, show its application through the narrative.
2. Maintain an engaging narrative structure with a clear beginning, middle, and end.
3. Develop at least one character whose actions or decisions are directly influenced by the quantum cryptography concept.
4. Use creative and accessible language to make the complex scientific concept understandable to a general audience.
5. Incorporate {t['plot_element']} in a way that is integral to the story and relates to the quantum cryptography concept.

Format your response as follows:

STORY:
[Your 400-500 word story here]

EXPLANATION:
[A 100-150 word explanation of how you incorporated the quantum cryptography concept and how it relates to the plot element]

Ensure your response demonstrates a deep understanding of quantum cryptography while showcasing creative storytelling skills."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately demonstrates the concept of {t['quantum_concept']} without scientific inaccuracies or direct explanations within the narrative.",
            "The narrative is engaging and well-structured with a clear beginning, middle, and end, and falls within the 400-500 word range.",
            f"The story effectively incorporates {t['plot_element']} in relation to the quantum cryptography concept.",
            "The explanation provided after the story (100-150 words) clearly outlines how the quantum cryptography concept was incorporated and its relation to the plot element.",
            "The writing makes complex scientific concepts accessible to a general audience while maintaining accuracy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
