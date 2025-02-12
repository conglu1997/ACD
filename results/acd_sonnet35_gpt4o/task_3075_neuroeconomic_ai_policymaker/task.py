import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        economic_behaviors = [
            "Risk aversion",
            "Intertemporal choice",
            "Social preferences",
            "Strategic decision-making"
        ]
        neural_regions = [
            "Prefrontal cortex",
            "Amygdala",
            "Striatum",
            "Insula"
        ]
        policy_areas = [
            "Retirement savings",
            "Healthcare choices",
            "Environmental conservation",
            "Education investment"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "economic_behavior": random.choice(economic_behaviors),
                "neural_region": random.choice(neural_regions),
                "policy_area": random.choice(policy_areas)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts economic decision-making based on neural activity, focusing on the economic behavior of {t['economic_behavior']} and the neural activity in the {t['neural_region']}. Then, analyze its potential applications in the policy area of {t['policy_area']}. Your response should include:

1. Neuroeconomic AI System Design (300-350 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how it integrates neuroscientific data with economic models.
   c) Detail how your system specifically addresses the given economic behavior and neural region.
   d) Discuss any novel algorithms or techniques you've incorporated to handle the complexity of neuroeconomic data.
   e) Include a high-level diagram or flowchart of your AI system architecture.

2. Neural-Economic Mapping (250-300 words):
   a) Explain how your system translates neural activity in the specified region to economic decision-making patterns.
   b) Provide a specific example of how this mapping works for the given economic behavior.
   c) Discuss potential advantages of this neuro-inspired approach over traditional economic models.

3. Predictive Capabilities (200-250 words):
   a) Describe the types of predictions your AI system can make about economic behavior.
   b) Explain how these predictions could be validated using real-world data.
   c) Discuss the limitations and uncertainties in your system's predictive capabilities.
   d) Provide a detailed example scenario of a prediction your system might make, including the input data and the resulting prediction.

4. Policy Application (250-300 words):
   a) Analyze how your AI system could be applied to inform policy decisions in the specified policy area.
   b) Provide a specific scenario where your system's predictions could guide policy-making.
   c) Discuss potential benefits and risks of using AI-driven neuroeconomic insights in public policy.

5. Ethical Considerations (200-250 words):
   a) Identify at least three ethical concerns related to using your AI system for policy-making.
   b) Propose guidelines or safeguards to address these ethical issues.
   c) Discuss the broader societal implications of using neuroscience-based AI in economic policy.

6. Future Research Directions (150-200 words):
   a) Suggest two potential research projects that could further enhance your AI system's capabilities.
   b) Explain how these projects could address current limitations or expand the system's applications.

Ensure your response demonstrates a deep understanding of neuroscience, economics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Adhere to the word count limits for each section as specified above. Your total response should be between 1350-1650 words. Include a high-level diagram or flowchart of your AI system architecture as mentioned in section 1.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an AI system that models economic decision-making based on neural activity, focusing on {t['economic_behavior']} and the {t['neural_region']}",
            "The design should include a high-level diagram or flowchart of the AI system architecture",
            "The response should provide a detailed example scenario of a prediction the system might make",
            f"The application of the AI system to {t['policy_area']} should be thoroughly analyzed with a specific policy-making scenario",
            "At least three ethical concerns should be identified and addressed with proposed guidelines or safeguards",
            "Two relevant future research directions should be proposed and well-described",
            "The overall response should demonstrate interdisciplinary thinking, creative problem-solving, and adhere to the specified word count limits for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
