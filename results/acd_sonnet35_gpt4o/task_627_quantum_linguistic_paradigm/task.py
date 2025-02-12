import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "wave function collapse",
            "quantum tunneling"
        ]
        linguistic_elements = [
            "syntax",
            "semantics",
            "pragmatics",
            "phonology"
        ]
        cognitive_aspects = [
            "memory formation",
            "decision making",
            "language acquisition",
            "conceptual blending"
        ]
        communication_contexts = [
            "cross-cultural dialogue",
            "political discourse",
            "scientific collaboration",
            "artistic expression"
        ]
        
        tasks = [
            {
                "quantum_concept": qc,
                "linguistic_element": le,
                "cognitive_aspect": ca,
                "communication_context": cc
            }
            for qc in quantum_concepts
            for le in linguistic_elements
            for ca in cognitive_aspects
            for cc in communication_contexts
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical linguistic framework based on the quantum mechanical principle of {t['quantum_concept']}, focusing on the linguistic element of {t['linguistic_element']}, analyze its implications for {t['cognitive_aspect']}, and explore its potential impact on {t['communication_context']}. Your response should include:

1. Conceptual Foundation (200-250 words):
   a) Explain the quantum mechanical principle of {t['quantum_concept']} in layman's terms.
   b) Describe the linguistic element of {t['linguistic_element']} and its role in language.
   c) Briefly discuss how {t['cognitive_aspect']} relates to language processing.
   d) Explain the key characteristics of {t['communication_context']}.

2. Quantum Linguistic Framework (300-350 words):
   a) Design a hypothetical linguistic framework that applies {t['quantum_concept']} to {t['linguistic_element']}.
   b) Explain how this framework differs from traditional linguistic theories.
   c) Provide at least two concrete examples of how language would function in this framework.
   d) Describe a potential mathematical or formal representation of your framework (e.g., equations, diagrams, or logical formulations).

3. Cognitive Implications (200-250 words):
   a) Analyze how your quantum linguistic framework might influence {t['cognitive_aspect']}.
   b) Discuss potential benefits and challenges this framework presents for human cognition.
   c) Propose a hypothetical experiment to test the effects of your framework on {t['cognitive_aspect']}.

4. Communication Analysis (200-250 words):
   a) Explore how communication in the context of {t['communication_context']} would change if language operated according to your quantum linguistic framework.
   b) Discuss potential implications for interpersonal relationships and social structures in this specific context.
   c) Provide a concrete example of how a typical interaction in {t['communication_context']} would unfold under your framework.

5. Technological Applications (150-200 words):
   a) Propose two potential applications of your quantum linguistic framework in language technology or artificial intelligence, specifically relevant to {t['communication_context']}.
   b) Discuss how these applications might advance our understanding of language or improve human-computer interaction in this context.

6. Philosophical and Ethical Considerations (150-200 words):
   a) Discuss the philosophical implications of your framework for our understanding of reality and consciousness.
   b) Address any ethical concerns or potential misuses of this framework, particularly in the context of {t['communication_context']}.

7. Interdisciplinary Connections (100-150 words):
   a) Explain how your framework integrates concepts from quantum mechanics, linguistics, cognitive science, and the field most relevant to {t['communication_context']}.
   b) Suggest two other scientific fields that might benefit from or contribute to the development of this framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, cognitive science, and the specific communication context. Be creative and speculative in your design while maintaining scientific plausibility and rigor. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum mechanical principle and its potential application to linguistics.",
            "The proposed linguistic framework is creative, coherent, and plausibly applies the quantum concept to the linguistic element.",
            "The analysis of cognitive implications is insightful and considers both potential benefits and challenges.",
            "The communication analysis is thorough and specifically addresses the given communication context.",
            "The technological applications are relevant to the communication context and logically derived from the proposed framework.",
            "The philosophical and ethical considerations demonstrate critical thinking about the broader implications of the framework, especially in the given communication context.",
            "The response effectively integrates concepts from quantum mechanics, linguistics, cognitive science, and the field relevant to the communication context.",
            "The examples and proposed experiments are concrete, relevant, and demonstrate the practical implications of the framework.",
            "The response adheres to the specified word count and structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0