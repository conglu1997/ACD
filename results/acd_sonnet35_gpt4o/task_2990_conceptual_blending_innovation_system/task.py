import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'domain1': 'Quantum Physics',
                'domain2': 'Urban Planning',
                'problem_area': 'Sustainable Energy Distribution'
            },
            {
                'domain1': 'Neuroscience',
                'domain2': 'Social Media',
                'problem_area': 'Digital Addiction Prevention'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating novel conceptual blends across different domains to solve complex problems and drive innovation. Your system should combine concepts from {t['domain1']} and {t['domain2']} to address challenges in {t['problem_area']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for conceptual blending.
   b) Explain how your system represents and manipulates concepts from different domains.
   c) Detail the process of generating and evaluating conceptual blends.
   d) Discuss any novel AI techniques or algorithms used in your system.

2. Conceptual Blending Process (250-300 words):
   a) Explain how your system identifies key concepts and structures in each domain.
   b) Describe the mapping process between domains.
   c) Detail how novel blends are created and refined.
   d) Provide an example of a potential conceptual blend your system might generate for the given problem area.

3. Knowledge Representation (200-250 words):
   a) Describe how domain knowledge is represented in your system.
   b) Explain how your system handles different types of knowledge (e.g., declarative, procedural, analogical).
   c) Discuss any challenges in representing knowledge from diverse domains and how you address them.

4. Evaluation and Refinement (200-250 words):
   a) Propose methods for evaluating the novelty, usefulness, and coherence of generated conceptual blends.
   b) Describe how your system refines and improves blends based on these evaluations.
   c) Discuss how you would validate the effectiveness of your system in real-world innovation scenarios.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI-generated conceptual blends in problem-solving and innovation.
   b) Address issues of bias, accountability, and transparency in your system.
   c) Propose guidelines for responsible development and use of conceptual blending AI systems.

6. Interdisciplinary Implications (200-250 words):
   a) Discuss how your system might contribute to our understanding of human creativity and cognition.
   b) Explore potential applications of your system in fields such as scientific research, education, or artistic expression.
   c) Propose a specific research question or experiment to further explore the intersection of AI, conceptual blending, and human cognition.

Ensure your response demonstrates a deep understanding of conceptual blending theory, the given domains, and AI technologies. Be creative in your approach while maintaining scientific and ethical plausibility. Your total response should be between 1300-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of conceptual blending theory, {t['domain1']}, {t['domain2']}, and AI technologies.",
            "The system architecture is well-designed and clearly explains how concepts from different domains are represented and blended.",
            "The conceptual blending process is thoroughly explained and includes a plausible example relevant to the given problem area.",
            "The knowledge representation approach is well-thought-out and addresses challenges in handling diverse domains.",
            "The evaluation and refinement methods are appropriate and comprehensive.",
            "Ethical considerations are thoughtfully discussed with proposed guidelines for responsible development.",
            "The interdisciplinary implications are insightful and include a relevant research question or experiment.",
            "The response is creative and innovative while maintaining scientific and ethical plausibility.",
            "The response follows the specified format with clear sections and subsections.",
            "The total word count is between 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
