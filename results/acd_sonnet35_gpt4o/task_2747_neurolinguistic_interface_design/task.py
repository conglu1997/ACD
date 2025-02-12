import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {"name": "Mandarin Chinese", "language_family": "Sino-Tibetan", "writing_system": "Logographic"},
            {"name": "Arabic", "language_family": "Afroasiatic", "writing_system": "Abjad"},
            {"name": "Swahili", "language_family": "Niger-Congo", "writing_system": "Latin alphabet"},
            {"name": "Russian", "language_family": "Indo-European", "writing_system": "Cyrillic"}
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        additional_challenge = random.choice(["memory enhancement", "emotion recognition", "non-verbal communication"])
        return f"""Design a hypothetical brain-computer interface (BCI) for accelerated language learning and cross-linguistic communication, focusing on {t['name']} ({t['language_family']} family, {t['writing_system']} writing system). Additionally, incorporate {additional_challenge} as a secondary feature of your BCI design. Your response should include the following sections:

1. BCI System Design (250-300 words):
   a) Describe the overall architecture of your neurolinguistic interface.
   b) Explain how it interfaces with the brain's language centers.
   c) Detail how it facilitates rapid acquisition of {t['name']}.
   d) Discuss how it enables real-time translation and communication.
   e) Explain how you've incorporated {additional_challenge} into your design.

2. Neurolinguistic Mechanisms (250-300 words):
   a) Explain how your BCI leverages neuroplasticity for language learning.
   b) Describe how it handles the specific challenges of {t['name']}'s phonology, syntax, and writing system.
   c) Discuss potential effects on the brain's existing language structures.

3. Learning and Communication Processes (250-300 words):
   a) Outline the step-by-step process of learning {t['name']} using your BCI.
   b) Explain how the system facilitates real-time communication between {t['name']} speakers and non-speakers.
   c) Discuss how the BCI handles cultural context and nuances in communication.

4. Technical Challenges and Solutions (200-250 words):
   a) Identify at least three major technical challenges in implementing your BCI.
   b) Propose innovative solutions to these challenges.
   c) Discuss any limitations of your proposed system.

5. Ethical Considerations (200-250 words):
   a) Analyze potential ethical issues related to your neurolinguistic interface.
   b) Discuss implications for privacy, cognitive liberty, and cultural preservation.
   c) Propose guidelines for ethical development and use of such technology.

6. Comparative Analysis (200-250 words):
   a) Compare your BCI's efficiency to traditional language learning methods.
   b) Discuss potential impacts on global communication and cultural exchange.
   c) Speculate on how this technology might evolve in the next 50 years.

7. Experiment Design (150-200 words):
   a) Propose an experiment to test the effectiveness and safety of your BCI.
   b) Describe the methodology, including control groups and measurable outcomes.
   c) Discuss how you would evaluate long-term effects on cognition and brain structure.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and computer science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (numbered 1-7 as above). Include the word count for each section in parentheses at the end of the section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a detailed design of a brain-computer interface for language learning and communication, addressing the specified language and its characteristics.",
            "The design should incorporate the additional challenge feature (memory enhancement, emotion recognition, or non-verbal communication) in a meaningful way.",
            "The design should demonstrate innovative and plausible neurolinguistic mechanisms for rapid language acquisition and real-time translation.",
            "The response must provide a clear explanation of how the BCI interfaces with the brain's language centers and leverages neuroplasticity.",
            "The learning and communication processes should be clearly outlined, including how the system handles cultural context and nuances.",
            "The response should identify at least three major technical challenges and propose innovative solutions.",
            "The ethical analysis must consider issues related to privacy, cognitive liberty, and cultural preservation, and propose guidelines for ethical use.",
            "The comparative analysis should provide insightful comparisons with traditional language learning methods and speculate on future developments.",
            "The proposed experiment design should be well-structured, with clear methodology and measurable outcomes.",
            "The response must demonstrate interdisciplinary knowledge integration, creative problem-solving, and ethical reasoning throughout.",
            "The response should adhere to the specified format, including clear headings and subheadings, word counts for each section, and the overall word count (1500-1850 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
