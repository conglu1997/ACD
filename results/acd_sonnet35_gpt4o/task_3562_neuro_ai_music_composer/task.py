import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        music_styles = [
            {"style": "Jazz", "feature": "Improvisation"},
            {"style": "Classical", "feature": "Counterpoint"},
            {"style": "Electronic", "feature": "Sound synthesis"},
            {"style": "World Music", "feature": "Microtonal scales"}
        ]
        return {str(i+1): style for i, style in enumerate(random.sample(music_styles, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system that uses neural signals and AI to compose music in the style of {t['style']}, with a focus on the musical feature of {t['feature']}. Then, analyze its potential impact on creativity and music theory. Your response should include:

1. BCI System Architecture (250-300 words):
   a) Describe the key components of your BCI system for music composition.
   b) Explain how it captures and interprets relevant neural signals.
   c) Detail how the AI component processes these signals and translates them into musical elements.
   d) Discuss how the system specifically addresses the {t['style']} style and the feature of {t['feature']}.

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your BCI design.
   b) Discuss which brain regions or neural processes are targeted for music composition.
   c) Address how your system might adapt to individual differences in neural patterns.

3. AI and Music Theory Integration (200-250 words):
   a) Describe the AI architecture used for music generation.
   b) Explain how music theory principles, especially those relevant to {t['style']} and {t['feature']}, are incorporated into the AI system.
   c) Discuss any novel algorithms or approaches necessary for this integration.

4. Creative Process Analysis (200-250 words):
   a) Analyze how this BCI system might alter the creative process of music composition.
   b) Discuss potential benefits and drawbacks compared to traditional composition methods.
   c) Explore how the system might influence or challenge current understanding of musical creativity.

5. Music Theory Implications (200-250 words):
   a) Discuss how your BCI system might impact or evolve music theory, especially in relation to {t['style']} and {t['feature']}.
   b) Propose new theoretical frameworks or concepts that might arise from this technology.
   c) Speculate on how this technology could influence future musical styles or techniques.

6. Ethical Considerations (150-200 words):
   a) Identify and discuss at least two ethical concerns raised by your BCI music composition system.
   b) Propose guidelines for the responsible development and use of such technology.
   c) Discuss potential impacts on the music industry and professional composers.

7. Future Research Directions (100-150 words):
   a) Propose two potential extensions or applications of your BCI music composition system.
   b) Suggest experiments that could validate or explore the effects of your system on creativity and musical cognition.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all 7 required sections for the {t['style']} style and {t['feature']} feature",
            "The BCI system architecture should integrate neuroscience, AI, and music theory principles",
            "The neuroscientific basis should be well-justified and relevant to music composition",
            "The AI and music theory integration should be innovative and well-explained",
            "The creative process and music theory implications should be thoughtfully analyzed",
            "Ethical considerations and future research directions should be thoroughly addressed",
            "The response should demonstrate interdisciplinary knowledge and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
