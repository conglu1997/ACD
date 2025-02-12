import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_adaptations = [
            "lotus leaf hydrophobicity",
            "gecko foot adhesion",
            "butterfly wing light manipulation",
            "spider silk strength",
            "shark skin drag reduction"
        ]
        engineering_challenges = [
            "water repellent surfaces",
            "reversible adhesives",
            "structural coloration",
            "high-strength materials",
            "fluid dynamics optimization"
        ]
        environmental_changes = [
            "increasing global temperatures",
            "rising sea levels",
            "increased UV radiation",
            "atmospheric composition changes",
            "extreme weather events"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "adaptation": random.choice(biological_adaptations),
                "challenge": random.choice(engineering_challenges),
                "environmental_change": random.choice(environmental_changes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a biomimetic engineering solution inspired by {t['adaptation']} to address the challenge of {t['challenge']}. Additionally, consider how your solution might adapt to {t['environmental_change']}. Your response should include the following sections:\n\n1. Biological Inspiration (200-250 words):\n   a) Describe the key features and mechanisms of {t['adaptation']}.\n   b) Explain how this adaptation benefits the organism in its natural environment.\n   c) Identify the core principles that make this adaptation effective.\n\n2. Engineering Solution (250-300 words):\n   a) Propose a detailed engineering solution inspired by {t['adaptation']}.\n   b) Explain how your solution addresses the challenge of {t['challenge']}.\n   c) Describe the key components and mechanisms of your design.\n   d) Discuss how your solution translates biological principles into technological applications.\n\n3. Materials and Fabrication (150-200 words):\n   a) Specify the materials required for your biomimetic solution.\n   b) Outline the fabrication process or manufacturing techniques needed to produce your design.\n   c) Address any challenges in scaling up the production of your solution.\n\n4. Performance Analysis (200-250 words):\n   a) Predict the performance of your biomimetic solution in addressing {t['challenge']}.\n   b) Compare your solution to existing non-biomimetic approaches to the same challenge.\n   c) Discuss any limitations or trade-offs in your design.\n   d) Analyze the scalability of your solution for large-scale implementation.\n\n5. Broader Implications (200-250 words):\n   a) Explore potential applications of your biomimetic solution beyond the initial challenge.\n   b) Discuss how your approach might inspire other biomimetic innovations.\n   c) Consider any ethical implications or environmental impacts of your solution.\n   d) Propose strategies to mitigate any negative environmental consequences of implementing your solution at scale.\n\n6. Adaptive Potential (200-250 words):\n   a) Describe how your solution might need to adapt to {t['environmental_change']}.\n   b) Propose modifications or enhancements to your original design to address this environmental change.\n   c) Discuss any new challenges or opportunities that may arise from these adaptations.\n   d) Consider how the principles of biomimicry could guide these future adaptations.\n\nEnsure your response demonstrates a deep understanding of both biological systems and engineering principles, as well as the ability to anticipate and adapt to future challenges. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary.\n\nFormat your response using clear headings for each section and number your paragraphs within each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['adaptation']} and how it can be applied to {t['challenge']}",
            "The proposed engineering solution is creative, plausible, and effectively addresses the given challenge",
            "The response shows strong interdisciplinary knowledge integration between biology and engineering",
            "The performance analysis includes a thorough discussion of scalability",
            "The broader implications section addresses potential environmental impacts and mitigation strategies",
            f"The adaptive potential section provides a plausible and innovative approach to addressing {t['environmental_change']}"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
