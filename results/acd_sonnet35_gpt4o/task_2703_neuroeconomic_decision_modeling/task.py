import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "type": "Intertemporal Choice",
                "description": "Deciding between immediate smaller rewards and delayed larger rewards",
                "brain_regions": ["prefrontal cortex", "striatum", "hippocampus"],
                "economic_factors": ["discount rate", "risk aversion", "opportunity cost"],
                "additional_constraint": "Include a mechanism to model the impact of stress on decision-making"
            },
            {
                "type": "Social Decision-Making",
                "description": "Making economic decisions in a social context, such as in a trust game or ultimatum game",
                "brain_regions": ["anterior cingulate cortex", "insula", "temporoparietal junction"],
                "economic_factors": ["fairness perception", "reciprocity", "social norms"],
                "additional_constraint": "Incorporate a mechanism to simulate the influence of cultural background on decision-making"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design two distinct computational models that simulate human decision-making processes in the context of {t['type']}. Both models should integrate principles from neuroscience, behavioral economics, and cognitive psychology, but should differ significantly in their approach or underlying assumptions. Focus on the scenario: {t['description']}. Note that this task is speculative and may go beyond current technological capabilities, testing your theoretical knowledge and creative problem-solving skills. You have 60 minutes to complete this task.\n\nYour response should include:\n\n1. Model Architectures (400-450 words, 200-225 per model):\n   a) Describe the key components of each computational model.\n   b) Explain how each model incorporates neuroscientific principles, particularly regarding the roles of {', '.join(t['brain_regions'])}.\n   c) Detail how economic factors such as {', '.join(t['economic_factors'])} are represented and processed in each model.\n   d) Include a simple diagram of each model's architecture using ASCII art or Unicode characters.\n   e) For each model, address: {t['additional_constraint']}\n\n2. Neural Basis (300-350 words, 150-175 per model):\n   a) Explain how each model simulates the neural processes involved in this type of decision-making.\n   b) Describe how you model the interactions between the relevant brain regions in each approach.\n   c) Discuss how each model accounts for individual differences in neural activity and connectivity.\n\n3. Economic Behavior Simulation (300-350 words, 150-175 per model):\n   a) Detail how each model simulates economic behavior in the given scenario.\n   b) Explain how you incorporate behavioral economics principles into each model.\n   c) Describe how each model handles the specified economic factors.\n\n4. Cognitive Processes (250-300 words, 125-150 per model):\n   a) Explain how each model simulates cognitive processes such as attention, memory, and learning in this decision-making context.\n   b) Discuss how these cognitive processes interact with neural and economic components in each model.\n\n5. Model Validation (250-300 words):\n   a) Propose methods to validate both models against empirical data from neuroscience and behavioral economics.\n   b) Describe potential experiments or data sources that could be used to test each model's predictions.\n   c) Discuss the limitations of each model and potential areas for improvement.\n\n6. Practical Applications (200-250 words):\n   a) Suggest two potential real-world applications for each model in fields such as public policy, marketing, or clinical psychology.\n   b) Explain how each model could provide unique insights or inform different strategies in these areas.\n\n7. Ethical Considerations (200-250 words):\n   a) Discuss the ethical implications of using such models to predict or influence human economic decision-making.\n   b) Propose guidelines for the responsible development and use of neuroeconomic models, considering the unique aspects of each model.\n\n8. Comparative Analysis (300-350 words):\n   a) Compare and contrast the two models, highlighting their respective strengths and weaknesses.\n   b) Analyze how the differences in approach affect each model's predictions and potential applications.\n   c) Discuss which model might be more suitable for different types of research questions or practical applications.\n   d) Propose a potential hybrid approach that combines the strengths of both models, if applicable.\n\nEnsure your response demonstrates a deep understanding of neuroscience, behavioral economics, and cognitive psychology. Be innovative in your approaches while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 2200-2600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, behavioral economics, and cognitive psychology.",
            "Two distinct model architectures are well-designed and incorporate principles from all relevant disciplines.",
            "The neural basis of decision-making is accurately represented and explained for both models.",
            "The simulation of economic behavior and cognitive processes is comprehensive and plausible in both models.",
            "The model validation methods are rigorous and well-thought-out for both approaches.",
            "Practical applications are relevant and demonstrate each model's potential impact.",
            "Ethical considerations are thoroughly discussed with insightful guidelines proposed for both models.",
            "The response includes clear and informative diagrams of both model architectures.",
            "The overall response is creative, scientifically plausible, and well-structured.",
            f"Both models accurately incorporate the specified brain regions: {', '.join(t['brain_regions'])}.",
            f"The economic factors {', '.join(t['economic_factors'])} are well-integrated into both models.",
            f"The additional constraint '{t['additional_constraint']}' is effectively addressed in both models.",
            "The comparative analysis demonstrates thoughtful reflection on the models' strengths, weaknesses, and potential applications.",
            "The proposed hybrid approach, if applicable, shows innovative thinking in combining the strengths of both models."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
