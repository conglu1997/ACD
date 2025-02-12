import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "name": "Coral Reef",
                "challenge": "Ocean Acidification",
                "key_species": ["Hard Corals", "Parrotfish", "Zooplankton"]
            },
            {
                "name": "Amazon Rainforest",
                "challenge": "Deforestation",
                "key_species": ["Brazil Nut Trees", "Jaguar", "Leaf-cutter Ants"]
            }
        ]
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of modeling complex ecosystems and proposing interventions to address environmental challenges. Then, apply your system to the following scenario:

Ecosystem: {t['name']}
Environmental Challenge: {t['challenge']}
Key Species: {', '.join(t['key_species'])}

Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the overall structure of your AI ecosystem modeling system.
   b) Explain how it incorporates principles from ecology, environmental science, and systems theory.
   c) Detail the components for data integration, ecosystem simulation, and intervention planning.
   d) Discuss how the system handles uncertainty and complex interactions within the ecosystem.

2. Ecosystem Modeling Approach (250-300 words):
   a) Explain how your AI system represents and processes key ecological concepts and relationships.
   b) Describe how it models the interactions between different species and environmental factors.
   c) Discuss any novel approaches your system uses to capture ecosystem complexity and dynamics.

3. Scenario Analysis (300-350 words):
   a) Apply your AI system to model the given ecosystem and environmental challenge.
   b) Provide a detailed analysis of the potential impacts of the challenge on the ecosystem, including effects on key species and their interactions.
   c) Describe any feedback loops or cascading effects your system identifies.
   d) Include a simple diagram or representation of the key relationships and dynamics in your model.

4. Intervention Proposals (250-300 words):
   a) Present three AI-generated intervention strategies to address the environmental challenge.
   b) For each intervention, explain:
      - The proposed action and its implementation
      - Predicted outcomes and potential side effects
      - How it leverages or affects key species and ecosystem dynamics

5. Evaluation and Refinement (200-250 words):
   a) Propose a method for evaluating the accuracy and effectiveness of your AI's ecosystem models and interventions.
   b) Describe how your AI system could improve its models based on new data and feedback.
   c) Suggest a specific metric for measuring the system's performance in ecosystem modeling and intervention planning.

6. Ethical and Practical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI for ecosystem management and intervention.
   b) Address challenges in implementing AI-proposed interventions in real-world ecosystems.
   c) Consider the potential impacts on local communities and biodiversity.

7. Broader Applications (150-200 words):
   a) Propose two potential applications of your AI ecosystem modeling system beyond environmental management.
   b) Briefly explain how these applications could benefit related fields or industries.

Ensure your response demonstrates a deep understanding of ecology, environmental science, and AI systems design. Be creative and innovative while maintaining scientific accuracy and feasibility. Use appropriate terminology throughout your answer.

Your total response should be between 1600-1950 words. Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly explain an AI system capable of modeling the {t['name']} ecosystem and addressing the challenge of {t['challenge']}.",
            "The AI system design should demonstrate a clear and plausible integration of ecological principles, environmental science, and AI techniques.",
            f"The scenario analysis should include detailed consideration of the key species: {', '.join(t['key_species'])}.",
            "The submission must include all seven required sections, adequately addressing each topic.",
            "The response should demonstrate creativity and innovation in AI ecosystem modeling while maintaining scientific accuracy and feasibility.",
            "The proposed interventions should be well-reasoned and account for potential cascading effects in the ecosystem.",
            "The response must show a deep understanding of both ecological systems and AI design principles.",
            "The response should include a simple diagram or representation of key ecosystem relationships and dynamics.",
            "The broader applications section should propose realistic and innovative uses of the AI ecosystem modeling system beyond environmental management."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
