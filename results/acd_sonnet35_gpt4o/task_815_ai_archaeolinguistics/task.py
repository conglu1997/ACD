class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Reconstructing a lost Etruscan dialect",
                "available_data": "Partial Etruscan-Latin bilingual inscriptions, archaeological artifacts with symbols",
                "target_output": "Proposed vocabulary and grammar rules for the dialect"
            },
            "2": {
                "scenario": "Deciphering an unknown script from ancient Indus Valley civilization",
                "available_data": "Seal impressions, pottery markings, correlation with archaeological context",
                "target_output": "Proposed phonetic values and semantic categories for the script symbols"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze ancient texts and archaeological data for reconstructing lost languages or dialects. Your task is focused on the following scenario: {t['scenario']}

Your system should be capable of processing the following available data: {t['available_data']}

The target output of your system should be: {t['target_output']}

Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system.
   b) Explain how these components interact to process the available data.
   c) Detail any novel AI techniques or algorithms you would employ.

2. Data Processing Approach (200-250 words):
   a) Explain how your system would preprocess and analyze the available data.
   b) Describe any feature extraction or pattern recognition techniques you would use.
   c) Discuss how your system would handle uncertainties or ambiguities in the data.

3. Linguistic Reconstruction Method (250-300 words):
   a) Detail the approach your system would take to reconstruct linguistic elements.
   b) Explain how it would generate hypotheses about vocabulary, grammar, or symbol meanings.
   c) Describe how the system would validate or refine these hypotheses.

4. Integration of Archaeological Context (150-200 words):
   a) Explain how your system would incorporate archaeological context into its analysis.
   b) Describe any techniques for correlating linguistic and archaeological data.

5. Output Generation and Validation (200-250 words):
   a) Describe how your system would generate the target output.
   b) Explain any methods for assessing the confidence or probability of the results.
   c) Propose how the system's output could be validated by human experts.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues related to using AI for analyzing cultural heritage.
   b) Address any limitations of your approach and potential biases in the results.

Ensure your response demonstrates a deep understanding of linguistics, archaeology, and AI techniques. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts.",
            "The proposed AI system demonstrates a clear understanding of linguistics, archaeology, and AI techniques.",
            "The approach is innovative and scientifically plausible.",
            "The system architecture and methods are well-explained and appropriate for the given scenario.",
            "Ethical considerations and limitations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
