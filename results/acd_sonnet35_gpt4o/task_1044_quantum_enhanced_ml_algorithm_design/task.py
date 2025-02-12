import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "image classification",
            "natural language processing",
            "recommendation systems",
            "financial forecasting"
        ]
        quantum_approaches = [
            "quantum annealing",
            "variational quantum circuits",
            "quantum Fourier transform",
            "quantum amplitude estimation"
        ]
        tasks = [
            {
                'problem': random.choice(problems),
                'quantum_approach': random.choice(quantum_approaches)
            },
            {
                'problem': random.choice(problems),
                'quantum_approach': random.choice(quantum_approaches)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced machine learning algorithm for {t['problem']} using {t['quantum_approach']}. Your response should include:

1. Algorithm Overview (200-250 words):
   a) Briefly describe the classical machine learning approach to the given problem.
   b) Explain your proposed quantum-enhanced algorithm and how it incorporates {t['quantum_approach']}.
   c) Highlight the key differences between your quantum-enhanced approach and classical methods.

2. Quantum Advantage (150-200 words):
   a) Analyze the potential advantages of your quantum-enhanced algorithm over classical approaches.
   b) Discuss any specific problem characteristics that make it suitable for quantum enhancement.
   c) Provide a theoretical analysis of the expected speedup or improvement in accuracy, if applicable.

3. Algorithm Details (250-300 words):
   a) Describe the step-by-step process of your quantum-enhanced algorithm.
   b) Explain how classical and quantum components of your algorithm interact.
   c) Discuss any novel quantum operations or subroutines you've designed for this algorithm.
   d) Provide a high-level pseudocode or quantum circuit diagram of your algorithm.

4. Implementation Considerations (150-200 words):
   a) Discuss the challenges in implementing your algorithm on current or near-term quantum hardware.
   b) Propose methods to mitigate errors or decoherence effects in your algorithm.
   c) Suggest a hybrid quantum-classical approach if applicable.

5. Benchmarking and Evaluation (100-150 words):
   a) Propose a method to benchmark your quantum-enhanced algorithm against classical approaches.
   b) Discuss potential metrics for evaluating the algorithm's performance and quantum advantage.
   c) Describe any datasets or simulation environments that could be used for testing.

6. Ethical Considerations and Limitations (100-150 words):
   a) Discuss any ethical implications or potential misuses of your quantum-enhanced algorithm.
   b) Identify limitations of your approach and suggest areas for future research and improvement.

Ensure your response demonstrates a deep understanding of both quantum computing principles and machine learning algorithms. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section.

Your entire response should be between 950-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and machine learning concepts.",
            "The proposed algorithm creatively integrates quantum computing principles with machine learning techniques.",
            "The quantum advantage is clearly explained and justified with theoretical analysis.",
            "The algorithm details are comprehensive and include a clear step-by-step process or pseudocode.",
            "Implementation challenges and mitigation strategies are thoroughly discussed.",
            "The benchmarking and evaluation methods are appropriate and well-explained.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
