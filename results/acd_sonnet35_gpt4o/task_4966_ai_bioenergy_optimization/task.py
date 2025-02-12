import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        algae_species = ['Chlorella vulgaris', 'Spirulina platensis', 'Dunaliella salina', 'Nannochloropsis gaditana']
        energy_types = ['biodiesel', 'bioethanol', 'biogas', 'biohydrogen']
        optimization_goals = ['maximize lipid production', 'increase biomass yield', 'enhance CO2 fixation', 'improve stress tolerance']
        environmental_factors = ['temperature fluctuations', 'nutrient limitations', 'light intensity variations', 'pH changes']
        performance_targets = ['30% increase in energy yield', '25% reduction in production costs', '40% improvement in CO2 fixation rate', '35% increase in stress tolerance']
        environmental_constraints = ['water usage reduction by 20%', 'zero increase in eutrophication risk', 'maintaining biodiversity in surrounding ecosystem', 'minimizing escape risk of genetically modified organisms']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'algae_species': random.choice(algae_species),
                'energy_type': random.choice(energy_types),
                'optimization_goal': random.choice(optimization_goals),
                'environmental_factor': random.choice(environmental_factors),
                'performance_target': random.choice(performance_targets),
                'environmental_constraint': random.choice(environmental_constraints)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system to optimize bioenergy production from the algae species {t['algae_species']}, focusing on {t['energy_type']} production. Your primary optimization goal is to {t['optimization_goal']}, while considering the environmental factor of {t['environmental_factor']}. You must achieve a performance target of {t['performance_target']} while adhering to the environmental constraint of {t['environmental_constraint']}.\n\nYour response should include the following sections:\n\n1. AI System Architecture (300-350 words):\n   a) Describe the overall structure and key components of your AI system for bioenergy optimization.\n   b) Explain how your system incorporates genetic engineering and machine learning techniques.\n   c) Detail how your AI system interfaces with bioreactors and monitoring equipment.\n   d) Discuss any novel features or innovations in your design.\n\n2. Genetic Engineering Strategy (250-300 words):\n   a) Outline your approach to genetically modifying {t['algae_species']} for improved {t['energy_type']} production.\n   b) Explain how your AI system guides the genetic engineering process.\n   c) Describe any safeguards or ethical considerations in your genetic modification approach.\n\n3. Machine Learning Implementation (250-300 words):\n   a) Detail the machine learning algorithms used in your system and their specific roles.\n   b) Explain how your AI system processes and analyzes data from bioreactors and other sources.\n   c) Describe how the system adapts to changing conditions and optimizes production over time.\n\n4. Environmental Factor Adaptation (200-250 words):\n   a) Explain how your AI system addresses the challenge of {t['environmental_factor']}.\n   b) Describe any predictive capabilities your system has for anticipating environmental changes.\n   c) Discuss how your system balances energy production with environmental sustainability.\n\n5. Optimization Process and Results (200-250 words):\n   a) Provide a step-by-step explanation of how your AI system would optimize {t['energy_type']} production.\n   b) Describe expected improvements in energy yield or efficiency.\n   c) Discuss any potential trade-offs or limitations in your optimization approach.\n\n6. Mathematical Model (150-200 words):\n   a) Present a mathematical model or algorithm that represents a key aspect of your AI system's optimization process.\n   b) Explain the variables, parameters, and equations in your model.\n   c) Discuss how this model contributes to achieving the specified performance target.\n\n7. Ethical and Safety Considerations (150-200 words):\n   a) Identify potential risks or ethical concerns related to your AI-driven bioenergy system.\n   b) Propose guidelines for responsible development and use of AI in biotechnology.\n   c) Discuss how your system ensures the containment and control of genetically modified algae.\n\n8. Future Developments and Broader Impact (150-200 words):\n   a) Suggest two potential improvements or extensions to your AI bioenergy optimization system.\n   b) Discuss how your approach might be applied to other areas of sustainable energy production.\n   c) Speculate on the potential long-term effects of AI-optimized bioenergy on global energy markets and climate change mitigation.\n\nEnsure your response demonstrates a deep understanding of biotechnology, energy science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing potential limitations.\n\nFormat your response with clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. AI System Architecture:') followed by your response for that section. Your total response should be between 1650-2050 words.\n\nIMPORTANT: Your response should be complete and coherent. Do not include any placeholder text or incomplete sections."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of biotechnology, energy science, and artificial intelligence in the context of bioenergy production from algae",
            f"The AI system design effectively incorporates genetic engineering and machine learning techniques for optimizing {t['energy_type']} production from {t['algae_species']}",
            f"The proposed solution addresses the specific optimization goal of {t['optimization_goal']} and considers the environmental factor of {t['environmental_factor']}",
            f"The solution presents a clear strategy to achieve the performance target of {t['performance_target']} while adhering to the environmental constraint of {t['environmental_constraint']}",
            "The response includes a relevant and well-explained mathematical model or algorithm for a key aspect of the AI system",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving",
            "Ethical considerations and potential risks are thoroughly discussed",
            "The response adheres to the specified format and word count requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
