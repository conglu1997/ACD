import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species_scenarios = [
            {
                "species": "dolphins",
                "communication_type": "echolocation and whistles",
                "conservation_issue": "ocean noise pollution"
            },
            {
                "species": "honeybees",
                "communication_type": "dance language and pheromones",
                "conservation_issue": "colony collapse disorder"
            },
            {
                "species": "elephants",
                "communication_type": "infrasound and body language",
                "conservation_issue": "habitat fragmentation"
            },
            {
                "species": "cephalopods",
                "communication_type": "color and pattern changes",
                "conservation_issue": "ocean acidification"
            }
        ]
        return {
            "1": random.choice(species_scenarios),
            "2": random.choice(species_scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI language model capable of understanding and generating communication patterns of {t['species']}, focusing on their {t['communication_type']}. Then, apply this model to address the conservation issue of {t['conservation_issue']}. Your response should include:\n\n1. Model Architecture (250-300 words):\n   a) Describe the key components of your AI language model.\n   b) Explain how your model is adapted to process and generate {t['species']} communication.\n   c) Discuss any novel techniques or architectures you've incorporated to handle non-human communication patterns.\n\n2. Data and Training (200-250 words):\n   a) Describe the type of data you would need to train your model.\n   b) Explain your data collection and preprocessing methods.\n   c) Outline your training approach, including any specific challenges and how you'd address them.\n\n3. Model Capabilities (200-250 words):\n   a) Detail the expected capabilities of your trained model in understanding {t['species']} communication.\n   b) Explain how the model would generate or respond to {t['species']} communication signals.\n   c) Discuss any limitations of your model and potential future improvements.\n\n4. Conservation Application (250-300 words):\n   a) Propose a specific application of your model to address {t['conservation_issue']}.\n   b) Explain how the model's understanding of {t['species']} communication would contribute to conservation efforts.\n   c) Describe a hypothetical scenario where your model could make a significant impact.\n\n5. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical implications of using AI to interpret and generate animal communication.\n   b) Address concerns about privacy and potential misuse of the technology.\n   c) Propose guidelines for responsible use of your model in research and conservation.\n\n6. Interdisciplinary Implications (150-200 words):\n   a) Discuss how your model could contribute to advancements in biology, ecology, and AI.\n   b) Propose potential applications of your model in fields beyond conservation.\n\nEnsure your response demonstrates a deep understanding of AI language models, animal communication, and conservation biology. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should propose an AI language model for {t['species']} communication, focusing on {t['communication_type']}.",
            "The model architecture should be clearly explained and adapted for non-human communication patterns.",
            "The data and training approach should be well-thought-out and address specific challenges.",
            "The model's capabilities and limitations should be realistically assessed.",
            f"The conservation application should specifically address {t['conservation_issue']} using the model.",
            "Ethical considerations should be thoroughly discussed.",
            "Interdisciplinary implications should be explored.",
            "The response should demonstrate a deep understanding of AI, animal communication, and conservation biology.",
            "The response should adhere to the specified word count for each section and the overall total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
