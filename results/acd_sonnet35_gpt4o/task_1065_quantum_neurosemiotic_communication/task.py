import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling"
        ]
        neuroscience_concepts = [
            "Neural oscillations",
            "Synaptic plasticity",
            "Neuroplasticity"
        ]
        semiotic_elements = [
            "Iconicity",
            "Indexicality",
            "Symbolism"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "neuroscience_concept": random.choice(neuroscience_concepts),
                "semiotic_element": random.choice(semiotic_elements)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "neuroscience_concept": random.choice(neuroscience_concepts),
                "semiotic_element": random.choice(semiotic_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical communication system that integrates principles from quantum mechanics, neuroscience, and semiotics. Your system should incorporate the quantum principle of {t['quantum_principle']}, the neuroscience concept of {t['neuroscience_concept']}, and the semiotic element of {t['semiotic_element']}. Provide your response in the following format:

1. System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum neurosemiotic communication system.
   b) Explain how it incorporates the specified quantum, neuroscience, and semiotic principles.
   c) Discuss any novel concepts or technologies you've invented for this system.
   d) Provide a diagram or schematic representation of your system (describe it in words).

2. Communication Process (250-300 words):
   a) Explain step-by-step how information is encoded, transmitted, and decoded in your system.
   b) Describe how your system handles complex or abstract concepts.
   c) Discuss any limitations or potential sources of error in the communication process.

3. Theoretical Implementation (200-250 words):
   a) Describe the theoretical hardware or biological interfaces required for your system.
   b) Explain how your system might be implemented or integrated with existing technologies or biological systems.
   c) Discuss any significant technical or biological challenges and propose potential solutions.

4. Applications and Implications (250-300 words):
   a) Propose three potential applications of your quantum neurosemiotic communication system in different fields (e.g., medicine, space exploration, education).
   b) Analyze the potential societal and ethical implications of widespread adoption of your system.
   c) Discuss how your system might influence or revolutionize our understanding of consciousness, cognition, or reality itself.

5. Comparative Analysis (200-250 words):
   a) Compare your quantum neurosemiotic communication system to existing communication technologies.
   b) Discuss the potential advantages and limitations of your system.
   c) Speculate on how your system might evolve or be improved in the future.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and semiotics. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide explanations where necessary.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system incorporates the quantum principle of {t['quantum_principle']}, the neuroscience concept of {t['neuroscience_concept']}, and the semiotic element of {t['semiotic_element']}",
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and semiotics",
            "The communication system design is innovative and scientifically plausible",
            "The response includes a clear explanation of the communication process, including encoding, transmission, and decoding of information",
            "The theoretical implementation is well-described, including hardware/biological interfaces and potential challenges",
            "Three potential applications in different fields are proposed and analyzed",
            "The response includes a thoughtful discussion of societal and ethical implications",
            "The comparative analysis with existing technologies is comprehensive and insightful",
            "The response is well-structured, following the provided format with clear sections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
