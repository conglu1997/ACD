import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        bci_applications = [
            {
                "name": "Memory Enhancement",
                "description": "Using BCIs to improve memory recall and storage"
            },
            {
                "name": "Direct Brain-to-Brain Communication",
                "description": "Enabling telepathic-like communication between individuals"
            },
            {
                "name": "Cognitive Augmentation",
                "description": "Enhancing problem-solving and analytical capabilities"
            },
            {
                "name": "Emotional Regulation",
                "description": "Modulating emotional responses and mental states"
            }
        ]
        return {
            "1": random.choice(bci_applications),
            "2": random.choice(bci_applications)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an ethical framework for AI-enhanced brain-computer interfaces (BCIs) focusing on the application of {t['name']} ({t['description']}). Your task involves the following steps:

1. Technological Overview (200-250 words):
   a) Describe the current state of BCI technology relevant to {t['name']}.
   b) Explain how AI could enhance this BCI application.
   c) Discuss potential near-future advancements in this area.

2. Ethical Framework Design (300-350 words):
   a) Propose a comprehensive ethical framework for the development and use of AI-enhanced BCIs for {t['name']}.
   b) Include principles addressing issues such as privacy, autonomy, informed consent, and potential misuse.
   c) Explain how your framework balances technological progress with human rights and societal values.
   d) Discuss how your framework addresses potential unintended consequences of this technology.

3. Implementation and Governance (250-300 words):
   a) Propose a governance structure for enforcing your ethical framework.
   b) Describe mechanisms for ongoing ethical review and adaptation as the technology evolves.
   c) Discuss how to ensure global cooperation and adherence to these ethical standards.

4. Societal Impact Analysis (250-300 words):
   a) Analyze potential impacts of widespread adoption of this BCI application on society, culture, and human relationships.
   b) Discuss how it might affect social equality and power structures.
   c) Consider both positive and negative potential outcomes.

5. Cognitive and Psychological Implications (200-250 words):
   a) Examine how this BCI application might alter human cognition and psychological processes.
   b) Discuss potential changes to our understanding of consciousness, identity, and free will.
   c) Consider long-term evolutionary implications for the human species.

6. Case Study (150-200 words):
   Present a hypothetical scenario that tests the limits of your ethical framework. Analyze how your framework would guide decision-making in this complex situation.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethical philosophy. Be innovative in your approach while considering real-world applicability and potential consequences. Use clear headings for each section of your response.

If you reference specific theories, research, or ethical frameworks, please provide brief citations or references.

Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of BCI technology and AI integration.",
            "The ethical framework is well-structured, addressing key issues such as privacy, autonomy, and potential misuse, with clear reasoning for each principle proposed.",
            "The governance structure and implementation strategies are practical and well-reasoned, considering global implications.",
            "The societal impact analysis is thorough, considering both positive and negative outcomes, with specific examples provided.",
            "The cognitive and psychological implications are explored in depth, showing an understanding of human cognition and consciousness, supported by relevant theories or research.",
            "The case study effectively tests the ethical framework and demonstrates its application in a complex scenario.",
            "The response shows creativity and innovation while maintaining scientific and ethical plausibility.",
            "The writing is clear, well-organized, and adheres to the specified word counts for each section, with a total word count provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
