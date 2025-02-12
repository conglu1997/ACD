import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                'concept': 'Logical implication',
                'representations': {
                    'logical': 'p → q',
                    'set_theory': '{x | x ∈ p → x ∈ q}',
                    'natural_language': 'If p, then q',
                    'programming': 'if p: q'
                }
            },
            {
                'concept': 'Existential quantification',
                'representations': {
                    'logical': '∃x P(x)',
                    'set_theory': '{x | P(x) ≠ ∅}',
                    'natural_language': 'There exists an x such that P(x) is true',
                    'programming': 'any(P(x) for x in domain)'
                }
            },
            {
                'concept': 'Negation',
                'representations': {
                    'logical': '¬p',
                    'set_theory': 'A\'',
                    'natural_language': 'It is not the case that p',
                    'programming': 'not p'
                }
            },
            {
                'concept': 'Universal quantification',
                'representations': {
                    'logical': '∀x P(x)',
                    'set_theory': '{x | ∀x P(x)}',
                    'natural_language': 'For all x, P(x) is true',
                    'programming': 'all(P(x) for x in domain)'
                }
            },
            {
                'concept': 'Intersection',
                'representations': {
                    'logical': 'p ∧ q',
                    'set_theory': 'A ∩ B',
                    'natural_language': 'Elements common to both sets A and B',
                    'programming': 'set(A) & set(B)'
                }
            }
        ]
        
        tasks = []
        for concept in concepts:
            reps = list(concept['representations'].keys())
            for i in range(len(reps)):
                for j in range(i+1, len(reps)):
                    tasks.append({
                        'concept': concept['concept'],
                        'from_rep': reps[i],
                        'to_rep': reps[j],
                        'from_value': concept['representations'][reps[i]],
                        'to_value': concept['representations'][reps[j]]
                    })
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following abstract concept from one representational system to another:

Concept: {t['concept']}
From: {t['from_rep']} representation
To: {t['to_rep']} representation

Given representation: {t['from_value']}

Your task:
1. Provide the correct translation of the concept into the target representational system.
2. Explain your reasoning process, including any intermediate steps or transformations you used. (100-150 words)
3. Discuss how the meaning or interpretation of the concept might change (if at all) between these two representational systems. (100-150 words)
4. Provide an example of how this concept might be applied or interpreted in a real-world context, using both representational systems. (100-150 words)

Format your response as follows:

Translation: [Your answer]

Reasoning Process: [Your explanation in 100-150 words]

Meaning Comparison: [Your discussion in 100-150 words]

Real-world Application: [Your example in 100-150 words]

Ensure your response is clear, precise, and demonstrates a deep understanding of the abstract concept and both representational systems. The total length of your response should be between 300-450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The translation from {t['from_rep']} to {t['to_rep']} representation is correct and equivalent to {t['to_value']}",
            "The reasoning process is clear, logical, and demonstrates understanding of both representational systems",
            "The meaning comparison provides insightful analysis of how the concept is represented in both systems, including any nuances or differences",
            "The real-world application is relevant, correctly uses both representational systems, and demonstrates the practical significance of the concept",
            "The response adheres to the specified format and word count guidelines for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
