import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "domains": ["physics", "biology", "information theory"],
                "concept": "entropy",
                "application": "ecosystem stability"
            },
            {
                "domains": ["psychology", "economics", "game theory"],
                "concept": "Nash equilibrium",
                "application": "social decision-making"
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create and manipulate abstract mental models to explore the concept of {t['concept']} across the domains of {', '.join(t['domains'])}, and apply your model to understand {t['application']}. Your task has the following parts:\n\n1. Concept Analysis (150-200 words):\n   a) Define {t['concept']} in the context of each domain: {', '.join(t['domains'])}.\n   b) Identify key similarities and differences in how the concept is understood across these domains.\n\n2. Mental Model Creation (250-300 words):\n   a) Develop an abstract mental model that represents {t['concept']} in a way that encompasses all the given domains.\n   b) Describe the key components, relationships, and dynamics of your model.\n   c) Explain how your model captures the essence of {t['concept']} across the different domains.\n\n3. Model Manipulation (200-250 words):\n   a) Describe how you would manipulate your mental model to explore different aspects of {t['concept']}.\n   b) Explain how these manipulations might lead to new insights or understanding about the concept.\n\n4. Application to {t['application']} (250-300 words):\n   a) Apply your mental model to analyze and understand {t['application']}.\n   b) Explain how your model provides insights into this application that might not be apparent from a single-domain perspective.\n   c) Discuss any limitations of your model in this application and how they might be addressed.\n\n5. Interdisciplinary Implications (150-200 words):\n   a) Discuss how your mental model and its application might foster new interdisciplinary research or collaborations.\n   b) Propose a novel research question or hypothesis that emerges from your interdisciplinary mental model.\n\nEnsure your response demonstrates a deep understanding of the concept across all given domains, creative and flexible thinking in model creation and manipulation, and insightful application of the model to the given problem. Use clear headings for each section of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the concept across all given domains.",
            "The mental model created is truly abstract and effectively represents the concept across domains.",
            "The model manipulation shows creativity and leads to meaningful insights.",
            "The application of the model to the given problem is insightful and demonstrates interdisciplinary thinking.",
            "The proposed research question or hypothesis is novel and emerges logically from the interdisciplinary model.",
            "The overall response shows high-level abstract reasoning and cognitive flexibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
