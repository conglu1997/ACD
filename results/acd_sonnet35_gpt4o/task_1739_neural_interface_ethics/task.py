import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        bci_applications = [
            {
                'application': 'Memory Enhancement',
                'target_group': 'Alzheimer\'s Patients',
                'key_feature': 'Hippocampal Neural Prosthesis',
                'time_constraint': '5 years to market'
            },
            {
                'application': 'Paralysis Treatment',
                'target_group': 'Spinal Cord Injury Patients',
                'key_feature': 'Motor Cortex-Limb Interface',
                'time_constraint': '3 years to clinical trials'
            },
            {
                'application': 'Cognitive Augmentation',
                'target_group': 'Knowledge Workers',
                'key_feature': 'Prefrontal Cortex Stimulation',
                'time_constraint': '7 years to regulatory approval'
            },
            {
                'application': 'Emotional Regulation',
                'target_group': 'Mental Health Patients',
                'key_feature': 'Amygdala Modulation',
                'time_constraint': '4 years to prototype'
            }
        ]
        
        return {str(i+1): random.choice(bci_applications) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical brain-computer interface (BCI) system for {t['application']} targeting {t['target_group']}, with a key feature of {t['key_feature']}. Then, analyze its ethical implications across various societal domains and cultures. Your response should include:

1. Technical Design (200-250 words):
   a) Describe the overall architecture of your BCI system.
   b) Explain how the {t['key_feature']} works and its role in {t['application']}.
   c) Discuss any novel neurotechnological approaches or materials used in your design.
   d) Address potential technical challenges and propose solutions.

2. Neuroscientific Basis (150-200 words):
   a) Explain the neurological principles underlying your BCI system.
   b) Discuss how your system interacts with specific brain regions or networks.
   c) Describe potential short-term and long-term effects on neural plasticity.
   d) Address any gaps in current neuroscientific knowledge that your system highlights.

3. User Experience and Efficacy (150-200 words):
   a) Describe the user experience for {t['target_group']}.
   b) Explain how your system improves upon current treatments or augmentations.
   c) Discuss potential side effects or unintended consequences.
   d) Propose a method for measuring the efficacy of your BCI system.

4. Ethical Analysis (200-250 words):
   a) Identify and discuss at least three ethical issues raised by your BCI system.
   b) Analyze how these issues might impact individuals, families, and society at large.
   c) Discuss potential misuse scenarios and propose safeguards.
   d) Consider how your system might exacerbate or alleviate existing societal inequalities.
   e) Examine these ethical issues from at least one different cultural perspective.

5. Legal and Regulatory Framework (150-200 words):
   a) Propose a regulatory framework for the development and use of your BCI system.
   b) Discuss how existing laws and regulations might apply to your system.
   c) Identify areas where new legislation might be necessary.
   d) Consider international implications and propose guidelines for global governance.

6. Societal Impact (150-200 words):
   a) Predict potential changes in social norms and behaviors resulting from widespread adoption.
   b) Discuss how your system might influence concepts of human identity and consciousness.
   c) Analyze potential economic impacts, including job creation/displacement.
   d) Consider long-term evolutionary implications of human-machine integration.

7. Future Directions (100-150 words):
   a) Propose two potential future advancements or applications of your BCI technology.
   b) Discuss ethical considerations specific to these advancements.
   c) Suggest areas for further research in neurotechnology and neuroethics.

8. Critical Analysis and Counterarguments (150-200 words):
   a) Present at least two potential counterarguments or criticisms to your proposed BCI system.
   b) Address these counterarguments, explaining how your system might be adapted or justified in response.
   c) Discuss any remaining unresolved ethical or technical challenges.

9. Time Constraint Considerations (100-150 words):
   a) Discuss how the time constraint of {t['time_constraint']} affects the development and implementation of your BCI system.
   b) Identify potential compromises or risks associated with this timeframe.
   c) Propose strategies to mitigate these risks while meeting the deadline.

Ensure your response demonstrates a deep understanding of neuroscience, computer science, ethics, and sociology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Throughout your response, cite at least five relevant scientific sources to support your arguments and design choices. Use a consistent citation format.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, computer science, and ethics in the context of brain-computer interfaces.",
            f"The proposed BCI system for {t['application']} is innovative, technically sound, and addresses the needs of {t['target_group']}.",
            f"The explanation of the {t['key_feature']} and its role in the system is clear and scientifically plausible.",
            "The ethical analysis is thorough, considering multiple perspectives, potential consequences, and at least one cross-cultural implication.",
            "The response addresses legal, regulatory, and societal impacts comprehensively.",
            "The discussion of future directions shows foresight and consideration of ethical implications.",
            "The critical analysis section presents valid counterarguments and addresses them thoughtfully.",
            "The time constraint considerations are realistic and demonstrate an understanding of development challenges.",
            "The response follows the required format and word count guidelines, and demonstrates originality and depth of thought throughout.",
            "At least five relevant scientific sources are cited throughout the response, supporting arguments and design choices."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
