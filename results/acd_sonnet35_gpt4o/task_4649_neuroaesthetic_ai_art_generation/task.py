import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artists = [
            'Vincent van Gogh',
            'Frida Kahlo',
            'Leonardo da Vinci',
            'Wassily Kandinsky'
        ]
        cognitive_processes = [
            'Visual perception',
            'Emotional processing',
            'Spatial reasoning',
            'Symbolic abstraction'
        ]
        art_movements = [
            'Post-Impressionism',
            'Surrealism',
            'Renaissance',
            'Abstract Expressionism'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'artist': random.choice(artists),
                'cognitive_process': random.choice(cognitive_processes),
                'art_movement': random.choice(art_movements)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the cognitive and neural processes involved in artistic creation to generate and analyze art in the style of {t['artist']}, focusing on the cognitive process of {t['cognitive_process']} and the art movement of {t['art_movement']}. Your response should include the following sections:

1. Neurocognitive Model (250-300 words):
   a) Describe the key components of your AI model for the specified cognitive process in artistic creation.
   b) Explain how your model incorporates current neuroscientific understanding of this process.
   c) Discuss how your model accounts for the unique aspects of the specified artist's style and the art movement.

2. AI System Architecture (200-250 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system integrates the neurocognitive model with art generation and analysis techniques.
   c) Describe any novel algorithms or techniques your system uses for artistic style emulation.

3. Art Generation Process (200-250 words):
   a) Detail how your AI system would generate art in the style of the specified artist.
   b) Explain how the system incorporates the cognitive process and art movement characteristics in its creations.
   c) Provide an example of how a specific artwork might be conceptualized and created by your system.

4. Art Analysis Capabilities (200-250 words):
   a) Describe how your system would analyze existing artworks by the specified artist.
   b) Explain how the analysis relates to the modeled cognitive process and art movement features.
   c) Discuss how your system's analysis could provide new insights into the artist's work or the art movement.

5. Ethical and Artistic Implications (150-200 words):
   a) Discuss the ethical considerations of using AI to emulate human artists.
   b) Explore the potential impact of such systems on the art world and human creativity.
   c) Propose guidelines for responsible development and use of neuroaesthetic AI art systems.

6. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the authenticity and quality of the AI-generated art.
   b) Describe how you would measure the system's understanding of the artist's style and the art movement.
   c) Discuss the challenges in evaluating such a system and how you'd address them.

7. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or applications of your neuroaesthetic AI system.
   b) Discuss how this approach might contribute to our understanding of human creativity and artistic cognition.

Ensure your response demonstrates a deep understanding of neuroscience, AI technologies, art history, and aesthetic theory. Be creative in your approach while maintaining scientific and artistic rigor. Use appropriate terminology and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, AI, and art history, particularly in relation to {t['artist']}, {t['cognitive_process']}, and {t['art_movement']}.",
            "The proposed AI system integrates neurocognitive modeling with art generation and analysis in a novel and plausible way.",
            "The art generation and analysis processes are clearly explained and demonstrate how they incorporate the specified cognitive process and art movement characteristics.",
            "Ethical implications and evaluation methods are thoroughly discussed.",
            "The response is creative and innovative while maintaining scientific and artistic rigor.",
            "The writing is clear, well-structured, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
