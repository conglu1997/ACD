import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                "challenge": "Urban heat island effect",
                "context": "Densely populated cities with high energy consumption and limited green spaces"
            },
            {
                "challenge": "Microplastic pollution in oceans",
                "context": "Accumulation of small plastic particles in marine ecosystems"
            },
            {
                "challenge": "Sustainable water purification",
                "context": "Limited access to clean water in developing regions"
            },
            {
                "challenge": "Carbon capture and storage",
                "context": "Reducing atmospheric CO2 levels to mitigate climate change"
            }
        ]
        return {
            "1": random.choice(environmental_challenges),
            "2": random.choice(environmental_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the environmental challenge of {t['challenge']} in the context of {t['context']}. Your task is to design a biomimetic solution that addresses this problem sustainably. Provide a detailed response addressing the following points:\n\n1. Problem Analysis (150-200 words):\n   a) Explain the key factors contributing to {t['challenge']}.\n   b) Discuss the environmental and societal impacts of this issue.\n   c) Identify the main requirements for an effective solution.\n\n2. Biological Inspiration (200-250 words):\n   a) Identify at least two biological systems or processes that could inspire a solution to this challenge.\n   b) Explain how these biological examples address similar problems in nature.\n   c) Analyze the key principles or mechanisms that make these biological solutions effective.\n\n3. Biomimetic Solution Design (250-300 words):\n   a) Propose an innovative biomimetic solution that addresses {t['challenge']}.\n   b) Explain how your design incorporates principles from the biological systems you identified.\n   c) Describe the key components and functionality of your solution.\n   d) Discuss how your design promotes sustainability and minimizes negative environmental impacts.\n\n4. Implementation and Scalability (200-250 words):\n   a) Outline the steps required to implement your solution in a real-world context.\n   b) Discuss potential challenges in scaling up your design and how they might be addressed.\n   c) Propose methods for testing and validating the effectiveness of your solution.\n\n5. Interdisciplinary Implications (150-200 words):\n   a) Explain how your biomimetic solution integrates knowledge from different scientific disciplines.\n   b) Discuss potential applications of your design principles in other fields or for other environmental challenges.\n   c) Reflect on how biomimicry as an approach can drive innovation in sustainable design.\n\nEnsure your response demonstrates a deep understanding of both the environmental challenge and the biological systems you've chosen as inspiration. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and addressing real-world constraints.\n\nFormat your response with clear headings for each section. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately analyzes the {t['challenge']} and its context.",
            "At least two relevant biological systems or processes are identified and explained as inspiration.",
            "The proposed biomimetic solution clearly incorporates principles from the identified biological systems.",
            "The design effectively addresses the environmental challenge and promotes sustainability.",
            "The implementation and scalability discussion is realistic and considers potential challenges.",
            "The response demonstrates interdisciplinary thinking and reflects on the broader implications of biomimicry.",
            "The answer shows creativity, scientific plausibility, and a deep understanding of biomimicry principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
