import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'wave-particle duality', 'uncertainty principle']
        philosophical_concepts = ['dualism', 'determinism', 'existentialism', 'phenomenology']
        linguistic_features = ['ergative alignment', 'evidentiality', 'polysynthesis', 'switch-reference']
        paradoxes = ['Ship of Theseus', 'Grandfather paradox', 'Schrödinger\'s cat', 'Zeno\'s paradox']

        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "philosophical_concept": random.choice(philosophical_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "paradox": random.choice(paradoxes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "philosophical_concept": random.choice(philosophical_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "paradox": random.choice(paradoxes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a hypothetical language based on the quantum mechanical principle of {t['quantum_principle']}, the philosophical concept of {t['philosophical_concept']}, and the linguistic feature of {t['linguistic_feature']}. Then, use this language to describe the {t['paradox']}. Your response should include:

1. Language Design (200-250 words):
   a) Explain how your language incorporates the given quantum principle, philosophical concept, and linguistic feature.
   b) Describe the basic structure and rules of your language, including its phonology, morphology, and syntax.
   c) Provide at least three example words or phrases in your language, along with their meanings and how they reflect the incorporated concepts.

2. Paradox Description (150-200 words):
   a) Use your created language to describe the given paradox. Provide both the description in your language and an English translation.
   b) Explain how your language's unique features enhance or provide new insights into the paradox.

3. Cognitive Implications (100-150 words):
   a) Discuss how thinking in this language might affect cognition and perception of reality.
   b) Speculate on potential applications or consequences of using this language in scientific or philosophical discourse.

4. Limitations and Challenges (100-150 words):
   a) Identify at least two significant limitations or challenges in using your language for everyday communication.
   b) Propose potential solutions or adaptations to address these challenges.

Ensure your response is creative, logically consistent, and demonstrates a deep understanding of quantum mechanics, philosophy, and linguistics. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design effectively incorporates the quantum principle of {t['quantum_principle']}, the philosophical concept of {t['philosophical_concept']}, and the linguistic feature of {t['linguistic_feature']}.",
            "The language structure and rules are clearly explained and logically consistent.",
            "At least three example words or phrases are provided, with clear explanations of their meanings and relevance to the incorporated concepts.",
            f"The {t['paradox']} is described using the created language, with both the original description and an English translation provided.",
            "The response explains how the language's unique features provide new insights into the paradox.",
            "The cognitive implications of thinking in this language are thoughtfully discussed.",
            "Potential applications or consequences of using this language in scientific or philosophical discourse are speculated upon.",
            "At least two significant limitations or challenges of using the language for everyday communication are identified.",
            "Potential solutions or adaptations to address the identified challenges are proposed.",
            "The overall response demonstrates creativity, logical consistency, and a deep understanding of quantum mechanics, philosophy, and linguistics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
