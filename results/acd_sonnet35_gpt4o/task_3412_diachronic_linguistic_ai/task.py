import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                'name': 'Democracy',
                'domain': 'Political Science',
                'origin': 'Ancient Greece',
                'related_concept': 'Freedom'
            },
            {
                'name': 'Privacy',
                'domain': 'Social Studies',
                'origin': 'Industrial Revolution',
                'related_concept': 'Security'
            },
            {
                'name': 'Consciousness',
                'domain': 'Philosophy',
                'origin': 'Ancient civilizations',
                'related_concept': 'Self'
            },
            {
                'name': 'Sustainability',
                'domain': 'Environmental Science',
                'origin': '20th century',
                'related_concept': 'Balance'
            }
        ]
        
        tasks = random.sample(concepts, 2)
        return {str(i+1): {'concept': concept} for i, concept in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of modeling and simulating the evolution of language and conceptual structures across human history, then use it to analyze the development of the concept of {t['concept']['name']} and predict its future evolution. Your task should address the following components:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling language and conceptual evolution.
   b) Explain how your system integrates knowledge from linguistics, cognitive science, and historical analysis.
   c) Detail how your system models the interaction between language, culture, and conceptual development.
   d) Provide a high-level diagram or pseudocode illustrating a key process in your system.

2. Historical Analysis (250-300 words):
   a) Use your AI system to trace the evolution of the concept of {t['concept']['name']} from its origin in {t['concept']['origin']} to the present day.
   b) Identify key linguistic and cultural factors that influenced the concept's development.
   c) Analyze how the meaning and connotations of the concept have changed over time.
   d) Discuss any challenges in modeling this concept's evolution and how your system addresses them.

3. Cross-linguistic Comparison (200-250 words):
   a) Compare how the concept of {t['concept']['name']} has evolved in at least three different language families.
   b) Discuss any significant divergences or convergences in the concept's development across cultures.
   c) Explain how your AI system accounts for these cross-linguistic and cross-cultural variations.

4. Cognitive Implications (200-250 words):
   a) Analyze how the evolution of the concept of {t['concept']['name']} reflects changes in human cognition and societal structures.
   b) Discuss how your AI system models the relationship between linguistic evolution and cognitive development.
   c) Propose a hypothesis about how this concept has influenced or been influenced by human thought patterns.

5. Future Prediction (250-300 words):
   a) Use your AI system to predict potential future evolutions of the concept of {t['concept']['name']} over the next century.
   b) Provide at least three different scenarios for how the concept might change, with reasoning for each.
   c) Discuss how these potential changes might affect the domain of {t['concept']['domain']}.
   d) Explain the limitations and uncertainties in your AI's predictive capabilities.

6. Conceptual Relationship Analysis (200-250 words):
   a) Analyze the relationship between {t['concept']['name']} and its related concept {t['concept']['related_concept']}.
   b) Explain how your AI system models the co-evolution of these related concepts.
   c) Predict how changes in one concept might influence the other in the future.

7. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI to model and predict language and conceptual evolution.
   b) Address concerns related to cultural bias and the potential influence of such predictions on society.
   c) Propose guidelines for responsible use of your AI system in linguistic and cognitive research.

8. Interdisciplinary Applications (150-200 words):
   a) Suggest two potential applications of your AI system in fields outside of linguistics and cognitive science.
   b) Briefly explain how these applications could benefit from understanding the evolution of language and concepts.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, historical analysis, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1700-2100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, historical analysis, and artificial intelligence.",
            f"The AI system design effectively addresses the modeling and simulation of the evolution of the concept of {t['concept']['name']}.",
            "The historical analysis and cross-linguistic comparison are thorough and insightful.",
            "The future predictions are creative, well-reasoned, and grounded in the historical analysis.",
            f"The relationship between {t['concept']['name']} and {t['concept']['related_concept']} is thoughtfully analyzed.",
            "The ethical considerations and interdisciplinary applications are thoughtfully discussed.",
            "The response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
