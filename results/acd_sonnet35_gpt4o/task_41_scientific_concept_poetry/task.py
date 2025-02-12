import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "Quantum Entanglement",
                "form": "Sonnet",
                "rules": "14 lines, typically in iambic pentameter, with a rhyme scheme of ABAB CDCD EFEF GG"
            },
            {
                "concept": "Theory of Relativity",
                "form": "Haiku",
                "rules": "Three lines with a syllable pattern of 5-7-5"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a poem that accurately explains the scientific concept of {t['concept']} while adhering to the {t['form']} form. Your poem must:

1. Accurately explain key aspects of {t['concept']} without introducing any scientific inaccuracies.
2. Adhere strictly to the rules of a {t['form']}: {t['rules']}.
3. Use creative and engaging language that makes the concept accessible to a general audience.
4. Incorporate at least one relevant metaphor or analogy to aid understanding.

Your response should include:

1. The poem itself, formatted correctly for the given poetic form.
2. A brief explanation (2-3 sentences) of how your poem accurately represents the scientific concept.
3. Identification of the metaphor or analogy used and how it relates to the concept.

Ensure your poem is both scientifically accurate and poetically sound."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The poem accurately explains key aspects of {t['concept']} without scientific inaccuracies.",
            f"The poem strictly adheres to the rules of a {t['form']}: {t['rules']}.",
            "The poem uses creative and engaging language that makes the concept accessible to a general audience.",
            "The poem incorporates at least one relevant metaphor or analogy to aid understanding.",
            "The explanation provided demonstrates how the poem accurately represents the scientific concept.",
            "The metaphor or analogy is clearly identified and its relation to the concept is well-explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
