import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "intervention": "Stratospheric aerosol injection",
                "region": "Arctic",
                "timeframe": "50 years"
            },
            {
                "intervention": "Ocean iron fertilization",
                "region": "Southern Ocean",
                "timeframe": "30 years"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and optimizes the climate intervention strategy of {t['intervention']} in the {t['region']} over a {t['timeframe']} period, then analyze its potential impact on global environmental policy and ethics. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for climate intervention simulation and optimization.
   b) Explain how your system integrates climate models with AI/ML techniques.
   c) Detail how the system handles uncertainty and long-term projections.
   d) Discuss any novel approaches you've incorporated to enhance prediction accuracy or optimization capabilities.
   e) Provide a high-level diagram or pseudocode illustrating your system's architecture.

2. Simulation and Optimization Process (250-300 words):
   a) Explain the step-by-step process your AI system would use to simulate the effects of {t['intervention']} in the {t['region']}.
   b) Describe how your system optimizes the intervention strategy over the {t['timeframe']} period.
   c) Discuss how your system accounts for potential feedback loops and unintended consequences.
   d) Explain how the system balances multiple objectives (e.g., temperature reduction, ecosystem preservation, economic impact).

3. Data Integration and Model Validation (200-250 words):
   a) Describe the types of data your system would incorporate (e.g., climate, ecological, economic).
   b) Explain how you would validate your AI model against historical climate data and other climate models.
   c) Discuss approaches for continually updating and improving the model as new data becomes available.
   d) Address potential biases in data sources and how you'd mitigate them.

4. Policy Implications Analysis (200-250 words):
   a) Analyze how your AI system's predictions and optimizations might influence global environmental policy.
   b) Discuss potential changes in international cooperation and governance structures.
   c) Explore the implications for climate justice and equitable global development.
   d) Consider how this technology might affect public perception and support for climate interventions.

5. Ethical Considerations (200-250 words):
   a) Discuss ethical challenges related to using AI to guide large-scale environmental interventions.
   b) Consider the moral implications of potentially irreversible changes to the Earth's climate system.
   c) Address issues of transparency, accountability, and democratic decision-making in the context of AI-guided climate interventions.
   d) Propose guidelines for the responsible development and use of such AI systems.

6. Potential Risks and Mitigation Strategies (200-250 words):
   a) Identify potential risks or unintended consequences of using your AI system for climate intervention.
   b) Propose strategies to mitigate these risks.
   c) Discuss the importance of fail-safes and human oversight in the system.
   d) Consider potential misuse scenarios and how to prevent them.

7. Future Research Directions (100-150 words):
   a) Suggest two potential areas for further research to advance AI-guided climate intervention strategies.
   b) Explain how these research directions could address current limitations or open up new possibilities in climate change mitigation.

Ensure your response demonstrates a deep understanding of climate science, artificial intelligence, complex systems modeling, and environmental ethics. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, artificial intelligence, complex systems modeling, and environmental ethics.",
            "The AI system architecture is well-designed and integrates climate models with AI/ML techniques effectively.",
            "The simulation and optimization process is clearly explained and accounts for potential feedback loops and unintended consequences.",
            "The analysis of policy implications and ethical considerations is thorough and thought-provoking.",
            "The response addresses potential risks and proposes mitigation strategies.",
            "The suggested future research directions are relevant and well-justified.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
