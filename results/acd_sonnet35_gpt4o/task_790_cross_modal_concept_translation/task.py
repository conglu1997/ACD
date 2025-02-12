import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "justice",
            "freedom",
            "love",
            "time",
            "infinity",
            "chaos",
            "balance",
            "truth"
        ]
        source_modalities = [
            "visual",
            "auditory",
            "tactile",
            "olfactory"
        ]
        target_modalities = [
            "visual",
            "auditory",
            "tactile",
            "olfactory"
        ]
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "source": random.choice(source_modalities),
                "target": random.choice([m for m in target_modalities if m != source_modalities])
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "source": random.choice(source_modalities),
                "target": random.choice([m for m in target_modalities if m != source_modalities])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the abstract concept of {t['concept']} from the {t['source']} modality to the {t['target']} modality while preserving its essential meaning and associations. Your response should include:

1. Conceptual Analysis (200-250 words):
   a) Analyze the abstract concept of {t['concept']}, discussing its key characteristics and associations.
   b) Explain how this concept is typically represented or experienced in the {t['source']} modality.
   c) Discuss the challenges in translating this concept to the {t['target']} modality.

2. System Architecture (250-300 words):
   a) Describe the overall structure of your cross-modal translation system.
   b) Explain the key components and their functions.
   c) Discuss how your system integrates insights from cognitive science, linguistics, and AI.
   d) Include a simple diagram or flowchart of your system's architecture using ASCII art or a clear textual description. For example:
      [Input] -> [Concept Analyzer] -> [Modality Mapper] -> [Output Generator] -> [Translated Output]

3. Translation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system would translate {t['concept']} from {t['source']} to {t['target']} modality.
   b) Describe any novel algorithms or techniques used in this process.
   c) Explain how your system preserves the essential meaning and associations of the concept during translation.
   d) Include a specific example of how a particular aspect of {t['concept']} would be translated from {t['source']} to {t['target']} modality.

4. Output Representation (150-200 words):
   a) Describe in detail how {t['concept']} would be represented in the {t['target']} modality after translation.
   b) Explain how this representation captures the key aspects of the original concept.
   c) Discuss any limitations or potential loss of information in this representation.
   d) Provide a concrete example of the output representation for a specific aspect of {t['concept']}.

5. Evaluation and Testing (150-200 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your cross-modal translation.
   b) Describe potential experiments or user studies to test your system.
   c) Discuss how you would measure the preservation of meaning across modalities.
   d) Suggest at least one quantitative metric for assessing the quality of the translation.

6. Implications and Applications (200-250 words):
   a) Discuss potential applications of your system in fields such as human-computer interaction, accessibility technology, or data visualization.
   b) Explore how this approach might enhance our understanding of human cognition and perception.
   c) Consider potential ethical implications or concerns related to cross-modal concept translation.
   d) Propose a novel research question that arises from your system design.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Conceptual Analysis:') on a new line, followed by your response for that section.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs a system to translate the concept of {t['concept']} from {t['source']} to {t['target']} modality.",
            "The system architecture and translation process are well-explained, scientifically plausible, and include specific examples.",
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence, using appropriate technical terminology.",
            "The proposed evaluation methods include at least one quantitative metric and consider user studies or experiments.",
            "The response is creative and innovative while maintaining scientific rigor, and proposes a novel research question.",
            "The response follows the specified format, including clear headings and staying within the word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
