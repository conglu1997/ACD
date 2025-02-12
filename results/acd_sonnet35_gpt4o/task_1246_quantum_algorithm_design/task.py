import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem": "graph coloring",
                "classical_algorithm": "backtracking",
                "quantum_resource": "quantum annealing",
                "graph_size": "100 nodes",
                "color_count": "4 colors"
            },
            {
                "problem": "prime factorization",
                "classical_algorithm": "general number field sieve",
                "quantum_resource": "quantum Fourier transform",
                "number_size": "1024-bit integer",
                "time_constraint": "polynomial time"
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(problems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm to solve the {t['problem']} problem, leveraging {t['quantum_resource']}. Then, analyze its potential advantages over the classical {t['classical_algorithm']} algorithm. Your algorithm should be able to handle {t['graph_size'] if 'graph_size' in t else t['number_size']} and achieve {t['color_count'] if 'color_count' in t else t['time_constraint']}.

IMPORTANT: Do not use or reference any existing quantum algorithms. Your design must be original.

Your response should include:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the key components and steps of your quantum algorithm.
   b) Explain how it utilizes {t['quantum_resource']} and any other quantum principles.
   c) Provide a high-level pseudocode or circuit diagram of your algorithm.
   d) Discuss any novel features that distinguish it from existing quantum algorithms for this problem.

2. Quantum Mechanics Principles (200-250 words):
   a) Explain the fundamental quantum mechanical principles your algorithm relies on.
   b) Discuss how these principles are leveraged to solve the {t['problem']} problem.
   c) Describe any quantum effects (e.g., superposition, entanglement) crucial to your algorithm's function.

3. Complexity Analysis (200-250 words):
   a) Analyze the time and space complexity of your quantum algorithm.
   b) Compare its complexity to that of the classical {t['classical_algorithm']} algorithm.
   c) Discuss any speedup or efficiency gains your algorithm might offer.
   d) Explain any trade-offs or limitations of your approach.

4. Implementation Considerations (200-250 words):
   a) Describe the quantum hardware requirements for implementing your algorithm.
   b) Discuss potential challenges in realizing your algorithm on current or near-term quantum devices.
   c) Propose methods to mitigate errors or decoherence effects in a physical implementation.

5. Broader Implications (150-200 words):
   a) Discuss the potential impact of your algorithm on the field of {t['problem']}.
   b) Explore how your approach might be extended to related problems or domains.
   c) Speculate on future developments that could enhance or build upon your algorithm.

Ensure your response demonstrates a deep understanding of quantum computing, algorithm design, and the specific problem domain. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific accuracy and plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a novel quantum algorithm design for the {t['problem']} problem, without referencing existing quantum algorithms.",
            f"The algorithm should leverage {t['quantum_resource']} as specified in the instructions.",
            f"The algorithm should be capable of handling {t['graph_size'] if 'graph_size' in t else t['number_size']} and achieve {t['color_count'] if 'color_count' in t else t['time_constraint']}.",
            "The submission should cover all five required sections with appropriate detail and formatting.",
            "The algorithm design should be innovative while maintaining scientific accuracy and plausibility.",
            "The response should demonstrate a deep understanding of quantum computing principles and their application to algorithm design.",
            f"The submission should include a detailed comparison with the classical {t['classical_algorithm']} algorithm, including complexity analysis.",
            "The response should include a high-level pseudocode or circuit diagram of the proposed algorithm.",
            "The implementation considerations should address current quantum hardware limitations and error mitigation strategies.",
            "The response should be well-structured and adhere to the specified word count range of 1050-1300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
