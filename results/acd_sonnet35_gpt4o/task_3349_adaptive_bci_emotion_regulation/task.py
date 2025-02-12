import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'emotion': 'anxiety',
                'neuroimaging_technique': 'fMRI',
                'target_brain_region': 'amygdala',
                'intervention_method': 'neurofeedback'
            },
            {
                'emotion': 'depression',
                'neuroimaging_technique': 'EEG',
                'target_brain_region': 'prefrontal cortex',
                'intervention_method': 'transcranial direct current stimulation (tDCS)'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an adaptive brain-computer interface (BCI) system for emotion regulation, focusing on the emotion of {t['emotion']}. Your system should incorporate real-time {t['neuroimaging_technique']} data, target the {t['target_brain_region']}, and use {t['intervention_method']} as the primary intervention method. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your adaptive BCI system for emotion regulation.
   b) Explain how your system integrates {t['neuroimaging_technique']} data acquisition, signal processing, and the {t['intervention_method']} intervention.
   c) Detail the machine learning algorithms used for real-time analysis of neural activity and emotion detection.
   d) Discuss how your system adapts its intervention based on the user's changing emotional state.
   e) Specify the temporal resolution of your system and how it handles potential delays in data processing and intervention delivery.
   f) Describe the hardware and software requirements for your BCI system, including any custom components.

2. Neuroscientific Basis (250-300 words):
   a) Explain the role of the {t['target_brain_region']} in regulating {t['emotion']}.
   b) Describe how {t['intervention_method']} can modulate activity in this brain region.
   c) Discuss potential neuroplasticity effects of long-term use of your BCI system.
   d) Address potential off-target effects on other brain regions and cognitive functions.

3. Machine Learning Implementation (250-300 words):
   a) Describe the specific machine learning techniques used for emotion detection and intervention optimization.
   b) Explain how you would train and validate your model using neuroimaging data.
   c) Discuss how your system handles individual variability in neural responses and emotional experiences.
   d) Detail your approach to online learning and model adaptation during ongoing use of the BCI system.
   e) Describe how you would implement safeguards against adversarial attacks or unintended model drift.
   f) Explain how your system balances exploration (trying new interventions) with exploitation (using known effective interventions).

4. User Interface and Experience (150-200 words):
   a) Describe the user interface for your BCI system, considering both the technical setup and the user's interaction during emotion regulation sessions.
   b) Explain how you would provide feedback to the user about their emotional state and the system's interventions.
   c) Discuss potential challenges in user adoption and how you would address them.

5. Ethical Considerations (250-300 words):
   a) Discuss the ethical implications of using BCIs for emotion regulation.
   b) Address potential risks such as unintended emotional manipulation or psychological dependence.
   c) Propose guidelines for responsible development, testing, and use of emotion-regulating BCI systems.
   d) Discuss the potential for coercive use of this technology and how to prevent it.
   e) Address privacy concerns related to the collection and use of neural and emotional data.
   f) Consider the societal implications of widespread adoption of emotion-regulating BCIs.
   g) Discuss how to ensure equitable access to this technology while preventing its misuse.

6. Evaluation and Future Directions (150-200 words):
   a) Propose a method to evaluate the effectiveness and safety of your BCI system.
   b) Suggest potential applications of your system beyond individual emotion regulation (e.g., in mental health treatment or research).
   c) Discuss how your system could be extended or improved in future iterations.

Ensure your response demonstrates a deep understanding of neuroscience, machine learning, and BCI technologies. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, particularly regarding emotion regulation and the specified brain region.",
            "The system architecture is well-designed, integrating neuroimaging, signal processing, and intervention methods effectively, with consideration for temporal resolution and hardware/software requirements.",
            "The machine learning implementation is appropriate for real-time emotion detection and adaptation, including online learning, safeguards against adversarial attacks, and balancing exploration and exploitation.",
            "Ethical considerations are thoroughly discussed, showing awareness of potential risks, proposing responsible guidelines, and addressing privacy concerns and societal implications.",
            "The user interface and experience are thoughtfully designed, considering both technical and user-centric aspects.",
            "The evaluation method and future directions are well-reasoned and demonstrate foresight in the field of BCI technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
