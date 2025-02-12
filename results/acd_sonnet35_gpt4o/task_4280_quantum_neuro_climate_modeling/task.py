import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "climate_factor": "Rising global temperatures",
                "brain_region": "Hippocampus",
                "cognitive_function": "Memory formation and consolidation",
                "quantum_approach": "Quantum annealing"
            },
            "2": {
                "climate_factor": "Increased frequency of extreme weather events",
                "brain_region": "Prefrontal cortex",
                "cognitive_function": "Executive function and decision-making",
                "quantum_approach": "Quantum neural networks"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that integrates neuroscience-inspired algorithms to model and predict the impacts of climate change on global brain health. Focus on the climate factor of {t['climate_factor']}, the brain region {t['brain_region']}, the cognitive function of {t['cognitive_function']}, and utilize the quantum approach of {t['quantum_approach']}. Your response should include the following sections:

1. Quantum System Architecture (300-350 words):
   a) Describe the key components of your quantum computing system for modeling climate-brain interactions.
   b) Explain how your system incorporates neuroscience-inspired algorithms.
   c) Detail how you utilize {t['quantum_approach']} in your system design.
   d) Discuss any novel quantum techniques you've developed for this specific application.
   e) Include a high-level diagram of your system architecture (describe it textually using clear, structured paragraphs).

2. Climate-Brain Interaction Modeling (250-300 words):
   a) Explain how your system models the impact of {t['climate_factor']} on the {t['brain_region']}.
   b) Describe how you quantify and simulate changes in {t['cognitive_function']}.
   c) Discuss how your quantum approach enhances the modeling of these complex interactions.

3. Data Integration and Processing (200-250 words):
   a) Specify the types of climate and neuroscience data your system would require.
   b) Explain how your quantum system processes and integrates these diverse datasets.
   c) Discuss any quantum algorithms you use for data analysis or pattern recognition.

4. Predictive Capabilities (250-300 words):
   a) Describe the predictive models your system generates.
   b) Explain how these models forecast long-term impacts of climate change on brain health.
   c) Discuss the advantages of your quantum approach in making these predictions.
   d) Provide an example prediction your system might make, with reasoning.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss ethical implications of using quantum computing to model brain health.
   b) Address potential misuse or misinterpretation of your system's predictions.
   c) Explain how your system could inform public health policies and interventions.

6. Limitations and Future Directions (150-200 words):
   a) Identify current limitations of your quantum neuro-climate modeling system.
   b) Propose two specific areas for future research to enhance your system.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and climate science, using appropriate technical terminology.",
            f"The quantum system architecture effectively incorporates {t['quantum_approach']} and neuroscience-inspired algorithms for modeling climate-brain interactions.",
            f"The system convincingly models the impact of {t['climate_factor']} on the {t['brain_region']} and {t['cognitive_function']}.",
            "The predictive capabilities of the system are well-explained and scientifically plausible.",
            "Ethical considerations and societal impacts are thoroughly addressed.",
            "The response includes innovative ideas while maintaining scientific plausibility.",
            "The response adheres to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
