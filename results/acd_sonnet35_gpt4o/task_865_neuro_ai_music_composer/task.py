import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genres = ['Classical', 'Jazz', 'Electronic']
        brain_regions = ['Primary Auditory Cortex', 'Broca\'s Area', 'Cerebellum']
        ai_techniques = ['Recurrent Neural Networks', 'Generative Adversarial Networks', 'Transformer Models']
        
        tasks = [
            {
                'genre': random.choice(genres),
                'brain_region': random.choice(brain_regions),
                'ai_technique': random.choice(ai_techniques)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human auditory system to compose original music in the {t['genre']} genre. Your design should specifically incorporate insights from the {t['brain_region']} and utilize {t['ai_technique']} as a key component. Provide your response in the following format:

1. Neuroanatomical Basis (200-250 words):
   a) Describe the function of the {t['brain_region']} in human auditory processing and music perception.
   b) Explain how this brain region's structure or function informs your neural network design.
   c) Discuss any other relevant brain areas and their potential roles in your architecture.

2. Neural Network Architecture (250-300 words):
   a) Provide a detailed description of your proposed neural network architecture.
   b) Explain how you've incorporated {t['ai_technique']} into your design.
   c) Describe how your architecture mimics or is inspired by the human auditory system.
   d) Include a simple diagram or flowchart of your architecture (use ASCII art or a text-based representation).

3. Music Generation Process (200-250 words):
   a) Explain the step-by-step process of how your network would generate {t['genre']} music.
   b) Describe how your architecture captures key elements of the {t['genre']} style.
   c) Discuss any specific musical features (e.g., rhythm, harmony, melody) that your network focuses on.

4. Training and Data Considerations (150-200 words):
   a) Propose a strategy for training your neural network.
   b) Describe the type and amount of data you would need.
   c) Discuss any potential challenges in data collection or preprocessing.

5. Evaluation Metrics (100-150 words):
   a) Propose quantitative and qualitative metrics to evaluate the quality and authenticity of the generated music.
   b) Explain how you would measure the network's creativity or originality.

6. Ethical and Artistic Implications (100-150 words):
   a) Discuss the potential impact of AI-generated music on human composers and the music industry.
   b) Address any ethical concerns related to your proposed system.
   c) Explore the artistic value and potential applications of AI-composed music.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1000-1300 words, not including the diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['brain_region']} and its role in auditory processing.",
            f"The neural network architecture effectively incorporates {t['ai_technique']} and is inspired by the human auditory system.",
            f"The music generation process is well-explained and captures key elements of the {t['genre']} style.",
            "The training strategy and data considerations are thoughtfully addressed.",
            "The proposed evaluation metrics are appropriate and well-justified.",
            "Ethical and artistic implications are insightfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
