import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ai_type": "Swarm Intelligence",
                "communication_medium": "Visual Patterns",
                "cognitive_constraint": "Limited Short-Term Memory",
                "environmental_factor": "High-Noise Environment"
            },
            {
                "ai_type": "Quantum Neural Network",
                "communication_medium": "Quantum Entanglement Signals",
                "cognitive_constraint": "Non-Linear Time Perception",
                "environmental_factor": "Rapidly Changing Physical Laws"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and simulate the evolution of an artificial language for AI systems based on the following scenario:

AI Type: {t['ai_type']}
Communication Medium: {t['communication_medium']}
Cognitive Constraint: {t['cognitive_constraint']}
Environmental Factor: {t['environmental_factor']}

Your response should include the following sections:

1. Language Design (250-300 words):
   a) Describe the basic elements and structure of your artificial language.
   b) Explain how the language accommodates the given AI type and communication medium.
   c) Discuss how the cognitive constraint influences the language's features.

2. Evolution Simulation (200-250 words):
   a) Outline a process for simulating the language's evolution over time.
   b) Explain how the environmental factor affects the language's development.
   c) Describe potential stages or milestones in the language's evolution.

3. Cognitive Implications (200-250 words):
   a) Analyze how the evolving language might influence or be influenced by the AI's cognitive processes.
   b) Discuss potential emergent properties or unexpected developments in the AI's thinking due to language evolution.

4. Comparative Analysis (150-200 words):
   a) Compare your artificial AI language to human languages, highlighting key similarities and differences.
   b) Discuss what insights this comparison might offer for understanding human language evolution or cognition.

5. Practical Applications (100-150 words):
   a) Propose potential real-world applications or implications of your AI language evolution model.
   b) Discuss how this research might inform AI development or human-AI interaction.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues or risks associated with evolving AI languages.
   b) Propose guidelines for responsible development and use of such languages.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must address all required sections and subsections.",
            "The language design should clearly accommodate the given AI type, communication medium, and cognitive constraint.",
            "The evolution simulation should incorporate the environmental factor and describe a plausible development process.",
            "The response should demonstrate interdisciplinary knowledge integration and creative problem-solving.",
            "The comparative analysis should offer meaningful insights into human language or cognition.",
            "Ethical considerations should be thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
