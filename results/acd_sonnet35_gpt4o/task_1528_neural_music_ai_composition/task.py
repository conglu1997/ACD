class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "brain_region": "prefrontal cortex",
                "musical_style": "jazz",
                "cognitive_state": "problem-solving",
                "neural_pattern": "increased gamma oscillations (30-100 Hz)"
            },
            "2": {
                "brain_region": "amygdala",
                "musical_style": "classical",
                "cognitive_state": "emotional processing",
                "neural_pattern": "heightened theta activity (4-8 Hz)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on real-time neural activity data from the {t['brain_region']}, focusing on the {t['musical_style']} style and the cognitive state of {t['cognitive_state']}. The system should specifically respond to {t['neural_pattern']}. Then, analyze its output and propose experiments to test its effectiveness. Your response should include:

        1. System Architecture (250-300 words):
           a) Describe the key components of your AI system for neural music composition.
           b) Explain how it processes neural activity data and translates it into musical elements.
           c) Detail how the system incorporates the specified musical style and cognitive state.
           d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters.

        2. Neural-Musical Mapping (200-250 words):
           a) Explain how {t['neural_pattern']} from the {t['brain_region']} are mapped to specific musical elements.
           b) Describe how the system captures and represents the cognitive state of {t['cognitive_state']}.
           c) Discuss any novel approaches to neural-musical translation in your design.

        3. AI Composition Process (200-250 words):
           a) Detail how your AI system generates {t['musical_style']} compositions.
           b) Explain how it maintains musical coherence while responding to changing neural inputs.
           c) Discuss how the system balances creativity and adherence to musical style conventions.

        4. Output Analysis (150-200 words):
           a) Describe the expected characteristics of the music produced by your system.
           b) Explain how the output reflects both the neural activity and the specified cognitive state.
           c) Discuss potential insights into brain function or music cognition that could be gained from this system.

        5. Experimental Design (200-250 words):
           a) Propose an experiment to test the effectiveness of your neural music AI system.
           b) Describe the methodology, including participant selection, data collection, and analysis techniques.
           c) Explain how you would measure both the musical quality and the neural-cognitive representation accuracy.

        6. Ethical Considerations (100-150 words):
           a) Discuss potential ethical implications of using neural data for music composition.
           b) Address privacy concerns and potential misuse of brain-computer interfaces.
           c) Propose guidelines for responsible development and use of such systems.

        7. Future Directions (100-150 words):
           a) Suggest two potential improvements or extensions to your system.
           b) Propose a research question that could further explore the relationship between neural activity, cognitive states, and music composition.

        Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

        Format your answer with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words. Stay within the specified word count for each section.

        For the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and adheres to the specified word counts.",
            "The system architecture is well-described and includes a clear ASCII art or Unicode diagram (max 20 lines by 80 characters).",
            f"The neural-musical mapping demonstrates a plausible connection between {t['neural_pattern']} in the {t['brain_region']} and specific musical elements.",
            f"The AI composition process is thoroughly explained and considers both creativity and adherence to {t['musical_style']} conventions.",
            f"The output analysis provides insightful predictions about the system's musical output in relation to {t['cognitive_state']}.",
            "The experimental design is well-thought-out and addresses both musical quality and neural-cognitive representation accuracy.",
            "Ethical considerations are thoroughly discussed with appropriate guidelines proposed for responsible development and use.",
            "Future directions are creative, relevant, and clearly advance the field of neural music AI composition.",
            "The overall response shows deep understanding and integration of neuroscience, music theory, and AI concepts, using appropriate technical terminology.",
            "The response stays within the overall word limit of 1200-1550 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
