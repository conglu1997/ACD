import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = [
            "visual",
            "auditory",
            "olfactory",
            "gustatory",
            "tactile",
            "proprioceptive"
        ]
        linguistic_elements = [
            "phonemes",
            "morphemes",
            "syntax",
            "semantics",
            "pragmatics"
        ]
        tasks = [
            {
                "modality": random.choice(sensory_modalities),
                "linguistic_element": random.choice(linguistic_elements)
            },
            {
                "modality": random.choice(sensory_modalities),
                "linguistic_element": random.choice(linguistic_elements)
            }
        ]
        return {"1": tasks[0], "2": tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a language model that incorporates linguistic synesthesia, focusing on the {t['modality']} sensory modality and the linguistic element of {t['linguistic_element']}. Your response should include:

1. Conceptual Framework (200-250 words):
   a) Explain the concept of linguistic synesthesia and its potential cognitive basis.
   b) Describe how the {t['modality']} modality might interact with {t['linguistic_element']} in language processing.
   c) Propose a theoretical mechanism for this interaction in your model.

2. Model Architecture (250-300 words):
   a) Design a neural network architecture that implements your linguistic synesthesia model.
   b) Explain how your model processes and generates language while incorporating {t['modality']} sensory information.
   c) Describe any novel components or algorithms in your model.
   d) Include a high-level diagram or pseudocode to illustrate your architecture (describe it textually).

3. Training and Data (150-200 words):
   a) Propose a method for creating a dataset that captures the synesthetic associations between {t['linguistic_element']} and {t['modality']} experiences.
   b) Describe how you would train your model on this dataset.
   c) Discuss any challenges in data collection or training and how you might address them.

4. Model Behavior and Outputs (200-250 words):
   a) Provide two specific examples of how your model would process input and generate output, highlighting the synesthetic aspects.
   b) Explain how your model's behavior differs from traditional language models.
   c) Discuss any potential emergent behaviors or capabilities of your model.

5. Applications and Implications (150-200 words):
   a) Propose two potential applications of your linguistic synesthesia model in AI or cognitive science.
   b) Discuss the ethical implications of using such a model, particularly in human-AI interaction.
   c) Explore how this model might contribute to our understanding of human cognition and language processing.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and adhere to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of linguistic synesthesia and its potential cognitive basis.",
            f"The model architecture should coherently integrate the {t['modality']} modality with {t['linguistic_element']}.",
            "The proposed training method and dataset creation should be feasible and well-reasoned.",
            "The examples of model behavior should clearly illustrate the synesthetic aspects of language processing.",
            "The proposed applications and implications should be innovative and demonstrate an understanding of the model's potential impact.",
            "The overall response should be creative, coherent, and demonstrate strong interdisciplinary reasoning.",
            "The response should adhere to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
