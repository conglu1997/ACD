import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            {
                "name": "Ayapaneco",
                "location": "Mexico",
                "speakers": "2",
                "unique_feature": "complex tonal system"
            },
            {
                "name": "Njerep",
                "location": "Cameroon",
                "speakers": "4",
                "unique_feature": "click consonants"
            },
            {
                "name": "Dumi",
                "location": "Nepal",
                "speakers": "8",
                "unique_feature": "complex honorific system"
            },
            {
                "name": "Tehuelche",
                "location": "Argentina",
                "speakers": "5",
                "unique_feature": "extensive use of suffixes"
            }
        ]
        quantum_principles = ["superposition", "entanglement", "quantum tunneling", "quantum coherence"]
        return {
            "1": {
                "language": random.choice(endangered_languages),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "language": random.choice(endangered_languages),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system for preserving and analyzing the endangered language {t['language']['name']}, focusing on its {t['language']['unique_feature']} and incorporating the quantum principle of {t['quantum_principle']}. Your task has five parts:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum computing system for language preservation.
   b) Explain how it incorporates {t['quantum_principle']} in its design.
   c) Detail how the system will capture and represent the {t['language']['unique_feature']} of {t['language']['name']}.

2. Quantum-Linguistic Interface (200-250 words):
   a) Explain how your system translates linguistic data into quantum states.
   b) Describe how {t['quantum_principle']} enhances the analysis or storage of {t['language']['unique_feature']}.
   c) Discuss any challenges in mapping linguistic concepts to quantum information and how you address them.

3. Preservation and Analysis Algorithms (200-250 words):
   a) Propose a quantum algorithm for preserving or analyzing the {t['language']['unique_feature']} of {t['language']['name']}.
   b) Explain how this algorithm leverages {t['quantum_principle']} for improved performance or capabilities.
   c) Compare the potential advantages of your quantum approach to classical computational linguistics methods.

4. Cultural Context Integration (200-250 words):
   a) Describe how your system incorporates the cultural context of {t['language']['name']} speakers in {t['language']['location']}.
   b) Explain how this cultural integration enhances language preservation or analysis.
   c) Discuss ethical considerations in applying quantum computing to endangered language preservation.

5. Future Applications and Implications (150-200 words):
   a) Propose two potential applications of your quantum-linguistic system beyond {t['language']['name']} preservation.
   b) Discuss how this technology might impact the field of linguistics or quantum computing.
   c) Speculate on how quantum-enhanced language preservation could affect endangered language communities.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic analysis, and cultural preservation. Be innovative in your approach while maintaining scientific and technological plausibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of both {t['quantum_principle']} and the linguistic features of {t['language']['name']}, particularly its {t['language']['unique_feature']}.",
            "The proposed quantum computing system is innovative yet scientifically plausible.",
            "The quantum-linguistic interface is well-explained and addresses potential challenges.",
            "The preservation and analysis algorithms clearly leverage quantum principles for linguistic analysis.",
            "The cultural context of the language is thoughtfully integrated into the system design.",
            "Ethical considerations are adequately addressed.",
            "The proposed future applications are creative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
