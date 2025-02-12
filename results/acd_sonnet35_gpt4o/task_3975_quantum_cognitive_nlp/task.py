import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_process': 'Analogical reasoning',
                'quantum_concept': 'Superposition',
                'literary_text': 'Borges\'s "The Garden of Forking Paths"'
            },
            {
                'cognitive_process': 'Conceptual blending',
                'quantum_concept': 'Entanglement',
                'literary_text': 'Calvino\'s "Invisible Cities"'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing system that models the cognitive process of {t['cognitive_process']}, incorporating the quantum concept of {t['quantum_concept']}. Then, apply your system to analyze {t['literary_text']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired NLP system.
   b) Explain how your system models {t['cognitive_process']} using quantum computing principles.
   c) Detail how you incorporate {t['quantum_concept']} into your language processing algorithms.
   d) Discuss how your system differs from classical NLP approaches.

2. Quantum-Cognitive Integration (200-250 words):
   a) Explain the theoretical basis for mapping {t['quantum_concept']} to {t['cognitive_process']}.
   b) Describe any novel algorithms or techniques you've developed for this integration.
   c) Discuss how your approach might provide insights into human cognition.

3. Literary Analysis Process (200-250 words):
   a) Outline how your system would analyze {t['literary_text']}.
   b) Explain how the quantum-cognitive approach enhances literary analysis.
   c) Describe specific features or patterns your system would identify in the text.

4. Sample Analysis Output (200-250 words):
   a) Provide a brief excerpt (2-3 sentences) from {t['literary_text']}.
   b) Present a sample analysis output from your system for this excerpt.
   c) Interpret the results, highlighting insights gained from your quantum-cognitive approach.
   d) Provide a specific example of how your system would process a key phrase or sentence from the excerpt, demonstrating the quantum-cognitive analysis in action.

5. Cognitive Science Implications (150-200 words):
   a) Discuss what your system's analysis reveals about {t['cognitive_process']}.
   b) Propose a hypothesis about human cognition that could be tested using your system.

6. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or biases in your quantum-cognitive NLP system.
   b) Discuss ethical implications of using quantum-inspired models to analyze human cognition and creativity.
   c) Propose guidelines for responsible development and use of such technology.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and natural language processing. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative and original in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Address all parts of each section thoroughly. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing concepts, cognitive science, and natural language processing.",
            f"The system architecture effectively incorporates {t['quantum_concept']} into NLP algorithms.",
            f"The quantum-cognitive integration provides a plausible mapping between {t['quantum_concept']} and {t['cognitive_process']}.",
            f"The literary analysis process for {t['literary_text']} is well-explained and leverages the quantum-cognitive approach.",
            "The sample analysis output provides meaningful insights derived from the quantum-cognitive system.",
            "A specific example of processing a key phrase or sentence is provided, demonstrating the quantum-cognitive analysis in action.",
            "The response addresses cognitive science implications and proposes a testable hypothesis.",
            "Limitations, ethical considerations, and responsible development guidelines are thoughtfully discussed.",
            "The response is innovative and original while maintaining scientific plausibility.",
            "The response is well-structured, following the required format and word count.",
            "All parts of each section are addressed thoroughly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
