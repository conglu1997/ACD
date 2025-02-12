import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        structures = [
            {
                "form": "Sonata",
                "elements": ["Exposition", "Development", "Recapitulation"]
            },
            {
                "form": "Rondo",
                "elements": ["A", "B", "A", "C", "A"]
            }
        ]
        return {
            "1": random.choice(structures),
            "2": random.choice(structures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the {t['form']} form in music and compose a new piece based on this analysis. Your task has two parts:

1. Analysis:
   a) Explain the structure of the {t['form']} form, detailing its main sections: {', '.join(t['elements'])}.
   b) Describe the typical characteristics and functions of each section.
   c) Provide an example of a well-known piece in this form.

2. Composition:
   Create a textual representation of a new musical piece in the {t['form']} form. Your composition should:
   a) Clearly demonstrate the structure of the {t['form']} form.
   b) Include descriptions of melody, harmony, and rhythm for each section.
   c) Incorporate at least one mathematical concept (e.g., symmetry, golden ratio, Fibonacci sequence) into your composition and explain how you've used it.

Format your response as follows:

Analysis:
1. Structure: [Explanation of the form's structure]
2. Characteristics:
   [Section name]: [Description of characteristics and function]
   [Repeat for each section]
3. Example: [Name and brief description of a well-known piece in this form]

Composition:
[Section name]:
- Melody: [Description of melodic elements]
- Harmony: [Description of harmonic elements]
- Rhythm: [Description of rhythmic elements]
[Repeat for each section]

Mathematical Concept:
[Explain which mathematical concept you used and how it's incorporated into your composition]

Ensure your analysis is accurate and your composition is creative while adhering to the principles of the given musical form."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes an accurate analysis of the {t['form']} form, explaining its structure and the characteristics of each section.",
            f"A relevant example of a well-known piece in the {t['form']} form is provided.",
            f"The composition clearly demonstrates the structure of the {t['form']} form, with descriptions for each section.",
            "The composition includes descriptions of melody, harmony, and rhythm for each section.",
            "A mathematical concept is incorporated into the composition, and its use is clearly explained.",
            "The response demonstrates a strong understanding of music theory and creativity in composition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
