import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = ['Jazz', 'Classical', 'Electronic', 'Folk']
        auditory_cortex_features = ['Tonotopic organization', 'Spectrotemporal receptive fields', 'Hierarchical processing', 'Plasticity']
        musical_elements = ['Melody', 'Harmony', 'Rhythm', 'Timbre']
        
        return {
            "1": {
                "style": random.choice(musical_styles),
                "cortex_feature": random.choice(auditory_cortex_features),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "style": random.choice(musical_styles),
                "cortex_feature": random.choice(auditory_cortex_features),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the auditory cortex to analyze and generate music, focusing on the following specifications:

Musical Style: {t['style']}
Auditory Cortex Feature: {t['cortex_feature']}
Musical Element to Focus On: {t['musical_element']}

Your response should include:

1. Neural Network Architecture (250-300 words):
   a) Describe the overall structure of your neural network, explaining how it mimics the specified auditory cortex feature.
   b) Detail the specific layers and connections in your network, including any novel elements.
   c) Explain how your architecture enables analysis and generation of the specified musical style and element.
   d) Discuss how your network incorporates principles from both neuroscience and deep learning.

2. Music Analysis Process (200-250 words):
   a) Explain how your network would analyze a piece of music in the specified style.
   b) Describe how the network identifies and processes the specified musical element.
   c) Discuss any preprocessing or feature extraction techniques used.
   d) Explain how the analysis relates to the auditory cortex feature your network is inspired by.

3. Music Generation Approach (200-250 words):
   a) Describe the step-by-step process your network would use to generate music in the specified style.
   b) Explain how your network ensures the generated music emphasizes the specified musical element.
   c) Discuss how the generation process relates to the auditory cortex feature your network is inspired by.
   d) Propose a method for maintaining long-term structure and coherence in the generated music.

4. Training and Learning (150-200 words):
   a) Propose a training approach for your network, including data requirements and potential sources.
   b) Explain how your network could adapt or fine-tune its understanding of different musical styles or elements.
   c) Discuss any challenges in training such a specialized network and how you'd address them.

5. Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the quality and style-accuracy of the generated music.
   b) Describe how you would validate the network's understanding of the specified musical element.
   c) Suggest experiments to compare your network's performance with human musicians or other AI systems.

6. Neuroscience and AI Implications (200-250 words):
   a) Discuss how your network's design might provide insights into auditory processing in the brain.
   b) Explore potential applications of your system in neuroscience research or music education.
   c) Analyze ethical considerations of using AI systems inspired by brain function for creative tasks.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, particularly the {t['cortex_feature']} of the auditory cortex.",
            f"The neural network architecture is well-designed and plausibly mimics the {t['cortex_feature']} of the auditory cortex.",
            f"The music analysis and generation processes are clearly explained and appropriate for the {t['style']} style and focus on {t['musical_element']}.",
            "The response shows creativity and innovation in combining principles from neuroscience, AI, and music theory.",
            "The proposed evaluation methods and implications are thoughtful and well-reasoned.",
            "The response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
