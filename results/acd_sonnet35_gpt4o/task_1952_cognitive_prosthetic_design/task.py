import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            'working memory',
            'attention control',
            'decision making',
            'emotional regulation',
            'language processing'
        ]
        target_populations = [
            'elderly individuals with mild cognitive impairment',
            'children with ADHD',
            'adults with depression',
            'individuals with autism spectrum disorder',
            'stroke survivors with language deficits'
        ]
        tasks = [
            {
                'cognitive_function': random.choice(cognitive_functions),
                'target_population': random.choice(target_populations)
            },
            {
                'cognitive_function': random.choice(cognitive_functions),
                'target_population': random.choice(target_populations)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered cognitive prosthetic to enhance {t['cognitive_function']} for {t['target_population']}. Then, analyze its potential impacts and ethical implications. Your response should include:

1. Prosthetic Design (300-350 words):
   a) Describe the key components and functioning of your cognitive prosthetic.
   b) Explain how it interfaces with the human brain or cognitive system.
   c) Detail how it enhances the specified cognitive function.
   d) Discuss any potential side effects or limitations of your design.

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your prosthetic's function.
   b) Discuss how your design takes into account the specific needs of the target population.
   c) Propose a method to measure the effectiveness of your prosthetic.

3. AI Integration (200-250 words):
   a) Describe the AI components of your prosthetic and their functions.
   b) Explain how the AI adapts to individual users' needs.
   c) Discuss potential challenges in integrating AI with human cognition and how you address them.

4. Ethical Analysis (250-300 words):
   a) Identify and discuss at least three ethical concerns raised by your cognitive prosthetic.
   b) Analyze potential social impacts, both positive and negative.
   c) Propose guidelines for the ethical development and use of cognitive prosthetics.

5. Future Implications (150-200 words):
   a) Speculate on how widespread adoption of such prosthetics might impact society and human evolution.
   b) Discuss potential future developments or extensions of your technology.

Ensure your response demonstrates a deep understanding of neuroscience, AI, ethics, and human-computer interaction. Be innovative in your design while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, ethics, and human-computer interaction.",
            "The cognitive prosthetic design is innovative, scientifically plausible, and specifically tailored to enhance the given cognitive function for the target population.",
            "The ethical analysis is thorough, considering multiple perspectives and proposing thoughtful guidelines.",
            "The response effectively integrates knowledge from multiple disciplines to address complex challenges.",
            "The writing is clear, well-structured, and uses appropriate terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
