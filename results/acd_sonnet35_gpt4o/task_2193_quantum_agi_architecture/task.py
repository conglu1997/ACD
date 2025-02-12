import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum annealing"
        ]
        agi_components = [
            "Knowledge representation",
            "Reasoning and problem-solving",
            "Learning and adaptation",
            "Natural language processing"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "agi_component": random.choice(agi_components)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "agi_component": random.choice(agi_components)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical architecture for an artificial general intelligence (AGI) system that leverages quantum computing principles to enhance its cognitive capabilities. Specifically, focus on integrating the quantum principle of {t['quantum_principle']} into the AGI component of {t['agi_component']}.

Your response should include the following sections:

1. Theoretical Foundation (200-250 words):
   a) Explain the chosen quantum principle and its potential relevance to AGI.
   b) Describe the selected AGI component and its role in general intelligence.
   c) Discuss potential synergies between the quantum principle and the AGI component.

2. Architecture Design (250-300 words):
   a) Propose a high-level architecture that integrates the quantum principle into the AGI component.
   b) Explain how quantum computing could enhance or transform the functionality of this component.
   c) Describe the key modules or subsystems in your architecture and their interactions.
   d) Include a simple diagram or flowchart of your proposed architecture (use ASCII art or a structured text description).

3. Quantum-Classical Interface (200-250 words):
   a) Explain how your architecture manages the interface between quantum and classical computing elements.
   b) Discuss any novel approaches or techniques used to leverage quantum advantages in a classical AGI framework.
   c) Address potential challenges in implementing this interface and propose solutions.

4. Cognitive Capabilities (150-200 words):
   a) Describe the expected enhanced cognitive capabilities resulting from your quantum-integrated AGI architecture.
   b) Provide specific examples of tasks or problems where your architecture might outperform classical AGI systems.

5. Theoretical Performance Analysis (150-200 words):
   a) Propose metrics to evaluate the performance of your quantum-enhanced AGI component.
   b) Discuss potential quantum advantages in terms of speed, efficiency, or cognitive capacity.
   c) Address any potential limitations or trade-offs in your approach.

6. Ethical and Philosophical Implications (100-150 words):
   a) Discuss ethical considerations specific to quantum-enhanced AGI systems.
   b) Explore philosophical questions raised by the integration of quantum principles into artificial general intelligence.

Ensure your response demonstrates a deep understanding of both quantum computing and artificial general intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1050-1350 words, not including the diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing principles and artificial general intelligence concepts.",
            "The proposed architecture clearly integrates the specified quantum principle into the given AGI component in a novel and plausible manner.",
            "The quantum-classical interface is well-explained and addresses potential challenges.",
            "The enhanced cognitive capabilities and potential advantages of the quantum-integrated AGI are clearly described and justified.",
            "The response includes thoughtful consideration of ethical and philosophical implications.",
            "The overall architecture is creative, innovative, and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
