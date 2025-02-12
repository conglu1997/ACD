import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "justice",
            "beauty",
            "time",
            "consciousness",
            "freedom"
        ]
        cultural_contexts = [
            "Ancient Greece",
            "Renaissance Europe",
            "Pre-colonial Mesoamerica",
            "Industrial Revolution Era",
            "Contemporary Global Society"
        ]
        
        tasks = {}
        for i in range(2):
            concept = random.choice(abstract_concepts)
            context = random.choice(cultural_contexts)
            tasks[str(i+1)] = {
                "abstract_concept": concept,
                "cultural_context": context
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of simulating the co-evolution of language and culture over time, then use it to explore how the abstract concept of {t['abstract_concept']} emerges and changes, with a focus on {t['cultural_context']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating language and cultural co-evolution.
   b) Explain how your system integrates linguistic, cultural, and cognitive models.
   c) Detail any novel approaches or algorithms used in your design.
   d) Include a brief description of a diagram representing your system's architecture.

2. Co-evolution Simulation (250-300 words):
   a) Explain how your system models the interaction between language and culture over time.
   b) Describe the mechanisms for simulating linguistic and cultural change.
   c) Discuss how your system accounts for historical and social factors in its simulations.

3. Abstract Concept Analysis (250-300 words):
   a) Detail how your system tracks and analyzes the evolution of the specified abstract concept.
   b) Provide an example of how the concept might change over time in the given cultural context.
   c) Explain how your system distinguishes between linguistic and conceptual changes.

4. Data and Training (200-250 words):
   a) Describe the types of data your system requires for accurate simulations.
   b) Explain your approach to training the system on historical and cultural information.
   c) Discuss how you address challenges related to data scarcity or bias in historical records.

5. Validation and Evaluation (200-250 words):
   a) Propose methods for validating your system's simulations against historical evidence.
   b) Describe how you would evaluate the accuracy of your system's predictions or reconstructions.
   c) Discuss potential limitations or biases in your evaluation approach.

6. Interdisciplinary Insights (150-200 words):
   a) Explain how your system could contribute to our understanding of cognitive science and anthropology.
   b) Propose a novel research question that could be explored using your system.

7. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to simulating cultural and linguistic evolution.
   b) Discuss how your system addresses concerns about cultural sensitivity and representation.
   c) Propose guidelines for the responsible use of such AI systems in academic and public contexts.

8. Case Study (200-250 words):
   Provide a detailed case study demonstrating how your system would simulate the evolution of the concept of {t['abstract_concept']} in {t['cultural_context']}. Include specific examples of linguistic and cultural changes over time.

Ensure your response demonstrates a deep understanding of linguistics, anthropology, cognitive science, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1700-2150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, anthropology, cognitive science, and machine learning",
            "The proposed AI system effectively integrates models of language, culture, and cognition",
            "The approach to simulating co-evolution of language and culture is innovative and scientifically plausible",
            "The analysis of abstract concept evolution is thorough and considers multiple factors",
            "The proposed validation and evaluation methods are appropriate and address potential limitations",
            "The response identifies relevant ethical considerations and proposes thoughtful guidelines",
            "The writing is clear, well-structured, and uses appropriate technical terminology",
            "The case study provides a concrete and detailed example of the system's application"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
