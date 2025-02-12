import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_structures = [
            {
                'structure': 'syntax trees',
                'quantum_concept': 'superposition',
                'cognitive_process': 'sentence parsing',
                'example_sentence': 'The cat chased the mouse that ate the cheese.'
            },
            {
                'structure': 'semantic networks',
                'quantum_concept': 'entanglement',
                'cognitive_process': 'conceptual association',
                'example_sentence': 'The scientist conducted groundbreaking research on climate change.'
            }
        ]
        return {str(i+1): structure for i, structure in enumerate(random.sample(linguistic_structures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to model and analyze {t['structure']} in natural language, incorporating the quantum concept of {t['quantum_concept']}. Then, use this system to explore theories of {t['cognitive_process']} in human language processing. Your response should include:

1. Quantum Linguistic System Architecture (300-350 words):
   a) Describe the key components of your quantum computing system for linguistic analysis.
   b) Explain how it incorporates principles from quantum computing, linguistics, and cognitive science.
   c) Detail how your system represents and processes {t['structure']} using quantum states and operations.
   d) Discuss how the quantum concept of {t['quantum_concept']} is utilized in your model.

2. Linguistic Representation and Processing (250-300 words):
   a) Explain how your system encodes linguistic information into quantum states.
   b) Describe the quantum operations used to manipulate and analyze {t['structure']}.
   c) Provide a specific example of how your system would process the sentence: "{t['example_sentence']}"
   d) Discuss any advantages your quantum approach might have over classical computing methods for linguistic analysis.

3. Cognitive Model Integration (250-300 words):
   a) Describe how your quantum linguistic system models the cognitive process of {t['cognitive_process']}.
   b) Explain how quantum phenomena in your system might correspond to cognitive phenomena in human language processing.
   c) Discuss how your model accounts for known empirical findings in psycholinguistics related to {t['cognitive_process']}.
   d) Propose a novel hypothesis about {t['cognitive_process']} that arises from your quantum linguistic model.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test a prediction of your quantum linguistic model about {t['cognitive_process']}.
   b) Describe the experimental methodology, including variables, procedures, and expected results.
   c) Explain how this experiment could distinguish between your quantum model and classical models of language processing.

5. Implications and Future Directions (200-250 words):
   a) Discuss the potential implications of your quantum linguistic system for our understanding of human language and cognition.
   b) Explore how this approach might contribute to advancements in natural language processing or cognitive computing.
   c) Propose an extension of your system to address another aspect of language or cognition not covered in your initial design.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical concerns related to using quantum computing systems to model human cognitive processes.
   b) Address any implications for privacy, free will, or human uniqueness that your system might raise.
   c) Propose guidelines for the responsible development and use of quantum cognitive models.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility throughout your response.

Format your response as follows:
1. Begin each section with a clear heading (e.g., "1. Quantum Linguistic System Architecture:").
2. Use subheadings (a, b, c, d) within each section as outlined above.
3. Ensure that each section adheres to the specified word count range.
4. Provide citations for any referenced research or theories.
5. Include a brief conclusion (50-100 words) summarizing the key points of your quantum linguistic system.

Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science, particularly in relation to {t['structure']}, {t['quantum_concept']}, and {t['cognitive_process']}.",
            "The quantum linguistic system architecture is well-explained, plausible, and integrates concepts from all relevant fields.",
            f"The linguistic representation and processing section provides a clear and innovative approach to analyzing language using quantum computing, including a specific example using the sentence: '{t['example_sentence']}'",
            "The cognitive model integration effectively connects the quantum linguistic system to theories of human language processing and proposes a novel hypothesis.",
            "The proposed experiment is well-designed, relevant to testing the quantum linguistic model, and distinguishes between quantum and classical approaches.",
            "The implications and future directions section provides insightful discussion on the potential impact of this approach and proposes a relevant extension.",
            "Ethical considerations are thoughtfully addressed, demonstrating awareness of broader implications and proposing responsible guidelines.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the specified format, including proper headings, subheadings, and a brief conclusion.",
            "The total word count falls within the specified range of 1400-1750 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
