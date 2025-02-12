import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "physical_law": "Time flows in reverse",
                "consciousness_property": "Non-local awareness",
                "quantum_concept": "Entanglement"
            },
            {
                "physical_law": "Gravity repels instead of attracts",
                "consciousness_property": "Collective mind",
                "quantum_concept": "Superposition"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-based artificial life simulation to model the evolution of consciousness in a hypothetical universe where {t['physical_law']}. Your simulation should explore the emergence of {t['consciousness_property']} and incorporate the quantum concept of {t['quantum_concept']}. Provide your response in the following format:

1. Universe Design (250-300 words):
   a) Describe the key properties and physical laws of your hypothetical universe.
   b) Explain how {t['physical_law']} affects the fundamental nature of reality in this universe.
   c) Discuss the implications of this altered physics for the emergence of life and consciousness.

2. Quantum Simulation Architecture (300-350 words):
   a) Outline the core components of your quantum computing-based simulation.
   b) Explain how you incorporate {t['quantum_concept']} into your simulation design.
   c) Describe how your simulation models the evolution of artificial life forms in this universe.
   d) Discuss any novel quantum algorithms or approaches used in your simulation.

3. Consciousness Model (250-300 words):
   a) Propose a theoretical framework for modeling {t['consciousness_property']} in your simulation.
   b) Explain how this form of consciousness might emerge from the artificial life forms in your simulated universe.
   c) Describe the key indicators or measurements used to detect and analyze consciousness in your simulation.

4. Simulation Experiments (200-250 words):
   a) Propose 2-3 key experiments to run in your simulation to explore the evolution of consciousness.
   b) Describe the expected outcomes and how they might differ from consciousness evolution in our universe.
   c) Explain how these experiments could provide insights into the nature of consciousness and reality.

5. Philosophical Implications (200-250 words):
   a) Discuss the philosophical implications of your simulation results for our understanding of consciousness.
   b) Explore how the relationship between physical laws and conscious experience in your simulation might inform theories of mind and reality.
   c) Speculate on what your simulation suggests about the possibility of radically different forms of consciousness in the actual universe.

6. Technical Challenges and Solutions (150-200 words):
   a) Identify the main technical challenges in implementing your quantum simulation.
   b) Propose innovative solutions or approaches to overcome these challenges.
   c) Discuss any limitations of current quantum computing technology that might affect your simulation.

7. Ethical Considerations (150-200 words):
   a) Examine the ethical implications of creating simulated conscious entities.
   b) Discuss the responsibilities of researchers when dealing with potentially conscious simulations.
   c) Propose guidelines for the ethical development and use of consciousness-simulating quantum systems.

Ensure your response demonstrates a deep understanding of quantum computing, artificial life, cosmology, and consciousness studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the specific physical law '{t['physical_law']}' and its implications for the simulated universe.",
            f"The quantum simulation architecture effectively incorporates the concept of {t['quantum_concept']}.",
            f"The consciousness model provides a plausible framework for {t['consciousness_property']} in the simulated universe.",
            "The proposed experiments are innovative and relevant to exploring consciousness evolution in the simulated universe.",
            "The response demonstrates a deep understanding of quantum computing, artificial life, cosmology, and consciousness studies.",
            "The philosophical implications and ethical considerations are thoroughly explored and thought-provoking.",
            "The response is creative and speculative while maintaining scientific plausibility.",
            "The technical challenges and proposed solutions are well-reasoned and innovative.",
            "The response is well-structured, following the specified format and word count (1500-1850 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
