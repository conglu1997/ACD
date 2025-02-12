class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neurological_states = [
            {"state": "Flow state", "characteristics": "Heightened focus, loss of self-consciousness, altered perception of time"},
            {"state": "Synesthesia", "characteristics": "Blending of senses, involuntary perceptual experiences"},
            {"state": "Lucid dreaming", "characteristics": "Awareness of dreaming, control over dream content"},
            {"state": "Meditation", "characteristics": "Reduced stress, increased awareness, altered brain waves"}
        ]
        import random
        selected_states = random.sample(neurological_states, 2)
        return {
            "1": selected_states[0],
            "2": selected_states[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music by mimicking the neural processes of human creativity and emotion, then use it to create a piece inspired by the neurological state of {t['state']}. Your response should include:

        1. Neural-AI Architecture (300-350 words):
           a) Describe the key components of your AI system and how they parallel neural processes.
           b) Explain how your system models creativity and emotion in music composition.
           c) Detail how you incorporate the characteristics of the given neurological state: {t['characteristics']}
           d) Include a diagram or flowchart of your system's architecture.

        2. Neuroscience-Music Mapping (250-300 words):
           a) Explain how specific neural processes are translated into musical elements.
           b) Describe how your system generates musical ideas based on simulated neural activity.
           c) Discuss how you maintain coherence between the neurological state and musical output.

        3. AI Composition Process (250-300 words):
           a) Provide a step-by-step explanation of how your AI composes a piece inspired by the given neurological state.
           b) Describe any machine learning algorithms or neural network architectures used.
           c) Explain how your system ensures musical quality and emotional resonance.

        4. Sample Composition (200-250 words):
           a) Describe a short musical piece (30-60 seconds) that your AI would compose for the given neurological state.
           b) Explain how specific musical elements reflect the characteristics of the neurological state.
           c) Discuss any unique or unexpected features of the composition.

        5. Evaluation and Iteration (200-250 words):
           a) Propose a method for evaluating the effectiveness of your AI's compositions in reflecting the given neurological state.
           b) Describe how you would iterate and improve your system based on feedback or evaluation results.
           c) Discuss potential challenges in validating the authenticity of the AI-generated 'neurological' music.

        6. Ethical Considerations and Future Applications (150-200 words):
           a) Discuss ethical implications of using AI to mimic human creativity and neurological states.
           b) Explore potential therapeutic or scientific applications of your system.
           c) Speculate on how this technology might evolve and impact our understanding of music and the brain.

        Ensure your response demonstrates a deep understanding of neuroscience, AI algorithms, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section. Your total response should be between 1350-1650 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI algorithms, and music theory.",
            "The neural-AI architecture is well-defined and effectively parallels neural processes.",
            "The neuroscience-music mapping is detailed and logically sound.",
            "The AI composition process is clearly explained and incorporates appropriate AI techniques.",
            "The sample composition description effectively reflects the given neurological state.",
            "The evaluation method is feasible and appropriate for assessing the AI's effectiveness.",
            "Ethical considerations are thoughtfully addressed.",
            "The overall response is well-structured, coherent, and adheres to the specified word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
