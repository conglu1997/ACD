import random
from typing import List, Optional

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "focus": "semantic_analysis",
                "quantum_concept": "entanglement",
                "nlp_task": "sentiment analysis",
                "sample_sentence": "The movie was both exciting and disappointing.",
                "quantum_state": "|ψ⟩ = (|00⟩ + |11⟩) / √2"
            },
            "2": {
                "focus": "language_generation",
                "quantum_concept": "superposition",
                "nlp_task": "text summarization",
                "sample_text": "Quantum computing leverages the principles of quantum mechanics to process information. Unlike classical computers that use bits, quantum computers use quantum bits or qubits. This allows for potentially exponential speedups in certain computational tasks.",
                "quantum_state": "|ψ⟩ = α|0⟩ + β|1⟩, where |α|² + |β|² = 1"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system for natural language processing that utilizes the quantum concept of {t['quantum_concept']} to enhance {t['nlp_task']}, focusing on {t['focus']}. Your response should include:

1. System Architecture (300-350 words):
   a) Key components of your quantum NLP system
   b) How quantum {t['quantum_concept']} is integrated into the NLP process
   c) Interaction between quantum and classical components
   d) A quantum circuit diagram or schematic representation (describe this textually, using ASCII characters if necessary)

2. Quantum-Linguistic Interface (250-300 words):
   a) Mechanism for encoding linguistic information into quantum states
   b) How {t['quantum_concept']} is utilized in processing language
   c) Novel quantum operations or algorithms for {t['nlp_task']}
   d) Example using the sample sentence/text "{t['sample_sentence' if 'sample_sentence' in t else 'sample_text']}" and the quantum state {t['quantum_state']}

3. NLP Process Enhancement (300-350 words):
   a) Step-by-step process of how your system performs {t['nlp_task']}
   b) Specific advantages gained by using quantum {t['quantum_concept']}
   c) Comparison with classical NLP methods for {t['nlp_task']}
   d) Potential improvements in accuracy or efficiency (with quantitative estimates)

4. Challenges and Solutions (250-300 words):
   a) Three major technical challenges in implementing your system
   b) Proposed solutions or approaches to address each challenge
   c) Limitations of your approach and potential future improvements

5. Practical Applications (200-250 words):
   a) Two potential real-world applications of your quantum NLP system
   b) How these applications could impact current NLP technologies
   c) Potential societal implications of advanced quantum NLP systems

6. Ethical Considerations (200-250 words):
   a) Potential ethical concerns related to quantum-enhanced NLP
   b) Proposed guidelines for responsible development and use
   c) Recommendations for policymakers and researchers

Ensure your response demonstrates a deep understanding of both quantum computing and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and include your quantum circuit diagram or schematic representation within the relevant section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and natural language processing concepts.",
            f"The proposed system integrates quantum {t['quantum_concept']} with {t['nlp_task']} in a scientifically plausible manner.",
            "The response includes innovative ideas for quantum-linguistic interfaces and NLP process enhancements.",
            f"The submission properly uses the provided sample sentence/text and quantum state in explaining the {t['nlp_task']} process.",
            "The response includes a clear description or representation of a quantum circuit or schematic diagram.",
            "The submission addresses potential challenges, ethical considerations, and practical applications of the proposed system.",
            "The response is well-structured, following the outlined sections, and within the specified word count range of 1500-1800 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
