class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "historical_concept": "Ancient Egyptian hieroglyphs",
                "future_domain": "interspecies communication",
                "challenge": "overcoming language barriers between humans and non-human animals"
            },
            {
                "historical_concept": "Leonardo da Vinci's flying machines",
                "future_domain": "personal space travel",
                "challenge": "making space travel accessible and safe for the general public"
            },
            {
                "historical_concept": "Gutenberg's printing press",
                "future_domain": "information dissemination in virtual reality",
                "challenge": "ensuring equitable access to information in a VR-dominated world"
            },
            {
                "historical_concept": "Ancient Greek Antikythera mechanism",
                "future_domain": "time manipulation technology",
                "challenge": "preventing paradoxes and maintaining causality"
            }
        ]
        import random
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a futuristic technology inspired by {t['historical_concept']} for application in the domain of {t['future_domain']}, specifically addressing the challenge of {t['challenge']}. Your response should include:

        1. Historical Analysis (200-250 words):
           a) Describe the historical concept, its original purpose, and its significance.
           b) Analyze the key principles or innovations that made it noteworthy for its time.
           c) Explain how this concept influenced subsequent technological or cultural developments.

        2. Futuristic Technology Design (250-300 words):
           a) Describe your proposed futuristic technology in detail.
           b) Explain how it incorporates or evolves principles from the historical concept.
           c) Discuss the scientific or technological advancements necessary to realize this innovation.
           d) Provide a simple diagram or schematic representation of your proposed technology.

        3. Application and Impact (200-250 words):
           a) Explain how your technology addresses the specified challenge in the future domain.
           b) Provide a concrete example or scenario demonstrating the technology in use.
           c) Analyze its potential impact on society, culture, or human behavior.
           d) Discuss any challenges or obstacles to its implementation.

        4. Ethical Considerations (150-200 words):
           a) Identify potential ethical issues or concerns raised by your proposed technology.
           b) Discuss how these ethical considerations might be addressed or mitigated.
           c) Propose guidelines for the responsible development and use of this technology.

        5. Comparative Analysis (150-200 words):
           a) Compare your futuristic technology to any existing or proposed technologies in the same domain.
           b) Discuss the advantages and potential drawbacks of your approach.
           c) Explain how your design pushes the boundaries of current technological paradigms.

        Format your response using clear headings for each section. Ensure that your total response is between 950-1200 words, not including the diagram. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the historical concept and its significance.",
            "The futuristic technology design is creative, plausible, and clearly inspired by the historical concept.",
            "The proposed technology directly addresses the specified challenge in the future domain.",
            "A concrete example or scenario is provided to demonstrate the technology's application.",
            "The impact analysis is comprehensive and considers multiple aspects of society.",
            "Ethical considerations are thoughtfully explored and addressed with specific mitigation strategies.",
            "The comparative analysis shows a deep understanding of current technological paradigms and how the proposed technology advances them.",
            "The response adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
