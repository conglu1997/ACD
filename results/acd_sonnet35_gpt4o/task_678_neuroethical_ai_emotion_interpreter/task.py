import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        brain_regions = ['amygdala', 'prefrontal cortex', 'hippocampus', 'insula', 'anterior cingulate cortex']
        ethical_concerns = ['privacy', 'autonomy', 'manipulation', 'bias', 'accountability']
        application_domains = ['mental health', 'education', 'customer service', 'law enforcement', 'social media']
        
        return {
            "1": {
                "emotional_state": random.choice(emotional_states),
                "brain_region": random.choice(brain_regions),
                "ethical_concern": random.choice(ethical_concerns),
                "application_domain": random.choice(application_domains)
            },
            "2": {
                "emotional_state": random.choice(emotional_states),
                "brain_region": random.choice(brain_regions),
                "ethical_concern": random.choice(ethical_concerns),
                "application_domain": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can interpret and respond to the human emotional state of {t['emotional_state']} based on neurological data from the {t['brain_region']}, while addressing the ethical concern of {t['ethical_concern']}. Consider its application in the domain of {t['application_domain']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system, including data input, processing, and output.
   b) Explain how your system interprets neurological data to identify the given emotional state.
   c) Discuss how your system generates appropriate responses to the identified emotion.

2. Neuroscientific Basis (200-250 words):
   a) Explain the role of the {t['brain_region']} in processing the emotion of {t['emotional_state']}.
   b) Describe how your system's design is informed by current neuroscientific understanding of emotion processing.
   c) Discuss any limitations in our current understanding and how your system accounts for these.

3. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of your system, focusing on the concern of {t['ethical_concern']}.
   b) Propose at least two specific design features or policies to address this ethical concern.
   c) Discuss any potential unintended consequences of your system and how they might be mitigated.

4. Application Scenario (150-200 words):
   a) Describe a specific scenario in the domain of {t['application_domain']} where your system could be applied.
   b) Explain the potential benefits and risks of using your system in this context.
   c) Discuss any necessary modifications or considerations for this specific application.

5. Future Directions (150-200 words):
   a) Propose two potential improvements or extensions to your system.
   b) Discuss how emerging technologies or neuroscientific discoveries might enhance your system's capabilities.
   c) Speculate on the broader implications of emotion-interpreting AI systems for society and human-AI interaction.

Ensure your response demonstrates a deep understanding of neuroscience, AI, and ethics. Be creative in your approach while maintaining scientific plausibility and ethical responsibility. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture clearly explains how it interprets neurological data from the {t['brain_region']} to identify {t['emotional_state']}.",
            f"The neuroscientific basis section accurately describes the role of the {t['brain_region']} in processing {t['emotional_state']}.",
            f"The ethical considerations section thoroughly analyzes the implications of {t['ethical_concern']} and proposes at least two relevant design features or policies.",
            f"The application scenario provides a plausible and well-explained use case in the domain of {t['application_domain']}.",
            "The future directions section proposes innovative yet plausible improvements and discusses broader implications.",
            "The response demonstrates a deep understanding of neuroscience, AI, and ethics, with appropriate use of technical terminology.",
            "The proposed system is creative and novel while maintaining scientific plausibility and ethical responsibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
