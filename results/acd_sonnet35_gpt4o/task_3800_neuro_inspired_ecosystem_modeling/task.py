import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "Coral Reef",
            "Amazon Rainforest",
            "Arctic Tundra",
            "Sahara Desert"
        ]
        climate_changes = [
            "Temperature Increase",
            "Ocean Acidification",
            "Extreme Weather Events",
            "Sea Level Rise"
        ]
        neural_principles = [
            "Hebbian Learning",
            "Neuroplasticity",
            "Lateral Inhibition",
            "Spike-Timing-Dependent Plasticity"
        ]
        tasks = {
            "1": {
                "ecosystem": random.choice(ecosystems),
                "climate_change": random.choice(climate_changes),
                "neural_principle": random.choice(neural_principles)
            },
            "2": {
                "ecosystem": random.choice(ecosystems),
                "climate_change": random.choice(climate_changes),
                "neural_principle": random.choice(neural_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts ecosystem responses to climate change using principles from neural networks and brain plasticity. Your system should focus on the {t['ecosystem']} ecosystem, addressing the impact of {t['climate_change']}, and incorporating the neural principle of {t['neural_principle']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling ecosystem responses.
   b) Explain how your system integrates principles from neuroscience, ecology, and artificial intelligence.
   c) Detail how your system incorporates the specified neural principle in its design and function.
   d) Include a visual representation of your system's architecture using ASCII art or a text-based diagram. The diagram should be at least 15 lines long and use characters such as |, -, +, >, <, and ^ to represent components and their relationships.

2. Ecosystem-Neural Network Mapping (250-300 words):
   a) Explain how you map components of the {t['ecosystem']} to elements of a neural network.
   b) Describe how interactions within the ecosystem are represented in your model.
   c) Discuss how your system accounts for the complexity and interconnectedness of ecosystem elements.
   d) Provide a mathematical formulation or pseudocode for a key process in your mapping (e.g., how a specific ecosystem interaction is translated into neural network operations).

3. Climate Change Response Modeling (250-300 words):
   a) Detail how your system models the impact of {t['climate_change']} on the ecosystem.
   b) Explain how the specified neural principle is used to simulate ecosystem adaptation or response.
   c) Describe any novel insights your system might provide about ecosystem resilience or tipping points.
   d) Include a mathematical equation or algorithm that represents how your system models the impact of the specified climate change.

4. Predictive Capabilities (200-250 words):
   a) Describe the types of predictions your system can make about ecosystem changes.
   b) Explain how these predictions account for both short-term and long-term effects.
   c) Provide an example of a specific prediction your system might make, along with its potential implications.
   d) Outline the process your system would use to generate this prediction, including any key calculations or decision points.

5. Data Requirements and Sample Dataset (200-250 words):
   a) Specify the types and sources of data your system would require.
   b) Provide a small sample dataset (5-10 data points) that your system would use, explaining the relevance of each data point.
   c) Discuss potential ethical issues in collecting and using this data.
   d) Propose guidelines for responsible development and use of your system.

6. Validation and Testing (150-200 words):
   a) Propose methods to validate your system's predictions and models.
   b) Describe potential experiments or studies that could test your system's accuracy.
   c) Discuss the challenges in validating such a complex system and how you would address them.

7. Comparative Analysis (200-250 words):
   a) Compare your proposed AI system with a traditional, non-AI approach to ecosystem modeling.
   b) Discuss the advantages and disadvantages of each approach.
   c) Explain scenarios where your AI system would be particularly beneficial or potentially problematic compared to traditional methods.

8. Practical Applications and Societal Impact (200-250 words):
   a) Suggest potential applications of your system in environmental management, conservation, or policy-making.
   b) Discuss how your system might influence our understanding of ecosystem dynamics and climate change impacts.
   c) Consider potential societal impacts, both positive and negative, of widespread use of such a system.

9. Critical Analysis and Limitations (200-250 words):
   a) Critically analyze the limitations of your proposed system.
   b) Discuss potential biases that might arise in your system's predictions and how they could be mitigated.
   c) Identify areas where the analogy between neural networks and ecosystems might break down or lead to incorrect conclusions.

10. Implementation Plan (150-200 words):
    a) Outline a brief plan for implementing your system, including key stages and milestones.
    b) Identify potential challenges in the implementation process and how you would address them.
    c) Discuss any interdisciplinary collaborations that would be necessary for successful implementation.

Ensure your response demonstrates a deep understanding of neuroscience, ecology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 2100-2600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['ecosystem']} ecosystem and the potential impacts of {t['climate_change']}",
            f"The system design effectively incorporates the neural principle of {t['neural_principle']} in modeling ecosystem responses",
            "The ecosystem-neural network mapping is creative, well-reasoned, and scientifically plausible",
            "The ASCII art diagram is detailed and accurately represents the system architecture",
            "Mathematical formulations or pseudocode are provided and correctly describe key processes",
            "The predictive capabilities of the system are clearly explained and demonstrate potential for real-world applications",
            "A relevant sample dataset is provided with clear explanations of each data point",
            "The comparative analysis with traditional methods is thorough and insightful",
            "The implementation plan is realistic and addresses potential challenges",
            "The critical analysis section thoroughly discusses limitations and potential biases of the system",
            "The writing is clear, well-structured, and uses appropriate technical terminology from neuroscience, ecology, and AI",
            "The response follows the required format and stays within the specified word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
