import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "working memory",
            "attention allocation",
            "decision making",
            "pattern recognition"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        tasks = [
            {
                "cognitive_process": process,
                "quantum_principle": principle
            }
            for process in cognitive_processes
            for principle in quantum_principles
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-inspired neural network architecture that mimics the cognitive process of {t['cognitive_process']}, incorporating the quantum principle of {t['quantum_principle']}. Your task is to:

1. Architecture Design (300-350 words):
   a) Describe the key components of your quantum-inspired neural network architecture.
   b) Explain how it incorporates the specified quantum principle into its design.
   c) Detail how this architecture mimics or enhances the given cognitive process.
   d) Provide a high-level schematic or description of the architecture's structure.

2. Quantum-Classical Integration (200-250 words):
   a) Discuss how your architecture bridges quantum and classical computing paradigms.
   b) Explain any novel computational properties that emerge from this integration.
   c) Address potential challenges in implementing this hybrid architecture and propose solutions.

3. Cognitive Process Simulation (250-300 words):
   a) Describe how your architecture simulates or enhances the specified cognitive process.
   b) Compare your quantum-inspired approach to traditional neural network models for this cognitive function.
   c) Propose a specific cognitive task or experiment that could demonstrate the advantages of your architecture.

4. Implications for AI and Neuroscience (200-250 words):
   a) Discuss how your architecture could advance our understanding of both artificial and biological intelligence.
   b) Speculate on potential applications of this architecture in AI research or cognitive neuroscience.
   c) Address any ethical considerations related to the development and use of such quantum-cognitive models.

5. Technical Feasibility and Challenges (150-200 words):
   a) Assess the technical feasibility of implementing your architecture with current or near-future technology.
   b) Identify key technological or theoretical obstacles that need to be overcome.
   c) Propose a roadmap for the development and validation of your architecture.

Ensure your response demonstrates a deep understanding of quantum computing principles, neural network architectures, and cognitive neuroscience. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the cognitive process of {t['cognitive_process']} and incorporates the quantum principle of {t['quantum_principle']}.",
            "The quantum-inspired neural network architecture is novel, coherent, and scientifically plausible.",
            "The response demonstrates a deep understanding of quantum computing, neural networks, and cognitive neuroscience.",
            "The architecture design effectively bridges quantum and classical computing paradigms.",
            "The implications for AI and neuroscience are thoroughly explored and logically presented.",
            "The response is creative while maintaining scientific accuracy and interdisciplinary coherence.",
            "All five sections (Architecture Design, Quantum-Classical Integration, Cognitive Process Simulation, Implications for AI and Neuroscience, Technical Feasibility and Challenges) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
