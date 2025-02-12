import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language": "Ainu",
                "brain_region": "Broca's area",
                "ml_technique": "Recurrent Neural Networks"
            },
            {
                "language": "Quechua",
                "brain_region": "Wernicke's area",
                "ml_technique": "Transformer models"
            },
            {
                "language": "Yiddish",
                "brain_region": "Angular gyrus",
                "ml_technique": "Generative Adversarial Networks"
            },
            {
                "language": "Hawaiʻi Creole",
                "brain_region": "Arcuate fasciculus",
                "ml_technique": "Reinforcement Learning"
            },
            {
                "language": "Sami",
                "brain_region": "Inferior frontal gyrus",
                "ml_technique": "Attention mechanisms"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that combines neurolinguistics and machine learning to assist in the preservation and revitalization of {t['language']}, an endangered language. Your system should focus on both language acquisition and cultural context preservation, with particular emphasis on the role of {t['brain_region']} in language processing. Incorporate {t['ml_technique']} as a key component of your machine learning approach. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for language revitalization.
   b) Explain how it integrates neurolinguistic principles, particularly related to {t['brain_region']}.
   c) Detail how {t['ml_technique']} is incorporated into the system's design.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Neurolinguistic Foundations (250-300 words):
   a) Explain the role of {t['brain_region']} in language processing and acquisition.
   b) Discuss how your system models or simulates these neural processes.
   c) Describe how this neurolinguistic approach enhances language learning and preservation.

3. Machine Learning Implementation (250-300 words):
   a) Detail the specific application of {t['ml_technique']} in your system.
   b) Explain how this technique is adapted for language revitalization tasks.
   c) Discuss any novel algorithms or approaches you've developed for this purpose.

4. Cultural Context Preservation (200-250 words):
   a) Describe how your system captures and integrates cultural context alongside language.
   b) Explain methods for preserving idiomatic expressions, oral traditions, and cultural nuances.
   c) Discuss ethical considerations in working with {t['language']} and its community.

5. Language Acquisition Strategies (200-250 words):
   a) Outline the language learning strategies employed by your system.
   b) Explain how these strategies are tailored to the specific challenges of {t['language']}.
   c) Describe how progress and proficiency are measured and evaluated.

6. Potential Impact and Future Directions (150-200 words):
   a) Discuss the potential impact of your system on {t['language']} revitalization efforts.
   b) Propose two potential extensions or improvements to your system.
   c) Suggest areas for further research in AI-assisted language preservation.

Ensure your response demonstrates a deep understanding of neurolinguistics, machine learning, and language preservation. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should accurately describe the role of {t['brain_region']} in language processing",
            f"The system should effectively incorporate {t['ml_technique']} in its design",
            f"The approach should demonstrate cultural sensitivity in preserving {t['language']}",
            "The response should show interdisciplinary integration of neurolinguistics and machine learning",
            "The proposed system should be innovative yet scientifically plausible",
            "The response should address ethical considerations in language preservation",
            "The language acquisition strategies should be well-tailored to the specific language",
            "The response should be well-structured and adhere to the word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
