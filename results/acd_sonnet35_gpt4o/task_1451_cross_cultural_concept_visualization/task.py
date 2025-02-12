import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "Time",
            "Freedom",
            "Justice",
            "Love",
            "Knowledge"
        ]
        cultures = [
            "Japanese",
            "Nigerian",
            "Brazilian",
            "Indian",
            "Egyptian"
        ]
        visual_elements = [
            "Color",
            "Shape",
            "Texture",
            "Composition",
            "Symbolism"
        ]
        
        tasks = {}
        for i in range(1, 3):
            concept = random.choice(abstract_concepts)
            culture = random.choice(cultures)
            element = random.choice(visual_elements)
            tasks[str(i)] = {"concept": concept, "culture": culture, "element": element}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of translating the abstract concept of {t['concept']} into visual metaphors for {t['culture']} culture, with a focus on the visual element of {t['element']}. Your response should include the following sections:\n\n1. Conceptual Framework (250-300 words):\n   a) Explain how your AI system understands and represents the abstract concept of {t['concept']}.\n   b) Describe how it incorporates cultural knowledge specific to {t['culture']} culture.\n   c) Discuss the role of {t['element']} in creating visual metaphors for this concept.\n\n2. System Architecture (300-350 words):\n   a) Describe the main components of your AI system and how they interact.\n   b) Explain how your system processes linguistic and cultural input to generate visual output.\n   c) Detail how your system incorporates cognitive theories of metaphor and visual perception.\n   d) Provide a visual representation of your system architecture (describe it textually, using ASCII art if helpful).\n\n3. Visualization Process (250-300 words):\n   a) Provide a step-by-step example of how your system would create a visual metaphor for {t['concept']} in {t['culture']} culture, focusing on {t['element']}.\n   b) Explain how this process incorporates principles from cognitive science and cultural studies.\n   c) Describe how your system ensures cultural sensitivity and appropriateness.\n   d) Include a pseudocode snippet (5-10 lines) illustrating a key algorithm in your visualization process.\n\n4. Evaluation Methods (200-250 words):\n   a) Propose quantitative and qualitative methods to evaluate your system's ability to create culturally appropriate visual metaphors.\n   b) Describe how you would compare your system's output to human-created visual metaphors.\n   c) Suggest a novel metric for measuring the cross-cultural effectiveness of the generated visual metaphors.\n\n5. Ethical Considerations and Future Directions (200-250 words):\n   a) Discuss potential ethical issues related to AI-generated cross-cultural visual metaphors.\n   b) Address any limitations of your approach, particularly in capturing cultural nuances.\n   c) Propose guidelines for the responsible development and use of cross-cultural concept visualization systems.\n   d) Suggest potential applications of your system beyond visual metaphor creation.\n\nEnsure your response demonstrates a deep understanding of cognitive science, cultural studies, visual design, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1200-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the abstract concept, cultural context, and visual element specified in the task.",
            "The proposed AI system architecture is innovative, well-explained, and scientifically plausible.",
            "The visualization process is clearly described and incorporates relevant principles from cognitive science and cultural studies.",
            "The evaluation methods are comprehensive and include a novel metric for cross-cultural effectiveness.",
            "Ethical considerations are thoroughly addressed, and future directions are insightful and relevant.",
            "The response shows strong interdisciplinary integration of cognitive science, cultural studies, visual design, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0