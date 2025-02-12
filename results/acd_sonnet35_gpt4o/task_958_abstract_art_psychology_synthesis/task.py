import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        psychological_concepts = [
            {
                "concept": "Cognitive Dissonance",
                "definition": "The mental discomfort experienced when holding contradictory beliefs or values",
                "art_movement": "Surrealism"
            },
            {
                "concept": "Gestalt Principles",
                "definition": "The mind's tendency to perceive patterns and organize visual elements into a unified whole",
                "art_movement": "Constructivism"
            },
            {
                "concept": "Sublimation",
                "definition": "The transformation of unacceptable impulses into socially acceptable actions or behavior",
                "art_movement": "Abstract Expressionism"
            },
            {
                "concept": "Archetype",
                "definition": "Universal, inherited patterns of thought or behavior present in the collective unconscious",
                "art_movement": "Symbolism"
            }
        ]
        return {str(i+1): random.choice(psychological_concepts) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are an art psychologist tasked with analyzing and creating abstract art based on psychological principles. Your task has four parts:

1. Psychological Concept Analysis (200-250 words):
   a) Explain the psychological concept of {t['concept']} and its relevance to human cognition or behavior.
   b) Discuss how this concept might be visually represented in abstract art.
   c) Provide an example of how an existing artwork from the {t['art_movement']} movement might embody this concept.

2. Abstract Artwork Generation (200-250 words):
   a) Describe an original abstract artwork that visually represents the concept of {t['concept']}.
   b) Explain your choice of colors, shapes, composition, and other visual elements.
   c) Discuss how specific features of your artwork relate to key aspects of the psychological concept.

3. Artistic Technique Analysis (150-200 words):
   a) Describe the artistic techniques and style you would use to create this artwork.
   b) Explain how these techniques contribute to conveying the psychological concept.
   c) Compare your approach to techniques commonly used in the {t['art_movement']} movement.

4. Viewer Impact and Critique (200-250 words):
   a) Predict how viewers might interpret and respond emotionally to your artwork.
   b) Analyze potential psychological effects of viewing your artwork.
   c) Critique your own work, discussing its strengths and limitations in conveying the psychological concept.
   d) Suggest one way to modify or enhance the artwork to better represent the concept.

Ensure your response demonstrates a deep understanding of both psychological principles and art theory. Be creative in your artwork description while maintaining conceptual coherence and plausibility. Use appropriate terminology from both psychology and art criticism.

Format your response with clear headings for each section. Your total response should be between 750-950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must accurately explain the psychological concept of {t['concept']}.",
            "The described artwork should clearly and creatively represent the given psychological concept.",
            f"The artistic techniques should be consistent with or thoughtfully deviate from the {t['art_movement']} movement.",
            "The critique should demonstrate insightful analysis of the artwork's effectiveness in conveying the psychological concept.",
            "The response should be well-structured, coherent, and adhere to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
