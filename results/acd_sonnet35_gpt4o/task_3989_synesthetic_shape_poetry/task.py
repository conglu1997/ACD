import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        shapes = [
            "circle", "triangle", "square", "spiral", "wave",
            "fractal", "star", "helix", "labyrinth", "mandala"
        ]
        patterns = [
            "repeating", "expanding", "contracting", "intersecting",
            "radiating", "cascading", "oscillating", "fragmenting",
            "merging", "transforming"
        ]
        themes = [
            "time", "consciousness", "infinity", "chaos", "harmony",
            "evolution", "duality", "transcendence", "entropy", "unity"
        ]
        poetic_forms = [
            "haiku", "sonnet", "free verse", "villanelle", "tanka",
            "cinquain", "ghazal", "pantoum", "etheree", "concrete poem"
        ]
        return {
            "1": {
                "shape": random.choice(shapes),
                "pattern": random.choice(patterns),
                "theme": random.choice(themes),
                "poetic_form": random.choice(poetic_forms)
            },
            "2": {
                "shape": random.choice(shapes),
                "pattern": random.choice(patterns),
                "theme": random.choice(themes),
                "poetic_form": random.choice(poetic_forms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Engage in a synesthetic interpretation of abstract visual patterns and create poetry based on your interpretation. Your task has four parts:

1. Visual Interpretation (150-200 words):
   a) Describe the mental image created by combining a {t['shape']} with a {t['pattern']} pattern.
   b) Explain how this visual construct might represent or evoke the concept of {t['theme']}.
   c) Discuss any emotions, sensations, or abstract ideas that this visual pattern brings to mind.

2. Conceptual Mapping (200-250 words):
   a) Create a detailed mapping between elements of your visualized pattern and aspects of {t['theme']}.
   b) Explain how the properties of the {t['shape']} and its {t['pattern']} relate to specific facets of {t['theme']}.
   c) Describe any synesthetic experiences (e.g., colors, sounds, textures) you associate with this mapping.

3. Poetic Creation (Poetry length appropriate to the form):
   Compose a {t['poetic_form']} that captures the essence of your visual-conceptual mapping. Your poem should:
   a) Reflect the visual properties of the {t['shape']} and its {t['pattern']}.
   b) Explore the theme of {t['theme']} through imagery and metaphor.
   c) Incorporate any synesthetic associations you've developed.
   d) Adhere to the structural requirements of a {t['poetic_form']}.

4. Reflective Analysis (150-200 words):
   a) Explain how your poem captures the visual-conceptual mapping you created.
   b) Discuss any challenges you faced in translating visual and abstract concepts into poetic language.
   c) Reflect on how this exercise in synesthetic thinking might enhance creative expression or understanding of abstract concepts.

Ensure your response demonstrates deep engagement with abstract visual thinking, conceptual mapping, and poetic creativity. Be innovative in your approach while maintaining coherence between the visual, conceptual, and poetic elements. Format your response with clear headings for each section.

Your total response should be between 500-700 words, excluding the poem itself."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear and creative visualization of the given shape and pattern.",
            "The conceptual mapping between the visual elements and the theme is well-developed and insightful.",
            "The poem effectively captures the essence of the visual-conceptual mapping and adheres to the specified poetic form.",
            "The reflective analysis shows deep engagement with the process of synesthetic thinking and poetic creation.",
            "The overall response showcases a high level of abstract reasoning and creative expression."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
