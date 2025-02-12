import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling"
        ]
        language_aspects = [
            "semantic processing",
            "syntactic analysis",
            "language generation"
        ]
        tasks = {
            "1": {"quantum_principle": random.choice(quantum_principles),
                  "language_aspect": random.choice(language_aspects)},
            "2": {"quantum_principle": random.choice(quantum_principles),
                  "language_aspect": random.choice(language_aspects)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface that uses quantum computing principles to enhance language processing and communication. Your design should specifically incorporate the quantum principle of {t['quantum_principle']} to improve {t['language_aspect']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum neural language interface.
   b) Explain how it integrates quantum computing, neuroscience, and linguistics.
   c) Detail how {t['quantum_principle']} is applied to enhance {t['language_aspect']}.
   d) Include a high-level diagram of your system architecture (describe it textually).
   e) Provide a brief pseudocode snippet illustrating a key aspect of your system.

2. Quantum-Neural Integration (250-300 words):
   a) Explain how quantum processes interface with neural activity in your system.
   b) Describe the theoretical basis for this integration, citing relevant principles.
   c) Discuss potential advantages over classical computing approaches in language processing.

3. Language Processing Enhancement (250-300 words):
   a) Detail how your system enhances {t['language_aspect']} using {t['quantum_principle']}.
   b) Provide a specific example of how this enhancement would work in practice.
   c) Discuss potential improvements in language understanding or communication.

4. Implementation Challenges (200-250 words):
   a) Identify key technological hurdles in realizing your proposed system.
   b) Discuss challenges in maintaining quantum coherence in a biological environment.
   c) Address potential limitations or side effects of the brain-computer interface.

5. Ethical Considerations (200-250 words):
   a) Discuss ethical implications of a quantum neural language interface.
   b) Address privacy concerns related to direct brain-computer communication.
   c) Consider potential societal impacts of enhanced language processing capabilities.

6. Future Research Directions (150-200 words):
   a) Propose two potential extensions or applications of your system.
   b) Suggest experiments to validate the effectiveness of your quantum neural interface.
   c) Speculate on how this technology might influence cognitive science and linguistics.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and linguistics. Use appropriate terminology from all fields and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive explanation of a quantum neural language interface that incorporates {t['quantum_principle']} to enhance {t['language_aspect']}",
            "The system architecture is well-described and integrates quantum computing, neuroscience, and linguistics",
            "The quantum-neural integration is clearly explained with a solid theoretical basis",
            "The enhancement of language processing is detailed with specific examples",
            "Implementation challenges and ethical considerations are thoroughly discussed",
            "The response demonstrates deep understanding of quantum computing, neuroscience, and linguistics",
            "The proposed system is creative and speculative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
