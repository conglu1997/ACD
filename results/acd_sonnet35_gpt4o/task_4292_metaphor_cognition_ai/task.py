import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "quantum physics",
            "ecology",
            "economics",
            "neuroscience",
            "social media"
        ]
        languages = [
            "Mandarin Chinese",
            "Arabic",
            "Swahili",
            "Russian",
            "Hindi"
        ]
        abstract_concepts = [
            "time",
            "causality",
            "consciousness",
            "justice",
            "innovation"
        ]
        return {
            "1": {
                "domain": random.choice(domains),
                "language": random.choice(languages),
                "concept": random.choice(abstract_concepts)
            },
            "2": {
                "domain": random.choice(domains),
                "language": random.choice(languages),
                "concept": random.choice(abstract_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating, analyzing, and translating conceptual metaphors across different languages and domains of knowledge. Then, apply your system to generate and analyze conceptual metaphors for the abstract concept of {t['concept']} in the domain of {t['domain']}, expressed in {t['language']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for conceptual metaphor cognition.
   b) Explain how your system integrates knowledge from cognitive linguistics, conceptual metaphor theory, and the target domain.
   c) Detail any novel AI techniques or algorithms used in your model.
   d) Provide a high-level diagram or flowchart of your system architecture (describe it textually).

2. Knowledge Representation (200-250 words):
   a) Explain how your system represents and utilizes knowledge about conceptual metaphors, languages, and specific domains.
   b) Describe the process of acquiring and updating this knowledge.
   c) Discuss how your system handles cross-linguistic and cross-domain mapping of concepts.

3. Metaphor Generation and Analysis Process (250-300 words):
   a) Outline the step-by-step process your AI system uses to generate conceptual metaphors.
   b) Explain how your system analyzes and interprets the generated metaphors.
   c) Describe how your system accounts for cultural and linguistic nuances in metaphor creation and interpretation.

4. Application to the Given Task (250-300 words):
   a) Apply your AI system to generate at least two conceptual metaphors for {t['concept']} in the domain of {t['domain']}, expressed in {t['language']}.
   b) Provide an English translation and a detailed analysis of each generated metaphor.
   c) Explain how these metaphors reflect both the abstract concept and the specific domain knowledge.
   d) Ensure that each metaphor incorporates at least two specific elements or principles from the domain of {t['domain']}.
   e) Discuss any challenges your system faced in this task and how it overcame them.

5. Cross-linguistic and Cross-domain Translation (200-250 words):
   a) Explain how your system would translate the generated metaphors into a different language while preserving their conceptual meaning.
   b) Describe how your system would adapt these metaphors to a different domain of knowledge.
   c) Discuss the challenges and potential limitations of such translations.

6. Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the creativity, coherence, and cross-cultural validity of your AI system's metaphor generation and analysis.
   b) Discuss potential biases in your system and how to mitigate them.
   c) Suggest how human experts could be integrated into the evaluation process.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using AI for conceptual metaphor generation and analysis across cultures and domains.
   b) Address concerns about the impact on human creativity and cross-cultural understanding.
   c) Propose guidelines for the responsible use of your AI system.
   d) Suggest future research directions to enhance AI-driven conceptual metaphor cognition.

Ensure your response demonstrates a deep understanding of cognitive linguistics, conceptual metaphor theory, the specified language, and the target domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of cognitive linguistics, conceptual metaphor theory, and AI system design.",
            "The AI system architecture is innovative, detailed, and scientifically plausible.",
            "The knowledge representation and metaphor generation processes are clearly explained and logically sound.",
            "The application to the given task produces creative and coherent conceptual metaphors that accurately reflect the abstract concept and domain.",
            "Each generated metaphor incorporates at least two specific elements or principles from the given domain.",
            "The cross-linguistic and cross-domain translation aspects are thoughtfully addressed.",
            "The evaluation methods and ethical considerations are comprehensive and well-reasoned.",
            "The response shows strong interdisciplinary reasoning, combining insights from linguistics, cognitive science, and artificial intelligence.",
            "The writing is clear, well-structured, and adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
