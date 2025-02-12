import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sentences = [
            "The cat chased the mouse.",
            "The scientist conducted groundbreaking research.",
            "Children often enjoy playing in the park.",
            "The ancient artifact was discovered by archaeologists."
        ]
        transformations = [
            "Passivize the sentence",
            "Convert to a yes/no question",
            "Add a relative clause to modify the subject",
            "Change tense to future perfect",
            "Embed the sentence as a complement clause",
            "Topicalize the object of the sentence"
        ]
        
        tasks = [
            {
                'sentence': random.choice(sentences),
                'transformation': random.choice(transformations)
            },
            {
                'sentence': random.choice(sentences),
                'transformation': random.choice(transformations)
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task involves syntactic tree transformation and sentence generation. Follow these steps:

1. Parse the following sentence into a syntactic tree structure: "{t['sentence']}"
   Represent the tree using bracket notation, e.g., [S [NP [Det The] [N cat]] [VP [V chased] [NP [Det the] [N mouse]]]]
   Ensure you include all relevant syntactic categories (S, NP, VP, Det, N, V, etc.).

2. Apply the following transformation to the tree: {t['transformation']}
   Show the transformed tree using the same bracket notation.
   Consider how the transformation affects different parts of the tree structure.

3. Generate a new grammatically correct sentence based on the transformed tree.
   Ensure that your new sentence accurately reflects the structure of the transformed tree.

4. Explain the transformation process and how it affects the sentence's meaning and structure. Your explanation should:
   - Be 3-5 sentences long
   - Describe the specific changes made to the tree structure
   - Discuss how the transformation impacts the sentence's syntax and semantics
   - Provide an example of how this transformation might change the meaning in a different context

Format your response as follows:

Original Tree:
[Your tree representation here]

Transformed Tree:
[Your transformed tree representation here]

New Sentence:
[Your generated sentence here]

Explanation:
[Your explanation here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The original tree is correctly represented using bracket notation with all relevant syntactic categories.",
            "The transformed tree correctly applies the specified transformation and maintains proper syntactic structure.",
            "The new sentence is grammatically correct and accurately reflects the transformed tree structure.",
            "The explanation comprehensively describes the transformation process, its effects on syntax and semantics, and provides a relevant example or counterexample."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
