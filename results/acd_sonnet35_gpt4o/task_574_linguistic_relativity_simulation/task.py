import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            'time perception',
            'color categorization',
            'spatial reasoning',
            'numerical cognition',
            'emotional expression',
            'causal reasoning',
            'social relationships',
            'environmental awareness'
        ]
        
        complexity_levels = ['basic', 'intermediate', 'advanced']
        
        tasks = {
            '1': {
                'concept': random.choice(concepts),
                'complexity': random.choice(complexity_levels),
                'focus': random.choice(['cognitive', 'cultural'])
            },
            '2': {
                'concept': random.choice(concepts),
                'complexity': random.choice(complexity_levels),
                'focus': random.choice(['cognitive', 'cultural'])
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language feature based on the concept of linguistic relativity (Sapir-Whorf hypothesis) that could potentially influence {t['concept']}. Then, analyze its potential cognitive and cultural impacts. Your task has a {t['complexity']} complexity level and should focus primarily on the {t['focus']} aspects.

Provide your response in the following format:

1. Language Feature Design (200-250 words):
   [Your description here]

2. Cognitive Impact Analysis (200-250 words):
   [Your analysis here]

3. Cultural Implications (150-200 words):
   [Your discussion here]

4. Experimental Design (150-200 words):
   [Your proposal here]

5. Interdisciplinary Connections (100-150 words):
   [Your explanation here]

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and cultural dynamics. Use clear, concise language and provide examples where appropriate to illustrate complex concepts. Pay special attention to the {t['focus']} aspects of your analysis, given the task's focus."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of linguistic relativity and its potential impacts on cognition and culture.",
            "The proposed language feature is novel, well-defined, and logically connected to the given concept.",
            f"The analysis of {t['focus']} impacts is thorough, plausible, and supported by reasoning.",
            "The experimental design is well-thought-out and appropriate for testing the hypothesized effects.",
            "The response shows interdisciplinary thinking and proposes relevant connections to other fields.",
            f"The overall complexity of the response matches the {t['complexity']} level specified in the task.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0