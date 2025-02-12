import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_challenges = [
            "Sea level rise adaptation",
            "Extreme weather event preparedness",
            "Agricultural resilience to changing climate",
            "Urban heat island mitigation"
        ]
        brain_regions = [
            "Prefrontal cortex",
            "Amygdala",
            "Hippocampus",
            "Insula"
        ]
        ai_techniques = [
            "Reinforcement learning",
            "Bayesian networks",
            "Neural architecture search",
            "Generative adversarial networks"
        ]
        return {
            "1": {
                "climate_challenge": random.choice(climate_challenges),
                "brain_region": random.choice(brain_regions),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "climate_challenge": random.choice(climate_challenges),
                "brain_region": random.choice(brain_regions),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuro-inspired AI system that enhances human decision-making capabilities for climate change adaptation strategies. Your system should address the climate challenge of {t['climate_challenge']}, draw inspiration from the {t['brain_region']}, and incorporate the AI technique of {t['ai_technique']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your neuro-inspired AI decision support system.
   b) Explain how your system integrates neuroscience principles, AI techniques, and climate science.
   c) Detail how you incorporate inspiration from the {t['brain_region']} into your system design.
   d) Discuss how the {t['ai_technique']} is utilized in your system.
   e) Include a high-level diagram of your system architecture (describe this textually).

2. Neuroscience-AI Integration (250-300 words):
   a) Explain how specific functions or properties of the {t['brain_region']} inform your AI system design.
   b) Describe how your system models or enhances cognitive processes relevant to decision-making.
   c) Discuss any novel algorithms or techniques that bridge neuroscience and AI in your system.

3. Climate Adaptation Application (250-300 words):
   a) Detail how your system addresses the specific challenge of {t['climate_challenge']}.
   b) Explain the decision-making process your system supports, from data input to recommended actions.
   c) Provide an example scenario demonstrating how your system would enhance human decision-making in this context.

4. Human-AI Collaboration (200-250 words):
   a) Describe the interface between your AI system and human decision-makers.
   b) Explain how your system balances AI recommendations with human expertise and intuition.
   c) Discuss strategies for building trust and transparency in the AI-human decision-making partnership.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in using AI to influence human decision-making on climate adaptation.
   b) Discuss how your system addresses concerns about AI bias, accountability, and human autonomy.
   c) Propose guidelines for the responsible development and use of neuro-inspired AI in climate decision support.

6. Performance Evaluation (200-250 words):
   a) Propose methods to evaluate the effectiveness of your system in enhancing human decision-making.
   b) Describe how you would measure improvements in climate adaptation outcomes.
   c) Discuss challenges in assessing the long-term impact of AI-assisted decision-making in climate contexts.

7. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how advancements in neuroscience or AI might further enhance climate adaptation decision support.
   c) Propose an experiment to validate or refine your system's effectiveness.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, climate science, and decision theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, climate science, and decision theory.",
            "The system architecture is well-designed and clearly explained, showing how neuroscience principles, AI techniques, and climate science are integrated.",
            "The neuroscience-AI integration is logically sound and innovative, drawing clear inspiration from the specified brain region.",
            "The application to the given climate adaptation challenge is well-developed and demonstrates practical utility.",
            "The human-AI collaboration aspect is thoughtfully considered and addresses potential challenges.",
            "Ethical considerations are thoroughly discussed and addressed.",
            "The performance evaluation methods are appropriate and comprehensive.",
            "Future directions and proposed experiments are insightful and relevant.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response falls within the specified word count range of 1500-1850 words.",
            "A word count is included at the end of the submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
