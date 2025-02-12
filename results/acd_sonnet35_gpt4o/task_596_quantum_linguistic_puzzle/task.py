import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum interference"
        ]
        linguistic_elements = [
            "syntax",
            "semantics",
            "pragmatics",
            "morphology"
        ]
        nlp_applications = [
            "machine translation",
            "sentiment analysis",
            "text summarization",
            "named entity recognition"
        ]
        
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_element": random.choice(linguistic_elements),
                "nlp_application": random.choice(nlp_applications)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_element": random.choice(linguistic_elements),
                "nlp_application": random.choice(nlp_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and solve a linguistic puzzle based on the quantum computing principle of {t['quantum_concept']}, focusing on the linguistic element of {t['linguistic_element']}. Then, analyze its implications for {t['nlp_application']} in natural language processing.

Brief explanations:
- {t['quantum_concept']}: [Insert a one-sentence explanation of the quantum concept]
- {t['linguistic_element']}: [Insert a one-sentence explanation of the linguistic element]

Your response should include:

1. Puzzle Design (200-250 words):
   a) Explain how your puzzle incorporates the quantum principle of {t['quantum_concept']}.
   b) Describe how the puzzle relates to the linguistic element of {t['linguistic_element']}.
   c) Provide the puzzle statement or rules.
   d) Include at least one example sentence or phrase that demonstrates the quantum-linguistic concept in action.

2. Puzzle Solution (150-200 words):
   a) Solve your own puzzle, explaining each step in detail.
   b) Discuss any challenges or insights gained from solving the puzzle.
   c) Explain how the solution reflects both the quantum principle and the linguistic element.

3. Quantum-Linguistic Analysis (200-250 words):
   a) Analyze the relationship between the quantum principle and the linguistic element in your puzzle.
   b) Discuss any novel insights or perspectives gained from this quantum-linguistic approach.
   c) Compare and contrast how this approach differs from traditional linguistic analysis.
   d) Cite at least one relevant academic source or research paper to support your analysis.

4. NLP Implications (200-250 words):
   a) Explore how the insights from your puzzle could be applied to {t['nlp_application']}.
   b) Propose a specific enhancement or novel approach to {t['nlp_application']} based on your quantum-linguistic puzzle.
   c) Discuss potential challenges and benefits of implementing this approach.
   d) Provide a hypothetical example of how this approach could improve current {t['nlp_application']} systems.

5. Future Research Directions (100-150 words):
   a) Suggest two potential research questions or experiments that could further explore the intersection of quantum computing, linguistics, and natural language processing based on your puzzle and analysis.
   b) Briefly outline a methodology for investigating one of these research questions.

Ensure your response demonstrates a deep understanding of both quantum computing principles and linguistic concepts. Be creative and original in your approach while maintaining scientific plausibility. Use clear headings for each section of your response and number your paragraphs within each section.

Your total response should be between 850-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The puzzle effectively incorporates the quantum principle of {t['quantum_concept']} and relates to the linguistic element of {t['linguistic_element']}, with a clear example demonstrating the concept.",
            "The puzzle solution is clear, logical, and demonstrates a deep understanding of both quantum and linguistic concepts.",
            "The quantum-linguistic analysis provides novel insights, compares the approach with traditional linguistic analysis, and cites at least one relevant academic source.",
            f"The implications for {t['nlp_application']} are well-reasoned, innovative, and include a specific, hypothetical example of improvement.",
            "The proposed future research directions are relevant, thought-provoking, and include a brief outline of a research methodology.",
            "The response includes all required elements, adheres to the specified word count and formatting guidelines, and demonstrates exceptional creativity and interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
