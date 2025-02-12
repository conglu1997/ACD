import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_factors = [
            "extreme heat waves",
            "unpredictable precipitation patterns",
            "sea level rise",
            "increased frequency of natural disasters"
        ]
        cognitive_processes = [
            "risk perception",
            "decision-making under uncertainty",
            "long-term planning",
            "emotional regulation"
        ]
        brain_regions = [
            "prefrontal cortex",
            "amygdala",
            "hippocampus",
            "insula"
        ]
        tasks = [
            {
                "climate_factor": random.choice(climate_factors),
                "cognitive_process": random.choice(cognitive_processes),
                "brain_region": random.choice(brain_regions)
            },
            {
                "climate_factor": random.choice(climate_factors),
                "cognitive_process": random.choice(cognitive_processes),
                "brain_region": random.choice(brain_regions)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses neuroscience-inspired algorithms to model and enhance human cognitive adaptation to climate change. Focus on the climate factor of {t['climate_factor']}, the cognitive process of {t['cognitive_process']}, and the brain region {t['brain_region']}. Your response should include the following sections:

1. Neuroscientific Framework (250-300 words):
   a) Explain the role of the {t['brain_region']} in {t['cognitive_process']}.
   b) Discuss how {t['climate_factor']} might impact this cognitive process.
   c) Describe current neuroscientific understanding of cognitive adaptation to environmental changes.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for modeling and enhancing cognitive adaptation.
   b) Explain how your system incorporates neuroscience-inspired algorithms, particularly related to the {t['brain_region']}.
   c) Describe how the AI models the impact of {t['climate_factor']} on {t['cognitive_process']}.
   d) Discuss any novel features in your AI design for this specific application.

3. Cognitive Adaptation Modeling (250-300 words):
   a) Explain how your AI system models the process of cognitive adaptation to {t['climate_factor']}.
   b) Describe the key variables and parameters in your model.
   c) Discuss how your model accounts for individual differences in cognitive adaptation.

4. Enhancement Strategies (200-250 words):
   a) Propose specific strategies your AI system would generate to enhance {t['cognitive_process']} in response to {t['climate_factor']}.
   b) Explain how these strategies are informed by the neuroscience of the {t['brain_region']}.
   c) Discuss potential limitations or risks of these enhancement strategies.

5. Data Requirements and Ethical Considerations (200-250 words):
   a) Specify the types of data your AI system would require for training and operation.
   b) Discuss ethical implications of using AI to model and enhance human cognition.
   c) Propose guidelines for responsible development and use of such systems.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your approach could advance our understanding of brain plasticity and environmental adaptation.
   b) Explain potential applications of your system in climate change education and policy-making.
   c) Propose a novel research question that arises from your system design.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, climate science, and cognitive psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, climate science, and cognitive psychology",
            "The proposed AI system effectively integrates neuroscience-inspired algorithms with climate adaptation modeling",
            f"The design addresses the specific climate factor of {t['climate_factor']}, cognitive process of {t['cognitive_process']}, and brain region {t['brain_region']}",
            "The cognitive adaptation modeling and enhancement strategies are innovative and scientifically plausible",
            "Ethical considerations and interdisciplinary implications are thoughtfully discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
