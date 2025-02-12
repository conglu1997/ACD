import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            "Ayapaneco",
            "Njerep",
            "Kaixana",
            "Sarcee",
            "Ainu"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum error correction",
            "quantum Fourier transform"
        ]
        linguistic_features = [
            "phonological patterns",
            "morphological structures",
            "syntactic rules",
            "semantic relationships",
            "pragmatic contexts"
        ]
        return {
            "1": {
                "language": random.choice(endangered_languages),
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "language": random.choice(endangered_languages),
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system for preserving and analyzing the endangered language {t['language']}, focusing on its {t['linguistic_feature']} and incorporating the quantum principle of {t['quantum_principle']}. Your task has five parts:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum computing system for language preservation.
   b) Explain how it incorporates {t['quantum_principle']} in its design.
   c) Detail how the system will capture and represent {t['linguistic_feature']} of {t['language']}.

2. Quantum-Linguistic Interface (200-250 words):
   a) Explain how your system translates linguistic data into quantum states.
   b) Describe how {t['quantum_principle']} enhances the analysis or storage of {t['linguistic_feature']}.
   c) Discuss any challenges in mapping linguistic concepts to quantum information and how you address them.

3. Preservation and Analysis Algorithms (200-250 words):
   a) Propose a quantum algorithm for preserving or analyzing {t['linguistic_feature']} of {t['language']}.
   b) Explain how this algorithm leverages {t['quantum_principle']} for improved performance or capabilities.
   c) Compare the potential advantages of your quantum approach to classical computational linguistics methods.

4. Cultural Context Integration (200-250 words):
   a) Describe how your system incorporates the cultural context of {t['language']} speakers.
   b) Explain how this cultural integration enhances language preservation or analysis.
   c) Discuss ethical considerations in applying quantum computing to endangered language preservation.

5. Future Applications and Implications (150-200 words):
   a) Propose two potential applications of your quantum-linguistic system beyond {t['language']} preservation.
   b) Discuss how this technology might impact the field of linguistics or quantum computing.
   c) Speculate on how quantum-enhanced language preservation could affect endangered language communities.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic analysis, and cultural preservation. Be innovative in your approach while maintaining scientific and technological plausibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of {t['language']} and its {t['linguistic_feature']}.",
            f"The system design should effectively incorporate the quantum principle of {t['quantum_principle']}.",
            "The proposed quantum-linguistic interface and algorithms should be innovative and well-explained.",
            "The response should address cultural context integration and ethical considerations.",
            "The future applications and implications should be relevant and thought-provoking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
