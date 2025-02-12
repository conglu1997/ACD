import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        civilizations = [
            {
                "name": "Ancient Sumerian",
                "writing_system": "Cuneiform",
                "artifact_type": "Clay tablets",
                "historical_period": "3rd millennium BCE",
                "sample_text": "𒀭𒈨",
                "context": "Known for developing one of the earliest writing systems and creating complex city-states."
            },
            {
                "name": "Classical Maya",
                "writing_system": "Maya script",
                "artifact_type": "Stone stelae",
                "historical_period": "3rd to 9th century CE",
                "sample_text": "𓂀𓏛",
                "context": "Renowned for their advanced mathematics, astronomy, and elaborate calendar systems."
            }
        ]
        return {str(i+1): task for i, task in enumerate(civilizations)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of decoding and interpreting ancient texts and artifacts from the {t['name']} civilization. Your system should integrate linguistic analysis, historical context, and pattern recognition to decipher {t['writing_system']} inscriptions found on {t['artifact_type']} from the {t['historical_period']}. Context: {t['context']}

Your response should include the following sections:

1. System Architecture (200-300 words):
   - Describe the main components of your AI system and how they interact.
   - Explain how your system integrates linguistic analysis, historical context, and pattern recognition.
   - Discuss any novel approaches or algorithms you've incorporated to handle the unique challenges of {t['writing_system']} and {t['artifact_type']}.
   - Provide an ASCII art diagram illustrating the system architecture and data flow. The diagram must include at least 5 distinct components and show the connections between them.

2. Data Preprocessing and Feature Extraction (150-250 words):
   - Explain how your system preprocesses images or 3D scans of {t['artifact_type']}.
   - Describe the feature extraction techniques used to identify and isolate {t['writing_system']} characters or symbols.
   - Discuss how your system handles variations in writing style, erosion, or damage to the artifacts.

3. Linguistic and Historical Analysis (200-300 words):
   - Describe how your system incorporates knowledge of {t['name']} language structure and evolution.
   - Explain how historical and cultural context is integrated into the interpretation process.
   - Discuss how your system handles ambiguities or multiple possible interpretations.

4. Pattern Recognition and Machine Learning (150-250 words):
   - Describe the machine learning algorithms used for character recognition and language modeling.
   - Explain how your system learns and improves its accuracy over time.
   - Discuss any techniques used to handle limited training data for this ancient language.

5. Output and Interpretation (100-200 words):
   - Describe the format of your system's output (e.g., translations, confidence scores, alternative interpretations).
   - Explain how your system presents its reasoning and supports its interpretations.
   - Discuss how your system handles uncertainty and communicates reliability of its interpretations.

6. Ethical Considerations and Limitations (100-200 words):
   - Discuss potential ethical issues related to AI interpretation of ancient texts and artifacts.
   - Identify limitations of your system and areas where human expertise is still necessary.
   - Propose guidelines for responsible use of AI in archaeological and historical research.

7. Interdisciplinary Impact (100-200 words):
   - Discuss how your AI system could contribute to our understanding of {t['name']} civilization.
   - Propose a novel research question that your system could help address.
   - Suggest potential applications of your system in other fields of study.

8. Novel Algorithm Proposal (150-250 words):
   - Propose a novel algorithm or technique specifically designed for this archaeolinguistic decoding task.
   - Explain how this algorithm addresses a unique challenge in deciphering {t['writing_system']} on {t['artifact_type']}.
   - Discuss potential advantages and limitations of your proposed algorithm.

9. Sample Decoding and Error Analysis (150-250 words):
   - Provide a step-by-step decoding of the following sample text using your proposed system: {t['sample_text']}
   - Analyze potential sources of error in your decoding process.
   - Describe how your system would handle edge cases or particularly challenging inputs.

Ensure your response demonstrates a deep understanding of computational linguistics, archaeology, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your system design while maintaining scientific plausibility and addressing the unique challenges of working with ancient texts and artifacts.

Your total response should be between 1500-2500 words, with each section adhering to the specified word ranges."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture includes components for linguistic analysis, historical context integration, and pattern recognition specific to {t['writing_system']} and {t['artifact_type']}, with an ASCII art diagram showing at least 5 distinct components and their connections.",
            f"The data preprocessing and feature extraction section addresses the challenges of working with {t['artifact_type']} from the {t['historical_period']}.",
            f"The linguistic and historical analysis section demonstrates knowledge of {t['name']} language structure and cultural context.",
            "The pattern recognition and machine learning section proposes suitable algorithms for ancient language processing with limited data.",
            "The output and interpretation section describes a method for presenting results and handling uncertainty.",
            "The ethical considerations section identifies at least two potential issues and proposes responsible use guidelines.",
            "The interdisciplinary impact section proposes a novel research question relevant to the given civilization.",
            "The novel algorithm proposal section presents an original technique for the given archaeolinguistic decoding task.",
            f"The sample decoding and error analysis section provides a decoding of the given sample text ({t['sample_text']}) and analyzes potential sources of error.",
            "The response adheres to the specified word ranges for each section and the overall word count (1500-2500 words)."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
