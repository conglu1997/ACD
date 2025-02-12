class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "optimization_problem": "Traveling Salesman Problem",
                "quantum_principle": "Superposition",
                "constraint": "Limited to 100 qubits"
            },
            "2": {
                "optimization_problem": "Portfolio Optimization",
                "quantum_principle": "Entanglement",
                "constraint": "Must operate on classical hardware"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for solving the {t['optimization_problem']}, incorporating the quantum principle of {t['quantum_principle']}. Your system must adhere to the following constraint: {t['constraint']}.

Quantum principles explanation:
- Superposition: A quantum state where a qubit can exist in multiple states simultaneously.
- Entanglement: A quantum phenomenon where the states of two or more qubits are correlated and cannot be described independently.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired AI system.
   b) Explain how it incorporates the specified quantum principle into a classical AI architecture.
   c) Discuss how your system addresses the given constraint.
   d) Provide a high-level visual representation of your system architecture (described in words).

2. Quantum-Classical Integration (200-250 words):
   a) Detail how your system translates the optimization problem into a quantum-inspired representation.
   b) Explain the mechanism for mapping quantum concepts to classical computations.
   c) Describe any novel algorithms or techniques used in this integration.

3. Optimization Approach (200-250 words):
   a) Outline your system's approach to solving the specified optimization problem.
   b) Explain how the quantum-inspired elements enhance the optimization process.
   c) Discuss potential advantages over purely classical optimization methods.

4. Performance Analysis (150-200 words):
   a) Propose metrics for evaluating your system's performance.
   b) Describe potential benchmarks for comparison with classical systems.
   c) Discuss expected scalability and limitations of your approach.

5. Theoretical Implications (150-200 words):
   a) Analyze how your system contributes to our understanding of quantum-classical interfaces in computation.
   b) Discuss potential insights into the nature of optimization problems or quantum phenomena.

6. Practical Applications (100-150 words):
   a) Suggest two potential real-world applications for your quantum-inspired AI system.
   b) Explain how these applications leverage the unique features of your system.

7. Future Directions (100-150 words):
   a) Propose two potential improvements or extensions to your system.
   b) Discuss how these changes could address current limitations or expand capabilities.

Ensure your response demonstrates a deep understanding of quantum computing principles, AI architectures, and optimization theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word count guidelines for each section. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, AI architectures, and optimization theory.",
            f"The system effectively incorporates the quantum principle of {t['quantum_principle']} into a classical AI architecture.",
            f"The design adheres to the specified constraint: {t['constraint']}.",
            f"The approach effectively addresses the {t['optimization_problem']}.",
            "The response is innovative while maintaining scientific plausibility.",
            "The analysis of theoretical implications and future directions is insightful and well-reasoned.",
            "The response adheres to the specified word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
