import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        decision_types = [
            "moral dilemmas",
            "financial decisions",
            "social interactions"
        ]
        tasks = [
            {
                "quantum_effect": effect,
                "decision_type": decision
            }
            for effect in quantum_effects
            for decision in decision_types
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum biological model of human decision-making focusing on {t['quantum_effect']} in {t['decision_type']}, implement it in an AI system, and analyze its ethical implications. Your response should include the following sections:

1. Quantum Biological Model (300-350 words):
   a) Explain how {t['quantum_effect']} might play a role in human decision-making processes for {t['decision_type']}.
   b) Describe a detailed model that integrates quantum effects with known neurobiological mechanisms.
   c) Provide a mathematical formalism (e.g., equations, matrices) to represent key aspects of your model.
   d) Discuss how this model differs from classical neuroscience models of decision-making.

2. AI Implementation (250-300 words):
   a) Propose an AI architecture that could implement your quantum biological model.
   b) Explain how the AI system would simulate quantum effects in its decision-making process.
   c) Describe how the AI would handle inputs and outputs related to {t['decision_type']}.

3. Comparative Analysis (200-250 words):
   a) Compare the decision-making process of your quantum-inspired AI with traditional AI approaches.
   b) Analyze potential advantages and limitations of your quantum biological AI model.
   c) Discuss how closely your AI model might approximate human decision-making in {t['decision_type']}.

4. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of using a quantum-inspired AI for {t['decision_type']}.
   b) Analyze potential societal impacts if such AI systems become widespread.
   c) Propose guidelines for responsible development and use of quantum biological AI.

5. Experimental Design (150-200 words):
   a) Propose an experiment to test the effectiveness of your quantum biological AI model.
   b) Describe how you would measure and compare its performance against human decision-makers and classical AI systems.

6. Future Directions (150-200 words):
   a) Suggest two potential advancements or applications of your quantum biological AI model.
   b) Discuss how these developments might influence our understanding of human cognition and AI capabilities.

Ensure your response demonstrates a deep understanding of quantum physics, biology, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should thoroughly address the quantum effect of {t['quantum_effect']} in the context of {t['decision_type']}",
            "The quantum biological model should be scientifically plausible, well-explained, and include appropriate mathematical formalism",
            "The AI implementation should clearly describe how it simulates quantum effects",
            "The ethical analysis should be comprehensive and consider multiple perspectives",
            "The response should demonstrate a deep understanding of quantum physics, biology, neuroscience, and AI",
            "The proposed experiment and future directions should be innovative and relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
