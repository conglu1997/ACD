import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling in synaptic transmission",
            "quantum coherence in microtubules",
            "quantum entanglement between neurons"
        ]
        optimization_problems = [
            "protein folding prediction",
            "financial portfolio optimization",
            "urban traffic flow optimization",
            "supply chain logistics",
            "drug discovery and molecular design"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "quantum_effect": random.choice(quantum_effects),
                "optimization_problem": random.choice(optimization_problems)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics the quantum effect of {t['quantum_effect']} observed in the brain to solve the complex optimization problem of {t['optimization_problem']}. Your response should include:

1. Quantum-Neural Mechanism (250-300 words):
   a) Explain the chosen quantum effect and its observed role in brain function.
   b) Describe how your AI system would mimic this quantum effect.
   c) Discuss how this mechanism could be implemented in artificial neural networks.

2. Optimization Algorithm (250-300 words):
   a) Outline your quantum-inspired optimization algorithm for solving {t['optimization_problem']}.
   b) Explain how the quantum-neural mechanism enhances the algorithm's performance.
   c) Compare your approach to traditional optimization methods for this problem.

3. System Architecture (200-250 words):
   a) Describe the overall structure of your quantum-neural AI system.
   b) Explain how classical and quantum components would interact.
   c) Discuss any special hardware requirements or quantum-classical hybrid approaches.

4. Performance Analysis (200-250 words):
   a) Predict the potential advantages of your system over classical AI approaches.
   b) Identify possible limitations or challenges in implementing your system.
   c) Propose metrics to evaluate the system's performance and quantum advantage.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to your quantum-neural AI system.
   b) Analyze possible societal impacts of applying this technology to {t['optimization_problem']}.
   c) Suggest guidelines or policies for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response using clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed explanation of the quantum effect {t['quantum_effect']} and how it's mimicked in the AI system",
            f"The response should outline a quantum-inspired optimization algorithm for {t['optimization_problem']}",
            "The response should describe the overall architecture of the quantum-neural AI system",
            "The response should analyze the potential performance advantages and limitations of the system",
            "The response should discuss ethical and societal implications of the technology",
            "The response should demonstrate a deep understanding of quantum mechanics, neuroscience, and artificial intelligence",
            "The response should be creative while maintaining scientific plausibility",
            "The response should be well-organized with clear headings for each section and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
