import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "Auditory cortex",
            "Prefrontal cortex",
            "Hippocampus",
            "Amygdala",
            "Cerebellum"
        ]
        
        musical_elements = [
            "Melody",
            "Harmony",
            "Rhythm",
            "Timbre",
            "Dynamics"
        ]
        
        cognitive_processes = [
            "Emotional processing",
            "Memory formation",
            "Attention",
            "Decision making",
            "Spatial reasoning"
        ]
        
        musical_genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "Folk",
            "World music"
        ]
        
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_genre": random.choice(musical_genres)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that synthesizes music based on neural activity patterns, exploring the relationship between brain function and musical composition. Your system should focus on the {t['brain_region']}, emphasize the musical element of {t['musical_element']}, incorporate the cognitive process of {t['cognitive_process']}, and be capable of generating music in the style of {t['musical_genre']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your neural music synthesis AI system.
   b) Explain how your system integrates neuroscientific data, music theory, and AI algorithms.
   c) Detail how your system specifically incorporates the {t['brain_region']} and {t['cognitive_process']}.
   d) Include a diagram or flowchart of your system's architecture (describe it textually).

2. Neural-Musical Mapping (250-300 words):
   a) Explain how your system translates neural activity patterns into musical elements, focusing on {t['musical_element']}.
   b) Describe the algorithms or methods used to convert brain signals into musical parameters.
   c) Discuss how your approach maintains musical coherence and aesthetics while reflecting neural patterns.

3. Cognitive Process Integration (200-250 words):
   a) Detail how your system incorporates {t['cognitive_process']} into the music generation process.
   b) Explain how this cognitive process influences the musical output.
   c) Discuss any challenges in mapping this cognitive process to musical elements and how you address them.

4. Genre Adaptation (200-250 words):
   a) Describe how your system adapts to generate music in the style of {t['musical_genre']}.
   b) Explain any specific techniques or models used to capture the essence of this genre.
   c) Discuss how your system balances genre-specific characteristics with neural-based composition.

5. Training and Data Requirements (150-200 words):
   a) Outline the types of data needed to train your system (e.g., neural recordings, musical corpora).
   b) Describe the training process for your AI system.
   c) Discuss any ethical considerations in data collection and usage.

6. Potential Applications and Implications (200-250 words):
   a) Propose potential applications of your system in neuroscience, music therapy, or artistic expression.
   b) Discuss how this technology might advance our understanding of the relationship between brain function and music.
   c) Consider any ethical implications or potential misuse of this technology.

7. Evaluation and Future Directions (150-200 words):
   a) Suggest methods for evaluating the quality and neural-fidelity of the generated music.
   b) Propose an experiment to validate your system's effectiveness in capturing brain-music relationships.
   c) Discuss potential future enhancements or extensions of your system.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, music theory, and artificial intelligence.",
            "The proposed system effectively integrates the specified brain region, musical element, cognitive process, and musical genre.",
            "The neural-musical mapping and cognitive process integration are well-explained and scientifically plausible.",
            "The system architecture is innovative, coherent, and addresses the complexities of translating neural patterns into music.",
            "Potential applications, implications, and future directions are thoughtfully explored.",
            "The overall response is well-structured, coherent, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
