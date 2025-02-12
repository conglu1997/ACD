import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        human_languages = [
            "Mandarin Chinese",
            "Arabic",
            "Swahili",
            "Hindi"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave function collapse"
        ]
        return {
            "1": {
                "human_language": random.choice(human_languages),
                "quantum_concept": random.choice(quantum_concepts)
            },
            "2": {
                "human_language": random.choice(human_languages),
                "quantum_concept": random.choice(quantum_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system for natural language processing and use it to translate between {t['human_language']} and a hypothetical quantum-based alien language. Your task should focus on the quantum concept of {t['quantum_concept']}. Provide your response in the following format:

1. Quantum NLP System Architecture (250-300 words):
   a) Describe the key components of your quantum NLP system.
   b) Explain how your system incorporates quantum computing principles, especially {t['quantum_concept']}.
   c) Detail how the system processes and represents linguistic information using quantum states.

2. Quantum-Based Alien Language (200-250 words):
   a) Design a hypothetical alien language based on quantum principles, particularly {t['quantum_concept']}.
   b) Explain how this language differs from human languages in its structure and expression.
   c) Provide an example of how a simple concept would be expressed in this quantum language.

3. Translation Mechanism (250-300 words):
   a) Describe the process of translating from {t['human_language']} to the quantum-based alien language.
   b) Explain how your system handles linguistic concepts that may not have direct quantum analogues.
   c) Discuss how {t['quantum_concept']} is utilized in the translation process.

4. Practical Example (200-250 words):
   a) Provide a short sentence in {t['human_language']}.
   b) Show the step-by-step process of how your system would translate this sentence into the quantum-based alien language.
   c) Explain the quantum states involved in representing the translated sentence.

5. Challenges and Limitations (150-200 words):
   a) Discuss the main challenges in implementing this quantum NLP system.
   b) Explain any limitations in translating between classical and quantum-based languages.
   c) Propose potential solutions or areas for future research to address these challenges.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of this technology for our understanding of language and quantum mechanics.
   b) Propose two potential applications of this system beyond interspecies communication.

Ensure your response demonstrates a deep understanding of both quantum computing and linguistics. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing principles, especially {t['quantum_concept']}.",
            f"The proposed system effectively integrates quantum computing concepts with natural language processing for {t['human_language']}.",
            "The quantum-based alien language design is creative, plausible, and well-explained.",
            "The translation mechanism and practical example demonstrate a clear understanding of both linguistic and quantum principles.",
            "The response addresses challenges, limitations, and potential applications thoroughly and insightfully."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
