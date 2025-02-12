import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "interface_type": "Cortical implant",
                "cognitive_enhancement": "Memory augmentation",
                "ethical_concern": "Personal identity and authenticity"
            },
            {
                "interface_type": "Non-invasive BCI",
                "cognitive_enhancement": "Accelerated learning",
                "ethical_concern": "Cognitive liberty and coercion"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for ethical human-AI symbiosis through direct neural interfaces, addressing cognitive enhancement, privacy, and autonomy concerns. Your framework should incorporate a {t['interface_type']} for {t['cognitive_enhancement']}, while specifically addressing the ethical concern of {t['ethical_concern']}. Provide your response in the following format:

1. Technological Framework (300-350 words):
   a) Describe the key components and functionality of the {t['interface_type']} for {t['cognitive_enhancement']}.
   b) Explain how the AI system interacts with human neural processes to achieve the desired enhancement.
   c) Discuss potential risks and safeguards in the technological implementation.

2. Cognitive Enhancement Mechanism (250-300 words):
   a) Detail the neuroscientific basis for {t['cognitive_enhancement']} through AI-neural interface.
   b) Explain the expected cognitive benefits and potential neural plasticity considerations.
   c) Discuss how the enhancement might affect overall cognitive function and human experience.

3. Ethical Analysis (300-350 words):
   a) Analyze the ethical implications of the proposed human-AI symbiosis, focusing on {t['ethical_concern']}.
   b) Discuss potential societal impacts, including issues of equity and access.
   c) Propose ethical guidelines and governance frameworks for the development and use of this technology.

4. Privacy and Data Security (200-250 words):
   a) Outline potential privacy risks associated with direct neural interfaces and AI symbiosis.
   b) Propose robust data protection measures and user control mechanisms.
   c) Discuss the ethical handling of neural data and AI-generated insights.

5. Autonomy and Agency (200-250 words):
   a) Examine how the proposed symbiosis might impact human autonomy and decision-making.
   b) Discuss the potential for AI influence or control over human thoughts and actions.
   c) Propose mechanisms to ensure user agency and the ability to disconnect or override the AI system.

6. Long-term Implications (150-200 words):
   a) Speculate on the long-term effects of widespread adoption of this human-AI symbiosis on human evolution and society.
   b) Discuss potential changes in human relationships, work, and culture.
   c) Consider how this technology might shape the future of human consciousness and identity.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethical philosophy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and ethical philosophy.",
            "The proposed framework is innovative while maintaining scientific plausibility.",
            "The ethical analysis is thorough and addresses the specified concern comprehensively.",
            "The response considers both short-term and long-term implications of human-AI symbiosis.",
            "The framework adequately addresses issues of privacy, autonomy, and data security.",
            "The response is well-structured and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
