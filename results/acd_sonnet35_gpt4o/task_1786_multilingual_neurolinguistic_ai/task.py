import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {"name": "Mandarin", "language_family": "Sino-Tibetan", "writing_system": "Logographic"},
            {"name": "Arabic", "language_family": "Afroasiatic", "writing_system": "Abjad"},
            {"name": "Hindi", "language_family": "Indo-European", "writing_system": "Abugida"},
            {"name": "Swahili", "language_family": "Niger-Congo", "writing_system": "Latin alphabet"}
        ]
        return {
            "1": random.sample(languages, 2),
            "2": random.sample(languages, 2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        lang1, lang2 = t
        return f"""Design a hypothetical neural network architecture inspired by the brain's language centers that can simultaneously learn and process {lang1['name']} and {lang2['name']}. Your response should include the following sections:

1. Neurolinguistic Foundation (200-250 words):
   a) Briefly describe the key language centers in the human brain and their functions.
   b) Explain how these centers might process two languages from different language families.
   c) Discuss any relevant neurolinguistic theories or findings that inform your design.

2. Neural Network Architecture (300-350 words):
   a) Describe the overall structure of your neural network, including main components and their interactions.
   b) Explain how your architecture mimics or is inspired by the brain's language centers.
   c) Detail how your system would handle the simultaneous processing of {lang1['name']} ({lang1['language_family']}) and {lang2['name']} ({lang2['language_family']}).
   d) Discuss how your architecture accounts for the different writing systems: {lang1['writing_system']} for {lang1['name']} and {lang2['writing_system']} for {lang2['name']}.
   e) Provide a high-level diagram or pseudocode to illustrate your architecture.

3. Learning and Adaptation Mechanisms (200-250 words):
   a) Explain how your system would learn both languages simultaneously.
   b) Describe any novel learning algorithms or techniques your system would employ.
   c) Discuss how your system might handle interference between the two languages during learning.

4. Performance Evaluation (150-200 words):
   a) Propose methods to evaluate your system's proficiency in both languages.
   b) Describe potential experiments to test your system's ability to switch between languages.
   c) Discuss how you would measure the system's performance compared to human bilingual speakers.

5. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your system for our understanding of human language acquisition and processing.
   b) Propose two novel applications of your multilingual neural architecture beyond language translation.
   c) Explain how your system might be extended to handle more than two languages simultaneously.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in implementing your proposed architecture.
   b) Discuss any ethical considerations related to the development and use of such a system.
   c) Suggest two future research directions to further develop or improve your architecture.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section (e.g., '1. Neurolinguistic Foundation', '2. Neural Network Architecture', etc.). Your total response should be between 1200-1500 words. Include a word count at the end of your submission.

Remember, while creativity is encouraged, all proposed mechanisms and systems should have a basis in current scientific understanding and plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence.",
            "The proposed neural network architecture is innovative and plausibly mimics the brain's language centers.",
            "The design effectively addresses the simultaneous learning and processing of two different languages.",
            "The response includes creative applications and future directions for the proposed system.",
            "The submission is well-structured, clear, and within the specified word count range.",
            "All required sections (Neurolinguistic Foundation, Neural Network Architecture, Learning and Adaptation Mechanisms, Performance Evaluation, Implications and Applications, Limitations and Future Directions) are addressed comprehensively.",
            "The proposed ideas and mechanisms maintain scientific plausibility while being creative and innovative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
