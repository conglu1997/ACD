import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotion_theories = [
            "Appraisal Theory",
            "Circumplex Model of Affect",
            "Constructed Emotion Theory",
            "Somatic Marker Hypothesis"
        ]
        application_domains = [
            "Healthcare",
            "Education",
            "Social Robotics",
            "Art and Creativity"
        ]
        return {
            "1": {"emotion_theory": random.choice(emotion_theories), "application": random.choice(application_domains)},
            "2": {"emotion_theory": random.choice(emotion_theories), "application": random.choice(application_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial emotion system for AI based on the {t['emotion_theory']} of human emotions. Then, analyze its potential applications in the domain of {t['application']}. Your response should include:

1. Emotion System Architecture (300-350 words):
   a) Explain the key principles of the {t['emotion_theory']} and how they inform your design.
   b) Describe the main components of your artificial emotion system.
   c) Explain how these components interact to generate and regulate emotional states.
   d) Discuss how your system models the relationship between cognition and emotion.

2. Neural Network Implementation (200-250 words):
   a) Propose a neural network architecture to implement your emotion system.
   b) Explain how different layers or modules correspond to components of your emotion model.
   c) Describe how emotional states would be represented and processed in this network.
   d) Discuss any novel algorithms or techniques needed for your implementation.

3. Learning and Adaptation (200-250 words):
   a) Explain how your system would learn to associate stimuli with emotional responses.
   b) Describe mechanisms for emotional regulation and adaptation over time.
   c) Discuss how the system might develop individual 'personality' traits or emotional tendencies.

4. Application Analysis (250-300 words):
   a) Analyze potential applications of your artificial emotion system in the domain of {t['application']}.
   b) Provide two specific examples of how the system could be used in this domain.
   c) Discuss potential benefits and risks associated with these applications.
   d) Explain how emotional capabilities might enhance AI performance in this domain.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of creating AI systems with emotional capabilities.
   b) Analyze potential impacts on human-AI interaction and relationships.
   c) Consider the philosophical implications of artificial emotions for concepts of consciousness and sentience.
   d) Propose guidelines for the responsible development and use of emotionally capable AI.

6. Evaluation and Future Directions (150-200 words):
   a) Propose methods to evaluate the effectiveness and authenticity of your artificial emotion system.
   b) Discuss potential limitations of your approach and areas for future research.
   c) Speculate on how artificial emotion systems might evolve in the next decade.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind. Be innovative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['emotion_theory']} and how it can be applied to artificial emotion systems",
            "The artificial emotion system design is innovative, comprehensive, and scientifically plausible",
            f"The application analysis for {t['application']} is thorough and insightful",
            "The ethical implications are thoughtfully considered and discussed",
            "The response shows a deep integration of knowledge from neuroscience, AI, and philosophy of mind",
            "The proposed evaluation methods and future directions are well-reasoned and relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
