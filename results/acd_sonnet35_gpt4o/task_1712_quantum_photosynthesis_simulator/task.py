import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = ['quantum coherence', 'quantum entanglement', 'quantum tunneling']
        photosynthetic_processes = ['light harvesting', 'electron transport', 'carbon fixation']
        optimization_goals = ['energy efficiency', 'carbon capture rate', 'adaptability to different light conditions']
        
        tasks = {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "photosynthetic_process": random.choice(photosynthetic_processes),
                "optimization_goal": random.choice(optimization_goals)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "photosynthetic_process": random.choice(photosynthetic_processes),
                "optimization_goal": random.choice(optimization_goals)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired computational system to simulate and optimize the {t['photosynthetic_process']} process in photosynthesis, focusing on the quantum effect of {t['quantum_effect']} and aiming to improve {t['optimization_goal']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the role of {t['quantum_effect']} in the {t['photosynthetic_process']} process.
   b) Describe how this quantum effect contributes to the efficiency of photosynthesis.
   c) Discuss the potential for optimizing {t['optimization_goal']} through quantum-inspired approaches.

2. Computational System Design (250-300 words):
   a) Outline the architecture of your quantum-inspired computational system.
   b) Explain how your system models the {t['photosynthetic_process']} process and incorporates {t['quantum_effect']}.
   c) Describe the key algorithms or techniques used in your simulation.

3. Optimization Strategy (200-250 words):
   a) Propose a method for optimizing {t['optimization_goal']} using your computational system.
   b) Explain how your optimization strategy leverages quantum principles.
   c) Discuss potential trade-offs or limitations in your approach.

4. Validation and Testing (200-250 words):
   a) Describe how you would validate your system's accuracy in simulating the {t['photosynthetic_process']} process.
   b) Propose experiments or tests to evaluate the effectiveness of your optimization strategy.
   c) Discuss how you would compare your system's performance to classical simulation methods.

5. Potential Applications (150-200 words):
   a) Suggest two potential real-world applications of your quantum-inspired photosynthesis simulator.
   b) Explain how these applications could contribute to addressing global challenges.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and computational modeling. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections: Theoretical Framework, Computational System Design, Optimization Strategy, Validation and Testing, and Potential Applications.",
            f"The design effectively incorporates the quantum effect of {t['quantum_effect']} in modeling the {t['photosynthetic_process']} process.",
            f"The proposed system demonstrates a clear strategy for optimizing {t['optimization_goal']}.",
            "The response shows a deep understanding of quantum mechanics, photosynthesis, and computational modeling.",
            "The proposed system and optimization strategy are innovative while maintaining scientific plausibility.",
            "The validation and testing methods are well-thought-out and appropriate for the proposed system.",
            "The potential applications are relevant and demonstrate an understanding of broader implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
