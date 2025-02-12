import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        enhancement_types = [
            "Memory augmentation",
            "Sensory expansion",
            "Cognitive processing speed increase",
            "Emotional regulation"
        ]
        brain_regions = [
            "Hippocampus",
            "Neocortex",
            "Prefrontal cortex",
            "Amygdala"
        ]
        societal_impacts = [
            "Economic inequality",
            "Social dynamics",
            "Education systems",
            "Workforce composition"
        ]
        time_constraints = [
            "5 years",
            "20 years",
            "50 years",
            "100 years"
        ]
        
        return {
            "1": {
                "enhancement": random.choice(enhancement_types),
                "brain_region": random.choice(brain_regions),
                "impact": random.choice(societal_impacts),
                "time_constraint": random.choice(time_constraints)
            },
            "2": {
                "enhancement": random.choice(enhancement_types),
                "brain_region": random.choice(brain_regions),
                "impact": random.choice(societal_impacts),
                "time_constraint": random.choice(time_constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a simulation system for predicting the long-term effects of nanotechnology-based cognitive enhancements on human brain function and society, then use it to propose ethical guidelines for human augmentation research. Focus on the following parameters:\n\nPrimary enhancement type: {t['enhancement']}\nPrimary brain region: {t['brain_region']}\nPrimary societal impact: {t['impact']}\nTime constraint: {t['time_constraint']}\n\nYour response should include the following sections:\n\n1. Simulation System Architecture (300-350 words):\n   a) Describe the key components of your nanotech neuroenhancement simulation system.\n   b) Explain how your system models the interaction between nanotech enhancements and neural circuits in the specified brain region.\n   c) Detail how your simulation predicts long-term effects on brain function and plasticity within the given time constraint.\n   d) Discuss how your system integrates societal factors to model broader impacts.\n   e) Explain how your simulation accounts for potential technological advancements within the given time frame.\n   f) Include a high-level diagram or pseudocode illustrating your system's architecture (describe this textually).\n\n2. Nanotechnology-Neural Interface (250-300 words):\n   a) Explain the theoretical mechanism by which your nanotech enhancement interacts with neurons in the specified brain region.\n   b) Describe how your system models the gradual integration of nanotech with biological neural networks over time.\n   c) Discuss potential side effects or unintended consequences predicted by your model within the time constraint.\n   d) Explain how your system handles potential interactions between multiple cognitive enhancements.\n\n3. Cognitive Enhancement Simulation (250-300 words):\n   a) Detail how your system simulates the specified cognitive enhancement over the given time period.\n   b) Explain how you model individual variations in enhancement outcomes.\n   c) Describe any emergent phenomena or unexpected results predicted by your simulation.\n   d) Discuss how your simulation accounts for potential synergies or conflicts between different types of cognitive enhancements.\n\n4. Societal Impact Analysis (200-250 words):\n   a) Explain how your system models the specified societal impact of widespread cognitive enhancement within the time constraint.\n   b) Discuss any feedback loops or complex interactions identified by your simulation.\n   c) Predict potential long-term consequences for social structures and human relationships.\n   d) Analyze how the combination of multiple cognitive enhancements might amplify or mitigate societal impacts.\n\n5. Ethical Implications and Guidelines (250-300 words):\n   a) Based on your simulation results, discuss the key ethical concerns raised by this type of cognitive enhancement.\n   b) Propose a set of at least five specific, actionable ethical guidelines for research and development in this area of human augmentation.\n   c) Explain how these guidelines address potential risks and inequalities identified in your simulation.\n   d) Discuss potential unintended consequences of implementing these guidelines.\n   e) Consider how these guidelines might need to evolve as multiple cognitive enhancements become available.\n\n6. Future Scenarios and Challenges (200-250 words):\n   a) Present two potential future scenarios predicted by your simulation: one optimistic and one pessimistic.\n   b) Identify key technical and societal challenges that need to be overcome for safe and equitable implementation of this technology within the given time frame.\n   c) Suggest areas for future research to address uncertainties in your simulation model.\n   d) Discuss how the development of multiple cognitive enhancement technologies might create new challenges or opportunities.\n\nEnsure your response demonstrates a deep understanding of nanotechnology, neuroscience, complex systems modeling, and ethical reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and rigorous ethical consideration.\n\nFormat your response with clear headings for each section. Your total response should be between 1450-1750 words.\n\nIMPORTANT: Your response should be complete and coherent. Do not include any placeholder text or incomplete sections."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of nanotechnology, neuroscience, and complex systems modeling, with scientifically accurate explanations and plausible predictions within the given time constraint.",
            "The simulation system design effectively integrates nanotech enhancements with neural circuits and societal factors, showing a clear cause-and-effect relationship over time.",
            "The analysis of cognitive enhancement and societal impact is thorough and considers long-term consequences, supported by logical reasoning and relevant examples within the specified time frame.",
            "The proposed ethical guidelines are well-reasoned, comprehensive, and directly address potential risks and benefits identified in the simulation. At least five specific, actionable guidelines are provided.",
            "The response shows creativity and innovation while maintaining scientific plausibility and adhering to known principles of neuroscience and nanotechnology.",
            "The future scenarios and challenges presented are thought-provoking, logically derived from the simulation results, and consider multiple perspectives on human enhancement within the given time constraint.",
            "The response adequately addresses potential unintended consequences of both the technology and the proposed ethical guidelines.",
            "The simulation system accounts for potential interactions between multiple cognitive enhancements and their combined effects on individuals and society.",
            "The response includes a plausible explanation of how the simulation handles potential technological advancements within the given time constraint."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
