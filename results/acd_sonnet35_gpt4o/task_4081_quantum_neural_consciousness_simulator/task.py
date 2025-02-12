import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum entanglement",
            "quantum superposition",
            "quantum tunneling"
        ]
        consciousness_aspects = [
            "self-awareness",
            "subjective experience",
            "information integration"
        ]
        tasks = [
            {
                "quantum_principle": principle,
                "consciousness_aspect": aspect
            }
            for principle in quantum_principles
            for aspect in consciousness_aspects
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system that simulates neural correlates of consciousness, focusing on the quantum principle of {t['quantum_principle']} and the consciousness aspect of {t['consciousness_aspect']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the selected quantum principle and its potential relevance to consciousness.
   b) Describe the chosen aspect of consciousness and current neuroscientific understanding of it.
   c) Propose a hypothesis linking the quantum principle to the consciousness aspect.

2. Quantum-Neural Interface (300-350 words):
   a) Design a theoretical interface between quantum systems and neural networks.
   b) Explain how this interface incorporates the selected quantum principle.
   c) Describe how the interface models or simulates the chosen aspect of consciousness.
   d) Include a diagram or flowchart of your proposed interface using ASCII art or structured text (at least 15 lines).

3. Simulation Architecture (250-300 words):
   a) Outline the key components of your quantum consciousness simulation system.
   b) Explain how these components interact to model consciousness.
   c) Describe any novel quantum algorithms or neural network structures used in your system.

4. Theoretical Predictions (200-250 words):
   a) Propose specific, testable predictions your system could make about consciousness.
   b) Explain how these predictions differ from those of classical neuroscience models.
   c) Describe potential experiments to validate these predictions.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss ethical considerations of simulating consciousness in a quantum system.
   b) Explore philosophical questions raised by your proposed system.
   c) Consider potential societal impacts of this technology.

6. Limitations and Future Directions (150-200 words):
   a) Identify key limitations or challenges in your proposed system.
   b) Suggest potential improvements or extensions to your model.
   c) Propose future research directions in quantum consciousness simulation.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and its potential relevance to {t['consciousness_aspect']}",
            "The proposed quantum-neural interface is innovative and scientifically plausible",
            "The simulation architecture is well-designed and integrates quantum and neural principles effectively",
            "The theoretical predictions are specific, testable, and distinct from classical models",
            "The ethical and philosophical implications are thoughtfully considered",
            "The limitations and future directions are insightful and relevant",
            "The response shows creativity and interdisciplinary knowledge integration throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
