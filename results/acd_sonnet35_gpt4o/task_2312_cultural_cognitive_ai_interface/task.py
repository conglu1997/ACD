import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        global_challenges = [
            {
                "challenge": "Climate change mitigation",
                "cultural_context": "Indigenous communities in the Amazon rainforest"
            },
            {
                "challenge": "Equitable access to education",
                "cultural_context": "Rural areas in Sub-Saharan Africa"
            }
        ]
        return {
            "1": random.choice(global_challenges),
            "2": random.choice(global_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can interface with and augment human cognition while adapting to diverse cultural contexts. Then, apply your system to address the global challenge of {t['challenge']} within the cultural context of {t['cultural_context']}. Your response should include the following sections:

1. Cognitive-Cultural AI Architecture (300-350 words):
   a) Describe the key components of your AI system, explaining how it interfaces with human cognition.
   b) Detail how your system adapts to and incorporates diverse cultural contexts.
   c) Explain any novel approaches or mechanisms in your design that enable cross-cultural cognitive augmentation.
   d) Include a visual representation of your architecture (use ASCII art or Unicode characters).

2. Cultural Adaptation Mechanism (250-300 words):
   a) Explain how your system learns and adapts to the specific cultural context provided.
   b) Describe the data sources and learning processes your system uses to understand cultural nuances.
   c) Discuss how your system handles potential cultural biases or misunderstandings.
   d) Provide an example of how your system might adapt its behavior or outputs based on cultural context.

3. Application to Global Challenge (300-350 words):
   a) Describe how your AI system would approach the given global challenge within the specified cultural context.
   b) Explain how the cognitive augmentation provided by your system enhances problem-solving capabilities.
   c) Discuss potential solutions or strategies your system might propose, highlighting how they respect and incorporate local cultural values and practices.
   d) Analyze potential challenges or limitations in applying your system to this specific scenario.

4. Ethical Considerations and Safeguards (200-250 words):
   a) Discuss ethical implications of using AI to augment human cognition across cultures.
   b) Explain how your system ensures respect for cultural autonomy and prevents unintended negative consequences.
   c) Propose guidelines for responsible development and use of culturally adaptive cognitive AI systems.
   d) Discuss how to address potential issues of inequality or power imbalances that may arise from the use of such technology.

5. Evaluation and Impact Assessment (200-250 words):
   a) Propose a method to evaluate the effectiveness of your system in both augmenting cognition and adapting to cultural contexts.
   b) Describe metrics or criteria you would use to assess the system's impact on addressing the global challenge.
   c) Suggest an experiment or pilot study to test your system's performance and cultural adaptability.
   d) Discuss how you would measure and mitigate any unintended consequences of your system's deployment.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, cultural anthropology, and the specific global challenge and cultural context provided. Be creative and innovative in your approach while maintaining scientific and ethical plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, adhering to the specified word counts. Your total response should be between 1250-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, AI, and cultural anthropology.",
            "The proposed AI system architecture is innovative, detailed, and technically feasible.",
            f"The cultural adaptation mechanism effectively addresses the specific context of {t['cultural_context']}.",
            f"The application to the global challenge of {t['challenge']} is well-reasoned and culturally sensitive.",
            "Ethical considerations are thoroughly addressed with practical safeguards proposed.",
            "The evaluation and impact assessment methods are comprehensive and well-thought-out.",
            "The response maintains coherence, creativity, and plausibility throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
