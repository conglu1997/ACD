import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'quantum tunneling', 'quantum walk']
        social_phenomena = ['information propagation', 'opinion formation', 'social influence', 'community detection']
        application_domains = ['political polarization', 'viral marketing', 'social movements', 'online radicalization']
        
        tasks = [
            {
                'quantum_principle': random.choice(quantum_principles),
                'social_phenomenon': random.choice(social_phenomena),
                'application_domain': random.choice(application_domains)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-inspired system to model and analyze complex social networks and phenomena, focusing on the quantum principle of {t['quantum_principle']} and the social phenomenon of {t['social_phenomenon']}. Then, apply your system to analyze the application domain of {t['application_domain']}. Your response should include:

1. Quantum Social Network Model (300-350 words):
   a) Describe the key components of your quantum-inspired social network model.
   b) Explain how you incorporate the specified quantum principle into your model.
   c) Detail how your model represents and analyzes the given social phenomenon.
   d) Discuss any novel computational or representational elements in your approach.
   e) Include a high-level diagram or pseudocode of your model (describe it textually).

2. Quantum-Social Integration (250-300 words):
   a) Explain how your model bridges quantum concepts with social network analysis.
   b) Describe any challenges in applying quantum principles to social systems and how you address them.
   c) Discuss how your approach differs from classical social network analysis methods.

3. Application Analysis (250-300 words):
   a) Apply your quantum social network model to analyze the specified application domain.
   b) Describe the insights your model provides that traditional methods might miss.
   c) Discuss any limitations of your model in addressing this specific domain.
   d) Propose a hypothetical experiment to validate your model's predictions.

4. Computational Implementation (200-250 words):
   a) Outline the computational requirements for implementing your model.
   b) Discuss any quantum algorithms or simulations necessary for your approach.
   c) Explain how you would handle the transition from quantum to classical data for analysis and interpretation.

5. Ethical Implications and Societal Impact (200-250 words):
   a) Identify potential ethical concerns related to using quantum-inspired models for social analysis.
   b) Discuss the broader societal implications of applying quantum concepts to social sciences.
   c) Propose guidelines for the responsible development and use of quantum social network models.

6. Future Research Directions (150-200 words):
   a) Suggest two potential enhancements or extensions to your quantum social network model.
   b) Propose a specific research question that could further advance this interdisciplinary field.
   c) Speculate on how this approach might impact future social science research and policy-making.

Ensure your response demonstrates a deep understanding of quantum computing principles, social network analysis, and relevant social science theories. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Quantum Social Network Model:') on a new line, followed by your response for that section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding and integration of quantum computing principles and social science concepts.",
            "The quantum social network model is innovative, coherent, and effectively incorporates the specified quantum principle and social phenomenon.",
            "The application analysis provides novel insights and demonstrates the potential advantages of the quantum-inspired approach.",
            "The computational implementation is well-explained and addresses the challenges of quantum-classical integration.",
            "Ethical implications and societal impacts are thoughtfully considered, with reasonable guidelines proposed.",
            "Future research directions are insightful and show potential for advancing the field.",
            "The response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
