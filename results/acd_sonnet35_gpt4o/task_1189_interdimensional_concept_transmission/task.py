import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_concepts = [
            "Free will",
            "Consciousness",
            "Ethics",
            "Beauty",
            "Justice",
            "Truth",
            "Identity",
            "Meaning",
            "Reality",
            "Knowledge"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Wave-particle duality",
            "Quantum tunneling",
            "Uncertainty principle"
        ]
        information_theory_concepts = [
            "Entropy",
            "Channel capacity",
            "Error correction",
            "Data compression",
            "Cryptography"
        ]
        
        tasks = {}
        for i in range(2):
            concept = random.choice(philosophical_concepts)
            quantum_principle = random.choice(quantum_principles)
            info_theory_concept = random.choice(information_theory_concepts)
            
            tasks[str(i+1)] = {
                "concept": concept,
                "quantum_principle": quantum_principle,
                "info_theory_concept": info_theory_concept
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for encoding and transmitting the abstract philosophical concept of {t['concept']} using the quantum mechanical principle of {t['quantum_principle']} and the information theory concept of {t['info_theory_concept']}. Then, analyze its implications for interstellar communication. Your response should include:

1. Concept Encoding (250-300 words):
   a) Explain how you would represent {t['concept']} using quantum states or processes.
   b) Describe how {t['quantum_principle']} is utilized in your encoding scheme.
   c) Discuss how {t['info_theory_concept']} is applied to optimize or secure the transmission.

2. Transmission Protocol (200-250 words):
   a) Outline a method for transmitting your encoded concept across vast distances.
   b) Explain how your protocol maintains the integrity of the quantum information.
   c) Discuss any potential issues with interstellar transmission and how you address them.

3. Decoding and Interpretation (200-250 words):
   a) Describe how an alien civilization might decode and interpret your transmission.
   b) Explain any assumptions about universal physical or mathematical principles.
   c) Discuss potential challenges in cross-species philosophical understanding.

4. Implications Analysis (200-250 words):
   a) Analyze the implications of your system for interstellar communication and knowledge sharing.
   b) Discuss how this method of concept transmission might influence alien understanding of human thought.
   c) Explore potential consequences for human philosophy and science if we received a similar transmission.

5. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of sharing complex philosophical ideas with unknown civilizations.
   b) Address potential risks or benefits of such communication.
   c) Propose guidelines for responsible interstellar philosophical exchanges.

Ensure your response demonstrates a deep understanding of the chosen philosophical concept, quantum mechanics, and information theory. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given philosophical concept, quantum mechanical principle, and information theory concept",
            "The encoding system creatively and plausibly integrates the philosophical concept with the specified quantum and information theory principles",
            "The transmission protocol and decoding method are logically explained and consider interstellar challenges",
            "The implications analysis shows insightful thinking about the consequences of such communication",
            "The ethical considerations are thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
