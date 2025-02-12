class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "decision_context": "financial investment",
                "neuroimaging_technique": "real-time fMRI",
                "ai_approach": "reinforcement learning",
                "ethical_focus": "privacy and consent"
            },
            "2": {
                "decision_context": "political voting",
                "neuroimaging_technique": "EEG with source localization",
                "ai_approach": "Bayesian networks",
                "ethical_focus": "free will and manipulation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel neuroeconomic model that integrates advanced neuroimaging techniques with artificial intelligence to predict and influence human decision-making under uncertainty in the context of {t['decision_context']}. Your model should utilize {t['neuroimaging_technique']} and {t['ai_approach']}, while addressing the ethical concern of {t['ethical_focus']}. Provide your response in the following format:

        1. Neuroeconomic Model Architecture (300-350 words):
           a) Describe the overall structure of your neuroeconomic model.
           b) Explain how you integrate {t['neuroimaging_technique']} data with {t['ai_approach']}.
           c) Detail the key components and their interactions within your model.
           d) Discuss any novel algorithms or approaches you've developed for this system.

        2. Decision-Making Prediction and Influence (250-300 words):
           a) Explain how your model predicts human decision-making in {t['decision_context']} scenarios.
           b) Describe the specific neural markers or patterns your model uses for prediction.
           c) Detail how your model could potentially influence decision-making processes.
           d) Provide an example scenario demonstrating your model's predictive and influential capabilities.

        3. Implementation and Data Processing (200-250 words):
           a) Outline the data acquisition and preprocessing steps for {t['neuroimaging_technique']}.
           b) Explain how your AI system processes and interprets the neuroimaging data.
           c) Describe any real-time analysis or feedback mechanisms in your model.
           d) Discuss how you handle individual variability in neural responses and decision-making.

        4. Model Validation and Performance Metrics (200-250 words):
           a) Propose a method to validate the accuracy of your model's predictions.
           b) Suggest performance metrics specific to neuroeconomic decision-making models.
           c) Describe how you would conduct experiments to test your model's effectiveness.
           d) Discuss potential limitations of your approach and how they might be addressed.

        5. Ethical Considerations and Safeguards (200-250 words):
           a) Analyze the ethical implications of using your model, focusing on {t['ethical_focus']}.
           b) Discuss potential misuse scenarios and propose safeguards against them.
           c) Suggest guidelines for the responsible development and use of neuroeconomic AI models.
           d) Explore the broader societal impacts of applying such technologies in {t['decision_context']}.

        6. Future Applications and Research Directions (150-200 words):
           a) Propose two potential applications of your model beyond {t['decision_context']}.
           b) Suggest areas for future research to enhance the capabilities of your neuroeconomic model.
           c) Discuss how advancements in neuroimaging or AI might impact the future of neuroeconomics.

        Ensure your response demonstrates a deep understanding of neuroscience, economics, artificial intelligence, and ethical reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section. Your total response should be between 1300-1600 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and adheres to the specified word counts.",
            "The neuroeconomic model architecture is well-described and integrates the specified neuroimaging technique and AI approach.",
            "The decision-making prediction and influence section provides a clear explanation of how the model works in the given context.",
            "The implementation and data processing section adequately addresses the challenges of working with neuroimaging data.",
            "The model validation and performance metrics section proposes plausible methods for testing the model's effectiveness.",
            f"The ethical considerations section thoroughly addresses the specified focus of {t['ethical_focus']}.",
            "The future applications and research directions section provides innovative yet plausible suggestions.",
            "The overall response demonstrates a deep understanding of neuroscience, economics, AI, and ethical reasoning, using appropriate technical terminology.",
            "The proposed model is innovative while maintaining scientific plausibility.",
            "The response stays within the overall word limit of 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
