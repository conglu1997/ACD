import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neural_processes = [
            {
                "process": "Memory consolidation",
                "brain_region": "Hippocampus",
                "quantum_aspect": "Quantum coherence in microtubules"
            },
            {
                "process": "Decision making",
                "brain_region": "Prefrontal cortex",
                "quantum_aspect": "Quantum entanglement in synaptic networks"
            },
            {
                "process": "Sensory perception",
                "brain_region": "Visual cortex",
                "quantum_aspect": "Quantum tunneling in ion channels"
            },
            {
                "process": "Emotional regulation",
                "brain_region": "Amygdala",
                "quantum_aspect": "Quantum superposition in neurotransmitter release"
            }
        ]
        return {
            "1": random.choice(neural_processes),
            "2": random.choice(neural_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate the neural process of {t['process']} in the {t['brain_region']}, focusing on the quantum aspect of {t['quantum_aspect']}. Then, compare it with classical approaches and analyze the ethical implications of using this system in a brain-computer interface. Your response should include:

1. Quantum Neural Simulation Design (300-350 words):
   a) Describe the architecture of your quantum computing system for simulating the specified neural process.
   b) Explain how your system models the quantum aspect mentioned, providing at least one relevant quantum algorithm or mathematical formulation.
   c) Discuss any novel quantum techniques used in your design, explaining their advantages.
   d) Provide a high-level schematic or pseudocode of your system's operation.
   e) Identify at least two potential limitations or drawbacks of your proposed system.

2. Neural Process Modeling (250-300 words):
   a) Explain how your quantum system models the specified neural process at both classical and quantum levels.
   b) Describe at least three advantages of your quantum approach over classical neural simulations.
   c) Discuss potential challenges in accurately simulating this neural process and propose solutions for each.

3. Comparison with Classical Approaches (200-250 words):
   a) Describe a state-of-the-art classical computing approach for simulating the same neural process.
   b) Compare the computational complexity of your quantum approach with the classical approach.
   c) Analyze the trade-offs between quantum and classical approaches in terms of accuracy, speed, and resource requirements.

4. Brain-Computer Interface Application (200-250 words):
   a) Propose a specific application of your quantum neural simulation in a brain-computer interface.
   b) Explain how this application could enhance or alter the simulated neural process.
   c) Discuss at least three potential benefits and three risks of this application for individuals and society.

5. Ethical Analysis (250-300 words):
   a) Identify and analyze at least three ethical concerns raised by the use of your quantum neural simulation in a brain-computer interface.
   b) Discuss how these ethical issues might be different from those raised by classical brain-computer interfaces.
   c) Propose specific guidelines or safeguards to address each ethical concern identified.
   d) Provide a detailed case study or scenario that illustrates one of the ethical dilemmas identified.

6. Future Implications and Research Directions (150-200 words):
   a) Speculate on how quantum neural simulations might evolve in the next decade, providing at least two specific predictions.
   b) Suggest two potential extensions of your system and their implications for neuroscience and ethics.
   c) Propose a novel research question that arises from the intersection of quantum computing, neuroscience, and ethics.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and ethical reasoning. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Adhere strictly to the word count specified for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically plausible design for a quantum computing system to simulate {t['process']} in the {t['brain_region']}, with at least one relevant quantum algorithm or mathematical formulation.",
            f"The quantum aspect of {t['quantum_aspect']} is clearly incorporated and explained in the neural process modeling, with at least three advantages over classical approaches identified.",
            "The comparison with classical approaches includes a description of a state-of-the-art classical method and a thorough analysis of trade-offs.",
            "The proposed brain-computer interface application is innovative, directly relates to the simulated neural process, and includes at least three benefits and three risks.",
            "The ethical analysis is thorough, identifying at least three relevant ethical concerns, proposing specific guidelines or safeguards for each, and including a detailed case study or scenario.",
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and ethics, with appropriate use of technical terminology and clear explanations of complex concepts.",
            "The future implications and research directions proposed are insightful and demonstrate creative thinking about the intersection of these fields, including two specific predictions and a novel research question.",
            "The response adheres to the specified word count for each section and the overall word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
