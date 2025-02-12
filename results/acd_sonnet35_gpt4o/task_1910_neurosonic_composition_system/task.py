import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "music_genre": "Classical",
                "brain_region": "Auditory cortex",
                "AI_technique": "Recurrent Neural Networks"
            },
            {
                "music_genre": "Jazz",
                "brain_region": "Prefrontal cortex",
                "AI_technique": "Generative Adversarial Networks"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates brain activity during music listening into a novel musical composition, focusing on the {t['music_genre']} genre, the {t['brain_region']}, and using {t['AI_technique']} as the primary AI technique. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your neurosonic composition system.
   b) Explain how brain activity is captured and processed.
   c) Detail how musical features are extracted and translated.
   d) Discuss how the AI component generates new compositions.

2. Neuroscientific Basis (200-250 words):
   a) Explain the role of the {t['brain_region']} in music perception and processing.
   b) Discuss how your system interprets neural activity in this region.
   c) Address potential challenges in accurately mapping brain activity to musical elements.

3. Music Theory Integration (200-250 words):
   a) Describe how your system incorporates music theory principles specific to {t['music_genre']}.
   b) Explain how these principles guide the composition process.
   c) Discuss how your system ensures musical coherence and aesthetic quality.

4. AI Implementation (200-250 words):
   a) Explain how {t['AI_technique']} are used in your system.
   b) Describe the training process for your AI model.
   c) Discuss any novel approaches in applying this AI technique to music composition.

5. Composition Process (150-200 words):
   a) Provide a step-by-step explanation of how your system would create a new composition.
   b) Include an example of how a specific neural pattern might be translated into a musical element.

6. Ethical and Practical Considerations (150-200 words):
   a) Discuss potential ethical implications of translating brain activity into music.
   b) Address privacy concerns and propose guidelines for responsible use.
   c) Explore potential applications in fields such as music therapy or brain-computer interfaces.

7. Evaluation and Future Directions (100-150 words):
   a) Propose methods for evaluating the quality and uniqueness of the generated compositions.
   b) Suggest potential improvements or extensions to your system.
   c) Discuss how this technology might impact the future of music creation and neuroscience research.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content",
            "The system design demonstrates integration of neuroscience, music theory, and artificial intelligence",
            f"The system focuses on the {t['music_genre']} genre and the {t['brain_region']}",
            f"The AI implementation properly utilizes {t['AI_technique']}",
            "The response is creative while maintaining scientific and technological plausibility",
            "The ethical considerations and limitations are thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
