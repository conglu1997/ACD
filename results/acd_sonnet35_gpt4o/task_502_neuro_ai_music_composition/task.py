import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_style": "Jazz",
                "neuroscience_focus": "Temporal processing in the auditory cortex",
                "ai_technique": "Recurrent Neural Networks (RNN)"
            },
            {
                "musical_style": "Classical",
                "neuroscience_focus": "Hierarchical structure processing in the auditory cortex",
                "ai_technique": "Transformer architecture"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human auditory cortex to compose original {t['musical_style']} music. Your task should focus on {t['neuroscience_focus']} and utilize {t['ai_technique']}. Provide a detailed response addressing the following points:

1. Neural Network Architecture (250-300 words):
   a) Describe the key components of your neural network architecture.
   b) Explain how your design is inspired by the structure and function of the human auditory cortex, particularly in relation to {t['neuroscience_focus']}.
   c) Detail how you incorporate {t['ai_technique']} into your model and why it's suitable for this task.
   d) Discuss how your architecture captures essential elements of {t['musical_style']}.

2. Training Process (200-250 words):
   a) Outline the training process for your neural network.
   b) Describe the dataset you would use, including its composition and preprocessing.
   c) Explain any specific training techniques or algorithms you would employ.
   d) Discuss potential challenges in training and how you would address them.

3. Music Generation Process (200-250 words):
   a) Explain step-by-step how your trained model would generate original {t['musical_style']} compositions.
   b) Describe how you ensure the output adheres to {t['musical_style']} conventions while maintaining originality.
   c) Discuss any post-processing techniques you would apply to refine the generated music.

4. Evaluation Metrics (150-200 words):
   a) Propose at least three quantitative metrics to evaluate the quality and style-adherence of the generated music.
   b) Describe a qualitative evaluation method involving human listeners.
   c) Explain how you would use these evaluations to improve your model.

5. Neuroscientific Insights (200-250 words):
   a) Discuss how your model's performance might provide insights into {t['neuroscience_focus']}.
   b) Propose a hypothesis about human auditory processing that could be tested using your model.
   c) Explain how your approach might contribute to our understanding of creativity in the human brain.

6. Ethical and Artistic Implications (150-200 words):
   a) Discuss the potential impact of AI-generated music on human composers and the music industry.
   b) Address copyright and ownership issues related to AI-composed music.
   c) Explore the philosophical question: Can AI-generated music be considered truly creative or artistic?

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Be creative in your approach while maintaining scientific accuracy and plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The neural network architecture effectively incorporates principles from neuroscience and AI, specifically addressing the given focus areas.",
            "The training and music generation processes are well-explained and scientifically sound.",
            "The proposed evaluation metrics are appropriate and well-justified.",
            "The discussion of neuroscientific insights demonstrates a deep understanding of both AI and neuroscience.",
            "The ethical and artistic implications are thoughtfully explored.",
            "The overall response shows strong interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
