import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "word1": "metamorphosis",
                "word2": "photosynthesis",
                "property1": "homotopy equivalence",
                "property2": "compactness"
            },
            "2": {
                "sentence1": "The quick brown fox jumps over the lazy dog",
                "sentence2": "All that glitters is not gold",
                "property1": "fundamental group",
                "property2": "homeomorphism"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "word1" in t:
            return f"""Analyze, compare, and visualize the words '{t['word1']}' and '{t['word2']}' as topological spaces, focusing on the properties of {t['property1']} and {t['property2']}. Your task is to:

1. Define what {t['property1']} and {t['property2']} mean in the context of linguistic topology (2-3 sentences each).
2. Explain how these properties apply to each word, considering morphemes, phonemes, or semantic components as 'points' in the space (3-4 sentences for each word).
3. Compare and contrast the topological structures of the two words based on these properties (3-4 sentences).
4. Describe how these properties might change if the words undergo linguistic transformations (e.g., adding affixes, changing part of speech) (2-3 sentences for each word).
5. Create and define a novel topological property specific to linguistics, and explain how it applies to these words (4-5 sentences).
6. Propose a method to visualize or represent the topological space of one of the words, incorporating at least one of the discussed properties (3-4 sentences).
7. Suggest a potential application of this linguistic-topological analysis in a field such as natural language processing or cognitive science (3-4 sentences).

Ensure your response is creative yet grounded in both linguistic and mathematical principles. Organize your answer using clear headings for each section."""
        else:
            return f"""Analyze, compare, and visualize the sentences '{t['sentence1']}' and '{t['sentence2']}' as topological spaces, focusing on the properties of {t['property1']} and {t['property2']}. Your task is to:

1. Define what {t['property1']} and {t['property2']} mean in the context of linguistic topology (2-3 sentences each).
2. Explain how these properties apply to each sentence, considering words, phrases, or clauses as 'points' or 'subsets' in the space (3-4 sentences for each sentence).
3. Compare and contrast the topological structures of the two sentences based on these properties (3-4 sentences).
4. Describe how these properties might change if the sentences undergo syntactic transformations (e.g., passive voice, question form) (2-3 sentences for each sentence).
5. Create and define a novel topological property specific to linguistics, and explain how it applies to these sentences (4-5 sentences).
6. Propose a method to visualize or represent the topological space of one of the sentences, incorporating at least one of the discussed properties (3-4 sentences).
7. Suggest a potential application of this linguistic-topological analysis in a field such as natural language processing or cognitive science (3-4 sentences).

Ensure your response is creative yet grounded in both linguistic and mathematical principles. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response defines both topological properties in a linguistic context",
            "The explanation applies the properties to both given words or sentences",
            "A comparative analysis of the topological structures is provided",
            "The analysis considers linguistic transformations for both words or sentences",
            "A novel topological property specific to linguistics is created and defined",
            "A method to visualize or represent the topological space is proposed",
            "A potential application in a related field is suggested",
            "The response demonstrates understanding of both linguistic and mathematical concepts",
            "The answer is organized with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
