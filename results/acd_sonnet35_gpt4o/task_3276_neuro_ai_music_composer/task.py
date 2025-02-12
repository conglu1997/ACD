import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'love', 'surprise']
        musical_styles = ['classical', 'jazz', 'electronic', 'folk', 'rock', 'ambient']
        brain_regions = ['auditory cortex', 'amygdala', 'hippocampus', 'prefrontal cortex', 'cerebellum', 'basal ganglia']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'target_emotion': random.choice(emotions),
                'musical_style': random.choice(musical_styles),
                'focus_brain_region': random.choice(brain_regions)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human auditory system and music processing areas of the brain to compose emotionally evocative music. Your system should aim to generate music that evokes the emotion of {t['target_emotion']} in the style of {t['musical_style']}, with a particular focus on incorporating insights from the {t['focus_brain_region']}. Your response should include:

1. Neuroscientific Basis (250-300 words):
   a) Explain the role of the {t['focus_brain_region']} in music perception and emotion processing.
   b) Describe how this brain region interacts with other areas involved in music cognition.
   c) Discuss any relevant neuroscientific theories or findings that inform your design.

2. Neural Network Architecture (300-350 words):
   a) Provide a detailed description of your proposed neural network architecture.
   b) Explain how your architecture mimics or is inspired by the structure and function of the {t['focus_brain_region']} and related brain areas.
   c) Describe how your system integrates auditory processing, emotion, and musical style generation.
   d) Include a diagram or detailed schematic representation of your architecture (describe it in words).

3. Music Generation Process (250-300 words):
   a) Explain how your system generates music to evoke {t['target_emotion']}.
   b) Describe the specific musical elements (e.g., rhythm, harmony, timbre) your system manipulates to achieve the desired emotion.
   c) Discuss how your system incorporates the characteristics of {t['musical_style']} into its compositions.

4. Training and Data (200-250 words):
   a) Describe the training process for your neural network.
   b) Explain what types of data would be used to train the system.
   c) Discuss any challenges in obtaining or creating suitable training data and how you would address them.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the emotional impact of the generated music.
   b) Describe how you would validate the neuroscientific plausibility of your system.
   c) Suggest experiments to test the effectiveness of your system in evoking {t['target_emotion']}.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI to generate emotionally evocative music.
   b) Address limitations of your approach and potential biases in the system.
   c) Propose guidelines for responsible development and use of emotion-generating AI in music.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, music theory, and emotional psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your points as shown above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed explanation of the role of the {t['focus_brain_region']} in music perception and emotion processing.",
            "The proposed neural network architecture is clearly described and demonstrates inspiration from brain structure and function.",
            f"The music generation process for evoking {t['target_emotion']} is thoroughly explained, including specific musical elements manipulated.",
            f"The response discusses how the system incorporates characteristics of {t['musical_style']} into its compositions.",
            "The training process and data requirements are clearly described, including addressing potential challenges.",
            "Evaluation methods are proposed for both emotional impact and neuroscientific plausibility of the system.",
            "Ethical considerations and limitations are thoughtfully discussed, with proposed guidelines for responsible development.",
            "The response demonstrates deep understanding of neuroscience, AI, music theory, and emotional psychology, using appropriate terminology.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
