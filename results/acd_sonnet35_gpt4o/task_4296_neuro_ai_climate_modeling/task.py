import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "brain_region": "hippocampus",
                "climate_phenomenon": "El Niño",
                "environmental_factor": "ocean temperatures"
            },
            {
                "brain_region": "visual cortex",
                "climate_phenomenon": "Arctic sea ice loss",
                "environmental_factor": "albedo effect"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics the {t['brain_region']}'s information processing capabilities to create advanced climate models for predicting {t['climate_phenomenon']}, with a focus on {t['environmental_factor']}. Your response should include:

1. Neuroscientific Basis (250-300 words):
   a) Explain the key information processing features of the {t['brain_region']}.
   b) Describe how these features could be applied to climate modeling.
   c) Discuss any challenges in translating neural processes to computational models.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your neuro-inspired AI system for climate modeling.
   b) Explain how your system mimics the {t['brain_region']}'s information processing.
   c) Describe how the AI integrates and processes diverse climate data.
   d) Discuss any novel features or innovations in your AI design for this specific application.

3. Climate Modeling Approach (250-300 words):
   a) Explain how your AI system models {t['climate_phenomenon']}.
   b) Describe how it incorporates {t['environmental_factor']} into its predictions.
   c) Discuss how your approach differs from traditional climate modeling techniques.
   d) Provide a hypothetical example of a specific insight your system might generate.

4. Predictive Capabilities and Validation (250-300 words):
   a) Describe the types of predictions your AI system could make about {t['climate_phenomenon']}.
   b) Explain how these predictions could be validated against real-world data.
   c) Discuss potential improvements in accuracy or efficiency compared to current models.
   d) Propose a novel hypothesis about climate change that your system could test.

5. Data Requirements and Challenges (200-250 words):
   a) Specify the types of data your AI system would require for training and operation.
   b) Discuss challenges in obtaining or generating relevant climate and environmental data.
   c) Propose innovative solutions to address these data-related challenges.

6. Ethical Considerations and Societal Impact (200-250 words):
   a) Identify potential ethical issues in using neuro-inspired AI for climate modeling.
   b) Discuss the potential societal impacts of your system's predictions on environmental policy and public perception.
   c) Propose guidelines for responsible development and use of such advanced climate modeling AI systems.

7. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your system for future research.
   b) Discuss how your approach could be applied to other areas of environmental science or neuroscience.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and climate science. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word limits provided. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, AI system design, and climate science.",
            "The proposed AI system effectively integrates knowledge from multiple disciplines and mimics neural processes for climate modeling.",
            "The climate modeling approach and predictive capabilities are well-reasoned and grounded in current scientific understanding.",
            "The response addresses the specific brain region, climate phenomenon, and environmental factor mentioned in the prompt.",
            "The ethical considerations and societal impacts are thoughtfully discussed.",
            "The proposed future research directions are innovative and relevant.",
            "The response is well-structured, adhering to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
