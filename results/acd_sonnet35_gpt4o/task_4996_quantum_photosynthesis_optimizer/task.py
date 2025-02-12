import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        optimization_targets = ['light harvesting efficiency', 'carbon fixation rate']
        application_domains = ['crop yield improvement', 'artificial photosynthesis for energy production']
        return {
            "1": {"target": random.choice(optimization_targets), "domain": random.choice(application_domains)},
            "2": {"target": random.choice(optimization_targets), "domain": random.choice(application_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system to model and optimize photosynthesis, focusing on {t['target']} for applications in {t['domain']}. Then, analyze its potential impact and implications. Your response should include the following sections:

1. Quantum-Biological Model (300-350 words):
   a) Describe the key components of your quantum-inspired model for photosynthesis.
   b) Explain how your model incorporates quantum effects observed in photosynthetic systems.
   c) Detail how your model addresses the optimization of {t['target']}.
   d) Include a high-level diagram or pseudocode illustrating your model's architecture (describe it textually).
   e) Provide a specific example of how your model would represent a particular aspect of photosynthesis.

2. AI System Design (250-300 words):
   a) Outline the architecture of your AI system for simulating and optimizing the quantum-biological model.
   b) Explain the machine learning techniques used in your system.
   c) Describe how your AI system interfaces with the quantum-biological model to achieve optimization.
   d) Discuss potential limitations or challenges in implementing your AI system.

3. Optimization Process (250-300 words):
   a) Detail the steps your AI system would take to optimize {t['target']}.
   b) Explain how your system handles the complexity and scale of photosynthetic processes.
   c) Discuss any novel approaches or algorithms used in the optimization process.
   d) Provide a hypothetical case study demonstrating your system's optimization process.

4. Application to {t['domain']} (200-250 words):
   a) Describe how your optimized model could be applied to {t['domain']}.
   b) Discuss potential challenges in translating the model's insights into practical applications.
   c) Propose a specific implementation strategy for your optimized photosynthesis model.
   d) Analyze potential limitations or drawbacks of your approach in this application domain.

5. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired approach to classical methods for photosynthesis optimization.
   b) Discuss the potential advantages and limitations of your approach.
   c) Analyze the scalability of your method for different photosynthetic systems or organisms.
   d) Provide a specific example comparing your method to a classical approach for a particular optimization task.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical issues related to optimizing natural biological processes.
   b) Discuss the broader implications of your technology for agriculture, energy production, and environmental sustainability.
   c) Propose guidelines for the responsible development and application of quantum-inspired biological optimization technologies.
   d) Consider potential unintended consequences of widespread adoption of your technology.

7. Future Research Directions (150-200 words):
   a) Suggest two potential expansions or modifications to your system to explore additional aspects of photosynthesis or other biological processes.
   b) Discuss how empirical research in quantum biology could validate or challenge your model's predictions.
   c) Propose a roadmap for developing practical applications based on your quantum-inspired photosynthesis optimization system.
   d) Identify key technological or scientific advancements needed to fully realize the potential of your approach.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and artificial intelligence. Use appropriate scientific terminology and provide clear explanations of complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word count ranges provided for each section. Your total response should be between 1500-1850 words. Include a word count at the end of each section and a total word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, photosynthesis, and artificial intelligence.",
            "The quantum-biological model is well-designed and incorporates relevant quantum effects observed in photosynthetic systems.",
            "The AI system architecture is clearly explained and appropriate for the task of optimizing the quantum-biological model.",
            "The optimization process is well-detailed and addresses the complexity of photosynthetic processes.",
            f"The application to {t['domain']} is thoroughly explored with practical implementation strategies.",
            "The comparative analysis provides insightful comparisons between the quantum-inspired approach and classical methods.",
            "Ethical considerations and societal impacts are thoughtfully discussed.",
            "Future research directions are innovative and well-reasoned.",
            "The response is creative and speculative while maintaining scientific plausibility.",
            "All sections are complete and adhere to the word count guidelines.",
            "Specific examples, case studies, or hypothetical scenarios are provided to illustrate key concepts.",
            "Potential limitations, challenges, and drawbacks of the proposed system are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
