import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neural_processes = [
            "Synaptic plasticity",
            "Neural oscillations",
            "Predictive coding",
            "Emotional processing",
            "Auditory scene analysis"
        ]
        musical_elements = [
            "Harmony",
            "Rhythm",
            "Melody",
            "Timbre",
            "Form"
        ]
        genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "Folk",
            "Avant-garde"
        ]
        
        tasks = {}
        for i in range(2):
            process = random.choice(neural_processes)
            element = random.choice(musical_elements)
            genre = random.choice(genres)
            tasks[str(i+1)] = {
                "neural_process": process,
                "musical_element": element,
                "genre": genre
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music by simulating and integrating the neurological process of {t['neural_process']}, focusing on the musical element of {t['musical_element']}, and applying it to the {t['genre']} genre. Your response should include:

1. Neuroscientific Foundation (200-250 words):
   a) Explain the chosen neurological process and its role in musical creativity or perception.
   b) Describe how this process relates to the specified musical element.
   c) Discuss current scientific understanding and any relevant research in this area.

2. AI System Architecture (250-300 words):
   a) Outline the main components of your AI system for music composition.
   b) Explain how your system models and integrates the specified neurological process.
   c) Describe how your system generates or manipulates the chosen musical element.
   d) Discuss any novel algorithms or techniques used in your AI model.

3. Musical Implementation (200-250 words):
   a) Explain how your AI system applies the neurological process to create music in the specified genre.
   b) Provide a specific example of how a musical piece would be composed, focusing on the chosen element.
   c) Describe how your system ensures the output adheres to the conventions of the given genre.

4. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the musicality and creativity of your AI system's compositions.
   b) Describe how you would validate the system's ability to simulate the specified neurological process.
   c) Discuss potential limitations of your approach and how they might be addressed.

5. Interdisciplinary Insights (150-200 words):
   a) Analyze how your system could provide insights into both neuroscience and musicology.
   b) Discuss potential applications of your system in music therapy or neuroscience research.
   c) Explore how this integration of AI, neuroscience, and music could impact our understanding of creativity.

6. Ethical Considerations (100-150 words):
   a) Discuss ethical implications of using AI to simulate human cognitive processes for creative tasks.
   b) Address potential impacts on human musicians and the music industry.
   c) Propose guidelines for responsible development and use of such AI systems in creative fields.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and musical authenticity.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified neurological process and its relation to music",
            "The AI system design effectively integrates neuroscientific principles with music composition techniques",
            "The musical implementation is creative and aligns with the given genre while focusing on the specified element",
            "The evaluation methods proposed are comprehensive and address both scientific and artistic aspects",
            "The discussion of interdisciplinary insights shows depth and originality",
            "Ethical considerations are thoughtfully addressed",
            "The response shows creativity and innovation while maintaining scientific and musical plausibility",
            "The response is properly formatted with clear headings for each section",
            "The total word count is between 1050-1350 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
