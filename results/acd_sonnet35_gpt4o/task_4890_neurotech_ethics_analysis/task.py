import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_enhancements = [
            "Memory augmentation",
            "Accelerated learning",
            "Enhanced problem-solving",
            "Improved multitasking"
        ]
        ethical_frameworks = [
            "Utilitarianism",
            "Deontology",
            "Virtue ethics",
            "Care ethics"
        ]
        societal_domains = [
            "Education",
            "Workforce",
            "Healthcare",
            "Social interactions"
        ]
        return {
            "1": {
                "cognitive_enhancement": random.choice(cognitive_enhancements),
                "ethical_framework": random.choice(ethical_frameworks),
                "societal_domain": random.choice(societal_domains)
            },
            "2": {
                "cognitive_enhancement": random.choice(cognitive_enhancements),
                "ethical_framework": random.choice(ethical_frameworks),
                "societal_domain": random.choice(societal_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system for enhancing human cognitive abilities, specifically focusing on {t['cognitive_enhancement']}. Then, analyze its potential societal impacts and ethical implications, particularly in the domain of {t['societal_domain']}, using the ethical framework of {t['ethical_framework']}. Your response should include the following sections:

1. BCI System Design (300-350 words):
   a) Describe the key components and functionality of your BCI system.
   b) Explain how it achieves {t['cognitive_enhancement']}.
   c) Discuss the neuroscientific principles underlying your design.
   d) Address potential technical challenges and propose solutions.

2. Cognitive Enhancement Mechanism (250-300 words):
   a) Detail the specific neural processes your BCI system targets.
   b) Explain how the enhancement is achieved without compromising other cognitive functions.
   c) Discuss potential short-term and long-term effects on the brain.

3. Societal Impact Analysis (250-300 words):
   a) Analyze how widespread adoption of your BCI system could affect {t['societal_domain']}.
   b) Discuss potential benefits and risks to individuals and society.
   c) Consider issues of access, equity, and potential social stratification.

4. Ethical Implications (250-300 words):
   a) Apply the framework of {t['ethical_framework']} to evaluate the ethical implications of your BCI system.
   b) Discuss potential conflicts between individual benefits and societal consequences.
   c) Address issues of autonomy, identity, and human nature.

5. Policy and Regulation (200-250 words):
   a) Propose guidelines for the ethical development and use of cognitive enhancement BCIs.
   b) Suggest regulatory frameworks to address potential misuse or unintended consequences.
   c) Discuss how to balance innovation with safety and ethical concerns.

6. Future Scenarios (150-200 words):
   a) Describe a best-case and worst-case scenario for the long-term impact of your BCI system.
   b) Discuss potential societal adaptations or changes in response to widespread cognitive enhancement.

Ensure your response demonstrates a deep understanding of neurotechnology, ethics, and societal dynamics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section, and adhere to the word count guidelines provided. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of BCI technology, {t['cognitive_enhancement']}, and {t['ethical_framework']}.",
            "The BCI system design is innovative, well-explained, and scientifically plausible.",
            f"The societal impact analysis thoroughly considers the effects on {t['societal_domain']}.",
            "The ethical analysis is comprehensive and applies the specified ethical framework appropriately.",
            "The proposed policy and regulation guidelines are thoughtful and address key concerns.",
            "The future scenarios are insightful and demonstrate foresight.",
            "The response shows interdisciplinary thinking and considers multiple perspectives throughout.",
            "The response is well-formatted with clear section headings and adheres to the provided word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
