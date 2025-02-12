import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Tunneling",
            "Coherence"
        ]
        evolutionary_mechanisms = [
            "Natural selection",
            "Genetic drift",
            "Gene flow",
            "Mutation"
        ]
        ai_techniques = [
            "Neural networks",
            "Genetic algorithms",
            "Reinforcement learning",
            "Swarm intelligence"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired artificial ecosystem that simulates evolutionary processes, incorporating principles from quantum biology, artificial intelligence, and evolutionary theory. Your task is to create a model that integrates the following elements:

1. Quantum Principle: {t['quantum_principle']}
2. Evolutionary Mechanism: {t['evolutionary_mechanism']}
3. AI Technique: {t['ai_technique']}

Your response should include the following sections:

1. Ecosystem Design (300-350 words):
   a) Describe the overall structure and components of your quantum-inspired artificial ecosystem.
   b) Explain how you incorporate the specified quantum principle into your model.
   c) Detail how the evolutionary mechanism is implemented in your ecosystem.
   d) Discuss how the AI technique is integrated into the simulation.

2. Quantum-Biological Processes (250-300 words):
   a) Explain how quantum effects manifest in your simulated organisms or environment.
   b) Describe how these quantum processes interact with classical biological mechanisms.
   c) Provide an example of a unique behavior or property that emerges from this quantum-biological interaction.

3. Evolutionary Dynamics (250-300 words):
   a) Detail how evolution occurs in your quantum-inspired ecosystem.
   b) Explain how the specified evolutionary mechanism drives change in your model.
   c) Discuss how quantum effects influence the evolutionary process.

4. AI Integration and Analysis (200-250 words):
   a) Describe how the specified AI technique is used to simulate or analyze the ecosystem.
   b) Explain how AI enhances our understanding of the quantum and evolutionary processes in your model.
   c) Propose a specific insight or discovery that your AI system might uncover about quantum evolution.

5. Theoretical Implications (150-200 words):
   a) Discuss the potential implications of your model for our understanding of life and evolution.
   b) Explore how quantum effects might influence biological evolution in the real world, based on your model.
   c) Propose a testable hypothesis derived from your quantum evolutionary AI ecosystem.

6. Challenges and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in implementing your model.
   b) Suggest ways to overcome these challenges or improve the model.
   c) Propose future research directions or extensions of your quantum evolutionary AI ecosystem.

Ensure your response demonstrates a deep understanding of quantum mechanics, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts.",
            "The ecosystem design effectively integrates the specified quantum principle, evolutionary mechanism, and AI technique.",
            "The explanation of quantum-biological processes is scientifically plausible and creative.",
            "The evolutionary dynamics are well-described and logically connected to the quantum effects.",
            "The AI integration is clearly explained and demonstrates potential for novel insights.",
            "The theoretical implications and proposed hypothesis are thought-provoking and grounded in the model's design.",
            "Challenges and future directions are thoughtfully considered and relevant to the field.",
            "The overall response shows a deep integration of knowledge from quantum mechanics, evolutionary biology, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
