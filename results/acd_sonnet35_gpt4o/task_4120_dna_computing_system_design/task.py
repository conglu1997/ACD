import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'problem_type': 'Graph Coloring',
                'application_field': 'Network Optimization'
            },
            {
                'problem_type': 'Traveling Salesman Problem',
                'application_field': 'Drug Discovery'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a DNA-based computing system capable of solving the {t['problem_type']} and analyze its potential applications in {t['application_field']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your DNA-based computing system.
   b) Explain how DNA sequences are used to represent and process information.
   c) Detail the mechanisms for input, computation, and output in your system.
   d) Discuss any novel techniques or algorithms used in your design.
   e) Provide a high-level diagram or description of your system architecture.

2. Problem Encoding (250-300 words):
   a) Explain how you encode the {t['problem_type']} using DNA sequences.
   b) Describe the mapping between problem elements and DNA structures.
   c) Discuss any optimizations in your encoding to improve computational efficiency.

3. Computation Process (250-300 words):
   a) Detail the steps your DNA-based system takes to solve the {t['problem_type']}.
   b) Explain how parallel processing is achieved in your system.
   c) Describe any error-correction mechanisms implemented in your design.
   d) Provide an example of how a specific instance of the problem would be solved.

4. Output Interpretation (200-250 words):
   a) Explain how the final DNA state is interpreted as a solution to the problem.
   b) Describe any post-processing steps required to obtain the final result.
   c) Discuss the scalability of your system for larger problem instances.

5. Application in {t['application_field']} (250-300 words):
   a) Analyze how your DNA-based computing system could be applied in {t['application_field']}.
   b) Describe specific scenarios where your system would provide advantages over traditional computing methods.
   c) Discuss any modifications needed to adapt your system for this application field.

6. Comparison with Traditional Computing (200-250 words):
   a) Compare the performance of your DNA-based system with traditional electronic computers for solving the {t['problem_type']}.
   b) Discuss advantages and limitations of your approach.
   c) Analyze energy efficiency and storage density of your DNA-based system.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using DNA-based computing systems.
   b) Address any biosafety concerns related to your design.
   c) Propose two potential improvements or extensions to your system for future research.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and computational design. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of DNA-based computing principles and molecular biology.",
            "The system architecture is well-designed and clearly explained, with novel elements.",
            "The problem encoding and computation process are logically sound and efficiently designed.",
            "The application analysis is thorough and identifies unique advantages of DNA-based computing in the specified field.",
            "The comparison with traditional computing is balanced and well-reasoned.",
            "Ethical considerations and future directions are thoughtfully addressed.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
