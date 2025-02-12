import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        data_types = ['time series', 'geospatial', 'network', 'textual', 'categorical']
        applications = ['scientific visualization', 'accessibility', 'artistic creation', 'data sonification', 'human-AI communication']
        
        tasks = {
            "1": {
                "input_modality": random.choice(sensory_modalities),
                "output_modality": random.choice(sensory_modalities),
                "data_type": random.choice(data_types),
                "application": random.choice(applications)
            },
            "2": {
                "input_modality": random.choice(sensory_modalities),
                "output_modality": random.choice(sensory_modalities),
                "data_type": random.choice(data_types),
                "application": random.choice(applications)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of artificial synaesthesia, then apply it to enhance data interpretation and human-AI interaction. Your system should transform information from the {t['input_modality']} modality to the {t['output_modality']} modality, focusing on {t['data_type']} data for applications in {t['application']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your artificial synaesthesia AI system.
   b) Explain how your system processes information from the input modality and translates it to the output modality.
   c) Discuss any novel algorithms or neural network architectures you've employed.
   d) Provide a brief textual description of a diagram illustrating your system's architecture.

2. Synaesthetic Mapping (200-250 words):
   a) Explain the principles behind your synaesthetic mapping from {t['input_modality']} to {t['output_modality']}.
   b) Describe how your system ensures consistency and meaningfulness in this mapping.
   c) Discuss how your mapping might differ from or be inspired by human synaesthesia.

3. Data Interpretation Enhancement (200-250 words):
   a) Explain how your system enhances the interpretation of {t['data_type']} data.
   b) Provide an example of how a specific {t['data_type']} dataset might be represented in the {t['output_modality']} modality.
   c) Discuss potential benefits and limitations of this approach to data interpretation.

4. Application in {t['application']} (200-250 words):
   a) Describe how your artificial synaesthesia system could be applied in {t['application']}.
   b) Explain the potential benefits of using your system in this context.
   c) Discuss any challenges that might arise and how you would address them.

5. Human-AI Interaction (150-200 words):
   a) Explain how your system enhances human-AI interaction.
   b) Discuss potential cognitive effects on users interacting with your system.
   c) Propose a method for training users to effectively interpret the synaesthetic output.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to artificial synaesthesia and your system's application.
   b) Discuss implications for privacy, cognitive manipulation, and sensory overload.
   c) Propose guidelines for the responsible development and use of artificial synaesthesia systems.

7. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your artificial synaesthesia system.
   b) Describe experiments you would conduct to validate its performance in {t['application']}.
   c) Discuss how you would measure improvements in data interpretation or human-AI interaction.

Ensure your response demonstrates a deep understanding of perception, cognition, artificial intelligence, and the specific domains involved in your chosen application. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed design of an AI system capable of artificial synaesthesia",
            f"The system transforms information from the {t['input_modality']} modality to the {t['output_modality']} modality",
            f"The response explains how the system enhances interpretation of {t['data_type']} data",
            f"The answer describes a concrete application in {t['application']}",
            "The response discusses ethical considerations and proposes guidelines for responsible use",
            "The answer demonstrates interdisciplinary knowledge integration and creative problem-solving",
            "The response is well-structured with clear headings for each section and adheres to the word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
