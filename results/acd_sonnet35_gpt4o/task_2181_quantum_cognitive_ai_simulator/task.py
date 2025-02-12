import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_cognitive_phenomena = [
            {
                "phenomenon": "Quantum coherence in microtubules",
                "cognitive_process": "Decision making"
            },
            {
                "phenomenon": "Quantum entanglement in neural networks",
                "cognitive_process": "Memory formation"
            },
            {
                "phenomenon": "Quantum tunneling in synaptic transmission",
                "cognitive_process": "Learning"
            },
            {
                "phenomenon": "Quantum superposition in mental states",
                "cognitive_process": "Consciousness"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(quantum_cognitive_phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates potential quantum effects in human cognition, focusing on the quantum phenomenon of {t['phenomenon']} and its possible role in the cognitive process of {t['cognitive_process']}. Then, explore the implications of this quantum-cognitive model for artificial intelligence. Your response should include the following sections:

1. Quantum-Cognitive Model (300-350 words):
   a) Explain the quantum phenomenon and how it might manifest in the brain.
   b) Describe how this quantum effect could influence the specified cognitive process.
   c) Propose a theoretical model that integrates quantum mechanics with cognitive science.
   d) Discuss any existing scientific evidence or theories that support or challenge your model.
   e) Address the scale discrepancy between quantum effects and neural processes.

2. AI Simulation Architecture (250-300 words):
   a) Design an AI system architecture that can simulate your quantum-cognitive model.
   b) Explain how your system represents and processes quantum and cognitive information.
   c) Describe any novel algorithms or data structures used in your simulation.
   d) Provide a high-level pseudocode or diagram illustrating a key component of your system.
   e) Discuss how your system handles the probabilistic nature of quantum phenomena.

3. Simulation Scenarios (200-250 words):
   a) Propose two specific scenarios to test your quantum-cognitive AI simulation.
   b) Describe the expected outcomes and how they might differ from classical cognitive models.
   c) Explain how you would validate the results of your simulation.
   d) Discuss potential limitations or biases in your simulation approach.

4. Implications for AI Development (200-250 words):
   a) Discuss how your quantum-cognitive model could influence AI design and capabilities.
   b) Explore potential advantages and challenges of incorporating quantum effects in AI systems.
   c) Propose a novel AI application that could leverage quantum-cognitive principles.
   d) Analyze potential impacts on AI performance, efficiency, or problem-solving abilities.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to simulating quantum effects in cognition.
   b) Discuss the philosophical implications of quantum consciousness for AI development.
   c) Propose guidelines for responsible research and development in this field.
   d) Consider potential misuse or unintended consequences of this technology.

6. Future Research Directions (100-150 words):
   a) Suggest two promising areas for future research in quantum-cognitive AI.
   b) Briefly describe potential experiments or technological developments that could advance this field.
   c) Discuss interdisciplinary collaborations that could contribute to this research.

Ensure your response demonstrates a deep understanding of quantum physics, cognitive science, and artificial intelligence. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should thoroughly address the quantum phenomenon of {t['phenomenon']} and its potential role in {t['cognitive_process']}",
            "The proposed AI simulation architecture should be coherent, scientifically plausible, and demonstrate an understanding of both quantum and cognitive processes",
            "The response should demonstrate a deep understanding of quantum physics, cognitive science, and artificial intelligence, using appropriate terminology and concepts from each field",
            "The implications for AI development should be thoughtfully explored, including potential advantages, challenges, and novel applications",
            "The ethical considerations should be thoroughly addressed, including philosophical implications and potential misuse",
            "The response should be creative and speculative while maintaining scientific integrity and acknowledging current limitations in our understanding of quantum effects in cognition",
            "The proposed simulation scenarios and future research directions should be innovative and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
