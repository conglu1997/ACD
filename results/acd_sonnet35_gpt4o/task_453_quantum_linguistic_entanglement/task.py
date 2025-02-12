import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'Superposition',
                'linguistic_element': 'Ambiguity',
                'application_domain': 'Poetry'
            },
            {
                'quantum_concept': 'Entanglement',
                'linguistic_element': 'Semantic relationships',
                'application_domain': 'Dialogue'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a linguistic system based on the quantum concept of {t['quantum_concept']}, focusing on the linguistic element of {t['linguistic_element']}. Then, apply this system to generate and interpret quantum-inspired text in the domain of {t['application_domain']}. Your response should include:

1. System Design (250-300 words):
   a) Explain how your linguistic system incorporates the principles of {t['quantum_concept']}, including concepts such as wave function, quantum states, and measurement.
   b) Describe how it manipulates {t['linguistic_element']} to create quantum-like effects in language.
   c) Provide 3-4 key rules or principles of your system, relating them to specific quantum mechanical phenomena.

2. Text Generation (200-250 words):
   a) Using your system, generate a short {t['application_domain']} piece (4-6 sentences or lines).
   b) Explain how each part of your text demonstrates the quantum-linguistic principles you've defined.
   c) Identify specific quantum analogies or metaphors used in your text.

3. Interpretation Guidelines (200-250 words):
   a) Provide a set of guidelines for interpreting text created with your system.
   b) Explain how these guidelines reflect both quantum and linguistic aspects.
   c) Include at least one mathematical or logical formalism to represent your interpretation process.

4. Analysis (250-300 words):
   a) Analyze your generated text using your interpretation guidelines.
   b) Discuss how the quantum-inspired elements affect the meaning or reader's experience of the text.
   c) Compare and contrast your quantum-linguistic approach with traditional linguistic analysis.
   d) Propose a hypothetical experiment to test the effectiveness of your quantum-linguistic system in enhancing language understanding or generation.

5. Quantum-Classical Correlation (150-200 words):
   a) Explain how your system might provide insights into the relationship between quantum phenomena and natural language processing or understanding.
   b) Discuss potential implications of your system for quantum computing applications in linguistics or vice versa.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics. Be creative in your system design and text generation while maintaining scientific plausibility. Use appropriate terminology from both fields throughout your answer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The linguistic system clearly incorporates principles of {t['quantum_concept']}, using accurate quantum mechanics terminology and concepts.",
            f"The generated text effectively demonstrates the quantum-linguistic principles in the domain of {t['application_domain']}, with clear quantum analogies or metaphors.",
            "The interpretation guidelines and analysis show a deep understanding of both quantum concepts and linguistic elements, including at least one mathematical or logical formalism.",
            "The response demonstrates creativity and scientific plausibility in connecting quantum mechanics and linguistics, including a hypothetical experiment to test the system's effectiveness.",
            "The quantum-classical correlation discussion provides insightful connections between quantum phenomena and natural language processing, with plausible implications for future applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
