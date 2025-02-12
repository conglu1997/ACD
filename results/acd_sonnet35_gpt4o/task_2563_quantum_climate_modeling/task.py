import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_variables = ['Ocean acidification', 'Extreme weather events', 'Biodiversity loss', 'Carbon cycle feedback loops']
        quantum_algorithms = ['Quantum phase estimation', 'Quantum machine learning', 'Quantum Fourier transform']
        time_scales = ['Decadal (10-30 years)', 'Centennial (100-300 years)', 'Millennial (1000+ years)']
        
        tasks = [
            {
                'climate_variable': random.choice(climate_variables),
                'quantum_algorithm': random.choice(quantum_algorithms),
                'time_scale': random.choice(time_scales),
                'scenario': 'Rapid transition to renewable energy'
            },
            {
                'climate_variable': random.choice(climate_variables),
                'quantum_algorithm': random.choice(quantum_algorithms),
                'time_scale': random.choice(time_scales),
                'scenario': 'Business-as-usual emissions'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm for advanced climate modeling, focusing on {t['climate_variable']} predictions using the {t['quantum_algorithm']} approach for {t['time_scale']} forecasting. Consider the scenario: {t['scenario']}. Then, analyze its potential impact on climate change predictions and mitigation strategies.

Your response must follow this exact structure:

1. Quantum Algorithm Design (300-350 words):
   1.1. Quantum algorithm basics and suitability
   1.2. Problem mapping to quantum algorithm
   1.3. Algorithm steps (initialization, operations, measurement)
   1.4. Potential advantages over classical models

2. Climate Science Integration (250-300 words):
   2.1. Incorporation of key climate variables and processes
   2.2. Handling complexity and non-linearity
   2.3. Addressing current modeling limitations

3. Implementation Considerations (200-250 words):
   3.1. Quantum hardware requirements
   3.2. Noise and error handling
   3.3. Classical pre/post-processing steps

4. Performance Analysis (200-250 words):
   4.1. Estimated improvements in accuracy/efficiency
   4.2. Scalability for global climate models
   4.3. Potential limitations and challenges

5. Impact on Climate Change Strategies (200-250 words):
   5.1. Improvements in climate change predictions
   5.2. Impacts on policy-making and mitigation
   5.3. Contributions to climate adaptation planning

6. Ethical Considerations and Future Directions (150-200 words):
   6.1. Ethical implications
   6.2. Potential risks of accurate predictions
   6.3. Future research directions

Ensure your response demonstrates a deep understanding of both quantum computing principles and climate science. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1300-1600 words.

Include at least one equation using LaTeX notation to represent a key concept in your quantum climate modeling approach.

Provide a simple pseudocode snippet (5-10 lines) illustrating a crucial part of your quantum algorithm.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the exact structure specified in the instructions.",
            "The quantum algorithm design is well-explained and tailored to the given climate variable and time scale.",
            "The climate science integration demonstrates a deep understanding of complex climate systems.",
            "Implementation considerations address specific challenges in quantum computing for climate modeling.",
            "The performance analysis provides a realistic and quantitative assessment of improvements and limitations.",
            "The impact on climate change strategies is thoroughly analyzed, considering multiple stakeholders.",
            "Ethical considerations and future directions are insightful and well-reasoned.",
            "The response includes at least one relevant equation using LaTeX notation.",
            "A pseudocode snippet (5-10 lines) illustrating a crucial part of the quantum algorithm is provided.",
            "The response is innovative while maintaining scientific plausibility and adheres to the word limits.",
            f"The proposed solution specifically addresses the given scenario: {t['scenario']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
