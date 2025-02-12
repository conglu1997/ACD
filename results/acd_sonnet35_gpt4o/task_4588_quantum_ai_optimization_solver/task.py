import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                'domain': 'supply_chain',
                'problem': 'Optimize global logistics network',
                'constraints': ['multiple warehouses', 'varying transportation costs', 'demand fluctuations']
            },
            {
                'domain': 'finance',
                'problem': 'Portfolio optimization under uncertainty',
                'constraints': ['risk management', 'market volatility', 'regulatory compliance']
            }
        ]
        return {str(i+1): task for i, task in enumerate(problems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-classical AI system to solve the following complex optimization problem in the {t['domain']} domain: {t['problem']}. Your system should address the following constraints: {', '.join(t['constraints'])}.

A hybrid quantum-classical AI system combines quantum computing capabilities with classical AI algorithms to leverage the strengths of both approaches in solving complex problems.

Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the overall architecture of your hybrid quantum-classical AI system.
   b) Explain which parts of the problem are handled by quantum computing and which by classical AI.
   c) Detail the key quantum and classical algorithms used in your system.
   d) Provide a high-level diagram of your system architecture (describe it textually).

2. Quantum Component (250-300 words):
   a) Explain the quantum algorithms or techniques used in your system.
   b) Describe how you encode the optimization problem into a quantum-compatible format.
   c) Discuss any quantum error correction or mitigation strategies employed.

3. Classical AI Component (250-300 words):
   a) Detail the classical AI algorithms used in your system.
   b) Explain how the classical component interacts with the quantum component.
   c) Describe any machine learning techniques used for problem decomposition or solution refinement.

4. Optimization Process (200-250 words):
   a) Outline the step-by-step process of how your system solves the given optimization problem.
   b) Explain how your system handles the specified constraints.
   c) Discuss any novel approaches or techniques you've incorporated to improve optimization performance.

5. Performance Analysis (200-250 words):
   a) Propose methods to evaluate the performance of your hybrid system.
   b) Compare the expected performance of your system to purely classical approaches.
   c) Discuss potential advantages and limitations of your hybrid approach.

6. Practical Implementation (150-200 words):
   a) Describe the hardware requirements for implementing your system.
   b) Discuss any challenges in scaling your system to handle larger, real-world problems.
   c) Suggest potential modifications to make your system more practical or efficient.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical implications of using your system in the given domain.
   b) Propose guidelines for responsible development and use of quantum-AI hybrid systems.
   c) Suggest future research directions to further improve quantum-classical optimization techniques.

Ensure your response demonstrates a deep understanding of both quantum computing and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of both quantum computing and artificial intelligence principles.",
            "The proposed hybrid system effectively addresses the given optimization problem and specified constraints.",
            "The system architecture is clearly described, innovative, and scientifically plausible.",
            "The quantum and classical components are well-explained and their integration is logically presented.",
            "The optimization process is clearly outlined and addresses the problem constraints.",
            "The performance analysis and practical implementation sections show critical thinking about real-world applications.",
            "Ethical considerations are thoughtfully addressed, and future research directions are insightful.",
            "The overall response showcases interdisciplinary knowledge integration and creative problem-solving in quantum computing and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
