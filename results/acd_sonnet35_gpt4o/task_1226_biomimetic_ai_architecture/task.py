import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            {
                "system": "insect swarm intelligence",
                "key_feature": "decentralized decision-making",
                "ai_application": "distributed computing"
            },
            {
                "system": "human immune system",
                "key_feature": "adaptive response to novel threats",
                "ai_application": "cybersecurity"
            },
            {
                "system": "plant root networks",
                "key_feature": "resource allocation and communication",
                "ai_application": "smart grid management"
            },
            {
                "system": "cetacean echolocation",
                "key_feature": "3D environment mapping",
                "ai_application": "autonomous navigation"
            },
            {
                "system": "cephalopod camouflage",
                "key_feature": "rapid pattern recognition and adaptation",
                "ai_application": "adaptive user interfaces"
            },
            {
                "system": "avian migration",
                "key_feature": "long-range navigation and energy optimization",
                "ai_application": "logistics and supply chain management"
            }
        ]
        return {
            "1": random.choice(biological_systems),
            "2": random.choice(biological_systems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel AI architecture inspired by {t['system']}, focusing on the key feature of {t['key_feature']}, and analyze its potential applications in {t['ai_application']}. Your response should include the following sections:\n\n1. Biological System Analysis (200-250 words):\n   a) Describe the key principles and mechanisms of {t['system']}.\n   b) Explain how {t['key_feature']} contributes to the system's effectiveness.\n   c) Discuss any notable adaptations or optimizations in this biological system.\n\n2. AI Architecture Design (250-300 words):\n   a) Propose a novel AI architecture that mimics or draws inspiration from {t['system']}.\n   b) Explain how your design incorporates {t['key_feature']}.\n   c) Describe the key components of your AI system and their interactions.\n   d) Include a high-level diagram or pseudocode representing your architecture.\n\n3. Application in {t['ai_application']} (200-250 words):\n   a) Explain how your biomimetic AI architecture could be applied to {t['ai_application']}.\n   b) Discuss the potential advantages of your approach over traditional AI methods.\n   c) Identify any challenges in implementing your system and propose solutions.\n\n4. Comparative Analysis (150-200 words):\n   a) Compare your biomimetic AI architecture to existing AI approaches in {t['ai_application']}.\n   b) Analyze the strengths and limitations of your bio-inspired approach.\n\n5. Ethical Considerations and Future Directions (150-200 words):\n   a) Discuss any ethical implications of implementing your biomimetic AI system.\n   b) Propose two potential research directions to further develop or expand upon your architecture.\n\nEnsure your response demonstrates a deep understanding of both the biological system and AI principles. Be creative in your design while maintaining scientific plausibility. Your total response should be between 950-1200 words. Include a word count at the end of your submission. Remember to provide a high-level diagram or pseudocode for your AI architecture as mentioned in section 2."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['system']} and its key feature of {t['key_feature']}.",
            f"The proposed AI architecture effectively incorporates principles from {t['system']} and addresses {t['ai_application']}.",
            "The design is innovative and scientifically plausible.",
            "A high-level diagram or pseudocode representing the AI architecture is included.",
            "The application analysis and comparative analysis are insightful and well-reasoned.",
            "Ethical considerations and future directions are thoughtfully addressed.",
            "The response follows the specified format with clearly labeled sections and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
