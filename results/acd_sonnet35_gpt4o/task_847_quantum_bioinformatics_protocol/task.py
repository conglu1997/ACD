import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_problems = [
            {
                "name": "Protein Folding Prediction",
                "description": "Predict the three-dimensional structure of a protein from its amino acid sequence"
            },
            {
                "name": "Gene Regulatory Network Analysis",
                "description": "Analyze and predict the behavior of complex gene regulatory networks"
            }
        ]
        
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling"
        ]
        
        return {
            "1": {
                "problem": random.choice(biological_problems),
                "principle": random.choice(quantum_principles)
            },
            "2": {
                "problem": random.choice(biological_problems),
                "principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing protocol for analyzing and manipulating biological information at the molecular level, then apply it to solve the problem of {t['problem']['name']}. Your protocol should incorporate the quantum principle of {t['principle']}. Your response should include:

1. Quantum-Biological Interface (250-300 words):
   a) Describe how your protocol translates biological information into quantum states.
   b) Explain how it incorporates the specified quantum principle.
   c) Discuss any novel quantum operations or gates you've designed for biological data processing.

2. Protocol Design (300-350 words):
   a) Provide a detailed description of your quantum bioinformatics protocol.
   b) Explain the step-by-step process of how it analyzes and manipulates biological information.
   c) Discuss how your protocol addresses the specific challenges of {t['problem']['description']}.

3. Theoretical Implementation (200-250 words):
   a) Describe the theoretical quantum hardware required for your protocol.
   b) Explain any quantum error correction methods you would employ.
   c) Discuss the scalability of your protocol for large biological datasets.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum approach to classical bioinformatics methods for solving the same problem.
   b) Discuss the potential advantages and limitations of your quantum protocol.
   c) Estimate the potential speedup or improvement in accuracy over classical methods.

5. Ethical Implications and Future Applications (150-200 words):
   a) Discuss any ethical considerations related to your quantum bioinformatics protocol.
   b) Propose two potential future applications of your protocol in other areas of biology or medicine.

Ensure your response demonstrates a deep understanding of quantum computing principles, molecular biology, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide explanations where necessary.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, molecular biology, and information theory, using appropriate terminology from all fields.",
            f"The quantum bioinformatics protocol effectively incorporates the specified quantum principle ({t['principle']}) and addresses the given biological problem ({t['problem']['name']}).",
            "The protocol design is innovative, scientifically plausible, and thoroughly explained.",
            "The comparative analysis shows insightful understanding of both quantum and classical approaches to the problem.",
            "The response is well-structured, following the specified format with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
