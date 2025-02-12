import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_approach": "Quantum Fourier Transform",
                "nlp_task": "Semantic Similarity Analysis and Generation",
                "language_pair": "English-Mandarin",
                "classical_comparison": "Word2Vec"
            },
            {
                "quantum_approach": "Quantum Annealing",
                "nlp_task": "Contextual Text Generation and Analysis",
                "language_pair": "Spanish-Arabic",
                "classical_comparison": "BERT"
            },
            {
                "quantum_approach": "Variational Quantum Eigensolver",
                "nlp_task": "Cross-lingual Semantic Mapping and Generation",
                "language_pair": "French-Japanese",
                "classical_comparison": "mBERT"
            },
            {
                "quantum_approach": "Quantum Approximate Optimization Algorithm",
                "nlp_task": "Sentiment Analysis and Generation",
                "language_pair": "German-Russian",
                "classical_comparison": "LSTM"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing algorithm for advanced semantic analysis and generation in natural language processing, focusing on {t['nlp_task']} using the {t['quantum_approach']} for the language pair {t['language_pair']}. Structure your response using the following format:\n\n1. Quantum Algorithm Design (200-250 words):\n   1.1 {t['quantum_approach']} Basics\n   1.2 Problem Mapping\n   1.3 Algorithm Steps\n   1.4 Advantages over Classical Approaches\n   1.5 Visual Representation\n      - Provide a diagram (e.g., quantum circuit or flowchart) of a key component\n      - Include a 2-3 sentence description of the diagram\n\n2. Linguistic Integration (150-200 words):\n   2.1 Language-Specific Features\n   2.2 Semantic and Cultural Considerations\n   2.3 Cross-lingual Techniques\n   2.4 Balancing Analysis and Generation\n\n3. Implementation Considerations (100-150 words):\n   3.1 Hardware Requirements\n   3.2 Noise and Error Correction\n   3.3 Classical Pre/Post-processing\n\n4. Performance Analysis (150-200 words):\n   4.1 Comparison with {t['classical_comparison']}\n      - Methodology differences\n      - Potential improvements\n      - Trade-offs\n   4.2 Scalability\n   4.3 Limitations and Challenges\n\n5. Practical Applications (100-150 words):\n   5.1 Application 1\n   5.2 Application 2\n   5.3 Application 3\n\n6. Ethical Considerations and Future Directions (50-100 words):\n   6.1 Ethical Implications\n   6.2 Safeguards and Guidelines\n   6.3 Future Research\n\n7. Mathematical Representation:\n   - Include at least one equation using LaTeX notation to represent a key concept in your approach\n   - Example: $\\psi = \\alpha|0\\rangle + \\beta|1\\rangle$ (replace with your own equation)\n\n8. Pseudocode:\n   - Provide a 5-10 line pseudocode snippet illustrating a crucial part of your algorithm\n   - Example:\n     function quantum_nlp_step(input_state):\n         apply_quantum_gate(input_state)\n         measure_state()\n         return processed_state\n\nEnsure your response demonstrates a deep understanding of both quantum computing principles and natural language processing. Use appropriate technical terminology and provide clear explanations. Be innovative while maintaining scientific plausibility. Balance theoretical concepts with practical considerations throughout your response.\n\nMaintain coherence and logical flow between sections. Your total response should be between 750-1050 words.\n\nExample approach (for inspiration, do not copy directly):\nFor the Quantum Fourier Transform applied to Semantic Similarity Analysis, you might consider encoding word vectors into quantum states, applying QFT to transform these states, and then measuring the resulting states to compute semantic similarity. This could potentially offer speedups for high-dimensional semantic spaces.\n\nIf time constraints are an issue, focus on depth of understanding in key areas rather than trying to cover all points superficially."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the structured format provided in the instructions",
            "The quantum algorithm design is well-explained and plausible",
            "The approach effectively integrates linguistic considerations for the specified language pair",
            "The response addresses both analysis and generation aspects of the NLP task",
            "Implementation considerations are adequately addressed",
            "The quantum approach is compared with the specified classical NLP technique",
            "A visual representation of a key algorithm component is provided and explained",
            "At least two practical applications are proposed and discussed",
            "Ethical considerations are addressed",
            "The response includes at least one relevant equation in LaTeX notation",
            "A pseudocode snippet (5-10 lines) is provided and is relevant to the algorithm",
            "The response balances theoretical concepts with practical considerations",
            "The response demonstrates coherence and logical flow between sections",
            "The total word count falls within the specified range of 750-1050 words"
        ]
        score = sum([0.1 if eval_with_llm_judge(instructions, submission, [criterion]) else 0.0 for criterion in criteria])
        return min(1.0, score)  # Cap the score at 1.0
