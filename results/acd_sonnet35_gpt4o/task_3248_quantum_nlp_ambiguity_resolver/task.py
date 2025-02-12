import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum interference",
            "quantum measurement"
        ]
        linguistic_challenges = [
            "lexical ambiguity",
            "syntactic ambiguity",
            "semantic ambiguity",
            "pragmatic ambiguity"
        ]
        nlp_applications = [
            "machine translation",
            "sentiment analysis",
            "named entity recognition",
            "question answering"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_challenge": random.choice(linguistic_challenges),
                "nlp_application": random.choice(nlp_applications)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_challenge": random.choice(linguistic_challenges),
                "nlp_application": random.choice(nlp_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing system capable of resolving linguistic ambiguities and understanding context using principles from quantum computing and cognitive science. Your system should specifically leverage the quantum principle of {t['quantum_principle']} to address the linguistic challenge of {t['linguistic_challenge']}, with a focus on improving {t['nlp_application']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired NLP system.
   b) Explain how it integrates classical NLP techniques with quantum computing principles.
   c) Detail how your system incorporates the specified quantum principle to address the linguistic challenge.
   d) Provide a diagram or pseudocode representation of a key algorithm in your system.

2. Ambiguity Resolution Mechanism (250-300 words):
   a) Explain how your system resolves the specified linguistic ambiguity using quantum-inspired methods.
   b) Discuss the advantages of using a quantum approach for this type of ambiguity resolution.
   c) Address any challenges or limitations in modeling language with your approach.

3. Context Understanding (200-250 words):
   a) Describe how your system captures and represents context in language processing.
   b) Explain any novel techniques used to maintain contextual information using quantum-inspired methods.
   c) Discuss how context understanding improves the specified NLP application.

4. Performance Analysis (200-250 words):
   a) Propose a method for evaluating the performance of your quantum-inspired NLP system.
   b) Compare the expected performance of your system to classical NLP approaches for the given application.
   c) Discuss any trade-offs between accuracy, computational complexity, and scalability.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss the potential ethical implications of using quantum-inspired NLP systems for language understanding.
   b) Address how your system might impact privacy, fairness, and transparency in NLP applications.
   c) Consider the practical challenges of implementing such a system with current or near-future technology.

6. Future Research Directions (150-200 words):
   a) Propose two potential improvements or extensions to your system.
   b) Discuss how emerging technologies in quantum computing or neuroscience could enhance your system's capabilities.
   c) Suggest a related NLP task that could benefit from a similar quantum-inspired approach.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and natural language processing. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed design of a quantum-inspired NLP system that incorporates {t['quantum_principle']} to address {t['linguistic_challenge']} in the context of {t['nlp_application']}.",
            "The system design should demonstrate a deep understanding of both quantum computing principles and natural language processing techniques.",
            "The proposed approach should be creative and speculative while maintaining scientific plausibility.",
            "The response should include a thorough analysis of the system's performance, ethical implications, and future research directions.",
            "The overall response should showcase interdisciplinary knowledge integration and creative problem-solving in the fields of quantum computing, linguistics, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
