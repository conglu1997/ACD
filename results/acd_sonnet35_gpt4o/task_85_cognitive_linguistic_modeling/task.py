import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept": "Time",
                "aspects": ["Linearity", "Cyclicality", "Relativity"]
            },
            {
                "concept": "Consciousness",
                "aspects": ["Self-awareness", "Qualia", "Intentionality"]
            }
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for representing mental models using linguistic structures, and apply it to the concept of {t['concept']}. Your task has four parts:

1. System Design:
   a) Create a linguistic framework for representing mental models. This framework should include:
      - A method for encoding conceptual relationships
      - A way to represent hierarchical structures
      - A mechanism for expressing uncertainty or ambiguity
   b) Explain how your system draws inspiration from cognitive science theories about mental models and linguistic structures (3-4 sentences).

2. Application:
   Apply your system to create a mental model representation of {t['concept']}, incorporating the following aspects: {', '.join(t['aspects'])}.
   a) Provide a detailed description of how your system represents this concept (5-6 sentences).
   b) Include a visual or structured textual representation of the mental model (e.g., a diagram, a structured list, or a specially formatted text).

3. Analysis:
   a) Explain how your representation captures the complexity and nuances of {t['concept']} (2-3 sentences).
   b) Identify one strength and one limitation of your system in representing this particular concept (2-3 sentences).

4. AI Implications:
   a) Discuss how this type of mental model representation could be used to improve AI language understanding or generation (3-4 sentences).
   b) Propose an experiment that could test whether an AI system using your representation has a deeper understanding of {t['concept']} compared to traditional language models (2-3 sentences).

Format your response as follows:

System Design:
[Your description of the linguistic framework]

Cognitive Science Inspiration:
[Your explanation]

Application to {t['concept']}:
[Your detailed description]

Visual/Structured Representation:
[Your representation]

Analysis:
[Your explanation and identification of strength/limitation]

AI Implications:
[Your discussion and proposed experiment]

Ensure your system is creative, grounded in cognitive and linguistic principles, and demonstrates a deep understanding of both the concept and the challenges of representing mental models."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed linguistic framework for representing mental models, with clear methods for encoding relationships, hierarchies, and ambiguity.",
            f"The system's inspiration from cognitive science theories is clearly explained.",
            f"The application of the system to the concept of {t['concept']} is detailed and incorporates all specified aspects: {', '.join(t['aspects'])}.",
            "A visual or structured textual representation of the mental model is provided.",
            "The analysis identifies both a strength and a limitation of the system in representing the given concept.",
            "The discussion of AI implications is insightful and the proposed experiment is relevant and well-designed.",
            "The overall response demonstrates creativity, interdisciplinary knowledge, and deep understanding of mental models and linguistic structures."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
