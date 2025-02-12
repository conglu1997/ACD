import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        group_theory_concepts = [
            "symmetry groups",
            "permutation groups",
            "cyclic groups",
            "dihedral groups"
        ]
        musical_elements = [
            "melody generation",
            "chord progression",
            "rhythm patterns",
            "musical form"
        ]
        return {
            "1": {
                "group_theory_concept": random.choice(group_theory_concepts),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "group_theory_concept": random.choice(group_theory_concepts),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses the group theory concept of {t['group_theory_concept']} to compose music, focusing on {t['musical_element']}. Your response should include the following sections:

1. Theoretical Framework (200-300 words):
   a) Explain the chosen group theory concept and its relevance to music composition.
   b) Describe how this concept can be applied to {t['musical_element']}.
   c) If possible, include a simple mathematical notation or formula related to the concept.

   Example (not to be used directly): Cyclic groups can be applied to chord progressions by representing the 12 pitch classes as elements of a group under addition modulo 12.

2. AI System Design (250-350 words):
   a) Outline the architecture of your AI system for music composition.
   b) Explain how the system incorporates the group theory concept.
   c) Describe the main algorithms or techniques used in your system.

3. Music Generation Process (200-300 words):
   a) Provide a step-by-step explanation of how your AI system would generate music.
   b) Describe how the group theory concept influences the composition process.

4. Example Composition (150-250 words):
   a) Describe a short musical piece that your system might generate.
   b) Explain how the group theory concept is reflected in the composition.

5. Implications and Future Directions (200-300 words):
   a) Discuss potential implications for mathematics, music theory, or AI research.
   b) Suggest ideas for expanding the system or applying it in other areas.

Ensure your response demonstrates understanding of both group theory and music theory. Balance mathematical accuracy with musical creativity and practical AI implementation. Your total response should be between 1000-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response explains the group theory concept {t['group_theory_concept']} and its application to {t['musical_element']} in music composition.",
            "The AI system design integrates group theory principles with music composition techniques in a coherent manner.",
            "The response demonstrates an understanding of both mathematical concepts and musical creativity in the context of AI-generated music.",
            "The example composition and implications discussed show innovative thinking about the intersection of group theory and music."
        ]
        results = eval_with_llm_judge(instructions, submission, criteria)
        return sum(results) / len(criteria) if isinstance(results, list) else 0.0
