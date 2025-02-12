import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                'type': 'Coral reef',
                'climate_threat': 'Ocean acidification',
                'neural_plasticity_concept': 'Synaptic pruning'
            },
            {
                'type': 'Boreal forest',
                'climate_threat': 'Increasing temperatures',
                'neural_plasticity_concept': 'Long-term potentiation'
            },
            {
                'type': 'Arctic tundra',
                'climate_threat': 'Permafrost thawing',
                'neural_plasticity_concept': 'Neurogenesis'
            },
            {
                'type': 'Savanna grassland',
                'climate_threat': 'Changing precipitation patterns',
                'neural_plasticity_concept': 'Axon guidance'
            }
        ]
        return {str(i+1): ecosystem for i, ecosystem in enumerate(random.sample(ecosystems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by neural plasticity to model and predict ecosystem adaptations to climate change. Focus on the {t['type']} ecosystem facing the threat of {t['climate_threat']}, and use the neural plasticity concept of {t['neural_plasticity_concept']} as a key inspiration for your model. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain the chosen neural plasticity concept ({t['neural_plasticity_concept']}) and its relevance to ecosystem adaptation.
   b) Describe how this concept can be analogously applied to model changes in the {t['type']} ecosystem.
   c) Discuss the key characteristics of the {t['type']} ecosystem and the specific challenges posed by {t['climate_threat']}.

2. AI System Architecture (300-350 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system incorporates the neural plasticity concept into its architecture or algorithms.
   c) Describe how your system models the {t['type']} ecosystem and its potential adaptations to {t['climate_threat']}.
   d) Include a diagram or flowchart illustrating your system's architecture (describe it textually).

3. Data Requirements and Processing (200-250 words):
   a) Specify the types of data your system would require to model the {t['type']} ecosystem and its adaptations.
   b) Describe any necessary data preprocessing or feature extraction steps.
   c) Explain how your system would handle the complexity and interconnectedness of ecosystem data.

4. Adaptation Modeling and Prediction (250-300 words):
   a) Detail how your system models potential adaptations of the {t['type']} ecosystem to {t['climate_threat']}.
   b) Explain how the neural plasticity concept informs the adaptation modeling process.
   c) Describe the output of your system and how it represents ecosystem changes over time.
   d) Provide an example of a specific adaptation your system might predict, and explain the reasoning behind it.

5. Evaluation and Validation (200-250 words):
   a) Propose methods for evaluating the accuracy and reliability of your system's predictions.
   b) Discuss the challenges in validating long-term ecosystem adaptation models.
   c) Suggest how your system could be tested or calibrated using real-world data or experiments.

6. Ethical Considerations and Potential Applications (150-200 words):
   a) Identify potential ethical issues or concerns related to using AI to predict ecosystem adaptations.
   b) Discuss the potential applications of your system in fields such as conservation, policy-making, or education.
   c) Propose guidelines for the responsible development and use of AI in ecosystem modeling and climate change research.

Ensure your response demonstrates a deep understanding of neural plasticity, ecosystem dynamics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the neural plasticity concept {t['neural_plasticity_concept']} and its application to ecosystem adaptation.",
            f"The AI system architecture effectively incorporates the neural plasticity concept to model the {t['type']} ecosystem's adaptation to {t['climate_threat']}.",
            "The proposed data requirements and processing methods are appropriate and comprehensive for the task.",
            "The adaptation modeling and prediction approach is innovative and scientifically plausible.",
            "The evaluation and validation methods proposed are rigorous and address the challenges of long-term ecosystem modeling.",
            "The response addresses ethical considerations and potential applications of the AI system in a thoughtful manner.",
            "The writing is clear, well-structured, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
