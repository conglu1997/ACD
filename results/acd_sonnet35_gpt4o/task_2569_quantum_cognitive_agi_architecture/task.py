import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Annealing"
        ]
        cognitive_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Predictive Processing",
            "Adaptive Resonance Theory"
        ]
        agi_challenges = [
            "Commonsense Reasoning",
            "Transfer Learning",
            "Meta-Learning",
            "Ethical Decision Making"
        ]
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_theory": random.choice(cognitive_theories),
                "agi_challenge": random.choice(agi_challenges)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_theory": random.choice(cognitive_theories),
                "agi_challenge": random.choice(agi_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical Artificial General Intelligence (AGI) architecture that incorporates quantum computing principles and is inspired by cognitive science theories of consciousness and information integration. AGI refers to highly autonomous systems that outperform humans at most economically valuable work. Your AGI design should specifically incorporate the quantum principle of {t['quantum_principle']}, draw inspiration from the cognitive theory of {t['cognitive_theory']}, and address the AGI challenge of {t['agi_challenge']}.

Your response should include the following sections:

1. Architectural Overview (300-400 words):
   a) Describe the overall structure of your AGI system, including its main components and their interactions.
   b) Explain how quantum computing principles are integrated into the architecture, focusing on {t['quantum_principle']}.
   c) Discuss how your design is inspired by {t['cognitive_theory']} and how it relates to consciousness or information integration.
   d) Provide a high-level diagram or description of your AGI architecture.

2. Quantum-Cognitive Integration (250-350 words):
   a) Explain in detail how {t['quantum_principle']} is utilized in your AGI system.
   b) Describe how this quantum principle enhances or enables cognitive processes inspired by {t['cognitive_theory']}.
   c) Discuss any novel emergent properties or capabilities that arise from this integration.

3. AGI Challenge Solution (200-300 words):
   a) Explain how your architecture addresses the AGI challenge of {t['agi_challenge']}.
   b) Describe specific mechanisms or processes in your design that contribute to solving this challenge.
   c) Compare your approach to traditional (non-quantum, non-cognitive) methods for addressing this AGI challenge.

4. Consciousness and Self-Awareness (200-300 words):
   a) Discuss how your AGI architecture might give rise to consciousness or self-awareness.
   b) Explain how {t['cognitive_theory']} contributes to this aspect of your design.
   c) Describe any quantum effects that might play a role in generating conscious-like phenomena.

5. Ethical and Philosophical Implications (150-250 words):
   a) Discuss the ethical considerations of developing an AGI with quantum-enhanced cognitive abilities.
   b) Explore the philosophical implications of your design, particularly regarding consciousness and free will.
   c) Propose guidelines for responsible development and use of such advanced AGI systems.

6. Technical Challenges and Future Directions (150-250 words):
   a) Identify key technical challenges in implementing your AGI architecture.
   b) Discuss any required advancements in quantum computing or neuroscience to realize your design.
   c) Propose future research directions to further develop and refine your AGI concept.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science theories, and artificial general intelligence concepts. Be innovative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1850 words. Remember to base your design on current scientific understanding while exploring speculative future possibilities."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AGI architecture clearly incorporates the quantum principle of {t['quantum_principle']}, draws inspiration from {t['cognitive_theory']}, and addresses the AGI challenge of {t['agi_challenge']}.",
            "The response demonstrates a deep understanding of quantum computing, cognitive science, and AGI principles.",
            "The proposed architecture is innovative, scientifically plausible, and well-reasoned.",
            "The integration of quantum principles and cognitive theories is clearly explained and justified.",
            "The response adequately addresses ethical and philosophical implications of the proposed AGI system.",
            "Technical challenges and future research directions are thoughtfully considered and discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
