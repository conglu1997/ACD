import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            ("Time", "River"),
            ("Knowledge", "Ocean"),
            ("Emotion", "Weather"),
            ("Life", "Journey"),
            ("Mind", "Computer"),
            ("Idea", "Seed"),
            ("Argument", "War"),
            ("Love", "Fire"),
            ("Memory", "Library"),
            ("Communication", "Bridge")
        ]
        return {
            "1": {"concept_pair": random.choice(concepts)},
            "2": {"concept_pair": random.choice(concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and implement a conceptual blending framework for AI, then use it to generate a novel concept by blending '{t['concept_pair'][0]}' and '{t['concept_pair'][1]}'. Your response should include:\n\n1. Framework Design (250-300 words):\n   a) Explain the key components of your conceptual blending framework.\n   b) Describe how your framework represents and manipulates conceptual spaces.\n   c) Outline the process of selecting, projecting, and integrating elements from input spaces.\n   d) Discuss how your framework handles emergent structure in the blended space.\n\n2. Concept Generation (200-250 words):\n   a) Apply your framework to blend the given concepts: '{t['concept_pair'][0]}' and '{t['concept_pair'][1]}'.\n   b) Describe the resulting blended concept, including its key features and emergent properties.\n   c) Explain how this blend extends or challenges our understanding of the input concepts.\n\n3. Linguistic Analysis (200-250 words):\n   a) Analyze the linguistic properties of your blended concept.\n   b) Discuss any novel metaphors, analogies, or semantic structures that emerge.\n   c) Explain how the blended concept might influence language use or conceptual framing.\n\n4. AI Implementation (150-200 words):\n   a) Propose a method for implementing your conceptual blending framework in an AI system.\n   b) Discuss potential challenges and solutions in training an AI to perform conceptual blending.\n   c) Explain how this implementation could enhance AI's creative and abstract thinking capabilities.\n\n5. Interdisciplinary Implications (150-200 words):\n   a) Explore potential applications of your framework in fields such as cognitive science, computational creativity, or knowledge representation.\n   b) Discuss how your approach to conceptual blending might inform or be informed by theories of human cognition.\n   c) Propose a novel research question that arises from your framework and its application.\n\nEnsure your response demonstrates a deep understanding of conceptual blending theory, linguistic analysis, and AI capabilities. Be creative and rigorous in your approach, providing clear explanations and examples throughout your answer."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of conceptual blending theory and its application to AI",
            "The proposed framework is logically consistent and well-explained",
            "The generated blended concept is creative and coherently integrates the given input concepts",
            "The linguistic analysis is insightful and identifies novel semantic structures or metaphors",
            "The AI implementation proposal is feasible and addresses potential challenges",
            "The interdisciplinary implications are well-reasoned and demonstrate broad knowledge application",
            "The response shows originality in approach and generates novel insights or research questions"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
