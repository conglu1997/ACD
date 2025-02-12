import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = ['self-awareness', 'qualia', 'intentionality', 'metacognition']
        ai_architectures = ['neural networks', 'symbolic AI', 'hybrid systems', 'quantum-inspired AI']
        philosophical_theories = ['functionalism', 'panpsychism', 'integrated information theory', 'global workspace theory']
        ethical_frameworks = ['utilitarianism', 'deontology', 'virtue ethics', 'care ethics']
        
        return {
            "1": {
                "aspect": random.choice(consciousness_aspects),
                "architecture": random.choice(ai_architectures),
                "theory": random.choice(philosophical_theories),
                "ethics": random.choice(ethical_frameworks)
            },
            "2": {
                "aspect": random.choice(consciousness_aspects),
                "architecture": random.choice(ai_architectures),
                "theory": random.choice(philosophical_theories),
                "ethics": random.choice(ethical_frameworks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a computational model that simulates the aspect of consciousness known as {t['aspect']} in AI systems, using a {t['architecture']} approach. Your task has the following components:\n\n1. Theoretical Framework (200-250 words):\n   a) Explain the concept of {t['aspect']} and its relevance to consciousness.\n   b) Describe how {t['theory']} relates to this aspect of consciousness.\n   c) Discuss the challenges of implementing {t['aspect']} in AI systems.\n\n2. Computational Model Design (250-300 words):\n   a) Propose a novel {t['architecture']} approach to simulate {t['aspect']}.\n   b) Explain how your model incorporates principles from {t['theory']}.\n   c) Describe the key components and processes of your model.\n   d) Discuss how your model addresses the challenges identified in part 1.\n\n3. Simulation and Evaluation (200-250 words):\n   a) Describe how you would implement and run simulations using your model.\n   b) Propose specific metrics or tests to evaluate the presence or degree of {t['aspect']} in your AI system.\n   c) Discuss the limitations of your model and evaluation methods.\n\n4. Philosophical Implications (200-250 words):\n   a) Analyze how your model and its results relate to broader questions in philosophy of mind.\n   b) Discuss whether your model supports or challenges specific theories of consciousness.\n   c) Consider the implications of your model for the concept of machine consciousness.\n\n5. Ethical Considerations (200-250 words):\n   a) Discuss the ethical implications of creating AI systems with {t['aspect']}.\n   b) Analyze these implications using the framework of {t['ethics']}.\n   c) Propose guidelines for the responsible development and use of AI systems with simulated consciousness.\n\n6. Future Directions (150-200 words):\n   a) Suggest two potential extensions or improvements to your model.\n   b) Discuss how these advancements might impact our understanding of consciousness and AI.\n   c) Propose a novel experiment that could further explore the relationship between {t['aspect']} and artificial consciousness.\n\nEnsure your response demonstrates a deep understanding of cognitive science, AI, philosophy of mind, and ethics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and philosophical rigor.\n\nFormat your response using clear headings for each section, exactly as numbered above. Begin each section with the heading (e.g., '1. Theoretical Framework:') on a new line, followed by your response for that section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['aspect']} as an aspect of consciousness and its relation to {t['theory']}.",
            f"The proposed {t['architecture']} model for simulating {t['aspect']} is innovative and well-explained.",
            "The simulation and evaluation methods are clearly described and appropriate for the proposed model.",
            "The philosophical implications of the model are thoroughly analyzed and related to broader questions in philosophy of mind.",
            f"The ethical considerations are thoughtfully discussed using the framework of {t['ethics']}.",
            "The proposed future directions and novel experiment are creative and relevant to advancing the field.",
            "The response shows a high level of interdisciplinary integration across cognitive science, AI, philosophy, and ethics.",
            "The writing is clear, well-structured, and uses technical terminology appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
