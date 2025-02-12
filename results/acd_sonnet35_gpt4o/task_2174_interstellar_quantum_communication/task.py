import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            'Entanglement',
            'Superposition',
            'Quantum Teleportation',
            'Quantum Error Correction'
        ]
        astrophysical_phenomena = [
            'Gravitational Lensing',
            'Pulsars',
            'Magnetars',
            'Neutron Stars'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'quantum_principle': random.choice(quantum_principles),
                'astrophysical_phenomenon': random.choice(astrophysical_phenomena)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical interstellar communication system using the quantum principle of {t['quantum_principle']} and the astrophysical phenomenon of {t['astrophysical_phenomenon']}. Your response should include the following sections:

1. Theoretical Framework (200-250 words):
   a) Explain the key aspects of the specified quantum principle and astrophysical phenomenon.
   b) Discuss how these concepts could be leveraged for interstellar communication.
   c) Describe any potential synergies or challenges in combining these concepts.

2. Communication System Design (250-300 words):
   a) Outline the core components of your interstellar communication system.
   b) Explain how your system incorporates the specified quantum principle and astrophysical phenomenon.
   c) Describe the proposed mechanism for encoding, transmitting, and receiving information.
   d) Discuss any novel technologies or theoretical advances required for your system.

3. Information Theory Analysis (200-250 words):
   a) Analyze the theoretical information capacity of your communication system.
   b) Discuss potential sources of noise or interference and how they are mitigated.
   c) Compare the efficiency of your system to classical communication methods.

4. Implementation Challenges (150-200 words):
   a) Identify the major technological and scientific hurdles to realizing your system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss any limitations on the range or speed of communication using your system.

5. Ethical and Societal Implications (150-200 words):
   a) Explore the potential impact of your communication system on human society and interstellar relations.
   b) Discuss ethical considerations related to long-distance space communication.
   c) Propose guidelines for the responsible development and use of such technology.

6. Future Developments (100-150 words):
   a) Suggest potential extensions or modifications to your system.
   b) Propose a research question that arises from your design.
   c) Speculate on how this technology might evolve over the next century.

Ensure your response demonstrates a deep understanding of quantum mechanics, astrophysics, and information theory. Use appropriate terminology and provide clear explanations of complex concepts. Be creative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section and adhere to the specified word counts. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and {t['astrophysical_phenomenon']}.",
            "The communication system design effectively incorporates both the quantum principle and astrophysical phenomenon.",
            "The information theory analysis is thorough and scientifically sound.",
            "Implementation challenges and potential solutions are thoughtfully addressed.",
            "Ethical and societal implications are thoroughly explored.",
            "The response is creative while maintaining scientific plausibility.",
            "The response adheres to the specified format and word count guidelines (1050-1350 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
