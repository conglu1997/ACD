import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_journeys = [
            {
                "journey": "From grief to acceptance",
                "emotions": ["sorrow", "anger", "reflection", "hope", "acceptance"]
            },
            {
                "journey": "Falling in love",
                "emotions": ["curiosity", "excitement", "joy", "vulnerability", "contentment"]
            }
        ]
        return {
            "1": random.choice(emotional_journeys),
            "2": random.choice(emotional_journeys)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of generating and analyzing abstract art based on human emotional states, then use it to create a series of artworks representing the emotional journey: {t['journey']}. Your task has five parts:\n\n1. System Architecture (250-300 words):\n   a) Describe the overall structure of your AI system, including its main components and their functions.\n   b) Explain how the system processes emotional input and translates it into visual elements.\n   c) Detail the AI techniques or algorithms used in your system (e.g., neural networks, evolutionary algorithms).\n\n2. Emotional-Visual Mapping (200-250 words):\n   a) Create a framework for mapping emotions to visual elements (e.g., colors, shapes, textures).\n   b) Explain the psychological or artistic theories that inform your mapping choices.\n   c) Provide an example of how a specific emotion would be represented visually.\n\n3. Artwork Generation (250-300 words):\n   a) Describe the process your AI system uses to generate abstract artworks.\n   b) Explain how the system ensures each artwork is unique while still representing the intended emotion.\n   c) Discuss how the system handles the transition between emotions in the journey.\n\n4. Analysis and Interpretation (200-250 words):\n   a) Explain how your AI system analyzes and interprets the artworks it generates.\n   b) Describe the criteria the system uses to evaluate the effectiveness of an artwork in conveying an emotion.\n   c) Discuss how the system might handle ambiguous or complex emotional states.\n\n5. Emotional Journey Representation (250-300 words):\n   a) Using your AI system, create a series of five abstract artworks representing the emotional journey: {t['journey']}.\n   b) For each artwork, provide a brief description (2-3 sentences) of its visual elements and how they represent the corresponding emotion: {', '.join(t['emotions'])}.\n   c) Explain how the series as a whole captures the progression of the emotional journey.\n\nEnsure your response demonstrates a deep understanding of human emotions, art theory, and AI capabilities. Be creative in your approach while maintaining scientific and artistic plausibility. Use clear headings for each section of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI systems, human emotions, and art theory.",
            "The proposed AI system architecture is innovative, logically consistent, and effectively addresses the challenge of generating emotion-based abstract art.",
            "The emotional-visual mapping framework is well-thought-out and grounded in psychological or artistic theories.",
            "The artwork generation process is clearly explained and accounts for uniqueness and emotional transitions.",
            "The analysis and interpretation component of the AI system is robust and considers the complexity of emotional states.",
            "The series of artworks effectively represents the given emotional journey, with clear descriptions linking visual elements to emotions.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
