import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        abstract_domains = ['mathematical', 'linguistic', 'emotional', 'spatial', 'temporal']
        complex_problems = [
            'Climate change mitigation',
            'Interstellar communication',
            'Consciousness transfer',
            'Quantum computing optimization',
            'Sustainable urban planning'
        ]
        
        tasks = [
            {
                'sensory_modality': modality,
                'abstract_domain': domain,
                'complex_problem': problem
            }
            for modality in sensory_modalities
            for domain in abstract_domains
            for problem in complex_problems
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of mapping cognitive processes between the {t['sensory_modality']} modality and the {t['abstract_domain']} domain, then apply it to address the complex problem of {t['complex_problem']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your cross-modal cognitive mapping AI system.
   b) Explain how your system processes and translates information between the {t['sensory_modality']} modality and the {t['abstract_domain']} domain.
   c) Discuss any novel algorithms or techniques you've incorporated to enable cross-modal mapping.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Cognitive Process Analysis (250-300 words):
   a) Analyze how cognitive processes differ between the {t['sensory_modality']} modality and the {t['abstract_domain']} domain.
   b) Explain how your system accounts for these differences in its mapping process.
   c) Discuss any cognitive theories or models that inform your system's design.

3. Application to Complex Problem (250-300 words):
   a) Describe how your system would approach the problem of {t['complex_problem']}.
   b) Explain how the cross-modal mapping between {t['sensory_modality']} and {t['abstract_domain']} could provide unique insights or solutions.
   c) Provide a specific example of how your system might generate a novel solution or perspective on the problem.

4. Evaluation and Validation (200-250 words):
   a) Propose a method for evaluating the effectiveness of your system's cross-modal mappings.
   b) Describe how you would validate the solutions generated for the complex problem.
   c) Discuss potential challenges in assessing the system's performance and how you might address them.

5. Ethical Considerations and Limitations (200-250 words):
   a) Analyze potential ethical implications of using cross-modal cognitive mapping in AI systems.
   b) Discuss any limitations of your approach and areas for future improvement.
   c) Propose guidelines for the responsible development and use of such systems.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how your system might impact or be applied to fields beyond AI and cognitive science.
   b) Discuss the potential long-term consequences of advanced cross-modal cognitive mapping technologies.

Ensure your response demonstrates a deep understanding of cognitive processes, AI systems, and the specified modalities and domains. Be creative and innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive processes in both the {t['sensory_modality']} modality and the {t['abstract_domain']} domain",
            "The AI system architecture is well-explained and incorporates novel techniques for cross-modal cognitive mapping",
            f"The application to {t['complex_problem']} is creative and demonstrates how cross-modal mapping could provide unique insights",
            "The evaluation and validation methods proposed are rigorous and address potential challenges",
            "Ethical considerations and limitations are thoroughly discussed with thoughtful guidelines proposed",
            "The response demonstrates interdisciplinary thinking and explores broader implications of the technology",
            "The response is creative, logically consistent, and scientifically plausible throughout all sections",
            "The response adheres to the specified format and word count guidelines for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
