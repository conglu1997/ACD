class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "region": "Mediterranean Basin",
                "resource": "Freshwater",
                "economic_sector": "Agriculture",
                "annual_rainfall": 500,  # mm
                "agricultural_water_use": 70,  # % of total water use
                "gdp_contribution": 12,  # % of regional GDP from agriculture
                "population": 150000000,  # estimated population
                "water_stress_index": 0.7  # 0-1 scale, higher means more stress
            },
            "2": {
                "region": "Great Lakes Region",
                "resource": "Freshwater",
                "economic_sector": "Manufacturing",
                "annual_rainfall": 900,  # mm
                "manufacturing_water_use": 45,  # % of total water use
                "gdp_contribution": 28,  # % of regional GDP from manufacturing
                "population": 85000000,  # estimated population
                "water_stress_index": 0.3  # 0-1 scale, higher means more stress
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that optimizes the management of {t['resource']} resources in the {t['region']}, while balancing the economic impacts on the {t['economic_sector']} sector. Your system should consider the following data:
- Annual rainfall: {t['annual_rainfall']} mm
- {t['economic_sector']} water use: {t['economic_sector'].lower()}_water_use% of total water use
- GDP contribution: {t['gdp_contribution']}% of regional GDP from {t['economic_sector'].lower()}
- Population: {t['population']}
- Water Stress Index: {t['water_stress_index']} (0-1 scale, higher means more stress)

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for eco-economic optimization.
   b) Explain how your system integrates environmental data, economic models, and resource management strategies.
   c) Detail the AI techniques and algorithms used in your system (e.g., reinforcement learning, multi-agent systems, neural networks).
   d) Provide a diagram or pseudocode snippet illustrating a key aspect of your system's implementation.

2. Data Sources and Processing (250-300 words):
   a) Identify the types of environmental, economic, and social data your system would use.
   b) Explain how your system would integrate and analyze these diverse data types.
   c) Describe any novel approaches for handling uncertainties or incomplete data in your model.

3. Resource Management Strategies (250-300 words):
   a) Outline the key strategies your AI system would employ for optimizing {t['resource']} management in the {t['region']}.
   b) Explain how your system would adapt these strategies based on changing environmental conditions or economic factors.
   c) Discuss how your system balances short-term economic needs with long-term environmental sustainability.

4. Economic Impact Analysis (200-250 words):
   a) Describe how your AI system models and predicts the economic impacts of resource management decisions on the {t['economic_sector']} sector.
   b) Explain any novel approaches your system uses to balance economic growth with environmental conservation.
   c) Discuss how your system might handle conflicting economic and environmental objectives.

5. Scenario Simulation (200-250 words):
   a) Present a specific scenario where your AI system optimizes {t['resource']} management in the {t['region']}.
   b) Walk through the decision-making process of your AI system, explaining key trade-offs and outcomes.
   c) Discuss potential long-term impacts of your system's decisions on both the environment and economy.

6. Quantitative Analysis (200-250 words):
   a) Provide a mathematical model or algorithm that your AI system uses for resource allocation or impact prediction. Your model should include at least three variables and two constraints.
   b) Explain the variables, constraints, and objective function(s) in your model.
   c) Describe how your system would optimize this model to balance environmental and economic factors.
   d) Include at least one equation or formula in your explanation.

Example template for the mathematical model:
Objective function: Maximize f(x, y, z) = ...
Subject to constraints:
g(x, y, z) ≤ ...
h(x, y, z) ≥ ...
Where x, y, z represent [explain variables]

7. Ethical Considerations and Unintended Consequences (200-250 words):
   a) Identify potential ethical implications of using AI for environmental resource management.
   b) Discuss how your system addresses issues of fairness and equity in resource allocation.
   c) Analyze potential unintended consequences of implementing your AI system, considering both environmental and socio-economic factors.
   d) Propose guidelines for transparent and responsible use of your AI system in policy-making.

8. Evaluation and Improvement (150-200 words):
   a) Propose methods for evaluating the effectiveness of your AI system in real-world applications.
   b) Discuss potential limitations of your approach and areas for future improvement.
   c) Suggest how your system could be adapted for other regions or resources.

Ensure your response demonstrates a deep understanding of environmental science, economics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1750-2150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of environmental science, economics, and artificial intelligence, integrating concepts from all three fields.",
            "The AI system design is innovative, scientifically plausible, and specifically addresses the challenges of the given region, resource, and economic sector.",
            "The response effectively balances environmental sustainability with economic impacts, considering all provided data including population and water stress index.",
            "The proposed system integrates diverse data sources and uses advanced AI techniques appropriately, with clear explanations of their application.",
            "The response includes a detailed scenario simulation that illustrates the system's decision-making process and considers long-term impacts.",
            "A quantitative analysis is provided, including a mathematical model or algorithm with at least three variables, two constraints, and one equation or formula.",
            "The response thoroughly addresses ethical considerations and potential unintended consequences of the AI system's implementation.",
            "The response is well-structured, clear, and within the specified word count range of 1750-2150 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
