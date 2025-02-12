import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            'entropy',
            'emergence',
            'recursion',
            'duality',
            'symmetry'
        ]
        musical_elements = [
            'harmony',
            'rhythm',
            'timbre',
            'form',
            'dynamics'
        ]
        tasks = [
            {
                'concept': random.choice(concepts),
                'musical_focus': random.choice(musical_elements)
            },
            {
                'concept': random.choice(concepts),
                'musical_focus': random.choice(musical_elements)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate the complex abstract concept of {t['concept']} into a musical composition, with a particular focus on the musical element of {t['musical_focus']}. Then, analyze its output for conceptual accuracy and musical coherence. Your response should include:

1. Conceptual Analysis (200-250 words):
   a) Define and explain the concept of {t['concept']} in detail.
   b) Identify key aspects or properties of this concept that could be represented musically.
   c) Discuss any challenges in translating this abstract concept into music.

2. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for conceptual music translation.
   b) Explain how your system integrates knowledge from cognitive science, music theory, and AI.
   c) Detail how the system translates abstract concepts into musical elements, with a focus on {t['musical_focus']}.
   d) Discuss any novel techniques or algorithms employed in your system.

3. Translation Process (200-250 words):
   a) Outline the step-by-step process your AI uses to translate {t['concept']} into a musical composition.
   b) Explain how the system ensures both conceptual accuracy and musical coherence.
   c) Provide specific examples of how aspects of {t['concept']} might be represented in {t['musical_focus']}.

4. Output Analysis (250-300 words):
   a) Describe how you would analyze the musical output of your AI system.
   b) Propose methods to evaluate the composition's effectiveness in representing {t['concept']}.
   c) Discuss potential metrics for assessing both conceptual accuracy and musical quality.
   d) Explain how you would validate the system's output against human expert evaluations.

5. Cognitive and Artistic Implications (150-200 words):
   a) Discuss what your AI system's approach might reveal about human cognition and creativity.
   b) Explore potential applications of this technology in fields such as education, therapy, or artistic expression.
   c) Address any ethical considerations related to AI-generated conceptual art.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in your AI conceptual music translation system.
   b) Propose two ways to extend or improve your system in future research.
   c) Suggest a specific experiment to further explore the relationship between abstract concepts, music, and AI.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and AI techniques. Be creative in your approach while maintaining scientific and artistic plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the concept of {t['concept']} and how it can be translated into music.",
            f"The AI system architecture effectively integrates knowledge from cognitive science, music theory, and AI, with a clear focus on {t['musical_focus']}.",
            "The translation process is well-explained and demonstrates a plausible method for converting abstract concepts into musical elements.",
            "The output analysis section proposes valid methods for evaluating both conceptual accuracy and musical quality.",
            "The response addresses cognitive and artistic implications, as well as ethical considerations of AI-generated conceptual art.",
            "The limitations and future directions section identifies relevant challenges and proposes interesting extensions to the research.",
            "The overall response is creative, scientifically plausible, and demonstrates interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
