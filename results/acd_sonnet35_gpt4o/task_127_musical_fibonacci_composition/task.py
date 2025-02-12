import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Harmonians",
                "description": "A society that values mathematical precision in their music and art."
            },
            {
                "name": "Rhythmites",
                "description": "A culture that believes the Fibonacci sequence is sacred and incorporates it into all aspects of life."
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a musical piece based on the Fibonacci sequence for the {t['name']} culture: {t['description']}

Your task is to create a short musical composition and analyze its cultural significance. Follow these steps:

1. Compose a musical piece (8-16 measures) using the Fibonacci sequence as a basis for either rhythm, melody, or harmony. Explain your compositional choices.

2. Provide a musical notation or tablature of your composition. If using standard notation, include time signature, key signature, and tempo.

3. Explain how your composition incorporates the Fibonacci sequence (e.g., in note durations, pitch selection, or harmonic progression).

4. Analyze the cultural significance of your composition for the given society. How does it reflect their values and beliefs?

5. Describe a ritual or ceremony in which this music might be performed in the society.

6. Propose how this musical tradition might evolve over time, considering potential influences or changes in the society.

Provide your response in the following format:

Composition Explanation:
[Your explanation of compositional choices]

Musical Notation:
[Your musical notation or tablature]

Fibonacci Incorporation:
[Explanation of how the Fibonacci sequence is used]

Cultural Significance:
[Analysis of the composition's meaning in the society]

Ritual or Ceremony:
[Description of a cultural event featuring this music]

Evolution of Tradition:
[Prediction of how this musical style might change over time]

Ensure that your composition is musically sound, mathematically accurate, and culturally relevant to the given society."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition incorporates the Fibonacci sequence in a meaningful way",
            "The musical notation or tablature is provided and consistent with the explanation",
            "The cultural analysis is insightful and relevant to the given society",
            "The ritual or ceremony description is creative and culturally appropriate",
            "The evolution prediction is plausible and considers societal factors",
            "The response follows the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
