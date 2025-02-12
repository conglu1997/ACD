import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_pairings = [
            ("color", "sound"),
            ("taste", "shape"),
            ("smell", "texture"),
            ("temperature", "emotion"),
            ("motion", "flavor")
        ]
        abstract_concepts = [
            "freedom",
            "justice",
            "time",
            "consciousness",
            "infinity"
        ]
        return {
            "1": {
                "pairing": random.choice(sensory_pairings),
                "concept": random.choice(abstract_concepts)
            },
            "2": {
                "pairing": random.choice(sensory_pairings),
                "concept": random.choice(abstract_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a synaesthetic language system based on the sensory pairing of {t['pairing'][0]} and {t['pairing'][1]}, then use it to describe the abstract concept of {t['concept']}. Your task has four parts:

1. Synaesthetic Language System (250-300 words):
   a) Explain how your language system translates experiences of {t['pairing'][0]} into {t['pairing'][1]} (or vice versa).
   b) Provide 5-7 example words or phrases in your language, along with their meanings.
   c) Describe the basic grammar or structure of your language system.

2. Abstract Concept Description (200-250 words):
   Using your synaesthetic language system, describe the abstract concept of {t['concept']}. Explain how the sensory pairing enhances or changes the understanding of this concept.

3. Cognitive Analysis (200-250 words):
   a) Analyze how your synaesthetic language might influence thought patterns and perception.
   b) Discuss potential cognitive advantages or disadvantages of using this language system.
   c) Explain how this language system might affect memory formation and recall.

4. Practical Applications (150-200 words):
   a) Propose two potential real-world applications for your synaesthetic language system.
   b) Explain how these applications could benefit fields such as education, therapy, or artistic expression.
   c) Discuss any challenges that might arise in implementing or using this language system.

Ensure your response demonstrates a deep understanding of synaesthesia, linguistics, and cognitive science. Be creative in your language design while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The synaesthetic language system clearly incorporates the sensory pairing of {t['pairing'][0]} and {t['pairing'][1]}.",
            "The language system is creative, coherent, and linguistically plausible.",
            f"The abstract concept of {t['concept']} is described using the synaesthetic language system in a meaningful way.",
            "The cognitive analysis shows insightful reasoning about the potential impacts of the synaesthetic language on thought and perception.",
            "The proposed practical applications are innovative and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
