import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise']
        musical_styles = ['classical', 'jazz', 'electronic', 'folk', 'rock']
        tasks = [
            {
                'emotion': random.choice(emotions),
                'musical_style': random.choice(musical_styles)
            },
            {
                'emotion': random.choice(emotions),
                'musical_style': random.choice(musical_styles)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human auditory system to compose music that elicits the emotion of {t['emotion']} in the style of {t['musical_style']} music. Then, analyze its implications for AI creativity and human-AI collaboration in the arts. Your response should include:

1. Neural Network Architecture (300-350 words):
   a) Describe the key components of your neural network, explaining how they mimic relevant parts of the human auditory system.
   b) Explain how your architecture incorporates both low-level auditory processing and high-level musical understanding.
   c) Discuss how your system generates music to elicit specific emotions.
   d) Include a diagram or detailed description of your neural network's structure.

2. Neuroscientific Basis (250-300 words):
   a) Explain the neuroscientific principles underlying your design, focusing on how the brain processes music and emotions.
   b) Discuss how your model incorporates current understanding of the neural correlates of musical perception and emotion.
   c) Address any simplifications or assumptions made in translating biological systems to artificial neural networks.

3. Musical Theory Integration (200-250 words):
   a) Describe how your system incorporates principles of music theory specific to the given musical style.
   b) Explain how these principles are used to generate emotionally evocative compositions.
   c) Discuss any challenges in translating music theory concepts into neural network parameters.

4. Training and Evaluation (250-300 words):
   a) Outline a training process for your neural network, including necessary datasets and learning algorithms.
   b) Propose a method to evaluate the emotional impact and musical quality of the generated compositions.
   c) Discuss potential biases in training data and how they might be addressed.

5. AI Creativity Analysis (200-250 words):
   a) Analyze the implications of your system for our understanding of AI creativity.
   b) Discuss how this approach might challenge or expand current definitions of artistic creativity.
   c) Consider the potential for your system to generate novel musical forms or emotional expressions.

6. Human-AI Collaboration (200-250 words):
   a) Propose a framework for collaboration between human composers and your AI system.
   b) Discuss potential benefits and challenges of this collaboration.
   c) Consider how this might impact the future of music composition and the role of human artists.

7. Ethical and Societal Implications (150-200 words):
   a) Discuss ethical considerations related to AI-generated emotional music.
   b) Analyze potential societal impacts of widespread use of such systems in the music industry.
   c) Propose guidelines for responsible development and use of emotion-generating AI in the arts.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-2000 words.

Note: Your response will be evaluated based on the depth of your analysis, the integration of concepts from neuroscience, AI, and music theory, and the creativity and feasibility of your proposed system. A successful response will thoroughly address all sections while maintaining scientific accuracy and innovative thinking."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed design of a neural network architecture inspired by the human auditory system for music composition.",
            "The neuroscientific basis of the design is thoroughly explained and related to current understanding of music and emotion processing in the brain.",
            "The integration of music theory principles specific to the given musical style is clearly described.",
            "A comprehensive training and evaluation process is outlined.",
            "The implications for AI creativity and human-AI collaboration are thoughtfully analyzed.",
            "Ethical and societal implications are considered, with proposed guidelines for responsible development.",
            f"The system is designed to compose music that elicits the emotion of {t['emotion']} in the style of {t['musical_style']} music."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
