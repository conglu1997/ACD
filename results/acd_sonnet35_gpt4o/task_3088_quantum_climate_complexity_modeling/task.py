class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principle": "superposition",
                "climate_factor": "ocean circulation patterns",
                "complex_system": "global food supply chains"
            },
            "2": {
                "quantum_principle": "entanglement",
                "climate_factor": "atmospheric carbon dioxide levels",
                "complex_system": "urban energy consumption networks"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired computational model that integrates complex systems theory to simulate and predict long-term climate change impacts on global ecosystems and human societies. Your model should incorporate the quantum principle of {t['quantum_principle']}, focus on the climate factor of {t['climate_factor']}, and analyze its effects on the complex system of {t['complex_system']}.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how you integrate the quantum principle of {t['quantum_principle']} into your climate modeling approach.
   b) Describe how your model incorporates complex systems theory to analyze {t['complex_system']}.
   c) Discuss how your approach improves upon classical climate modeling techniques.
   d) Provide a high-level mathematical or diagrammatic representation of your model, including at least one key equation and a labeled diagram.

2. Climate Factor Analysis (250-300 words):
   a) Analyze how your model simulates and predicts changes in {t['climate_factor']}.
   b) Explain how quantum-inspired computations enhance the accuracy or efficiency of these predictions.
   c) Describe a hypothetical experiment that could validate your model's predictions about {t['climate_factor']}.
   d) Provide a specific example or case study demonstrating your model's application to {t['climate_factor']}.

3. Complex System Impact Assessment (250-300 words):
   a) Apply your model to assess the long-term impacts of changes in {t['climate_factor']} on {t['complex_system']}.
   b) Explain how your model captures the nonlinear dynamics and emergent properties of this complex system.
   c) Discuss potential feedback loops between {t['complex_system']} and {t['climate_factor']}.
   d) Provide a concrete example of how your model predicts a specific impact on {t['complex_system']}.

4. Computational Implementation (200-250 words):
   a) Describe the computational architecture required to implement your model.
   b) Discuss any novel algorithms or data structures used in your approach.
   c) Address scalability and performance considerations for global-scale simulations.
   d) Identify potential limitations or challenges in implementing your model and propose solutions.

5. Ethical Implications and Policy Recommendations (150-200 words):
   a) Analyze potential ethical concerns related to using quantum-inspired models for climate prediction.
   b) Discuss how your model's predictions could inform climate policy and adaptation strategies.
   c) Propose guidelines for responsible development and use of advanced climate modeling techniques.

6. Future Research Directions (150-200 words):
   a) Suggest potential improvements or extensions to your model.
   b) Propose interdisciplinary collaborations that could further advance this field.
   c) Discuss how your approach could be applied to other complex global challenges.

Ensure your response demonstrates a deep understanding of quantum computing principles, climate science, and complex systems theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include at least one diagram and one equation to illustrate key aspects of your model.

Cite at least 5 relevant scientific papers or resources throughout your response to support your design choices and theoretical foundations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, climate science, and complex systems theory.",
            "The proposed model effectively integrates the specified quantum principle, climate factor, and complex system.",
            "The theoretical framework is innovative yet scientifically plausible.",
            "The response includes a clear mathematical or diagrammatic representation of the model, including at least one key equation and a labeled diagram.",
            "The climate factor analysis and complex system impact assessment are thorough and well-reasoned.",
            "The response provides specific examples or case studies demonstrating the model's application.",
            "The computational implementation section addresses practical considerations and potential limitations of the model.",
            "The response discusses ethical implications and provides thoughtful policy recommendations.",
            "Future research directions are relevant and well-justified.",
            "The response cites at least 5 relevant scientific papers or resources.",
            "The response adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
