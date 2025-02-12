import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            ("Time", "River"),
            ("Ideas", "Light"),
            ("Memory", "Computer"),
            ("Emotions", "Weather"),
            ("Knowledge", "Ocean"),
            ("Language", "Tree"),
            ("Consciousness", "Network"),
            ("Creativity", "Fire")
        ]
        problems = [
            "Improve communication between diverse cultures",
            "Enhance long-term information retention in education",
            "Develop a new form of artistic expression",
            "Create a novel approach to environmental conservation",
            "Design an innovative conflict resolution method",
            "Invent a new way to measure and quantify abstract concepts",
            "Conceptualize a new model of economic value",
            "Reimagine the structure of social interactions in digital spaces"
        ]
        return {
            "1": {"concepts": random.choice(concepts), "problem": random.choice(problems)},
            "2": {"concepts": random.choice(concepts), "problem": random.choice(problems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are tasked with applying the theory of conceptual blending to create a novel concept and use it to address a complex problem. Your task has the following parts:\n\n1. Conceptual Blend (100-150 words):\n   Create a conceptual blend using the input spaces '{t['concepts'][0]}' and '{t['concepts'][1]}'. Describe the emergent structure of your blended concept, including:\n   - Shared elements from both input spaces\n   - New emergent properties that arise from the blend\n   - Potential tensions or contradictions in the blend\n\n2. Visualization (50-75 words):\n   Describe a visual representation or metaphor for your conceptual blend. How would you illustrate this new concept?\n\n3. Problem Application (150-200 words):\n   Use your conceptual blend to address the following problem: {t['problem']}\n   Explain how the unique properties of your blended concept provide novel insights or approaches to the problem. Include at least two specific strategies or solutions derived from your conceptual blend.\n\n4. Cognitive Analysis (100-150 words):\n   Analyze the cognitive processes involved in creating and applying your conceptual blend. Consider aspects such as:\n   - The role of analogy and metaphor\n   - How the blend restructures our understanding of the input spaces\n   - Potential cognitive biases or limitations in the blending process\n\n5. Interdisciplinary Implications (75-100 words):\n   Discuss potential implications or applications of your conceptual blend in at least two other fields (e.g., artificial intelligence, neuroscience, philosophy, art, etc.).\n\nEnsure your response demonstrates a deep understanding of conceptual blending theory, creative problem-solving skills, and the ability to apply abstract concepts to real-world problems. Be innovative in your approach while maintaining logical consistency and scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and application of conceptual blending theory.",
            "The conceptual blend is creative, coherent, and effectively combines elements from both input spaces.",
            "The problem application is innovative and directly utilizes properties of the conceptual blend.",
            "The cognitive analysis shows depth of understanding in cognitive science and linguistics.",
            "The interdisciplinary implications are insightful and well-reasoned.",
            "The overall response is well-structured, logically consistent, and demonstrates high-level abstract reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
