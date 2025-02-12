import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "name": "Aquatic",
                "description": "A synthetic ocean ecosystem with varying depths and temperatures"
            },
            {
                "name": "Terrestrial",
                "description": "A synthetic land-based ecosystem with diverse terrain and climate zones"
            }
        ]
        return {
            "1": random.choice(environments),
            "2": random.choice(environments)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model for a synthetic ecosystem that evolves over time, incorporating principles of synthetic biology and evolutionary algorithms. Your task is to create an innovative and scientifically plausible model for a {t['name']} environment: {t['description']}. Your response should include:

1. Ecosystem Design (300-350 words):
   a) Describe the key components of your synthetic ecosystem, including types of organisms and their interactions.
   b) Explain how you incorporate principles of synthetic biology in designing the organisms.
   c) Discuss how the physical characteristics of the {t['name']} environment influence your design choices.

2. Evolutionary Algorithm (250-300 words):
   a) Detail the evolutionary algorithm used to simulate the ecosystem's development over time.
   b) Explain how fitness is calculated and selection occurs in your model.
   c) Describe how you handle genetic variation, mutation, and crossover in your synthetic organisms.

3. Computational Model (250-300 words):
   a) Outline the structure of your computational model, including key variables and processes.
   b) Explain how you simulate complex interactions between organisms and their environment.
   c) Provide a pseudocode snippet or flow diagram illustrating a critical part of your model.

4. Stability Analysis (200-250 words):
   a) Describe methods for analyzing the long-term stability of your synthetic ecosystem.
   b) Discuss potential tipping points or catastrophic failures in your system.
   c) Explain how your model accounts for external perturbations or changing environmental conditions.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of designing and implementing synthetic ecosystems.
   b) Analyze potential risks and benefits of applying this technology in real-world scenarios.
   c) Propose guidelines for responsible development and use of synthetic ecosystems.

6. Real-world Applications (150-200 words):
   a) Suggest two potential applications of your synthetic ecosystem model in scientific research or industry.
   b) Explain how these applications could contribute to addressing real-world challenges.

7. Future Directions (150-200 words):
   a) Propose two potential improvements or extensions to your model.
   b) Discuss how these improvements could enhance our understanding of natural ecosystems or advance synthetic biology.

Ensure your response demonstrates a deep understanding of synthetic biology, evolutionary computation, and ecological modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of synthetic biology, evolutionary algorithms, and ecological modeling.",
            "The ecosystem design is innovative, detailed, and scientifically plausible, incorporating principles of synthetic biology.",
            "The evolutionary algorithm is well-explained and appropriate for simulating ecosystem development.",
            "The computational model is clearly structured and accounts for complex interactions within the ecosystem.",
            "The stability analysis demonstrates a deep understanding of ecosystem dynamics and potential failure modes.",
            "Ethical implications are thoughtfully addressed, covering important issues related to synthetic ecosystems.",
            "Real-world applications and future directions are creative and well-reasoned.",
            "The response shows strong interdisciplinary reasoning, combining insights from biology, computer science, and ecology.",
            "The writing is clear, well-structured, and adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
