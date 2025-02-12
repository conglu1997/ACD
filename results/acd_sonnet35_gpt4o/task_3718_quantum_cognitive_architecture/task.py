import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        cognitive_processes = [
            "Decision making",
            "Memory formation",
            "Attention",
            "Learning"
        ]
        biological_systems = [
            "Photosynthesis",
            "Magnetoreception",
            "Olfaction",
            "Enzyme catalysis"
        ]
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "biological_system": random.choice(biological_systems)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "biological_system": random.choice(biological_systems)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired cognitive architecture that integrates principles from quantum biology, artificial neural networks, and cognitive science to model advanced cognitive processes. Your architecture should focus on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and draw inspiration from the biological system of {t['biological_system']}.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain the chosen quantum principle and its potential role in cognitive processes.
   b) Describe how the selected biological system demonstrates quantum effects and how this relates to the cognitive process.
   c) Discuss how these concepts could be integrated into a quantum-inspired cognitive architecture.

2. Architecture Design (350-400 words):
   a) Outline the main components of your quantum cognitive architecture.
   b) Explain how your architecture incorporates the specified quantum principle and cognitive process.
   c) Describe how your architecture is inspired by the biological system and artificial neural networks.
   d) Discuss how information is represented, processed, and transmitted in your architecture.

3. Cognitive Process Model (250-300 words):
   a) Explain in detail how your architecture models the specified cognitive process.
   b) Describe any novel algorithms or methods used in your architecture.
   c) Compare your model to classical cognitive architectures and discuss potential advantages.

4. Simulation Proposal (200-250 words):
   a) Propose a specific experiment or simulation to test your quantum cognitive architecture.
   b) Describe the expected outcomes and how they would validate your model.
   c) Discuss any technical challenges in implementing such a simulation.

5. Implications and Future Directions (200-250 words):
   a) Analyze the potential implications of your architecture for our understanding of cognition and quantum biology.
   b) Discuss how your architecture might influence the development of advanced AI systems.
   c) Propose future research directions or extensions of your model.

6. Ethical Considerations (150-200 words):
   a) Discuss any ethical implications of developing quantum-inspired cognitive architectures.
   b) Consider potential risks or misuses of such technology.
   c) Propose guidelines for responsible research and development in this field.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, artificial intelligence, and cognitive science. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive theoretical framework that integrates {t['quantum_principle']}, {t['cognitive_process']}, and draws inspiration from {t['biological_system']}.",
            "The architecture design effectively incorporates quantum principles, cognitive processes, and biological inspiration.",
            "The cognitive process model demonstrates a novel approach to modeling the specified process using quantum-inspired methods.",
            "The simulation proposal is well-thought-out and addresses potential challenges.",
            "The response discusses implications, future directions, and ethical considerations in depth.",
            "The submission demonstrates a deep understanding and creative integration of quantum mechanics, neuroscience, artificial intelligence, and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
