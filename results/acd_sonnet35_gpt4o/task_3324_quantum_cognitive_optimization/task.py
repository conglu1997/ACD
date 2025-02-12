import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        optimization_problems = [
            {
                "name": "Traffic Flow Optimization",
                "description": "Optimize traffic flow in a city with 1 million inhabitants and 100,000 vehicles during peak hours."
            },
            {
                "name": "Green Space Distribution",
                "description": "Optimize the distribution of green spaces in a city to maximize environmental benefits and accessibility for residents."
            },
            {
                "name": "Public Transportation Network",
                "description": "Design an optimal public transportation network to minimize travel times and maximize coverage for a city of 2 million people."
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(optimization_problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model and apply it to solve the following urban planning optimization problem: {t['name']} - {t['description']}

Your response should include the following sections:

1. Quantum-Inspired Cognitive Model (300-350 words):
   a) Describe the key components of your quantum-inspired cognitive model.
   b) Explain how quantum principles (e.g., superposition, entanglement) are incorporated into your model.
   c) Discuss how your model represents and processes information differently from classical cognitive models.
   d) Provide a textual description of a simple diagram or equation that illustrates a core concept of your model.

2. Application to Urban Planning (250-300 words):
   a) Explain how your quantum-inspired cognitive model can be applied to the given urban planning problem.
   b) Describe the specific quantum-inspired algorithms or techniques you would use to approach the optimization task.
   c) Discuss any potential advantages your approach might have over classical optimization methods.
   d) Provide a specific example of how your model would solve a sub-problem within the larger optimization task.

3. Implementation Strategy (200-250 words):
   a) Outline the steps required to implement your quantum-inspired solution.
   b) Describe any technical challenges you anticipate and propose potential solutions.
   c) Discuss how your implementation could be scaled to handle larger, more complex urban systems.

4. Comparative Analysis (150-200 words):
   a) Compare your quantum-inspired approach to a classical cognitive model or optimization technique.
   b) Discuss the potential differences in computational efficiency and solution quality.
   c) Identify any trade-offs between quantum-inspired and classical approaches in this context.

5. Ethical and Practical Considerations (200-250 words):
   a) Discuss any ethical implications of using quantum-inspired cognitive models for urban planning decisions.
   b) Address potential concerns about the interpretability and transparency of quantum-inspired solutions.
   c) Propose guidelines for responsible implementation of your approach in real-world urban planning scenarios.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your quantum-inspired cognitive model.
   b) Propose an experiment to empirically validate the effectiveness of your approach.
   c) Discuss how your model might contribute to our understanding of both quantum cognition and urban systems.

Ensure your response demonstrates a deep understanding of quantum principles, cognitive science, and urban planning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above (e.g., '1. Quantum-Inspired Cognitive Model'). Adhere strictly to the word count for each section. Your total response should be between 1250-1550 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum principles and their application to cognitive modeling.",
            "The proposed quantum-inspired cognitive model is innovative and clearly explained.",
            f"The approach to solving the {t['name']} problem is well-reasoned and leverages the unique features of the quantum-inspired model.",
            "The response includes a specific example of how the model would solve a sub-problem within the larger optimization task.",
            "The response addresses implementation challenges and ethical considerations comprehensively.",
            "The future research directions proposed are insightful and demonstrate a broad understanding of the field.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
