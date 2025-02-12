import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            "Infinity",
            "Fractals",
            "Non-Euclidean geometry",
            "Chaos theory",
            "Quantum superposition"
        ]
        philosophy_concepts = [
            "Existentialism",
            "Dualism",
            "Epistemology",
            "Utilitarianism",
            "Phenomenology"
        ]
        return {
            "1": {"math": random.choice(math_concepts), "philosophy": random.choice(philosophy_concepts)},
            "2": {"math": random.choice(math_concepts), "philosophy": random.choice(philosophy_concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a conceptual art piece that embodies the mathematical concept of {t['math']} and the philosophical concept of {t['philosophy']}. Your task involves the following steps:

1. Conceptual Design (200-250 words):
   a) Describe your conceptual art piece, including its form, materials, and presentation.
   b) Explain how it incorporates and represents both the mathematical and philosophical concepts.
   c) Discuss any interactive or participatory elements of the piece.

2. Mathematical Representation (150-200 words):
   a) Elaborate on how your art piece specifically embodies the concept of {t['math']}.
   b) Explain any mathematical principles or formulas that inform the design.
   c) Discuss how the mathematical concept is made accessible to a non-expert audience.

3. Philosophical Interpretation (150-200 words):
   a) Analyze how your art piece explores or represents {t['philosophy']}.
   b) Discuss any philosophical arguments or questions your piece raises or addresses.
   c) Explain how the philosophical concept interacts with or complements the mathematical one.

4. Viewer Experience (100-150 words):
   Describe the intended experience and interpretation of the art piece from the viewer's perspective. How might it challenge or transform their understanding of the concepts involved?

5. Cultural and Societal Implications (100-150 words):
   Discuss potential broader implications or applications of your conceptual art piece in fields such as education, scientific communication, or social discourse.

6. Artistic Precedents and Innovation (100-150 words):
   a) Briefly discuss any existing artworks or artists that may have inspired your concept.
   b) Explain what makes your piece innovative or unique in its approach to combining math, philosophy, and art.

7. Technical Realization (optional, 100-150 words):
   If applicable, provide a brief explanation of how your conceptual art piece could be technically realized, including any challenges that might arise in its creation or exhibition.

Ensure your response demonstrates a deep understanding of both the mathematical and philosophical concepts, as well as the principles of conceptual art. Be creative and original in your design while maintaining intellectual rigor in your explanations and analyses. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section and adhere to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conceptual art piece must clearly incorporate both {t['math']} and {t['philosophy']}.",
            "The response must include all seven required sections (or six if the optional technical realization is omitted).",
            "The explanation of the mathematical concept must be accurate and well-integrated into the art piece.",
            "The philosophical interpretation must demonstrate a good understanding of the chosen concept and its relevance to the artwork.",
            "The response should show creativity and originality in combining math, philosophy, and art.",
            "The analysis of viewer experience and cultural implications should be thoughtful and well-reasoned.",
            "The response must adhere to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
