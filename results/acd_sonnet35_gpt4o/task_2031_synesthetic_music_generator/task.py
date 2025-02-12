import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        visual_inputs = [
            {
                "type": "Abstract Painting",
                "description": "A vibrant abstract expressionist painting with bold strokes of red, blue, and yellow"
            },
            {
                "type": "Natural Scene",
                "description": "A serene landscape photograph of a misty forest at dawn"
            },
            {
                "type": "Urban Environment",
                "description": "A bustling cityscape with neon lights and towering skyscrapers at night"
            },
            {
                "type": "Emotional Portrait",
                "description": "A black and white portrait photograph capturing intense human emotion"
            }
        ]
        return {str(i+1): input for i, input in enumerate(random.sample(visual_inputs, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates music based on visual input, simulating synesthesia, and analyze its implications for cognitive science and creativity research. Your system should focus on translating the following visual input into a musical composition: {t['type']} - {t['description']}

Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for translating visual input into music.
   b) Explain how your system processes visual information and converts it into musical elements.
   c) Detail how your architecture incorporates principles of synesthesia and cognitive science.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Visual-to-Music Translation Mechanism (250-300 words):
   a) Explain how your system translates visual elements (e.g., color, shape, texture) into musical components (e.g., pitch, rhythm, timbre).
   b) Describe any novel algorithms or techniques used in this translation process.
   c) Discuss how your system ensures musical coherence and aesthetic quality in its output.

3. Synesthesia Simulation (200-250 words):
   a) Explain how your system models the cognitive process of synesthesia.
   b) Discuss how individual differences in synesthetic experiences are accounted for in your model.
   c) Propose a method to validate the authenticity of your system's synesthetic simulations.

4. Music Theory Integration (200-250 words):
   a) Describe how your system incorporates music theory principles in its composition process.
   b) Explain how different visual inputs might result in variations in musical style or genre.
   c) Discuss any challenges in maintaining musical structure while faithfully representing the visual input.

5. Machine Learning Approach (150-200 words):
   a) Outline the machine learning techniques used in your system.
   b) Explain how your system could be trained and improved over time.
   c) Discuss potential biases in your ML approach and how you would mitigate them.

6. Cognitive Science Implications (200-250 words):
   a) Analyze how your system could contribute to our understanding of cross-modal perception.
   b) Discuss potential insights into the nature of creativity that your system might provide.
   c) Propose an experiment using your system to explore a specific question in cognitive science.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of simulating synesthetic experiences and generating AI-composed music.
   b) Explore potential applications of your system beyond music generation.
   c) Suggest future research directions stemming from your synesthetic music generator.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1450-1800 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a coherent design for an AI system that generates music based on visual input, simulating synesthesia",
            "The system architecture is well-described and incorporates principles of synesthesia and cognitive science",
            "The visual-to-music translation mechanism is clearly explained and uses innovative techniques",
            "The synesthesia simulation aspect is well-thought-out and includes a validation method",
            "Music theory principles are effectively integrated into the system's composition process",
            "The machine learning approach is appropriate and addresses potential biases",
            "The cognitive science implications are insightful and include a proposed experiment",
            "Ethical considerations are thoroughly discussed, and future research directions are suggested",
            "The response demonstrates a deep understanding of music theory, cognitive science, and machine learning",
            "The overall approach is innovative while maintaining scientific plausibility",
            "The response follows the specified format, uses clear headings for each section, and adheres to the 1450-1800 word count guideline"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
