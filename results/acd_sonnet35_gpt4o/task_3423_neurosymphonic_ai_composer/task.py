import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = ['joy', 'sorrow', 'anger', 'fear', 'love']
        cognitive_functions = ['memory', 'attention', 'decision-making', 'language processing', 'spatial reasoning']
        musical_styles = ['classical', 'jazz', 'electronic', 'folk', 'avant-garde']
        neural_architectures = ['LSTM', 'Transformer', 'GAN', 'CNN', 'Reservoir Computing']
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "inspiration": random.choice(emotional_states + cognitive_functions),
                "musical_style": random.choice(musical_styles),
                "duration": random.randint(2, 5),  # in minutes
                "neural_architecture": random.choice(neural_architectures),
                "composition_time": random.randint(10, 30)  # in seconds
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics the human brain's neural processes to compose music, then use it to create a piece based on the {t['inspiration']} in {t['musical_style']} style, with a duration of {t['duration']} minutes. Your system should incorporate a {t['neural_architecture']} architecture and be able to compose the piece within {t['composition_time']} seconds. Your response should include the following sections:

1. Neuroscientific Framework (250-300 words):
   a) Explain the neural processes involved in {t['inspiration']} and music composition.
   b) Describe how these processes interact in the human brain.
   c) Propose a novel hypothesis about the neural basis of musical creativity related to {t['inspiration']}.
   d) Discuss how the time constraint of {t['composition_time']} seconds relates to human cognitive processes in music composition.

2. AI System Architecture (300-350 words):
   a) Design the key components of your AI system that mimic the relevant neural processes.
   b) Explain how your system integrates neuroscientific principles with AI algorithms.
   c) Describe how your system models the interaction between {t['inspiration']} and musical composition.
   d) Explain how you incorporate the {t['neural_architecture']} architecture into your system, detailing how it maps to the neuroscientific framework.
   e) Discuss potential limitations or challenges of using {t['neural_architecture']} for this specific task.
   f) Include a simple diagram or flowchart of your system architecture.

3. Music Composition Process (250-300 words):
   a) Detail how your AI system generates musical elements (melody, harmony, rhythm) based on {t['inspiration']}.
   b) Explain how it incorporates the characteristics of {t['musical_style']} into the composition.
   c) Describe the decision-making process your system uses to structure the {t['duration']}-minute piece.
   d) Explain how your system optimizes the composition process to meet the {t['composition_time']}-second time constraint.

4. Output Analysis (200-250 words):
   a) Provide a detailed description of the composed piece, including its structure and key musical features.
   b) Explain how the composition reflects both {t['inspiration']} and {t['musical_style']}.
   c) Discuss any unexpected or creative elements in the AI-generated music.
   d) Analyze how the time constraint might have influenced the composition's quality or complexity.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the neuroscientific accuracy of your AI system.
   b) Suggest approaches to assess the musical quality and emotional/cognitive impact of the composition.
   c) Describe an experiment to compare your AI's compositions with those of human composers under similar time constraints.
   d) Discuss how you would evaluate the system's efficiency in meeting the {t['composition_time']}-second constraint.

6. Ethical Considerations and Future Implications (150-200 words):
   a) Discuss ethical issues related to AI systems that mimic human cognitive and creative processes.
   b) Explore potential applications of your system in music therapy or cognitive research.
   c) Propose future research directions combining neuroscience, AI, and music composition.
   d) Consider the implications of AI systems that can create art more quickly than humans.

7. Code Implementation (100-150 words):
   a) Provide a short code snippet or pseudocode for a key component of your AI system, specifically related to the {t['neural_architecture']} architecture and the time-constrained composition process.
   b) Explain how this component integrates with the rest of your system to generate music based on {t['inspiration']} within the given time constraint.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, music theory, neural network architectures, and computational efficiency. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a clear explanation of the neural processes involved in {t['inspiration']} and music composition, including how they relate to the {t['composition_time']}-second time constraint",
            "The AI system architecture should be described in detail, integrating neuroscientific principles with AI algorithms",
            f"The system should appropriately incorporate the {t['neural_architecture']} architecture, with a discussion of its limitations for this task",
            f"The music composition process should be well-explained, incorporating {t['inspiration']} and {t['musical_style']} characteristics, and addressing the {t['composition_time']}-second time constraint",
            f"The output analysis should provide a detailed description of the {t['duration']}-minute AI-composed piece, including the impact of the time constraint",
            "The response should propose valid methods for evaluating the neuroscientific accuracy, musical quality, and computational efficiency of the AI system",
            "Ethical considerations and future implications of the AI system should be thoroughly discussed, including the impact of rapid AI art creation",
            "The response should demonstrate a deep understanding of neuroscience, artificial intelligence, music theory, neural network architectures, and computational efficiency",
            "The proposed AI system should be creative and innovative while maintaining scientific plausibility",
            f"A code snippet or pseudocode for a key component related to the {t['neural_architecture']} architecture and time-constrained composition process should be provided and explained"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
