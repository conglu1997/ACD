import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "Graph Coloring",
            "Integer Factorization",
            "Traveling Salesman Problem",
            "Database Search",
            "Machine Learning Classification"
        ]
        return {
            "1": {"problem": random.choice(problems)},
            "2": {"problem": random.choice(problems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hybrid quantum-classical algorithm for the {t['problem']} problem. Your response should include:\n\n1. Algorithm Design (300-350 words):\n   a) Describe the key components of your hybrid quantum-classical algorithm.\n   b) Explain which parts of the problem are solved classically and which quantum.\n   c) Detail the quantum operations or subroutines used in your algorithm.\n   d) Provide a high-level pseudocode or flowchart of your algorithm.\n\n2. Complexity Analysis (250-300 words):\n   a) Analyze the time and space complexity of your hybrid algorithm.\n   b) Compare the complexity with purely classical and purely quantum approaches.\n   c) Discuss any speedup or advantage gained by the hybrid approach.\n\n3. Implementation Considerations (200-250 words):\n   a) Describe the quantum hardware requirements for your algorithm.\n   b) Discuss any challenges in implementing the algorithm on current quantum devices.\n   c) Propose methods to mitigate errors or decoherence effects.\n\n4. Comparative Analysis (200-250 words):\n   a) Compare your hybrid approach with the best known classical and quantum algorithms for the problem.\n   b) Discuss the trade-offs between your approach and others.\n   c) Identify scenarios where your hybrid approach would be preferable.\n\n5. Potential Applications and Extensions (150-200 words):\n   a) Suggest potential real-world applications of your hybrid algorithm.\n   b) Propose an extension or modification to your algorithm for a related problem.\n   c) Discuss how your approach might inform future quantum-classical algorithm design.\n\nEnsure your response demonstrates a deep understanding of both quantum and classical computing principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1100-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing principles and classical algorithm design",
            "The proposed hybrid algorithm is logically consistent and well-explained",
            "The complexity analysis is thorough and compares the hybrid approach with classical and quantum alternatives",
            "The implementation considerations address realistic quantum hardware constraints",
            "The comparative analysis shows a deep understanding of the problem and existing solutions",
            "The potential applications and extensions are innovative and well-reasoned",
            "The response shows originality in approach and generates novel insights or research directions"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
