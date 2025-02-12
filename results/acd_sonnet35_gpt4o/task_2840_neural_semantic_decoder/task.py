import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "Wernicke's area",
                "linguistic_feature": "Metaphor",
                "target_modality": "Visual imagery"
            },
            {
                "brain_region": "Broca's area",
                "linguistic_feature": "Syntactic structure",
                "target_modality": "Tactile sensation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural semantic decoder that can interpret complex semantic representations from neural activity in {t['brain_region']}, focusing on the linguistic feature of {t['linguistic_feature']}, and translate these representations into {t['target_modality']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your neural semantic decoder.
   b) Explain how it interfaces with {t['brain_region']} to capture neural activity.
   c) Detail the process of decoding {t['linguistic_feature']} from neural signals.
   d) Explain how your system translates the decoded information into {t['target_modality']}.
   e) Propose a novel method for maintaining semantic fidelity across modalities.

2. Neurolinguistic Foundation (200-250 words):
   a) Analyze the role of {t['brain_region']} in processing {t['linguistic_feature']}.
   b) Discuss current theories about the neural representation of {t['linguistic_feature']}.
   c) Explain how your system leverages these theories in its decoding process.

3. AI and Machine Learning Approach (250-300 words):
   a) Describe the AI and machine learning techniques used in your decoder.
   b) Explain how your system learns to map neural activity to semantic representations.
   c) Discuss any novel algorithms or architectures you've incorporated.
   d) Address challenges in generalizing across different individuals or languages.

4. Cross-Modal Translation (200-250 words):
   a) Detail the process of translating decoded semantic information into {t['target_modality']}.
   b) Discuss challenges in preserving meaning across different modalities.
   c) Propose a method for evaluating the accuracy of cross-modal translations.

5. Potential Applications (150-200 words):
   a) Suggest three potential applications of your neural semantic decoder.
   b) Discuss how each application could impact fields such as neuroscience, linguistics, or human-computer interaction.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to decoding and translating thoughts.
   b) Discuss privacy concerns and propose safeguards for protecting mental privacy.
   c) Consider the broader societal implications of this technology.

7. Future Research Directions (100-150 words):
   a) Propose two follow-up research questions or experiments.
   b) Discuss how advances in this field might influence our understanding of language and cognition.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence.",
            "The proposed neural semantic decoder effectively integrates knowledge from multiple disciplines.",
            "The system architecture is innovative and plausible, addressing the specific requirements of the task.",
            "The AI and machine learning approach is well-explained and appropriate for the task.",
            "The cross-modal translation process is thoroughly described and addresses potential challenges.",
            "Ethical considerations are comprehensively discussed.",
            "Proposed applications and future research directions are relevant and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
