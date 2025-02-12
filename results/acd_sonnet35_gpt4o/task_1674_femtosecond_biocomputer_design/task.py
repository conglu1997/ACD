import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_process': 'Photosynthetic energy transfer',
                'computational_architecture': 'Quantum annealing',
                'application_domain': 'Climate modeling',
                'performance_metric': 'Energy efficiency (operations per joule)'
            },
            {
                'biological_process': 'Protein folding dynamics',
                'computational_architecture': 'Neuromorphic computing',
                'application_domain': 'Drug discovery',
                'performance_metric': 'Speed (operations per femtosecond)'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical femtosecond-scale biological computer system that integrates {t['biological_process']} with {t['computational_architecture']} for applications in {t['application_domain']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your femtosecond biocomputer.
   b) Explain how it leverages {t['biological_process']} for computation.
   c) Detail how you integrate this with {t['computational_architecture']}.
   d) Discuss any novel technologies or techniques required for your system.

2. Operational Principles (200-250 words):
   a) Explain the fundamental principles enabling femtosecond-scale computation in your system.
   b) Describe how information is encoded, processed, and retrieved.
   c) Discuss how your system maintains coherence and manages errors at this timescale.

3. Performance Analysis (200-250 words):
   a) Estimate the theoretical performance capabilities of your system in terms of {t['performance_metric']}.
   b) Compare these to current classical and quantum computing systems.
   c) Discuss potential advantages and limitations of your femtosecond biocomputer.

4. Application in {t['application_domain']} (200-250 words):
   a) Describe how your system could be applied to solve problems in {t['application_domain']}.
   b) Provide a specific example of a computation it could perform in this domain.
   c) Discuss potential impacts and benefits of using your system in this field.

5. Fabrication and Implementation (150-200 words):
   a) Propose a method for fabricating or growing your femtosecond biocomputer.
   b) Discuss challenges in implementing and scaling up your system.
   c) Suggest potential solutions or areas for future research to address these challenges.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical implications of developing and using femtosecond biocomputers.
   b) Discuss possible societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of ultrafast biological processes, advanced computational architectures, and their potential applications. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate scientific terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. System Architecture:') on a new line, followed by your response for that section. Use subheadings (a, b, c, d) within each section as outlined above. Your total response should be between 1150-1450 words, with each section adhering to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_process']}, {t['computational_architecture']}, and their potential applications in {t['application_domain']}.",
            "The system architecture is well-designed, clearly incorporates the specified biological process and computational architecture, and includes novel technologies or techniques.",
            "The operational principles are well-explained, including information encoding, processing, and retrieval at femtosecond scales.",
            f"The performance analysis provides reasonable estimates of {t['performance_metric']} and comparisons to current systems.",
            f"The application to {t['application_domain']} is well-described with a specific example of a computation it could perform.",
            "Fabrication and implementation challenges are identified with potential solutions or research directions.",
            "Ethical considerations and societal impacts are thoughtfully discussed with proposed guidelines for responsible development.",
            "The response is creative and speculative while maintaining scientific plausibility.",
            "The response follows the specified format with clear headings and subheadings for each section.",
            "The total word count is between 1150-1450 words, with each section adhering to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
