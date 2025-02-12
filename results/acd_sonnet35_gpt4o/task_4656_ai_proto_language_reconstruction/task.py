import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_families = [
            {
                "name": "Indo-European",
                "branches": ["Germanic", "Romance", "Slavic", "Indo-Iranian", "Celtic"],
                "time_depth": "5500-6500 years",
                "challenge": "Extensive documentation but complex branching"
            },
            {
                "name": "Austronesian",
                "branches": ["Malayo-Polynesian", "Formosan"],
                "time_depth": "5000-6000 years",
                "challenge": "Vast geographical spread and numerous languages"
            },
            {
                "name": "Sino-Tibetan",
                "branches": ["Sinitic", "Tibeto-Burman"],
                "time_depth": "4000-6000 years",
                "challenge": "Tonal languages and complex writing systems"
            },
            {
                "name": "Afroasiatic",
                "branches": ["Semitic", "Berber", "Cushitic", "Chadic"],
                "time_depth": "7000-8000 years",
                "challenge": "Diverse phonological systems and morphological complexity"
            }
        ]
        return {
            "1": random.choice(language_families),
            "2": random.choice(language_families)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to reconstruct the proto-language of the {t['name']} language family using machine learning techniques and comparative linguistics methods. Your task has the following parts:

1. AI System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for proto-language reconstruction.
   b) Explain how your system integrates machine learning with traditional comparative linguistics methods.
   c) Detail key components such as data preprocessing, feature extraction, and reconstruction algorithms.
   d) Discuss how your system handles the specific challenge of this language family: {t['challenge']}.
   e) Include a simple diagram of your system's architecture using ASCII characters within your response.

2. Data Processing and Feature Extraction (250-300 words):
   a) Describe the types of linguistic data your system uses (e.g., phonological, morphological, lexical).
   b) Explain how your system processes and represents this data for machine learning.
   c) Detail your approach to extracting relevant features for proto-language reconstruction.
   d) Discuss how you handle missing or ambiguous data in the reconstruction process.

3. Machine Learning Approach (250-300 words):
   a) Describe the specific machine learning techniques your system employs.
   b) Explain how these techniques are adapted for the task of proto-language reconstruction.
   c) Discuss how your system learns patterns and rules from the data of descendant languages.
   d) Provide a brief pseudocode or algorithm sketch for a key part of your machine learning approach.

4. Reconstruction Process (200-250 words):
   a) Explain how your system synthesizes information to reconstruct proto-forms.
   b) Describe your approach to handling sound changes and semantic shifts.
   c) Discuss how your system determines the time depth of reconstructed forms.
   d) Provide an example of how your system would reconstruct a specific linguistic feature in the {t['name']} proto-language.
   e) Include a small sample (3-5 items) of reconstructed proto-forms with their meanings and descendant forms.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and reliability of your system's reconstructions.
   b) Describe how you would validate your results against existing linguistic scholarship.
   c) Discuss potential biases or limitations in your approach and how you might address them.

6. Implications and Future Work (150-200 words):
   a) Discuss the potential impact of your AI system on historical linguistics and language reconstruction.
   b) Propose two novel applications or extensions of your system beyond proto-language reconstruction.
   c) Suggest areas for future research based on your findings.

Ensure your response demonstrates a deep understanding of historical linguistics, comparative methods, and machine learning techniques. Be innovative in your approach while maintaining scientific plausibility. Use appropriate linguistic terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, etc.) where applicable. Your total response should be between 1350-1650 words. Include a word count at the end of your response.

Language Family Parameters:
- Name: {t['name']}
- Major Branches: {', '.join(t['branches'])}
- Estimated Time Depth: {t['time_depth']}
- Specific Challenge: {t['challenge']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical linguistics and comparative methods.",
            "The proposed AI system effectively integrates machine learning techniques with traditional linguistic approaches.",
            "The design addresses the specific challenges of the given language family.",
            "The approach to data processing, feature extraction, and reconstruction is well-reasoned and innovative.",
            "The evaluation and validation methods are appropriate and comprehensive.",
            "The response effectively synthesizes knowledge from linguistics, history, and artificial intelligence.",
            "The proposed system is creative and novel while remaining scientifically plausible.",
            "The response includes a sample of reconstructed proto-forms with their meanings and descendant forms.",
            "The response follows the specified format with clear headings and subheadings."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
