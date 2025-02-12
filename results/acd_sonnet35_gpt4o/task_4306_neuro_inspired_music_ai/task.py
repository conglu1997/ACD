import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy and excitement",
            "melancholy and nostalgia",
            "fear and tension",
            "serenity and calmness"
        ]
        auditory_regions = [
            "primary auditory cortex",
            "superior temporal gyrus",
            "inferior colliculus",
            "amygdala"
        ]
        return {
            "1": {
                "emotion": random.choice(emotions),
                "region": random.choice(auditory_regions)
            },
            "2": {
                "emotion": random.choice(emotions),
                "region": random.choice(auditory_regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human auditory system, with a focus on the {t['region']}, to generate and analyze music. Then, use this system to compose a piece that evokes the emotions of {t['emotion']}. Your response should include the following sections:

1. Neural Network Architecture (300-350 words):
   a) Describe the key components of your neural network and how they correspond to structures in the human auditory system.
   b) Explain how your architecture incorporates the {t['region']} and its role in music processing.
   c) Discuss any novel approaches or algorithms used in your design.
   d) Provide a high-level diagram or pseudocode representing your neural network's structure (describe this textually).

2. Music Generation and Analysis Process (250-300 words):
   a) Explain how your system generates music, including the input and output formats.
   b) Describe the method used to analyze the emotional content of the generated music.
   c) Discuss how you've incorporated music theory principles into your system.

3. Composition for {t['emotion']} (200-250 words):
   a) Describe the key features of a musical piece composed by your system to evoke {t['emotion']}.
   b) Explain how specific musical elements (e.g., key, tempo, rhythm, instrumentation) contribute to the intended emotional response.
   c) Discuss any challenges faced in generating music for this specific emotion and how your system addressed them.

4. Neuroscientific Basis (200-250 words):
   a) Analyze how your system's approach to music generation and emotion relates to current neuroscientific understanding of music perception and emotional processing.
   b) Discuss any insights your system might provide about the role of the {t['region']} in music-related emotional responses.
   c) Propose a hypothesis about music cognition that could be tested using your system.

5. Evaluation and Validation (150-200 words):
   a) Propose a method to evaluate the effectiveness of your system in generating emotionally evocative music.
   b) Describe an experiment to validate the neuroscientific plausibility of your system's music generation process.
   c) Discuss potential applications of your system in music therapy or emotional regulation.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using AI to generate emotionally manipulative music.
   b) Address potential concerns about the impact of AI-generated music on human creativity and the music industry.
   c) Propose two future research directions to enhance or expand your neuro-inspired music AI system.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed description of a neural network architecture inspired by the human auditory system, with a focus on the {t['region']}.",
            f"The music generation and analysis process should be clearly explained and incorporate music theory principles.",
            f"The composition description should effectively demonstrate how the system would evoke the emotions of {t['emotion']}.",
            "The response should show a deep understanding of the neuroscientific basis of music perception and emotional processing.",
            "The proposed evaluation method and experiment should be scientifically sound and relevant to the system's goals.",
            "The response should address ethical considerations and propose meaningful future research directions.",
            "The overall response should demonstrate interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
