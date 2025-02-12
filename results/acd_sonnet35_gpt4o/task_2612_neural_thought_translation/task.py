import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'abstract_concept': 'Justice',
                'brain_region': 'Prefrontal cortex',
                'target_language': 'English'
            },
            {
                'abstract_concept': 'Time',
                'brain_region': 'Hippocampus',
                'target_language': 'Mandarin Chinese'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of translating neural activity patterns into natural language, focusing on the abstract concept of {t['abstract_concept']}. Your system should specifically analyze activity in the {t['brain_region']} and translate it into {t['target_language']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for neural-to-language translation.
   b) Explain how your system integrates neuroscientific data, linguistic processing, and machine learning techniques.
   c) Detail any novel approaches or algorithms used in your system, particularly for handling abstract concepts.
   d) Include a high-level diagram or flowchart of your system architecture (described textually).

2. Neural Data Processing (200-250 words):
   a) Explain how your system would process and interpret neural activity data from the {t['brain_region']}.
   b) Describe the specific techniques used to isolate and analyze patterns related to the concept of {t['abstract_concept']}.
   c) Discuss how your system accounts for individual variations in neural representations of abstract concepts.

3. Language Generation (200-250 words):
   a) Detail the process of translating identified neural patterns into {t['target_language']}.
   b) Explain how your system ensures the generated language accurately reflects the abstract nature of the original thought.
   c) Describe any mechanisms for maintaining coherence and context in the generated language.

4. Abstract Concept Handling (150-200 words):
   a) Analyze the challenges specific to translating neural patterns of {t['abstract_concept']} into language.
   b) Propose how your system overcomes these challenges.
   c) Discuss how cultural and linguistic differences might affect the translation of this abstract concept.

5. Potential Applications (150-200 words):
   a) Propose two potential applications of your neural thought translation system.
   b) Explain how these applications could advance our understanding of cognition or benefit society.
   c) Discuss any limitations or potential risks associated with these applications.

6. Ethical Implications (150-200 words):
   a) Analyze the ethical considerations of translating thoughts directly into language.
   b) Discuss potential privacy concerns and propose safeguards to protect individuals.
   c) Explore the philosophical implications of this technology on our understanding of consciousness and free will.

7. Evaluation and Validation (100-150 words):
   a) Propose a method to evaluate the accuracy and reliability of your system's translations.
   b) Describe potential experiments or studies to validate your system's performance.
   c) Discuss how you would ensure the system's effectiveness across different individuals and cultures.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the translation of neural activity patterns related to the abstract concept of {t['abstract_concept']}.",
            f"The system design focuses on analyzing activity in the {t['brain_region']} and translating it into {t['target_language']}.",
            "The proposed system demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence.",
            "The response is innovative while maintaining scientific plausibility.",
            "All sections (System Architecture, Neural Data Processing, Language Generation, Abstract Concept Handling, Potential Applications, Ethical Implications, and Evaluation and Validation) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
