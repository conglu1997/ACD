import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modality_pairs = [
            {"input_modality": "auditory", "output_modality": "visual", "concept": "melody"},
            {"input_modality": "visual", "output_modality": "tactile", "concept": "texture"},
            {"input_modality": "olfactory", "output_modality": "auditory", "concept": "fragrance"},
            {"input_modality": "gustatory", "output_modality": "visual", "concept": "flavor profile"}
        ]
        return {
            "1": random.choice(modality_pairs),
            "2": random.choice(modality_pairs)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates synesthesia-like experiences by translating information from the {t['input_modality']} modality to the {t['output_modality']} modality, focusing on the concept of {t['concept']}.

Synesthesia is a neurological condition in which stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway. For example, some people might see colors when they hear music or taste flavors when they read words.

Your response should include the following sections, with the specified word counts:

1. System Architecture (250-300 words):
   a) Describe the key components of your cross-modal synesthesia simulator.
   b) Explain how your system processes input from the {t['input_modality']} modality.
   c) Detail the mechanism for translating this input into the {t['output_modality']} modality.
   d) Discuss any novel AI techniques or approaches you've incorporated to handle cross-modal translation.

2. Neural Basis and Cognitive Model (200-250 words):
   a) Explain how your system models the neural mechanisms underlying synesthesia.
   b) Describe how you incorporate current cognitive theories of cross-modal perception.
   c) Discuss how your model accounts for individual differences in synesthetic experiences.

3. Training and Data (200-250 words):
   a) Describe the type of data you would use to train your system.
   b) Explain your approach to creating or obtaining this training data.
   c) Discuss any ethical considerations in data collection or usage for this task.

4. Example Translation (150-200 words):
   a) Provide a detailed example of how your system would translate a specific {t['input_modality']} input related to {t['concept']} into a {t['output_modality']} output.
   b) Explain the rationale behind this translation, referencing both synesthesia research and your system's design.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the quality and consistency of your system's cross-modal translations.
   b) Describe how you would validate your system's outputs against experiences reported by human synesthetes.
   c) Discuss potential biases or limitations in your evaluation approach.

6. Novel Applications (150-200 words):
   a) Suggest two innovative applications of your cross-modal synesthesia simulator outside of pure research.
   b) Briefly explain how each application could benefit from simulated synesthetic experiences.

7. Ethical Implications and Future Directions (150-200 words):
   a) Discuss the ethical implications of simulating synesthetic experiences.
   b) Explore potential impacts on our understanding of perception and consciousness.
   c) Propose a direction for future research building on your system.

Ensure your response demonstrates a deep understanding of synesthesia, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere to the specified word count for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of synesthesia, cognitive science, and artificial intelligence, particularly in relation to {t['input_modality']}-to-{t['output_modality']} translation of {t['concept']}.",
            "The proposed system architecture is innovative, logically consistent, and effectively addresses the challenges of cross-modal translation.",
            "The example translation is detailed, plausible, and well-explained, showing a clear connection to both synesthesia research and the system's design.",
            "The response addresses the ethical implications and potential applications of simulating synesthetic experiences.",
            "The proposed evaluation methods and future directions show a nuanced understanding of the challenges in this field.",
            "The response adheres to the specified format and word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
