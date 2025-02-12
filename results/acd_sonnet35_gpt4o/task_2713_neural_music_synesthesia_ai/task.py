import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "prefrontal cortex",
            "auditory cortex",
            "visual cortex",
            "hippocampus"
        ]
        music_styles = [
            "Classical",
            "Jazz",
            "Electronic",
            "World Music"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "music_style": random.choice(music_styles)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "music_style": random.choice(music_styles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates neural activity patterns from the {t['brain_region']} into musical compositions in the style of {t['music_style']}, simulating a form of artificial synesthesia. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for neural-to-music translation.
   b) Explain how your system integrates neuroscientific data with music generation algorithms.
   c) Detail how you incorporate the specific characteristics of the {t['brain_region']} in your design.
   d) Discuss any novel computational or representational elements in your approach.

2. Neural-Music Mapping (200-250 words):
   a) Explain your approach to mapping neural activity patterns to musical elements.
   b) Describe how you ensure the generated music adheres to the principles of {t['music_style']}.
   c) Discuss challenges in translating complex neural data into coherent musical structures and how you address them.

3. Music Theory Integration (200-250 words):
   a) Analyze how your system's output relates to traditional music theory concepts.
   b) Propose a new music theory concept or principle that emerges from this neural-music integration.
   c) Discuss how this approach might influence our understanding of music cognition and creativity.

4. Neuroscientific Implications (200-250 words):
   a) Discuss how your model might provide insights into the functioning of the {t['brain_region']}.
   b) Propose an experiment to test a hypothesis about brain-music relationships using your system.
   c) Explain potential implications for understanding synesthesia and cross-modal perception.

5. Evaluation and Analysis (150-200 words):
   a) Propose methods to evaluate the quality and neurological fidelity of the generated music.
   b) Describe how you would validate the system's representation of {t['brain_region']} activity.
   c) Discuss potential applications of this technology in neuroscience or music therapy.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of translating neural activity into music, particularly regarding privacy and cognitive liberty.
   b) Propose two future research directions that could further develop the integration of neuroscience and music through AI.
   c) Speculate on how this technology might influence the future of music composition and performance.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and AI principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, music theory, and AI principles.",
            f"The system architecture effectively integrates neural activity from the {t['brain_region']} with music generation in the style of {t['music_style']}.",
            "The neural-music mapping approach is well-explained and addresses challenges in translating neural data to music.",
            "The response provides insightful analysis of music theory implications and proposes novel concepts.",
            "The discussion of neuroscientific implications is thorough and includes a well-designed experimental proposal.",
            "Evaluation methods for both musical quality and neurological fidelity are clearly described.",
            "Ethical considerations are thoughtfully addressed, and future research directions are innovative and relevant.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
