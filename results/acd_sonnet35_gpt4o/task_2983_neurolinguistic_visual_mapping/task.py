import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_structures = [
            {
                'structure': 'Syntactic tree',
                'neurolinguistic_concept': 'Broca\'s area activation',
                'visualization_technique': 'Force-directed graph'
            },
            {
                'structure': 'Semantic network',
                'neurolinguistic_concept': 'N400 component',
                'visualization_technique': 'Heatmap'
            }
        ]
        return {str(i+1): structure for i, structure in enumerate(random.sample(linguistic_structures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets abstract visual representations of language structures, focusing on the {t['structure']} and incorporating insights from the neurolinguistic concept of {t['neurolinguistic_concept']}. Use the {t['visualization_technique']} as your primary visualization method. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and interpreting visual representations of {t['structure']}.
   b) Explain how your system incorporates insights from {t['neurolinguistic_concept']}.
   c) Detail how the system uses {t['visualization_technique']} to represent linguistic information.
   d) Discuss any novel AI algorithms or approaches used in your system.
   e) Provide a simple diagram or pseudocode snippet (5-10 lines) illustrating a key aspect of your system design.

2. Linguistic-Visual Mapping (250-300 words):
   a) Explain how your system translates {t['structure']} into visual elements using {t['visualization_technique']}.
   b) Describe how different linguistic features are encoded in the visual representation.
   c) Discuss how {t['neurolinguistic_concept']} influences the visual mapping process.

3. Interpretation and Analysis (250-300 words):
   a) Detail how your AI system interprets and extracts linguistic information from the visual representations.
   b) Explain any machine learning or pattern recognition techniques used in this process.
   c) Discuss potential challenges in accurately interpreting complex linguistic structures from visual data.

4. Neurolinguistic Implications (200-250 words):
   a) Analyze how your system's approach might provide insights into human language processing.
   b) Discuss any parallels between your AI system and theories of neural language representation.
   c) Propose an experiment to test whether your system's visual representations align with human brain activity during language processing.

5. Applications and Extensions (200-250 words):
   a) Propose two potential applications of your system in linguistics research or language technology.
   b) Discuss how your approach could be extended to other linguistic structures or neurolinguistic concepts.
   c) Consider potential benefits and limitations of using visual representations for language processing in AI.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to using AI-generated visual representations of language structures.
   b) Discuss any implications for privacy, cognitive manipulation, or cross-cultural misunderstandings.
   c) Propose guidelines for responsible development and use of such technology.

Ensure your response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Present any diagrams or pseudocode as ASCII art or text-based representations within your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture clearly incorporates {t['structure']}, {t['neurolinguistic_concept']}, and {t['visualization_technique']}.",
            "The response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence.",
            "The linguistic-visual mapping process is well-explained and innovative.",
            "The interpretation and analysis section includes specific machine learning or pattern recognition techniques.",
            "The response addresses neurolinguistic implications and proposes a relevant experiment.",
            "Applications and extensions are thoughtfully considered and scientifically plausible.",
            "Ethical considerations are thoroughly discussed with specific guidelines proposed.",
            "The response is well-structured with clear headings and adheres to the specified word count ranges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
