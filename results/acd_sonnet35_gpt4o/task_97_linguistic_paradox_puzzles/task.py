import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        puzzles = [
            {
                'type': 'ambiguity',
                'context': 'Time flies like an arrow; fruit flies like a banana.',
                'question': 'Explain the multiple layers of ambiguity in this sentence pair and provide at least three distinct interpretations.'
            },
            {
                'type': 'paradox',
                'context': 'This sentence is false. The previous sentence is true.',
                'question': 'Explain the paradox created by these two sentences and propose a resolution.'
            },
            {
                'type': 'meta-linguistic',
                'context': 'The word "heterological" is defined as a word that does not describe itself.',
                'question': 'Is the word "heterological" heterological? Explain your reasoning and the paradox this creates.'
            },
            {
                'type': 'ambiguity',
                'context': 'The complex houses married and single soldiers and their families.',
                'question': 'Identify at least two different ways this sentence can be interpreted and explain the structural ambiguity.'
            },
            {
                'type': 'paradox',
                'context': 'In a town where the barber shaves all and only those who do not shave themselves, who shaves the barber?',
                'question': 'Explain this paradox in detail and propose a logical resolution.'
            },
            {
                'type': 'meta-linguistic',
                'context': 'The following sentence is true. The preceding sentence is false.',
                'question': 'Analyze the self-referential nature of these sentences and explain the paradox they create.'
            }
        ]
        
        tasks = random.sample(puzzles, 2)
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task involves analyzing and solving a linguistic puzzle based on {t['type']}.

Context: {t['context']}

{t['question']}

Additionally, create a new {t['type']} puzzle of your own, similar in style but more complex than the one provided. Present both the puzzle and its solution.

Format your response as follows:

1. Analysis of given puzzle:
[Your detailed analysis here]

2. Your original puzzle:
[Your more complex puzzle here]

3. Solution to your puzzle:
[Your comprehensive solution here]

Ensure that your original puzzle is more challenging than the given one and demonstrates a deep understanding of the linguistic or logical principles involved."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The analysis of the given {t['type']} puzzle is comprehensive, accurate, and insightful.",
            f"The original {t['type']} puzzle created is valid, more complex than the given puzzle, and demonstrates creativity.",
            "The solution to the original puzzle is correct, well-explained, and shows deep understanding of the principles involved.",
            "The response demonstrates advanced linguistic knowledge, logical reasoning, and meta-linguistic awareness where applicable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
