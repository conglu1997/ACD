import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'environment': 'Global climate change',
                'cultural_shift': 'Increased digital communication',
                'time_frame': '100 years',
                'language_family': 'Indo-European'
            },
            {
                'environment': 'Interplanetary colonization',
                'cultural_shift': 'AI integration in daily life',
                'time_frame': '200 years',
                'language_family': 'Sino-Tibetan'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a computational model that simulates the evolution and adaptation of language in response to environmental and cultural pressures, then use it to predict future linguistic changes. Your task involves the following scenario:

Environment: {t['environment']}
Cultural Shift: {t['cultural_shift']}
Time Frame: {t['time_frame']}
Language Family: {t['language_family']}

Your response should include the following sections:

1. Computational Model Design (300-350 words):
   a) Describe the key components and architecture of your language evolution model.
   b) Explain how your model incorporates principles from linguistics, evolutionary biology, and cognitive science.
   c) Detail how the model simulates the effects of environmental and cultural pressures on language.
   d) Discuss any novel or unique features of your model that distinguish it from existing approaches.

2. Implementation and Parameterization (250-300 words):
   a) Explain how you would implement your model using computational techniques.
   b) Describe the key parameters of your model and how they relate to real-world linguistic phenomena.
   c) Discuss how you would calibrate your model using historical linguistic data.
   d) Provide a simple pseudo-code snippet or algorithm that illustrates a core aspect of your model.

3. Simulation and Analysis (250-300 words):
   a) Describe how you would run a simulation using your model for the given scenario.
   b) Explain how you would analyze the results of the simulation.
   c) Discuss any challenges in interpreting the output of your model and how you would address them.

4. Predictions and Implications (250-300 words):
   a) Based on your model's simulation, predict 3-5 specific linguistic changes that might occur in the given language family over the specified time frame.
   b) Explain the reasoning behind each prediction, linking it to the environmental and cultural factors.
   c) Discuss the potential broader implications of these linguistic changes on society and culture.

5. Model Evaluation and Limitations (200-250 words):
   a) Propose methods for evaluating the accuracy and reliability of your model's predictions.
   b) Discuss the limitations of your approach and potential areas for improvement.
   c) Explain how your model could be extended or adapted for other linguistic scenarios.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using computational models to predict language evolution.
   b) Address concerns about linguistic diversity and the potential impact of such predictions on minority languages.
   c) Propose guidelines for the responsible use of language evolution models in policy-making or education.

Ensure your response demonstrates a deep understanding of linguistics, evolutionary biology, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, evolutionary biology, and computational modeling.",
            "The computational model design is innovative, well-explained, and incorporates principles from multiple disciplines.",
            "The implementation and parameterization section provides a clear explanation of how the model would be implemented and calibrated.",
            "The simulation and analysis section describes a plausible approach to running and interpreting the model's output.",
            "The predictions are specific, well-reasoned, and clearly linked to the given environmental and cultural factors.",
            "The response includes a thoughtful discussion of the model's limitations and potential ethical implications.",
            "The submission adheres to the specified structure and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
