import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            'Global Workspace Theory',
            'Integrated Information Theory',
            'Higher-Order Thought Theory',
            'Quantum Consciousness Theory',
            'Predictive Processing Theory'
        ]
        cognitive_perspectives = [
            'Neuroscientific',
            'Philosophical',
            'Computational',
            'Evolutionary',
            'Phenomenological'
        ]
        
        tasks = {}
        for i in range(1, 3):
            theory = random.choice(consciousness_theories)
            perspective = random.choice(cognitive_perspectives)
            tasks[str(i)] = {
                'theory': theory,
                'perspective': perspective
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to create a narrative exploring a theory of consciousness and then analyze it from a specific cognitive perspective.\n\n" \
               f"Consciousness Theory: {t['theory']}\n" \
               f"Cognitive Perspective: {t['perspective']}\n\n" \
               f"1. Write a short story (300-400 words) that creatively illustrates or explores the {t['theory']} of consciousness. Your story should demonstrate a deep understanding of the theory while presenting it in an engaging narrative format.\n\n" \
               f"2. Analyze your story from the {t['perspective']} perspective (200-250 words). Discuss how elements of your narrative reflect key aspects of the consciousness theory and how they might be interpreted or studied from this cognitive perspective.\n\n" \
               f"3. Propose a hypothetical experiment or study (150-200 words) inspired by your story that could further explore the intersection of the {t['theory']} and the {t['perspective']} approach to cognition.\n\n" \
               f"4. Reflect on the process of creating this narrative and analysis (100-150 words). Discuss any challenges you encountered in translating abstract theories into narrative form and analyzing them from different perspectives.\n\n" \
               f"Format your response with clear headings for each section. Your total response should be between 750-1000 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story effectively illustrates or explores the {t['theory']} of consciousness.",
            f"The analysis from the {t['perspective']} perspective is insightful and well-reasoned.",
            "The proposed experiment or study is creative and relevant to the theory and perspective.",
            "The reflection demonstrates meta-cognitive awareness and critical thinking.",
            "The response demonstrates a deep understanding of both the consciousness theory and the cognitive perspective.",
            "The writing is clear, engaging, and follows the requested format and word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
