import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "prefrontal cortex",
                "ai_technique": "reinforcement learning",
                "climate_challenge": "carbon sequestration optimization"
            },
            {
                "brain_region": "hippocampus",
                "ai_technique": "generative adversarial networks",
                "climate_challenge": "extreme weather prediction and response"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system that utilizes AI to enhance human decision-making in climate change mitigation efforts. Your system should focus on the {t['brain_region']}, incorporate {t['ai_technique']} as the primary AI technique, and address the climate challenge of {t['climate_challenge']}. Your response should include:

1. Neurotechnology Design (300-350 words):
   a) Describe the BCI system's architecture and how it interfaces with the {t['brain_region']}.
   b) Explain the neural signals or patterns the system targets and their relevance to decision-making.
   c) Discuss potential risks and safety measures in the BCI design.
   d) Explain how the system ensures user autonomy and prevents undue influence.

2. AI Integration (250-300 words):
   a) Detail how {t['ai_technique']} is implemented in your system.
   b) Explain how the AI component interacts with and enhances human cognitive processes.
   c) Describe the data flow between the human brain, the AI system, and climate data sources.
   d) Discuss how the system balances AI suggestions with human decision-making.

3. Climate Challenge Application (250-300 words):
   a) Explain how your system specifically addresses {t['climate_challenge']}.
   b) Provide a scenario demonstrating the system's operation in a critical decision-making moment.
   c) Discuss potential improvements in decision-making efficiency and effectiveness.
   d) Address any ethical considerations specific to this climate challenge.

4. Performance Evaluation (200-250 words):
   a) Propose methods to assess the system's impact on decision quality and climate outcomes.
   b) Describe how you would measure improvements in human cognitive performance.
   c) Suggest approaches for long-term monitoring of the system's effectiveness and safety.

5. Scalability and Global Implementation (200-250 words):
   a) Discuss how your system could be scaled for wider use in climate change mitigation.
   b) Address challenges in implementing the system across different cultures and environments.
   c) Propose strategies for ensuring equitable access and preventing technological divides.

6. Ethical and Societal Implications (150-200 words):
   a) Analyze potential societal impacts of enhancing human cognition for climate decision-making.
   b) Discuss data privacy and security concerns related to brain-computer interfaces.
   c) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world challenges.

Format your answer with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of neuroscience, particularly regarding the {t['brain_region']} and its role in decision-making.",
            f"The AI integration section should clearly explain how {t['ai_technique']} is implemented and how it enhances human cognitive processes.",
            f"The climate challenge application must provide a plausible and detailed scenario addressing {t['climate_challenge']}.",
            "The response should thoroughly address ethical considerations and societal implications of the proposed system.",
            "The design should be innovative while maintaining scientific plausibility and real-world applicability."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
