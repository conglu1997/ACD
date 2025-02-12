import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "name": "Coral Reef",
                "key_features": ["Symbiotic relationships", "Biodiversity", "Nutrient cycling", "Structural complexity"]
            },
            {
                "name": "Rainforest",
                "key_features": ["Layered canopy", "Rapid decomposition", "Species interdependence", "Adaptive strategies"]
            }
        ]
        return {str(i+1): ecosystem for i, ecosystem in enumerate(ecosystems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language inspired by the {t['name']} ecosystem. Your task is to create a novel programming paradigm that maps ecological concepts to programming constructs. Follow these steps:

1. Language Overview (150-200 words):
   Provide a high-level description of your programming language, explaining its core philosophy and how it relates to the {t['name']} ecosystem.

2. Key Features (200-250 words):
   Describe at least 4 key features of your language, each inspired by one of the following ecological concepts: {', '.join(t['key_features'])}. For each feature, explain:
   a) The ecological concept it's based on
   b) How it's implemented in the programming language
   c) Its advantages or unique aspects compared to traditional programming constructs

3. Syntax and Structure (200-250 words):
   Outline the basic syntax and structure of your language. Provide at least 2 code snippets demonstrating unique aspects of your language, with explanations of how they work.

4. Ecosystem Parallel (150-200 words):
   Explain how your language as a whole parallels the functioning of the {t['name']} ecosystem. Discuss any emergent properties or behaviors that might arise from the interaction of your language features.

5. Use Case (100-150 words):
   Propose a specific use case where your ecosystem-inspired language would be particularly effective. Explain why it's well-suited for this application.

6. Challenges and Limitations (100-150 words):
   Discuss potential challenges in implementing or using your language, and any limitations it might have compared to traditional programming languages.

Ensure your response demonstrates a deep understanding of both programming language design and ecosystem dynamics. Be creative in drawing parallels between ecological and computational concepts while maintaining technical feasibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a programming language design inspired by the {t['name']} ecosystem",
            "The language features should creatively and logically map to ecological concepts",
            "The response should include at least 2 code snippets demonstrating unique aspects of the language",
            "The explanation should draw clear parallels between the language design and ecosystem functioning",
            "The response should demonstrate understanding of both programming language design and ecological principles"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
