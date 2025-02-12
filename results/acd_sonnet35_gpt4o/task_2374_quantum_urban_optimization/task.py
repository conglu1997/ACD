import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_issues = ['traffic congestion', 'public transportation efficiency', 'emergency response times']
        quantum_approaches = ['quantum annealing', 'quantum approximate optimization algorithm (QAOA)', 'variational quantum eigensolver (VQE)']
        city_sizes = ['small (population 100,000)', 'medium (population 500,000)', 'large (population 2,000,000)']
        
        tasks = {
            "1": {
                "urban_issue": random.choice(urban_issues),
                "quantum_approach": random.choice(quantum_approaches),
                "city_size": random.choice(city_sizes)
            },
            "2": {
                "urban_issue": random.choice(urban_issues),
                "quantum_approach": random.choice(quantum_approaches),
                "city_size": random.choice(city_sizes)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm to optimize urban transportation networks for a {t['city_size']} city, focusing on the issue of {t['urban_issue']} using the {t['quantum_approach']} approach. Then, analyze its potential impact on city planning and sustainability. Your response should include the following sections:

1. Quantum Algorithm Design (300-350 words):
   a) Explain the basics of {t['quantum_approach']} and why it's suitable for addressing {t['urban_issue']} in a {t['city_size']} city.
   b) Describe how you would formulate the {t['urban_issue']} problem as a quantum optimization problem.
   c) Detail the steps of your quantum algorithm, including initialization, quantum operations, and measurement.
   d) Discuss how your algorithm leverages quantum superposition and entanglement to solve the problem more efficiently than classical methods.
   e) Provide a simple pseudocode or flowchart (using ASCII characters) of your quantum algorithm (10-15 lines).

2. Implementation Considerations (200-250 words):
   a) Describe the quantum hardware requirements for your algorithm.
   b) Discuss any classical pre-processing or post-processing steps needed.
   c) Address potential issues such as decoherence and error correction in your implementation.
   d) Explain how your implementation would scale for different city sizes.

3. Performance Analysis (200-250 words):
   a) Estimate the computational complexity of your quantum algorithm compared to the best known classical algorithm for this problem.
   b) Discuss the expected scalability of your algorithm as the size of the urban network increases.
   c) Propose a method to benchmark your quantum algorithm against classical optimization techniques.
   d) Provide a hypothetical performance comparison table for small, medium, and large cities.

4. Urban Planning Impact (250-300 words):
   a) Analyze how your quantum optimization algorithm could improve {t['urban_issue']} in a {t['city_size']} city.
   b) Discuss potential changes in urban planning strategies enabled by your quantum approach.
   c) Explore how the improved optimization could contribute to urban sustainability goals.
   d) Provide a specific example of how your algorithm could be applied to a real-world urban planning scenario.

5. Challenges and Limitations (150-200 words):
   a) Identify potential challenges in implementing your quantum algorithm in real urban environments.
   b) Discuss any limitations of your approach and propose potential solutions or areas for future research.
   c) Address any specific challenges related to the {t['city_size']} city scale.

6. Ethical Considerations (150-200 words):
   a) Analyze potential ethical implications of using quantum computing for urban optimization.
   b) Discuss issues such as data privacy, equity in resource allocation, and potential unintended consequences.
   c) Propose guidelines for the responsible development and deployment of quantum urban optimization systems.
   d) Consider any ethical issues specific to {t['urban_issue']} in a {t['city_size']} city.

Ensure your response demonstrates a deep understanding of quantum computing principles, optimization techniques, and urban planning concepts. Use appropriate technical terminology and provide clear explanations for complex ideas. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section, numbered exactly as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a quantum algorithm using {t['quantum_approach']} to address {t['urban_issue']} in a {t['city_size']} city",
            "The answer demonstrates a clear understanding of quantum computing principles and their application to optimization problems",
            "The response includes a simple pseudocode or flowchart of the quantum algorithm",
            "The answer discusses implementation considerations, including hardware requirements, error correction, and scalability for different city sizes",
            "The response includes a performance analysis comparing the quantum algorithm to classical methods, with a hypothetical performance comparison table",
            "The answer analyzes the potential impact of the quantum algorithm on urban planning and sustainability, with a specific real-world example",
            "The response identifies challenges, limitations, and ethical considerations of the proposed approach, addressing issues specific to the given city size",
            "The answer is well-structured with clear headings for each section, numbered exactly as instructed, and adheres to the provided word limits",
            "The response demonstrates interdisciplinary knowledge of quantum computing, optimization techniques, and urban planning",
            "The answer is creative while maintaining scientific and technological plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
