import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'script': 'Linear A',
                'civilization': 'Minoan',
                'artifact_type': 'Clay tablets',
                'ai_technique': 'Transformer-based language models'
            },
            {
                'script': 'Rongorongo',
                'civilization': 'Easter Island',
                'artifact_type': 'Wooden tablets',
                'ai_technique': 'Evolutionary algorithms'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to decipher and analyze the ancient {t['script']} script of the {t['civilization']} civilization, found primarily on {t['artifact_type']}. Your system should utilize {t['ai_technique']} as its primary AI technique. Provide your response in the following format:

1. Historical and Linguistic Context (200-250 words):
   a) Briefly describe the {t['civilization']} civilization and the importance of deciphering {t['script']}.
   b) Discuss known characteristics of {t['script']} and any related languages or scripts.
   c) Explain challenges specific to deciphering {t['script']}.

2. AI System Architecture (300-350 words):
   a) Design an AI architecture for deciphering and analyzing {t['script']}.
   b) Explain how you incorporate {t['ai_technique']} into your system.
   c) Describe other AI or computational linguistics techniques used in your design.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

3. Data Preprocessing and Feature Extraction (200-250 words):
   a) Describe how your system preprocesses images or transcriptions of {t['artifact_type']}.
   b) Explain your approach to extracting relevant features from the script.
   c) Discuss any data augmentation techniques you employ.

4. Decipherment Process (250-300 words):
   a) Outline the step-by-step process your AI system uses to decipher {t['script']}.
   b) Explain how your system handles ambiguities and uncertainties in the decipherment process.
   c) Describe how your system validates its interpretations and improves over time.

5. Linguistic Analysis (200-250 words):
   a) Explain how your system analyzes the linguistic properties of the deciphered text.
   b) Describe methods for identifying grammatical structures, vocabulary, and semantic meanings.
   c) Discuss how your system compares the deciphered language to known languages.

6. Historical and Cultural Insights (150-200 words):
   a) Describe how your AI system extracts historical and cultural information from the deciphered texts.
   b) Explain how these insights could contribute to our understanding of the {t['civilization']} civilization.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss ethical implications of using AI to decipher ancient scripts.
   b) Address potential biases in your system and how they might be mitigated.
   c) Explain limitations of your approach and areas for future improvement.

Ensure your response demonstrates a deep understanding of linguistics, history, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, history, and artificial intelligence.",
            "The AI system design is innovative, plausible, and clearly explained.",
            "The approach to deciphering and analyzing the ancient script is well-reasoned and comprehensive.",
            "The response shows creative problem-solving while maintaining scientific plausibility.",
            "The ethical considerations and limitations are thoughtfully addressed.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
