import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'artist': 'Vincent van Gogh',
                'art_movement': 'Post-Impressionism',
                'neuroscientific_focus': 'Visual perception and emotional processing'
            },
            {
                'artist': 'Salvador Dalí',
                'art_movement': 'Surrealism',
                'neuroscientific_focus': 'Dream states and subconscious processes'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and simulates the cognitive and emotional processes of {t['artist']}, a key figure in the {t['art_movement']} movement, to generate new artworks in their style. Your system should focus on {t['neuroscientific_focus']} from a neuroscientific perspective. Your response should include:

1. Neurocognitive Analysis (250-300 words):
   a) Analyze the key cognitive and emotional processes involved in {t['artist']}'s artistic style.
   b) Explain how these processes relate to {t['neuroscientific_focus']}.
   c) Describe how you would model these processes in an AI system.

2. AI System Architecture (300-350 words):
   a) Design the architecture of your AI system, including key components and their interactions.
   b) Explain how your system incorporates neuroscientific principles related to {t['neuroscientific_focus']}.
   c) Describe how your system simulates the artistic decision-making process.
   d) Include a diagram or pseudocode snippet illustrating a key component of your system.

3. Art Historical Integration (200-250 words):
   a) Discuss how your system incorporates art historical knowledge about {t['art_movement']} and {t['artist']}'s specific techniques.
   b) Explain how this knowledge is used to guide the AI's artistic choices.
   c) Describe how your system balances historical accuracy with creative innovation.

4. Artwork Generation Process (250-300 words):
   a) Provide a step-by-step explanation of how your system would generate a new artwork in {t['artist']}'s style.
   b) Describe how the system incorporates randomness or creativity while maintaining stylistic consistency.
   c) Explain how the system evaluates and iterates on its generated artworks.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to simulate an artist's cognitive processes and generate new artworks.
   b) Address potential issues of copyright, artistic integrity, and the definition of creativity.
   c) Propose guidelines for the responsible development and use of such AI systems in the art world.

6. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the authenticity and quality of the AI-generated artworks.
   b) Describe how you would validate that your system accurately simulates {t['artist']}'s cognitive and emotional processes.
   c) Discuss the limitations of your approach and potential areas for improvement.

7. Concrete Example (200-250 words):
   Provide a detailed description of a hypothetical artwork that your AI system might generate, explaining how it reflects {t['artist']}'s style, the principles of {t['art_movement']}, and the neuroscientific focus on {t['neuroscientific_focus']}.

Ensure your response demonstrates a deep understanding of neuroscience, art history, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['artist']}'s artistic style and the {t['art_movement']} movement.",
            f"The AI system design effectively incorporates neuroscientific principles related to {t['neuroscientific_focus']}.",
            "The proposed AI architecture is technically sound and innovative.",
            "The response shows a nuanced understanding of the challenges in simulating artistic cognitive processes.",
            "The ethical considerations and limitations are thoughtfully addressed.",
            "The concrete example of a generated artwork is detailed and reflects the artist's style, art movement, and neuroscientific focus."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
