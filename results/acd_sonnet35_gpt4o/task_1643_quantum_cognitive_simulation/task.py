import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            'Working Memory',
            'Pattern Recognition',
            'Decision Making',
            'Language Processing'
        ]
        quantum_concepts = [
            'Superposition',
            'Entanglement',
            'Quantum Tunneling',
            'Quantum Annealing'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'cognitive_process': random.choice(cognitive_processes),
                'quantum_concept': random.choice(quantum_concepts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate and enhance the cognitive process of {t['cognitive_process']}, leveraging the quantum concept of {t['quantum_concept']}. Then, analyze its potential impact on our understanding of cognition and AI development. Your response should include:

1. Quantum-Cognitive Interface Design (300-350 words):
   a) Describe the key components and functioning of your proposed quantum cognitive simulation system.
   b) Explain how it leverages {t['quantum_concept']} to simulate or enhance {t['cognitive_process']}.
   c) Discuss the theoretical basis for how quantum effects could influence this cognitive process.
   d) Address potential challenges in implementing quantum effects in cognitive simulations and propose solutions.

2. Simulation Protocol (250-300 words):
   a) Outline a detailed protocol for simulating {t['cognitive_process']} using your quantum system.
   b) Describe how you would measure and verify the system's performance in replicating or enhancing this cognitive process.
   c) Explain how your simulation incorporates current understanding of both quantum mechanics and cognitive science.
   d) Discuss potential limitations of your approach and how you might address them.

3. Cognitive Science Implications (200-250 words):
   a) Analyze how your quantum simulation might inform or challenge current theories of {t['cognitive_process']}.
   b) Discuss the implications of quantum effects in cognitive processing for our understanding of consciousness and intelligence.
   c) Consider how the ability to simulate cognitive processes through quantum means might affect our view of artificial vs. biological intelligence.

4. AI Development Impact (200-250 words):
   a) Explore how your quantum cognitive simulation system could influence the development of artificial intelligence.
   b) Discuss potential applications in enhancing AI capabilities, particularly in tasks related to {t['cognitive_process']}.
   c) Consider any risks or ethical concerns related to the development of quantum-enhanced AI systems.

5. Experimental Proposal (150-200 words):
   a) Design a hypothetical experiment to test a key aspect of your quantum cognitive simulation system.
   b) Describe the experimental setup, including any novel equipment or techniques required.
   c) Explain how you would analyze the results and what outcomes would support or refute your approach.

6. Future Research Directions (150-200 words):
   a) Suggest 2-3 follow-up research questions or experiments based on your proposal.
   b) Discuss how advances in this field might influence other areas of science and technology.
   c) Speculate on potential long-term implications for our understanding of mind, matter, and computation.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, and their potential intersections. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively describes a quantum computing system that simulates or enhances {t['cognitive_process']} using {t['quantum_concept']}.",
            "The simulation protocol is well-defined and incorporates principles from both quantum mechanics and cognitive science.",
            "The implications for cognitive science and AI development are thoroughly explored and plausible.",
            "The proposed experiment is well-designed and relevant to testing the system's key aspects.",
            "The response demonstrates a deep understanding of quantum computing and cognitive science concepts.",
            "The ideas presented are creative and innovative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
