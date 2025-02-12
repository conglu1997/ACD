import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                "challenge": "Climate Change Mitigation",
                "focus_area": "Greenhouse Gas Emissions Reduction",
                "policy_domain": "Energy Policy"
            },
            {
                "challenge": "Biodiversity Conservation",
                "focus_area": "Habitat Preservation",
                "policy_domain": "Land Use Planning"
            }
        ]
        return {
            "1": random.choice(environmental_challenges),
            "2": random.choice(environmental_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for environmental modeling and decision-making focused on {t['challenge']}, specifically addressing {t['focus_area']} in the context of {t['policy_domain']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system.
   b) Explain how your system integrates environmental data, machine learning, and policy analysis.
   c) Detail the specific AI/ML techniques used (e.g., deep learning, reinforcement learning).
   d) Provide a high-level diagram or flowchart of your system architecture (describe it textually).

2. Data and Modeling (200-250 words):
   a) Specify the types of data your system would use and potential sources.
   b) Explain how your system would process and analyze this data.
   c) Describe any novel modeling techniques or algorithms employed.
   d) Discuss how your system handles uncertainties in environmental data and projections.

3. Decision-Making Framework (200-250 words):
   a) Explain how your AI system supports decision-making in {t['policy_domain']}.
   b) Describe the criteria your system uses to evaluate policy options.
   c) Discuss how stakeholder inputs are incorporated into the decision-making process.
   d) Provide an example scenario demonstrating your system's decision-making process.

4. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues arising from the use of AI in environmental decision-making.
   b) Discuss how your system addresses issues of fairness, transparency, and accountability.
   c) Propose safeguards to prevent misuse or over-reliance on the AI system.

5. Implementation and Impact Assessment (200-250 words):
   a) Describe how your system could be implemented in real-world policy-making processes.
   b) Propose a method for assessing the impact of your system on environmental outcomes.
   c) Discuss potential challenges in adoption and how they might be overcome.
   d) Suggest a pilot project or case study to test your system's effectiveness.

6. Future Developments (100-150 words):
   a) Propose two potential enhancements or extensions to your AI system.
   b) Discuss how emerging technologies (e.g., quantum computing, IoT) could be integrated into your system.
   c) Suggest a research question that could further improve AI-driven environmental decision-making.

Ensure your response demonstrates a deep understanding of artificial intelligence, environmental science, and policy-making. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of AI, environmental science, and policy-making related to {t['challenge']}.",
            "The proposed AI system is innovative, logically consistent, and effectively integrates environmental modeling with decision-making processes.",
            f"The system architecture and decision-making framework are well-suited to address {t['focus_area']} in the context of {t['policy_domain']}.",
            "The response thoughtfully addresses ethical considerations and proposes realistic implementation strategies.",
            "The proposed system demonstrates creativity and novelty in applying AI to environmental challenges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
