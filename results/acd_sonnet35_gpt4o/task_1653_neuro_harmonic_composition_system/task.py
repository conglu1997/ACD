import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "Harmony",
            "Rhythm",
            "Melody",
            "Timbre"
        ]
        neural_mechanisms = [
            "Predictive coding",
            "Oscillatory synchronization",
            "Reward prediction error",
            "Auditory scene analysis"
        ]
        ml_techniques = [
            "Recurrent Neural Networks",
            "Transformer models",
            "Generative Adversarial Networks",
            "Reinforcement Learning"
        ]
        musical_genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "World Music"
        ]
        musical_concepts = [
            "Polyrhythms",
            "Modulation",
            "Counterpoint",
            "Microtonal intervals"
        ]
        
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "neural_mechanism": random.choice(neural_mechanisms),
                "ml_technique": random.choice(ml_techniques),
                "musical_genre": random.choice(musical_genres),
                "musical_concept": random.choice(musical_concepts)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "neural_mechanism": random.choice(neural_mechanisms),
                "ml_technique": random.choice(ml_techniques),
                "musical_genre": random.choice(musical_genres),
                "musical_concept": random.choice(musical_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a neural network-based system that composes and analyzes music by integrating principles from neuroscience, machine learning, and music theory. Your system should focus on the musical element of {t['musical_element']}, incorporate the neural mechanism of {t['neural_mechanism']}, utilize the machine learning technique of {t['ml_technique']}, be applied to the musical genre of {t['musical_genre']}, and demonstrate understanding of the musical concept of {t['musical_concept']}. Your response should include the following sections:\n\n1. System Architecture (275-325 words):\n   a) Describe the key components of your neuro-harmonic composition system. (60-80 words)\n   b) Explain how it integrates neuroscientific principles, machine learning techniques, and music theory. (60-80 words)\n   c) Discuss how it models the brain's response to {t['musical_element']}. (50-70 words)\n   d) Explain how it incorporates the neural mechanism of {t['neural_mechanism']}. (50-70 words)\n   e) Detail how the {t['ml_technique']} is implemented in your system. (50-70 words)\n\n2. Musical Analysis and Generation (225-275 words):\n   a) Describe how your system analyzes existing music in the {t['musical_genre']} genre. (50-70 words)\n   b) Explain the process by which it generates new musical compositions. (60-80 words)\n   c) Discuss how it captures and reproduces the stylistic elements of {t['musical_genre']}. (50-70 words)\n   d) Provide an example of how your system would analyze or generate a specific musical passage incorporating {t['musical_concept']}. (60-80 words)\n\n3. Neuroscientific Basis (225-275 words):\n   a) Explain the neuroscientific theories or findings that inform your system's design. (60-80 words)\n   b) Discuss how your system models or simulates relevant brain processes. (50-70 words)\n   c) Describe how the incorporation of {t['neural_mechanism']} enhances your system's capabilities. (50-70 words)\n   d) Propose a testable hypothesis about brain function that your system could help investigate. (60-80 words)\n\n4. Machine Learning Implementation (225-275 words):\n   a) Provide a detailed explanation of how {t['ml_technique']} is used in your system. (60-80 words)\n   b) Discuss the advantages and limitations of this technique for music composition and analysis. (60-80 words)\n   c) Explain how you would train and validate your model, including specific datasets or methods you would use. (50-70 words)\n   d) Describe any novel adaptations or innovations you've made to the {t['ml_technique']} for this specific application. (50-70 words)\n\n5. Evaluation and Applications (200-250 words):\n   a) Propose specific methods for evaluating the quality and creativity of your system's musical output, including quantitative metrics and qualitative assessments. (60-80 words)\n   b) Discuss potential applications of your system in music education, therapy, or creative industries, providing concrete examples. (50-70 words)\n   c) Analyze ethical considerations related to AI-generated music and creativity, including issues of authorship and cultural appropriation. (50-70 words)\n   d) Suggest future research directions or extensions of your system, including potential interdisciplinary collaborations. (50-70 words)\n\nEnsure your response demonstrates a deep understanding of neuroscience, machine learning, and music theory. Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1150-1400 words. Include at least one diagram or pseudocode snippet to illustrate a key aspect of your system.\n\nCite at least 5 relevant scientific papers or resources throughout your response to support your design choices and theoretical foundations."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, machine learning, and music theory principles, with accurate use of technical terminology.",
            "The system architecture is innovative, plausible, and well-explained, integrating all required elements (musical element, neural mechanism, ML technique, musical genre, and musical concept).",
            "The musical analysis and generation process is clearly described, appropriate for the specified genre, and incorporates the given musical concept.",
            "The neuroscientific basis is well-founded, and the proposed hypothesis is relevant, specific, and testable.",
            "The machine learning implementation is thoroughly explained, with clear details on training, validation, and any novel adaptations.",
            "The evaluation methods are specific and comprehensive, including both quantitative and qualitative approaches.",
            "The response addresses all required sections coherently, includes at least one diagram or pseudocode snippet, and falls within the specified word count for each section and subsection.",
            "The ethical considerations and future research directions are thoughtfully discussed with concrete examples and interdisciplinary perspectives.",
            "At least 5 relevant scientific papers or resources are cited throughout the response to support design choices and theoretical foundations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
