import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture': 'Japanese',
                'concept': 'perseverance',
                'domain': 'nature'
            },
            {
                'culture': 'Maasai',
                'concept': 'leadership',
                'domain': 'animals'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a machine learning system that generates and analyzes culturally-specific metaphors. Your task is to create a system that can produce and interpret metaphors for the concept of {t['concept']} in {t['culture']} culture, using elements from the domain of {t['domain']}. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the main components of your machine learning system.
   b) Explain how these components interact to generate and analyze metaphors.
   c) Detail any novel techniques or algorithms you would employ.

2. Cultural Knowledge Integration (150-200 words):
   a) Explain how your system would incorporate and represent cultural knowledge specific to {t['culture']}.
   b) Describe how this cultural knowledge would influence metaphor generation and analysis.

3. Metaphor Generation Process (200-250 words):
   a) Detail the approach your system would take to generate metaphors for {t['concept']} using elements from {t['domain']}.
   b) Explain how your system ensures the generated metaphors are culturally appropriate and meaningful.
   c) Provide an example of a potential metaphor your system might generate, and explain its cultural significance.

4. Metaphor Analysis Capabilities (200-250 words):
   a) Describe how your system would analyze and interpret generated or given metaphors.
   b) Explain how it would evaluate the cultural relevance and impact of a metaphor.
   c) Discuss any techniques for assessing the novelty or creativity of generated metaphors.

5. Learning and Adaptation (150-200 words):
   a) Explain how your system would learn and improve its metaphor generation and analysis over time.
   b) Describe any feedback mechanisms or training processes you would implement.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues related to generating and analyzing culturally-specific metaphors.
   b) Address any limitations of your approach and potential biases in the system.

7. Interdisciplinary Implications (100-150 words):
   a) Discuss how this system might contribute to fields such as cognitive linguistics, cultural anthropology, or creative AI.
   b) Propose a potential application of this system outside of pure research.

Ensure your response demonstrates a deep understanding of machine learning, computational linguistics, and cultural anthropology. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['culture']} culture and how it might influence metaphors for {t['concept']}.",
            f"The system design effectively incorporates elements from the domain of {t['domain']} in metaphor generation.",
            "The proposed machine learning system is technically sound and innovative.",
            "The response shows a nuanced understanding of the challenges in generating culturally-appropriate metaphors.",
            "The ethical considerations and limitations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
