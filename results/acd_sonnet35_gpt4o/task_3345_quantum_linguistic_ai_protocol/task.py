import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            'Superposition',
            'Entanglement',
            'Quantum tunneling',
            'Wave function collapse'
        ]
        linguistic_features = [
            'Semantic density',
            'Pragmatic inference',
            'Syntactic ambiguity',
            'Phonological encoding'
        ]
        ai_applications = [
            'Multi-agent systems',
            'Swarm intelligence',
            'Federated learning',
            'Explainable AI'
        ]
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_feature': random.choice(linguistic_features),
                'ai_application': random.choice(ai_applications)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model and communication protocol for AI systems, leveraging the quantum principle of {t['quantum_principle']}, the linguistic feature of {t['linguistic_feature']}, and focusing on the AI application of {t['ai_application']}. Your response should include:

1. Quantum-Linguistic Model (300-350 words):
   a) Describe the key components of your quantum-inspired language model.
   b) Explain how you integrate {t['quantum_principle']} into the linguistic framework.
   c) Detail how your model enhances {t['linguistic_feature']} through quantum principles.
   d) Discuss any novel mathematical or conceptual representations used in your model.

2. AI Communication Protocol (250-300 words):
   a) Outline the communication protocol for AI systems using your quantum-linguistic model.
   b) Explain how this protocol enhances information exchange in {t['ai_application']}.
   c) Describe the encoding and decoding processes in your protocol.
   d) Discuss potential advantages over classical communication methods.

3. Implementation Strategy (200-250 words):
   a) Propose a high-level architecture for implementing your model and protocol.
   b) Discuss any required quantum or classical computing resources.
   c) Address potential challenges in realizing this system and suggest solutions.

4. Information Density Analysis (200-250 words):
   a) Analyze how your model improves information density compared to classical methods.
   b) Provide a quantitative estimate of the potential improvement, with justification.
   c) Discuss any trade-offs between information density and other factors (e.g., error rates, computational complexity).

5. Semantic Representation (150-200 words):
   a) Explain how your model enhances semantic representation in AI communication.
   b) Provide an example of how complex concepts might be more efficiently represented.
   c) Discuss implications for AI reasoning and knowledge representation.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical concerns related to highly efficient AI-to-AI communication.
   b) Analyze possible impacts on human-AI interaction and transparency.
   c) Propose guidelines for responsible development and use of such communication systems.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, linguistics, and artificial intelligence.",
            "The proposed quantum-linguistic model and communication protocol are innovative and scientifically plausible.",
            f"The model effectively integrates the quantum principle of {t['quantum_principle']} and enhances the linguistic feature of {t['linguistic_feature']}.",
            f"The communication protocol shows clear advantages for the AI application of {t['ai_application']}.",
            "The response includes thoughtful analysis of information density, semantic representation, and ethical implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
