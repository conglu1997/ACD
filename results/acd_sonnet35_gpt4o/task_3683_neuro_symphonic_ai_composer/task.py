import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                'region': 'Prefrontal Cortex',
                'function': 'Executive function and decision-making',
                'musical_element': 'Melody and harmonic progression'
            },
            {
                'region': 'Temporal Lobe',
                'function': 'Auditory processing and memory',
                'musical_element': 'Rhythm and tempo'
            }
        ]
        return {str(i+1): region for i, region in enumerate(random.sample(brain_regions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on real-time brain activity, focusing on the {t['region']} and its associated function of {t['function']}. Your system should translate neural patterns from this region into the musical element of {t['musical_element']}. Your response should include:

1. Neuroscience Foundation (250-300 words):
   a) Explain the role of the {t['region']} in brain function and how it relates to {t['function']}.
   b) Describe the typical neural patterns or signals associated with this brain region.
   c) Discuss how these patterns might be influenced by different cognitive or emotional states.
   d) Explain potential challenges in accurately measuring and interpreting signals from this region.

2. Signal Processing and Musical Translation (300-350 words):
   a) Propose a method for capturing and processing neural signals from the {t['region']} in real-time.
   b) Describe how you would translate these processed signals into {t['musical_element']}.
   c) Explain how your system ensures that the generated musical elements adhere to basic music theory principles.
   d) Discuss any novel algorithms or techniques you're using in this translation process.
   e) Include a simple diagram or flowchart illustrating the signal processing and translation pipeline.

3. AI Composition System (250-300 words):
   a) Describe the architecture of your AI system, including its main components and their interactions.
   b) Explain how your system integrates the translated neural signals with other musical elements to create a coherent composition.
   c) Discuss how your AI handles musical structure, development, and overall coherence.
   d) Describe any machine learning techniques or models used in your system.

4. Artistic and Scientific Implications (200-250 words):
   a) Analyze the potential artistic value of music composed by your neuro-symphonic AI system.
   b) Discuss how this technology might advance our understanding of the relationship between brain activity and musical creativity.
   c) Explore potential applications of this technology in fields such as music therapy or brain-computer interfaces.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues related to using brain activity for artistic creation.
   b) Address privacy concerns and propose guidelines for the responsible use of this technology.
   c) Consider potential psychological effects on users of this neuro-symphonic composition system.

6. Future Developments (150-200 words):
   a) Propose two potential enhancements or extensions to your neuro-symphonic AI composer.
   b) Suggest an experiment to further explore the relationship between {t['function']} and {t['musical_element']}.
   c) Speculate on how this technology might influence the future of music composition and performance.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified brain region and its function.",
            "The signal processing and musical translation method is well-explained and scientifically plausible.",
            "The AI composition system is innovative and coherently integrates neural signals with musical elements.",
            "The artistic and scientific implications are thoughtfully analyzed.",
            "Ethical considerations are thoroughly addressed.",
            "Future developments and experiments are creative and relevant.",
            "The overall response shows a strong integration of neuroscience, music theory, and AI concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
