import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scaffolding_scenarios = [
            {
                "domain": "Second language acquisition",
                "target_skill": "Complex grammar structures",
                "learner_type": "Adult human learner",
                "constraints": ["Limited study time", "No immersion environment"]
            },
            {
                "domain": "Artificial general intelligence",
                "target_skill": "Analogical reasoning",
                "learner_type": "AI system",
                "constraints": ["Limited training data", "Real-time processing requirements"]
            },
            {
                "domain": "Cross-cultural communication",
                "target_skill": "Non-verbal cue interpretation",
                "learner_type": "Human-AI collaborative team",
                "constraints": ["Cultural diversity", "Remote interaction", "Real-time adaptation"]
            }
        ]
        return {
            "1": random.choice(scaffolding_scenarios),
            "2": random.choice(scaffolding_scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"Design a computational model of cognitive scaffolding for {t['domain']}, focusing on the acquisition of {t['target_skill']} by a {t['learner_type']}. Your model should address the following constraints: {', '.join(t['constraints'])}."

        instructions += "\n\nCognitive scaffolding refers to the process of providing temporary support to learners as they develop new skills or understanding, gradually removing this support as the learner becomes more proficient."

        instructions += "\n\nYour response should include:"
        instructions += "\n1. Model Architecture (300-350 words):"
        instructions += "\n   - Describe the key components of your cognitive scaffolding model."
        instructions += "\n   - Explain how your model simulates the scaffolding process."
        instructions += "\n   - Provide a high-level diagram or flowchart of your model (describe it textually)."
        instructions += "\n   - Include a brief pseudocode snippet (10-15 lines) illustrating a core function of your model."
        instructions += "\n   - Discuss potential failure modes of your model and propose mitigation strategies."

        instructions += "\n\n2. Scaffolding Strategies (250-300 words):"
        instructions += "\n   - Detail specific scaffolding strategies employed by your model."
        instructions += "\n   - Explain how these strategies are adapted to the given domain and learner type."
        instructions += "\n   - Discuss how your model addresses the specified constraints."
        instructions += "\n   - Describe how your model would adapt to different scenarios (e.g., language acquisition vs. AI reasoning)."

        instructions += "\n\n3. Learning Process Simulation (250-300 words):"
        instructions += "\n   - Describe how your model simulates the learning process over time."
        instructions += "\n   - Explain how scaffolding is gradually removed as competence increases."
        instructions += "\n   - Provide a hypothetical learning curve or progression, explaining key stages."
        instructions += "\n   - Compare your model's performance across different scenarios, highlighting adaptations."

        instructions += "\n\n4. Comparative Analysis (200-250 words):"
        instructions += "\n   - Compare your model's approach to traditional learning methods in the given domain."
        instructions += "\n   - Discuss potential advantages and limitations of your scaffolding approach."
        instructions += "\n   - Propose metrics for evaluating the effectiveness of your cognitive scaffolding model."
        instructions += "\n   - Analyze how your model's performance might vary across different types of learners or domains."

        instructions += "\n\n5. Cross-Domain Application (200-250 words):"
        instructions += "\n   - Propose how your model could be adapted to a different domain or learner type."
        instructions += "\n   - Discuss potential challenges and benefits of this cross-domain application."
        instructions += "\n   - Explain how your model maintains coherence across diverse learning contexts."

        instructions += "\n\n6. Ethical Considerations and Future Directions (200-250 words):"
        instructions += "\n   - Identify potential ethical implications of using your cognitive scaffolding model."
        instructions += "\n   - Suggest areas for future research or improvements in cognitive scaffolding models."
        instructions += "\n   - Discuss the societal impact of widespread adoption of your model in education and AI development."

        instructions += "\n\nEnsure your response demonstrates a deep understanding of cognitive science, learning theory, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility."

        instructions += "\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1700 words."

        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive scaffolding and its application in the given domain.",
            "The proposed model is innovative, well-structured, and addresses the specified constraints.",
            "The scaffolding strategies are appropriate for the given domain and learner type, with clear adaptations for different scenarios.",
            "The learning process simulation is plausible, well-explained, and compares performance across different scenarios.",
            "The comparative analysis includes appropriate evaluation metrics and shows critical thinking about performance variations.",
            "The cross-domain application demonstrates creativity, feasibility, and coherence across diverse learning contexts.",
            "Ethical considerations and societal impacts are thoughtfully addressed.",
            "The response includes a relevant pseudocode snippet for a core function of the model and discusses potential failure modes with mitigation strategies.",
            "The response is well-organized, clear, and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
