import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "climate_factor": "Rising temperatures",
                "brain_region": "Prefrontal cortex",
                "cognitive_function": "Executive function",
                "population": "Urban elderly"
            },
            {
                "climate_factor": "Increased air pollution",
                "brain_region": "Hippocampus",
                "cognitive_function": "Memory formation",
                "population": "Children in developing countries"
            },
            {
                "climate_factor": "Extreme weather events",
                "brain_region": "Amygdala",
                "cognitive_function": "Emotional regulation",
                "population": "Coastal communities"
            },
            {
                "climate_factor": "Changing biodiversity",
                "brain_region": "Insula",
                "cognitive_function": "Interoception",
                "population": "Indigenous populations"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts the long-term neurological impacts of climate change on human cognition and behavior, then use it to propose adaptive strategies for a specific population. Focus on the following parameters:

Climate Factor: {t['climate_factor']}
Brain Region: {t['brain_region']}
Cognitive Function: {t['cognitive_function']}
Target Population: {t['population']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling climate-neurology interactions.
   b) Explain how your system integrates climate data, neurological models, and behavioral predictions.
   c) Detail the mechanisms used for long-term forecasting and uncertainty quantification.
   d) Discuss how your system handles the complexity of brain-environment interactions.
   e) Include a brief description of a flowchart or diagram representing your system's architecture.

2. Climate-Neurology Modeling (250-300 words):
   a) Explain your approach to modeling the impact of the specified climate factor on the given brain region.
   b) Describe how your model links changes in brain structure/function to alterations in cognitive function.
   c) Discuss how your system accounts for individual variability and population-level differences.
   d) Address potential limitations or assumptions in your modeling approach.

3. Behavioral Prediction (250-300 words):
   a) Detail how your AI system predicts changes in behavior based on the modeled neurological impacts.
   b) Explain how your system accounts for social, cultural, and environmental factors in behavioral predictions.
   c) Describe any novel algorithms or techniques used for integrating neurological and behavioral models.
   d) Discuss how your system validates its predictions against current scientific understanding.

4. Adaptive Strategies (200-250 words):
   a) Based on your AI system's predictions, propose three adaptive strategies for the specified population.
   b) Explain how each strategy addresses the predicted neurological and behavioral changes.
   c) Discuss potential challenges in implementing these strategies and how they might be overcome.

5. Ethical Considerations (200-250 words):
   a) Identify and analyze at least three ethical concerns raised by the development and use of your AI system.
   b) Discuss the potential societal implications of long-term neurobehavioral predictions.
   c) Propose guidelines for the responsible development and application of climate-neurology AI systems.

6. Future Directions and Limitations (150-200 words):
   a) Acknowledge current limitations of your AI system and propose ways to address them.
   b) Suggest potential advancements or extensions of your system for future research.
   c) Discuss how evolving climate science and neurotechnology might impact your system's predictions and applications.

Ensure your response demonstrates a deep understanding of neuroscience, climate science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Where relevant, cite or reference current research or studies to support your design choices and predictions. This will help ground your response in existing scientific knowledge.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, climate science, and artificial intelligence.",
            "The AI system design is innovative, detailed, and scientifically plausible.",
            "The climate-neurology modeling approach is well-explained and accounts for complexity and uncertainty.",
            "The behavioral prediction method integrates neurological impacts with social and environmental factors.",
            "The proposed adaptive strategies are creative, relevant, and well-reasoned.",
            "Ethical considerations are thoroughly analyzed and addressed.",
            "The response maintains coherence and relevance throughout all sections.",
            "Technical terminology is used appropriately and complex concepts are clearly explained.",
            "Where relevant, the response cites or references current research to support design choices and predictions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
