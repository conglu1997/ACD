import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        constraints = [
            {
                "form": "Haiku",
                "structure": "5-7-5 syllables",
                "theme": "nature",
                "linguistic_constraint": "Use only monosyllabic words"
            },
            {
                "form": "Sonnet",
                "structure": "14 lines, iambic pentameter",
                "theme": "love",
                "linguistic_constraint": "Each line must contain at least one homophone"
            },
            {
                "form": "Villanelle",
                "structure": "19 lines with repeating rhymes and refrains",
                "theme": "time",
                "linguistic_constraint": "Use only words with consonant clusters"
            },
            {
                "form": "Acrostic",
                "structure": "First letter of each line spells a word",
                "theme": "technology",
                "linguistic_constraint": "Each line must be a complete sentence with a subject-verb-object structure"
            }
        ]
        return {
            "1": random.choice(constraints),
            "2": random.choice(constraints)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate and analyze a poem based on specific constraints:

1. Generate a {t['form']} with the following specifications:
   - Structure: {t['structure']}
   - Theme: {t['theme']}
   - Linguistic constraint: {t['linguistic_constraint']}

2. Provide a brief analysis of your generated poem (100-150 words), addressing:
   a) How you incorporated the theme
   b) How you adhered to the linguistic constraint
   c) Any challenges you faced in the generation process

3. Explain how the linguistic constraint affects the poem's meaning or impact (50-75 words)

4. Propose an alternative linguistic constraint that could be applied to this poetic form, and briefly explain how it might change the writing process or the resulting poem (50-75 words)

Format your response as follows:

Generated Poem:
[Your poem here]

Analysis:
[Your analysis here]

Linguistic Constraint Impact:
[Your explanation here]

Alternative Constraint:
[Your proposal and explanation here]

Ensure that your response demonstrates a deep understanding of poetic forms, linguistic principles, and creative application of constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The generated poem adheres to the {t['form']} structure: {t['structure']}",
            f"The poem incorporates the theme of {t['theme']}",
            f"The poem follows the linguistic constraint: {t['linguistic_constraint']}",
            "The analysis addresses how the theme was incorporated",
            "The analysis explains how the linguistic constraint was adhered to",
            "The analysis discusses challenges faced in the generation process",
            "The explanation of the linguistic constraint's impact is insightful",
            "An alternative linguistic constraint is proposed with a thoughtful explanation",
            "The overall response demonstrates a deep understanding of poetic forms and linguistic principles"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
