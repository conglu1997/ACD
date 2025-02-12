import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_phenomena = [
            "state-dependent memory",
            "context-dependent forgetting",
            "retrieval-induced forgetting",
            "spacing effect",
            "testing effect"
        ]
        brain_regions = [
            "hippocampus",
            "prefrontal cortex",
            "amygdala",
            "cerebellum",
            "striatum"
        ]
        info_theory_concepts = [
            "mutual information",
            "Kolmogorov complexity",
            "channel capacity",
            "rate-distortion theory",
            "error correction codes"
        ]
        ml_techniques = [
            "recurrent neural networks",
            "reinforcement learning",
            "Bayesian inference",
            "sparse coding",
            "attention mechanisms"
        ]
        
        return {
            "1": {
                "phenomenon": random.choice(memory_phenomena),
                "brain_region": random.choice(brain_regions),
                "info_theory_concept": random.choice(info_theory_concepts),
                "ml_technique": random.choice(ml_techniques)
            },
            "2": {
                "phenomenon": random.choice(memory_phenomena),
                "brain_region": random.choice(brain_regions),
                "info_theory_concept": random.choice(info_theory_concepts),
                "ml_technique": random.choice(ml_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a computational model of human memory formation and retrieval that integrates principles from neuroscience, information theory, and machine learning. Your model should focus on explaining the phenomenon of {t['phenomenon']}, emphasizing the role of the {t['brain_region']}. Incorporate the information theory concept of {t['info_theory_concept']} and use {t['ml_technique']} as a key component of your model. Your response should include:\n\n1. Model Architecture (300-350 words):\n   a) Describe the main components of your memory model and how they interact.\n   b) Explain how your model incorporates neuroscientific principles, particularly regarding the {t['brain_region']}.\n   c) Detail how {t['info_theory_concept']} is integrated into your model's information processing.\n   d) Explain the role of {t['ml_technique']} in your model's learning and memory processes.\n   e) Provide a diagram or pseudocode representing your model's architecture.\n\n2. Memory Formation and Retrieval (250-300 words):\n   a) Describe step-by-step how your model simulates memory formation.\n   b) Explain the process of memory retrieval in your model.\n   c) Discuss how your model accounts for factors like attention, emotion, and prior knowledge.\n\n3. Simulating {t['phenomenon']} (200-250 words):\n   a) Explain how your model simulates or explains {t['phenomenon']}.\n   b) Provide a specific example scenario demonstrating this phenomenon in your model.\n   c) Discuss how your model's predictions compare to empirical findings on {t['phenomenon']}.\n\n4. Information Theoretic Analysis (200-250 words):\n   a) Analyze your model's memory processes using {t['info_theory_concept']}.\n   b) Explain how this analysis provides insights into memory efficiency or capacity.\n   c) Discuss any trade-offs or limitations revealed by this analysis.\n   d) Provide a quantitative estimate of your model's memory capacity or efficiency using appropriate units.\n\n5. Learning and Adaptation (200-250 words):\n   a) Describe how {t['ml_technique']} enables your model to learn and adapt.\n   b) Explain how this learning process relates to current theories of neuroplasticity.\n   c) Propose an experiment to test the learning capabilities of your model.\n   d) Provide a quantitative prediction of your model's learning rate or efficiency.\n\n6. Comparative Analysis (150-200 words):\n   a) Compare your model to at least two existing models of human memory.\n   b) Discuss the advantages and limitations of your approach.\n   c) Explain how your model addresses specific shortcomings of previous models.\n\n7. Implications and Future Directions (150-200 words):\n   a) Discuss the broader implications of your model for our understanding of human memory.\n   b) Propose two potential applications of your model in cognitive science or AI.\n   c) Suggest future research directions to refine or expand your model.\n\nEnsure your response demonstrates a deep understanding of neuroscience, information theory, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1450-1800 words.\n\nInclude a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, information theory, and machine learning principles.",
            f"The model effectively incorporates {t['info_theory_concept']} and {t['ml_technique']}.",
            f"The model convincingly simulates or explains {t['phenomenon']}.",
            "The response addresses all required sections comprehensively and coherently.",
            "The model design is innovative while maintaining scientific plausibility.",
            "The comparative analysis and future directions are thoughtful and well-reasoned.",
            "The response is well-structured, clear, and within the specified word count.",
            "The response includes quantitative estimates for memory capacity/efficiency and learning rate/efficiency.",
            "The proposed experiment to test the model's learning capabilities is well-designed and feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
