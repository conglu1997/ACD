import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin", "English"),
            ("Spanish", "Arabic"),
            ("French", "Japanese"),
            ("German", "Russian"),
            ("Hindi", "Portuguese")
        ]
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Supramarginal gyrus",
            "Inferior frontal gyrus"
        ]
        neural_imaging_techniques = [
            "fMRI",
            "EEG",
            "MEG",
            "PET",
            "fNIRS"
        ]
        return {
            "1": {
                "languages": random.choice(language_pairs),
                "brain_region": random.choice(brain_regions),
                "imaging_technique": random.choice(neural_imaging_techniques)
            },
            "2": {
                "languages": random.choice(language_pairs),
                "brain_region": random.choice(brain_regions),
                "imaging_technique": random.choice(neural_imaging_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can simultaneously interpret between {t['languages'][0]} and {t['languages'][1]} by directly interfacing with and analyzing neural activity patterns in multilingual individuals' brains, with a focus on {t['brain_region']} and using {t['imaging_technique']} for neural data acquisition. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI interpretation system.
   b) Explain how your system interfaces with human neural activity.
   c) Detail how your system processes and interprets neural patterns related to language.
   d) Discuss how you incorporate {t['brain_region']} into your design.
   e) Explain how you utilize {t['imaging_technique']} for data acquisition.
   f) Include a high-level diagram or pseudocode (at least 10 lines) to illustrate your architecture.

2. Neural-Linguistic Mapping (250-300 words):
   a) Explain how your system maps neural patterns to linguistic elements in {t['languages'][0]} and {t['languages'][1]}.
   b) Describe how you account for differences in language structure and grammar.
   c) Discuss how your system handles idiomatic expressions and cultural nuances.

3. Real-time Interpretation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system performs real-time interpretation.
   b) Describe how your system ensures accuracy and preserves meaning.
   c) Explain how your system handles ambiguity or multiple possible interpretations.

4. Learning and Adaptation (150-200 words):
   a) Describe how your system learns and improves its interpretation capabilities.
   b) Explain how it adapts to individual users' neural patterns and language use.

5. Ethical Considerations (200-250 words):
   a) Discuss potential privacy concerns related to direct neural interfacing.
   b) Analyze ethical implications of real-time thought interpretation.
   c) Propose guidelines for responsible development and use of this technology.

6. Challenges and Future Directions (200-250 words):
   a) Identify key technical or scientific challenges in implementing your system.
   b) Discuss potential limitations of your proposed system.
   c) Propose two potential applications beyond language interpretation.
   d) Suggest areas for future research or improvement.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and AI technologies. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, linguistics, and AI technologies, particularly in relation to {t['brain_region']} and {t['imaging_technique']}.",
            f"The system design effectively incorporates {t['brain_region']} and utilizes {t['imaging_technique']} for neural data acquisition.",
            f"The approach to neural-linguistic mapping and real-time interpretation between {t['languages'][0]} and {t['languages'][1]} is innovative and scientifically plausible.",
            "The ethical considerations and challenges are thoroughly explored and demonstrate critical thinking.",
            "The response addresses all required sections with appropriate depth, clarity, and follows the specified format.",
            "The high-level diagram or pseudocode provided is sufficiently detailed (at least 10 lines) and accurately represents the proposed system architecture.",
            "The proposed applications beyond language interpretation are feasible and innovative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
