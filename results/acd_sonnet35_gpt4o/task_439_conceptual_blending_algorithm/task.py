import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            ("Music", "Programming"),
            ("Biology", "Architecture"),
            ("Cooking", "Chemistry"),
            ("Sports", "Mathematics"),
            ("Art", "Physics"),
            ("Literature", "Economics")
        ]
        return {
            "1": {"domains": random.choice(domains)},
            "2": {"domains": random.choice(domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an algorithm that simulates the cognitive process of conceptual blending, and use it to create a novel concept by combining the domains of {t['domains'][0]} and {t['domains'][1]}. Your response should include:\n\n1. Algorithm Design (200-250 words):\n   a) Outline the key steps of your conceptual blending algorithm.\n   b) Explain how it models the cognitive processes involved in conceptual blending.\n   c) Discuss how your algorithm handles potential conflicts or incompatibilities between input domains.\n\n2. Implementation (150-200 words):\n   Provide a high-level pseudocode or flowchart representation of your algorithm. Explain any key functions or data structures used.\n\n3. Application (250-300 words):\n   a) Apply your algorithm to blend the given domains: {t['domains'][0]} and {t['domains'][1]}.\n   b) Describe the resulting blended concept in detail.\n   c) Explain how elements from each input domain contribute to the blended concept.\n   d) Discuss any emergent properties or novel features of the blended concept.\n\n4. Evaluation (150-200 words):\n   a) Propose criteria for evaluating the quality and creativity of the blended concept.\n   b) Assess your blended concept based on these criteria.\n   c) Discuss potential applications or implications of your blended concept.\n\n5. Cognitive Science Analysis (200-250 words):\n   a) Analyze how well your algorithm models human cognitive processes in conceptual blending.\n   b) Discuss any limitations of your approach compared to human cognition.\n   c) Propose an experiment that could test whether your algorithm produces results similar to human conceptual blending.\n\nEnsure your response demonstrates a deep understanding of conceptual blending theory, cognitive science, and computational creativity. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content and word counts.",
            "The algorithm design and implementation demonstrate a clear understanding of conceptual blending theory and cognitive processes.",
            f"The application successfully blends the domains of {t['domains'][0]} and {t['domains'][1]} to create a novel concept.",
            "The evaluation and cognitive science analysis show depth of thought and critical reasoning.",
            "The overall response is creative, scientifically plausible, and demonstrates interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
