import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {"name": "Linear A", "civilization": "Minoan", "period": "Bronze Age", "known_info": "syllabic script, some signs deciphered"},
            {"name": "Rongorongo", "civilization": "Easter Island", "period": "Pre-colonial", "known_info": "glyphs, possibly logographic"}
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of decoding and interpreting extinct or undeciphered languages, and apply it to the case of {t['name']} from the {t['civilization']} civilization ({t['period']}). Known information about this script: {t['known_info']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system for decoding extinct languages.
   b) Explain how your system integrates techniques from linguistics, machine learning, and cryptography.
   c) Detail any novel computational approaches or modeling techniques you would employ.
   d) Discuss how your system handles uncertainty and ambiguity in linguistic data.

2. Data Acquisition and Preprocessing (200-250 words):
   a) Specify the types of data your system would use (e.g., inscriptions, contextual archaeological information).
   b) Explain how your system would preprocess and represent the linguistic data.
   c) Describe any data augmentation techniques you would use to handle limited sample sizes.

3. Decoding Methodology (250-300 words):
   a) Outline your AI system's approach to decoding the {t['name']} script.
   b) Explain how your system would identify patterns and potential meanings in the script.
   c) Describe how your approach leverages known information about the script and its cultural context.
   d) Discuss how your system would validate its interpretations and handle multiple hypotheses.

4. Interdisciplinary Integration (200-250 words):
   a) Explain how your AI system incorporates knowledge from archaeology and cultural anthropology.
   b) Describe how the system would collaborate with human experts in these fields.
   c) Discuss any potential challenges in interdisciplinary integration and how you'd address them.

5. Case Study Application (250-300 words):
   a) Apply your AI system to a hypothetical undeciphered {t['name']} text.
   b) Provide a step-by-step walkthrough of how your system would approach the decoding process.
   c) Present a plausible (speculative) partial translation or interpretation based on your system's analysis.
   d) Explain the reasoning behind your system's conclusions.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues in using AI for decoding culturally significant scripts.
   b) Address concerns about cultural sensitivity and ownership of linguistic heritage.
   c) Acknowledge the limitations of your approach and potential for misinterpretation.

7. Future Directions (100-150 words):
   a) Propose two potential improvements or extensions to your system.
   b) Discuss how your approach could be adapted to other extinct or undeciphered languages.

Ensure your response demonstrates a deep understanding of linguistics, archaeology, and artificial intelligence. Be innovative in your approach while maintaining scientific and practical plausibility. Use technical terminology appropriately and provide explanations where necessary. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, archaeology, and artificial intelligence",
            "The proposed AI system integrates techniques from multiple disciplines in a novel and plausible way",
            f"The approach to decoding {t['name']} is well-reasoned and takes into account the known information about the script",
            "The case study application provides a clear and logical walkthrough of the decoding process",
            "Ethical considerations and limitations are thoughtfully addressed",
            "The response is innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
