import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_effect": "quantum coherence",
                "environmental_condition": "low light",
                "optimization_goal": "energy transfer efficiency"
            },
            {
                "quantum_effect": "quantum entanglement",
                "environmental_condition": "high temperature",
                "optimization_goal": "carbon fixation rate"
            },
            {
                "quantum_effect": "quantum tunneling",
                "environmental_condition": "high salinity",
                "optimization_goal": "water use efficiency"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-enhanced photosynthesis system for a novel plant species, incorporating the quantum effect of {t['quantum_effect']}, optimized for {t['environmental_condition']} conditions, with the primary goal of improving {t['optimization_goal']}. Then, analyze its efficiency and propose experiments to test its viability. Your response should include:

1. Quantum-Enhanced Photosynthesis System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum-enhanced photosynthesis system.
   b) Explain how you incorporate the specified quantum effect into the photosynthetic process.
   c) Detail how your system is adapted to the given environmental condition.
   d) Discuss how your design aims to improve the specified optimization goal.

2. Quantum-Biological Integration (200-250 words):
   a) Explain how the quantum effect enhances or modifies the classical photosynthetic process.
   b) Describe any novel biological structures or molecules you've designed to harness the quantum effect.
   c) Provide a conceptual or mathematical representation of how quantum states contribute to the photosynthetic process.

3. Efficiency Analysis (200-250 words):
   a) Quantitatively estimate the improvement in efficiency compared to classical photosynthesis.
   b) Analyze potential limitations or trade-offs in your quantum-enhanced system.
   c) Discuss how your system's efficiency might vary under different environmental conditions.

4. Experimental Design (250-300 words):
   a) Propose two experiments to test the viability and efficiency of your quantum-enhanced photosynthesis system:
      - One in vitro experiment to isolate and measure the quantum effect
      - One in vivo experiment to assess the overall system performance
   b) For each experiment, describe:
      - The methodology and required equipment
      - The data you would collect and how you would analyze it
      - Potential challenges and how you would address them

5. Ecological and Practical Implications (150-200 words):
   a) Discuss the potential impact of your system on plant productivity and ecological balance.
   b) Analyze possible applications in agriculture, environmental remediation, or sustainable energy.
   c) Consider any ethical implications or potential risks of introducing quantum-enhanced plants into ecosystems.

Ensure your response demonstrates a deep understanding of quantum physics, plant biology, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should incorporate the quantum effect of {t['quantum_effect']}",
            f"The design should be appropriately optimized for {t['environmental_condition']} conditions",
            f"The system should demonstrate improvement in {t['optimization_goal']}",
            "The quantum-biological integration should be logically explained",
            "The efficiency analysis should include quantitative estimates",
            "The experimental designs should be well-thought-out and feasible",
            "The ecological and practical implications should be thoroughly analyzed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
