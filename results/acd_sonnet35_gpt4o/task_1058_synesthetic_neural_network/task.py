import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ["vision", "audition", "olfaction", "gustation", "somatosensation"]
        synesthesia_types = [
            ("grapheme-color", "Assigning colors to letters or numbers"),
            ("chromesthesia", "Associating sounds with colors"),
            ("lexical-gustatory", "Tasting words"),
            ("spatial-sequence", "Perceiving numerical sequences as points in space"),
            ("mirror-touch", "Feeling observed touch sensations on one's own body")
        ]
        
        tasks = []
        for _ in range(2):
            primary_modality = random.choice(sensory_modalities)
            secondary_modality = random.choice([m for m in sensory_modalities if m != primary_modality])
            tasks.append({
                "primary_modality": primary_modality,
                "secondary_modality": secondary_modality,
                "synesthesia_type": random.choice(synesthesia_types)
            })
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network model that simulates synesthesia, specifically the {t['synesthesia_type'][0]} type ({t['synesthesia_type'][1]}), then use it to generate and analyze cross-modal sensory experiences between {t['primary_modality']} and {t['secondary_modality']}.

Synesthesia is a neurological condition in which stimulation of one sensory or cognitive pathway leads to involuntary experiences in a second sensory or cognitive pathway.

Your response should include:

1. Neural Network Architecture (250-300 words):
   a) Describe the overall structure of your neural network model.
   b) Explain how your model incorporates both {t['primary_modality']} and {t['secondary_modality']} processing.
   c) Detail any novel elements in your design that enable the simulation of synesthetic experiences.
   d) Include a simple diagram or ASCII representation of your network architecture.

2. Synesthesia Simulation Mechanism (200-250 words):
   a) Explain how your model simulates the {t['synesthesia_type'][0]} type of synesthesia.
   b) Describe the specific mechanisms that link {t['primary_modality']} and {t['secondary_modality']} in your model.
   c) Discuss how your model accounts for individual variations in synesthetic experiences.

3. Training and Data (200-250 words):
   a) Propose a method for training your neural network.
   b) Describe the type of data you would need and how you would obtain or generate it.
   c) Explain any challenges in data collection or preparation specific to synesthesia modeling.

4. Experience Generation and Analysis (250-300 words):
   a) Describe how your model would generate a synesthetic experience given a {t['primary_modality']} input.
   b) Provide a specific example of an input and the resulting cross-modal output.
   c) Explain how you would analyze and interpret the generated experiences.
   d) Discuss how your model's output could be validated against real synesthetic experiences.

5. Implications and Applications (150-200 words):
   a) Discuss potential insights about human perception and cognition that could be gained from your model.
   b) Propose an application of your model in cognitive science, art, or technology.
   c) Consider any ethical implications of simulating or inducing synesthetic experiences.

Ensure your response demonstrates a deep understanding of neural network architectures, sensory processing, and the phenomenon of synesthesia. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from neuroscience and machine learning, providing explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a well-defined neural network architecture for simulating synesthesia",
            "The model should specifically address the given synesthesia type and sensory modalities",
            "The response should include a diagram or ASCII representation of the network architecture",
            "The synesthesia simulation mechanism should be clearly explained",
            "The response should propose a plausible training method and data collection strategy",
            "The experience generation and analysis section should include a specific example",
            "The response should discuss potential implications and applications of the model",
            "The submission should demonstrate interdisciplinary knowledge integration",
            "The proposed model and methods should be creative yet scientifically plausible",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1050-1300 words)",
            "All five required sections (Neural Network Architecture, Synesthesia Simulation Mechanism, Training and Data, Experience Generation and Analysis, Implications and Applications) must be present and adequately addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
