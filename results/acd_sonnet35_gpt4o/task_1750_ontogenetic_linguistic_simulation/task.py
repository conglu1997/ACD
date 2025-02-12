class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "linguistic_feature": "syntax",
                "cognitive_constraint": "working memory limitations",
                "environmental_factor": "multilingual exposure"
            },
            {
                "linguistic_feature": "phonology",
                "cognitive_constraint": "attention span",
                "environmental_factor": "socioeconomic status"
            }
        ]
        return {
            "1": scenarios[0],
            "2": scenarios[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulated environment for language acquisition and development, focusing on the acquisition of {t['linguistic_feature']}. Your simulation should incorporate the cognitive constraint of {t['cognitive_constraint']} and consider the environmental factor of {t['environmental_factor']}. Provide your response in the following format:

        1. Simulation Design (300-350 words):
           a) Describe the key components of your simulated environment.
           b) Explain how your simulation models the acquisition of {t['linguistic_feature']}.
           c) Detail how you incorporate {t['cognitive_constraint']} into the learning agents.
           d) Discuss how {t['environmental_factor']} is represented and influences the simulation.

        2. Theoretical Framework (200-250 words):
           a) Explain the linguistic and cognitive theories that inform your simulation design.
           b) Discuss how your simulation integrates insights from developmental psychology and neuroscience.
           c) Justify your choices in terms of current research in language acquisition.

        3. Implementation Details (200-250 words):
           a) Outline the key algorithms or computational models used in your simulation.
           b) Explain how you represent and process linguistic input and output.
           c) Describe how learning and development are measured and tracked in your simulation.

        4. Experimental Setup (150-200 words):
           a) Propose an experiment using your simulation to test a specific hypothesis about language acquisition.
           b) Describe the variables, controls, and expected outcomes of your experiment.
           c) Explain how you would validate the results of your simulation against real-world data.

        5. Limitations and Future Directions (150-200 words):
           a) Discuss potential limitations of your simulation and how they might affect its validity.
           b) Propose at least two extensions or improvements to your simulation for future research.
           c) Suggest how insights from your simulation could inform real-world language teaching or AI development.

        Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section. Your total response should be between 1000-1250 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The simulation design is comprehensive and incorporates the specified linguistic feature, cognitive constraint, and environmental factor.",
            "The theoretical framework is well-grounded in current research and integrates insights from multiple disciplines.",
            "The implementation details are clear and demonstrate a good understanding of computational modeling of language acquisition.",
            "The proposed experiment is well-designed and relevant to testing hypotheses about language acquisition.",
            "Limitations are thoughtfully addressed, and future directions are insightful and relevant.",
            "The response is creative while maintaining scientific plausibility.",
            "The writing is clear, well-structured, and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
