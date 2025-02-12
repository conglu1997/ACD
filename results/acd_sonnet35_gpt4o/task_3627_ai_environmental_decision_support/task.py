import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "deforestation in the Amazon rainforest",
            "coral reef degradation in the Great Barrier Reef",
            "air pollution in megacities",
            "plastic pollution in oceans",
            "desertification in sub-Saharan Africa"
        ]
        ai_techniques = [
            "deep reinforcement learning",
            "federated learning",
            "explainable AI",
            "generative adversarial networks",
            "multi-agent systems"
        ]
        return {
            "1": {
                "challenge": random.choice(environmental_challenges),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "challenge": random.choice(environmental_challenges),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered environmental decision support system to address the challenge of {t['challenge']}, incorporating {t['ai_technique']} as a key component. Your system should assist policymakers in making informed decisions to mitigate or adapt to this environmental issue.

Your response should be structured with clear headings for each section and be between 1500-1800 words in total. Include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure and key components of your AI-powered decision support system.
   b) Explain how you incorporate {t['ai_technique']} into your system design.
   c) Detail how your system integrates multi-modal data sources (e.g., satellite imagery, sensor networks, social media data).
   d) Include a high-level diagram or flowchart illustrating the system's architecture (describe it textually).

2. Data Processing and Analysis (250-300 words):
   a) Explain how your system processes and analyzes diverse data sources related to {t['challenge']}.
   b) Describe any novel data fusion or feature extraction techniques used in your system.
   c) Discuss how your system handles uncertainties and biases in the input data.

3. AI Model and Decision Support (250-300 words):
   a) Detail the specific implementation of {t['ai_technique']} in addressing {t['challenge']}.
   b) Explain how your AI model generates actionable insights or recommendations for policymakers.
   c) Describe how the system adapts to new data or changing environmental conditions.

4. User Interface and Visualization (200-250 words):
   a) Design a user interface for policymakers to interact with your system.
   b) Describe how complex environmental data and AI-generated insights are visualized for easy comprehension.
   c) Explain how the interface supports collaborative decision-making among diverse stakeholders.

5. Ethical Considerations and Safeguards (200-250 words):
   a) Identify potential ethical issues or risks associated with using AI for environmental decision-making.
   b) Propose safeguards or guidelines to ensure responsible and equitable use of your system.
   c) Discuss how your system maintains transparency and accountability in its decision-making process.

6. Evaluation and Impact Assessment (200-250 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your decision support system.
   b) Describe potential challenges in implementing your system and how they might be addressed.
   c) Discuss the broader implications of your system for environmental policy and governance.

7. Case Study (100-150 words):
   Provide a specific example scenario demonstrating how your system would be applied to a real-world situation related to {t['challenge']}.

8. Limitations and Future Work (100-150 words):
   Discuss potential limitations or edge cases of your proposed system and suggest areas for future improvement or research.

Ensure your response demonstrates a deep understanding of both environmental science and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical feasibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system must specifically address {t['challenge']} using {t['ai_technique']}.",
            "The response must include a clear description of the system architecture, including data processing, AI model, and user interface components.",
            "The implementation of the specified AI technique must be explained in detail and be relevant to the environmental challenge.",
            "The response must discuss ethical considerations and propose safeguards for responsible use of AI in environmental decision-making.",
            "The proposed system must demonstrate integration of multi-modal data sources and novel approaches to environmental decision support.",
            "The response must include methods for evaluating the system's effectiveness and discuss potential challenges and broader implications.",
            "The answer must demonstrate a deep understanding of both environmental science and artificial intelligence, using appropriate technical terminology.",
            "The response must be innovative while maintaining scientific and practical feasibility.",
            "The response must include a specific case study demonstrating the application of the system to a real-world scenario.",
            "The response must discuss limitations or edge cases of the proposed system and suggest areas for future improvement.",
            "The response must be well-structured with clear headings for each section and be between 1500-1800 words."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
