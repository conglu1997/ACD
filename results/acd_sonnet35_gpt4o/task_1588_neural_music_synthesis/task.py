import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "auditory cortex",
            "prefrontal cortex",
            "hippocampus",
            "amygdala"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre"
        ]
        musical_genres = [
            "classical",
            "jazz",
            "electronic",
            "world music"
        ]
        
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "musical_genre": random.choice(musical_genres)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "musical_genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a neural network model that can synthesize original music based on brain activity patterns associated with musical perception and creativity. Your model should focus on the {t['brain_region']} for neural input, emphasize the musical element of {t['musical_element']}, and generate music in the {t['musical_genre']} genre. Provide your response in the following format:\n\n1. Neural Network Architecture (250-300 words):\n   a) Describe the key components of your neural network model.\n   b) Explain how your model processes neural signals from the {t['brain_region']}.\n   c) Detail how the model generates musical output, focusing on {t['musical_element']}.\n   d) Discuss any novel techniques or algorithms used in your model.\n\n2. Brain-Music Interface (200-250 words):\n   a) Explain how your model interprets brain activity patterns related to musical perception and creativity.\n   b) Describe the specific neural features or patterns associated with {t['musical_element']} in the {t['brain_region']}.\n   c) Discuss any challenges in mapping neural activity to musical parameters.\n\n3. Musical Output Generation (200-250 words):\n   a) Describe the process of generating {t['musical_genre']} music from the neural input.\n   b) Explain how your model ensures the output adheres to the conventions of {t['musical_genre']}.\n   c) Discuss how the emphasis on {t['musical_element']} is maintained in the generated music.\n\n4. Training and Optimization (150-200 words):\n   a) Propose a method for training your neural network model.\n   b) Describe the data requirements and potential sources for training.\n   c) Discuss any potential overfitting issues and how to address them.\n\n5. Evaluation and Validation (150-200 words):\n   a) Suggest metrics for evaluating the quality and creativity of the generated music.\n   b) Propose an experiment to validate the model's ability to capture brain-music relationships.\n   c) Discuss how you would ensure the model's output is original and not simply reproducing existing music.\n\n6. Ethical Considerations and Applications (100-150 words):\n   a) Discuss potential ethical implications of a brain-music interface.\n   b) Explore possible applications of this technology in fields such as music therapy, creativity enhancement, or brain-computer interfaces.\n   c) Address any privacy concerns related to decoding musical creativity from brain activity.\n\nEnsure your response demonstrates a deep understanding of neuroscience, music theory, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section and use subheadings where appropriate."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and machine learning.",
            "The neural network architecture is well-designed and plausibly integrates brain activity with music generation.",
            "The brain-music interface is explained clearly and accounts for the specified brain region and musical element.",
            "The process of generating music in the specified genre is well-described and theoretically sound.",
            "The training, optimization, and evaluation methods are appropriate and well-reasoned.",
            "Ethical considerations and potential applications are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
