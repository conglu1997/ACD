import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Inferior frontal gyrus"
        ]
        language_aspects = [
            "Semantic processing",
            "Syntactic structure",
            "Phonological encoding",
            "Pragmatic interpretation"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "language_aspect": random.choice(language_aspects)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "language_aspect": random.choice(language_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural linguistic translation system that can translate between human brain activity in the {t['brain_region']} and natural language, focusing on the aspect of {t['language_aspect']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your neural linguistic translation system.
   b) Explain how it interfaces with the brain and processes neural signals.
   c) Detail the AI and computational linguistics techniques used for translation.
   d) Include a high-level diagram or flowchart of your system (describe it textually).

2. Neuroscientific Basis (200-250 words):
   a) Explain the role of the {t['brain_region']} in language processing.
   b) Describe how your system leverages current understanding of this brain region.
   c) Discuss any novel hypotheses or approaches your system proposes regarding brain function.

3. Linguistic Framework (200-250 words):
   a) Explain how your system addresses the aspect of {t['language_aspect']}.
   b) Describe the linguistic theories or models incorporated in your design.
   c) Discuss any challenges specific to this aspect of language processing.

4. Data Processing and Machine Learning (200-250 words):
   a) Describe the data preprocessing steps for neural signals and language inputs.
   b) Explain the machine learning algorithms used for translation.
   c) Discuss how your system handles ambiguity and context in language.

5. Potential Applications (150-200 words):
   a) Propose three potential applications of your neural linguistic translation system.
   b) Explain how each application could benefit society or advance scientific understanding.

6. Ethical Implications (200-250 words):
   a) Discuss potential ethical concerns related to brain-computer interfaces for language.
   b) Address privacy and security issues associated with decoding thoughts into language.
   c) Propose guidelines for responsible development and use of this technology.

7. Limitations and Future Directions (150-200 words):
   a) Identify current technological or scientific limitations of your system.
   b) Propose two areas for future research to enhance your neural linguistic translation system.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, linguistics, and artificial intelligence.",
            "The proposed system architecture is innovative and scientifically plausible.",
            "The explanation of the neuroscientific basis and linguistic framework is thorough and accurate.",
            "The data processing and machine learning approaches are well-explained and appropriate for the task.",
            "Potential applications and ethical implications are thoughtfully considered.",
            "The response addresses all seven points in the instructions comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
