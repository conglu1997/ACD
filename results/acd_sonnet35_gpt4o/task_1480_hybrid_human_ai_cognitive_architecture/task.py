import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_domains = [
            {
                "domain": "decision making",
                "ai_component": "reinforcement learning",
                "ethical_focus": "autonomy"
            },
            {
                "domain": "creativity",
                "ai_component": "generative adversarial networks",
                "ethical_focus": "intellectual property"
            },
            {
                "domain": "memory",
                "ai_component": "neural networks",
                "ethical_focus": "privacy"
            },
            {
                "domain": "language processing",
                "ai_component": "transformers",
                "ethical_focus": "bias"
            }
        ]
        return {
            "1": random.choice(cognitive_domains),
            "2": random.choice(cognitive_domains)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid human-AI cognitive architecture for enhanced problem-solving in the domain of {t['domain']}, incorporating {t['ai_component']} as the primary AI component. Then, analyze its potential impacts on human cognition and society, with a focus on the ethical consideration of {t['ethical_focus']}. Your response should include:

1. Architecture Design (250-300 words):
   a) Describe the key components of your hybrid human-AI cognitive architecture.
   b) Explain how {t['ai_component']} is integrated into the human cognitive process for {t['domain']}.
   c) Discuss the interface between human and AI components, including input/output mechanisms.
   d) Propose a novel feature that enhances the synergy between human and AI cognition.

2. Enhanced Problem-Solving Analysis (200-250 words):
   a) Explain how your architecture enhances problem-solving in {t['domain']}.
   b) Provide a specific example of a complex problem this architecture could address.
   c) Compare the expected performance of your hybrid system to human-only and AI-only approaches.

3. Cognitive Impact Assessment (200-250 words):
   a) Analyze potential short-term and long-term effects on human cognitive abilities in {t['domain']}.
   b) Discuss how this architecture might influence human learning and skill development.
   c) Consider potential cognitive risks or drawbacks of human-AI integration in this domain.

4. Societal Implications (150-200 words):
   a) Explore broader societal impacts of widespread adoption of this technology.
   b) Discuss potential changes in social structures, work environments, or educational systems.
   c) Address concerns related to inequality or accessibility of this technology.

5. Ethical Considerations (200-250 words):
   a) Analyze ethical implications related to {t['ethical_focus']} in the context of your architecture.
   b) Identify potential misuses or unintended consequences of this technology.
   c) Propose guidelines or safeguards to ensure responsible development and use.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and ethics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and creative design for a hybrid human-AI cognitive architecture that effectively integrates {t['ai_component']} for enhanced problem-solving in {t['domain']}, with clear explanations of key components and mechanisms.",
            f"The analysis of enhanced problem-solving demonstrates a clear understanding of how the hybrid architecture improves capabilities in {t['domain']}, including a specific, well-explained example.",
            "The cognitive impact assessment shows depth of thought regarding both short-term and long-term effects on human cognitive abilities, learning, and skill development.",
            "The discussion of societal implications is comprehensive, considering multiple aspects of potential societal change and addressing concerns about inequality or accessibility.",
            f"The ethical considerations section thoroughly analyzes implications related to {t['ethical_focus']}, identifies potential misuses, and proposes thoughtful guidelines for responsible development and use.",
            "The overall response demonstrates a strong grasp and integration of cognitive science, artificial intelligence, and ethics, with appropriate use of technical terminology and clear connections drawn between disciplines.",
            "The response adheres to the specified format and word count requirements, and provides specific examples and concrete details throughout to support the proposed ideas and analyses."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
