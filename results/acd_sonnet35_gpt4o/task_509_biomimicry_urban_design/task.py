import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            {
                "challenge": "Sustainable water management",
                "inspiration": "Desert beetle's water collection mechanism"
            },
            {
                "challenge": "Energy-efficient building cooling",
                "inspiration": "Termite mound ventilation systems"
            },
            {
                "challenge": "Urban air pollution reduction",
                "inspiration": "Giant sequoia's air filtration properties"
            },
            {
                "challenge": "Noise reduction in cities",
                "inspiration": "Owl's silent flight mechanism"
            },
            {
                "challenge": "Sustainable urban waste management",
                "inspiration": "Leaf-cutter ant's circular economy"
            }
        ]
        return {
            "1": random.choice(urban_challenges),
            "2": random.choice(urban_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a biomimetic solution for the urban challenge of {t['challenge']}, inspired by {t['inspiration']}. Your response should include:\n\n1. Biological Inspiration Analysis (250-300 words):\n   a) Describe the natural system or organism that serves as inspiration.\n   b) Explain the key biological principles or mechanisms relevant to the urban challenge.\n   c) Discuss how this biological system efficiently solves a similar problem in nature.\n\n2. Biomimetic Solution Design (300-350 words):\n   a) Propose an innovative solution to the urban challenge based on the biological inspiration.\n   b) Explain how your design mimics or adapts the natural system's principles.\n   c) Describe the key components and functionality of your biomimetic solution.\n\n3. Implementation and Scalability (250-300 words):\n   a) Outline the steps needed to implement your solution in an urban environment.\n   b) Discuss potential challenges in scaling the solution and how they might be addressed.\n   c) Explain how your solution could be adapted for different urban contexts or climates.\n\n4. Environmental Impact Assessment (200-250 words):\n   a) Analyze the potential environmental benefits of your biomimetic solution.\n   b) Discuss any possible negative environmental impacts and how they could be mitigated.\n   c) Compare the sustainability of your solution to traditional approaches to the urban challenge.\n\n5. Interdisciplinary Collaboration (200-250 words):\n   a) Identify the key disciplines and experts needed to fully develop and implement your solution.\n   b) Explain how knowledge from different fields would be integrated in the project.\n   c) Propose a framework for effective collaboration among diverse experts in this biomimetic urban design project.\n\nEnsure your response demonstrates a deep understanding of biological systems, urban planning, and environmental science. Be creative in your approach while maintaining scientific and practical feasibility. Use clear headings for each section of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the biological inspiration and its relevance to the urban challenge.",
            "The proposed biomimetic solution is innovative, feasible, and effectively addresses the given urban challenge.",
            "The implementation and scalability analysis is thorough and considers practical challenges.",
            "The environmental impact assessment is well-reasoned and considers both positive and negative effects.",
            "The interdisciplinary collaboration proposal is comprehensive and demonstrates an understanding of the diverse expertise required.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
