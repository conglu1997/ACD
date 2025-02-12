class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "art_description": "A surrealist painting depicting a barren landscape with a melting clock hanging from a barren tree. The landscape is filled with scattered rocks and distorted human-like figures. The colors are predominantly muted earth tones with occasional bright highlights in yellow and red. The sky has a gradient from dark blue to light orange, creating a contrasting backdrop.",
                "task": "Critique this art piece. Discuss the use of surrealism, the symbolism of the melting clock, the effect of the color palette, and the overall impact of the composition."
            },
            "2": {
                "criteria": "Create a concept for a new abstract painting. The painting should convey a sense of chaos and order. Use contrasting colors, geometric shapes, and include elements that represent time and space. Describe the concept in detail, including the intended emotional impact and the techniques to be used."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "art_description" in t:
            return f"""Analyze and critique the following art piece based on the detailed description provided. Your critique should cover the following aspects:
1. The use of surrealism.
2. The symbolism of the melting clock.
3. The effect of the color palette.
4. The overall impact of the composition.

Description of the art piece: {t['art_description']}

Submit your critique in the following format:
- Use of Surrealism: [Your analysis]
- Symbolism of the Melting Clock: [Your analysis]
- Effect of the Color Palette: [Your analysis]
- Overall Impact of the Composition: [Your analysis]"""
        elif "criteria" in t:
            return f"""Create a concept for a new abstract painting based on the criteria provided. Your concept description should include:
1. How the painting conveys a sense of chaos and order.
2. The use of contrasting colors.
3. The use of geometric shapes.
4. The intended emotional impact.
5. The techniques to be used.

Criteria: {t['criteria']}

Submit your concept in the following format:
- Sense of Chaos and Order: [Your description]
- Use of Contrasting Colors: [Your description]
- Use of Geometric Shapes: [Your description]
- Intended Emotional Impact: [Your description]
- Techniques to be Used: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "art_description" in t:
            validation_criteria = [
                "The critique should cover the use of surrealism.",
                "The critique should discuss the symbolism of the melting clock.",
                "The critique should analyze the effect of the color palette.",
                "The critique should evaluate the overall impact of the composition.",
                "The critique should be detailed, insightful, logically structured, and clear."]
        elif "criteria" in t:
            validation_criteria = [
                "The concept should convey a sense of chaos and order.",
                "The concept should describe the use of contrasting colors.",
                "The concept should describe the use of geometric shapes.",
                "The concept should include the intended emotional impact.",
                "The concept should describe the techniques to be used."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
