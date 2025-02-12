import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_authors = ['William Shakespeare', 'Jane Austen', 'Ernest Hemingway', 'Virginia Woolf']
        target_authors = ['Franz Kafka', 'Gabriel García Márquez', 'Toni Morrison', 'Haruki Murakami']
        source_texts = [
            "To be, or not to be: that is the question.",
            "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
            "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish.",
            "Mrs Dalloway said she would buy the flowers herself."
        ]
        return {
            "1": {"source_author": random.choice(source_authors), "target_author": random.choice(target_authors), "source_text": source_texts[source_authors.index(source_authors[0])]},
            "2": {"source_author": random.choice(source_authors), "target_author": random.choice(target_authors), "source_text": source_texts[source_authors.index(source_authors[1])]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop an algorithm to transfer the syntactic style of {t['source_author']} to the content of a text by {t['target_author']}, then analyze and recreate the result. Your response should include:

1. Syntactic Style Analysis (200-250 words):
   a) Identify and describe 3-5 key syntactic features characteristic of {t['source_author']}'s writing style.
   b) Explain how these features contribute to the author's unique voice and impact on readers.
   c) Provide brief examples illustrating each feature.
   Use this sample text for reference: "{t['source_text']}"

2. Algorithm Design (250-300 words):
   a) Outline a step-by-step algorithm for transferring the identified syntactic features to a target text.
   b) Explain how your algorithm handles potential conflicts between the source style and target content.
   c) Discuss any linguistic theories or computational methods that inform your approach.
   d) Address potential limitations or edge cases in your algorithm.

3. Implementation Example (200-250 words):
   a) Provide a short (2-3 sentences) original text in the style of {t['target_author']}.
   b) Apply your algorithm to this text, showing the step-by-step transformation.
   c) Present the final 'style-transferred' version of the text.

4. Analysis of Results (200-250 words):
   a) Compare the original and style-transferred texts, highlighting successful style transfers.
   b) Discuss any unexpected outcomes or challenges in applying the algorithm.
   c) Analyze how the style transfer affects the meaning or impact of the original text.

5. Literary and Linguistic Implications (150-200 words):
   a) Discuss the potential applications of syntactic style transfer in literary analysis or creative writing.
   b) Explore how this technique might inform our understanding of authorial style and linguistic patterns.
   c) Consider the ethical implications of algorithmic style imitation in literature.

Ensure your response demonstrates a deep understanding of linguistic structures, computational approaches to style analysis, and literary theory. Be creative in your approach while maintaining analytical rigor. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1250 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include all five required sections: Syntactic Style Analysis, Algorithm Design, Implementation Example, Analysis of Results, and Literary and Linguistic Implications.",
            f"The syntactic style analysis must accurately identify and describe at least 3 key features of {t['source_author']}'s writing style, with reference to the provided sample text.",
            "The algorithm design must include a clear step-by-step process for syntactic style transfer.",
            f"The implementation example must show a clear attempt to transfer {t['source_author']}'s style to an original text in the style of {t['target_author']}.",
            "The analysis of results must provide specific examples of successful style transfers and challenges encountered.",
            "The discussion of literary and linguistic implications must include at least one potential application and one ethical consideration.",
            "The response must be within the specified word count range (1000-1250 words) and include a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
