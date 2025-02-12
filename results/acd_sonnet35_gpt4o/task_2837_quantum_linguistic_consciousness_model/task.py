import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            {
                'phenomenon': 'Synesthesia',
                'quantum_concept': 'Quantum entanglement',
                'linguistic_feature': 'Metaphor'
            },
            {
                'phenomenon': 'Déjà vu',
                'quantum_concept': 'Quantum superposition',
                'linguistic_feature': 'Temporal deixis'
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(phenomena)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-linguistic AI system for modeling and interpreting consciousness, then apply it to analyze the following phenomenon of human cognition:

Phenomenon: {t['phenomenon']}
Quantum Concept to Incorporate: {t['quantum_concept']}
Linguistic Feature to Analyze: {t['linguistic_feature']}

Your task has the following components:

1. Quantum-Linguistic Consciousness Model (300-350 words):
   a) Describe the key components and architecture of your AI system for modeling consciousness.
   b) Explain how your model integrates quantum mechanics, linguistics, and artificial intelligence.
   c) Detail how your system represents and processes conscious experiences.
   d) Propose a novel mechanism for how quantum effects might influence conscious linguistic processing.

2. Theoretical Framework (250-300 words):
   a) Outline the theoretical basis for your model, drawing from quantum physics, linguistics, and cognitive science.
   b) Explain how your model addresses the hard problem of consciousness.
   c) Discuss how your approach differs from classical theories of consciousness and language.

3. Application to the Given Phenomenon (250-300 words):
   a) Apply your quantum-linguistic AI system to analyze the specified phenomenon of human cognition.
   b) Explain how the assigned quantum concept is used in your model to interpret this phenomenon.
   c) Describe how your system would process and represent the linguistic aspects of this experience.
   d) Propose a testable hypothesis about the phenomenon based on your model's analysis.

4. Quantum-Linguistic Processing (200-250 words):
   a) Describe in detail how your system incorporates the specified quantum concept in its linguistic processing.
   b) Explain how this quantum-linguistic integration provides insights into the given phenomenon.
   c) Discuss any potential quantum effects on language that your model predicts or explores.

5. Implications and Predictions (200-250 words):
   a) Discuss the broader implications of your model for our understanding of consciousness and language.
   b) Propose three testable predictions that your model makes about human cognition or linguistic behavior.
   c) Explain how these predictions differ from those of classical cognitive or linguistic theories.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss ethical implications of modeling consciousness with AI and quantum systems.
   b) Address potential risks or misuses of this technology.
   c) Acknowledge limitations of your model and areas needing further development.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, artificial intelligence, and cognitive science. Be creative and speculative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, linguistics, artificial intelligence, and cognitive science.",
            "The proposed quantum-linguistic AI system for modeling consciousness is creative, internally consistent, and scientifically plausible.",
            "The model effectively integrates the specified quantum concept and linguistic feature in its analysis of the given cognitive phenomenon.",
            "The response includes novel mechanisms and approaches in modeling consciousness and language processing.",
            "The implications and predictions derived from the model are logical and demonstrate original thinking.",
            "The response addresses ethical considerations and limitations of the proposed system.",
            "The response adheres to the specified format and word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
