import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "name": "Protein Folding Prediction",
                "description": "Develop a quantum algorithm to predict the three-dimensional structure of proteins based on their amino acid sequences."
            },
            {
                "name": "Cryptographic Hash Function Inversion",
                "description": "Create a quantum algorithm to efficiently find input values that produce a given hash output, potentially impacting cryptographic security."
            },
            {
                "name": "Climate Model Optimization",
                "description": "Design a quantum algorithm to optimize complex climate models, potentially improving the accuracy of long-term climate predictions."
            },
            {
                "name": "Financial Portfolio Optimization",
                "description": "Develop a quantum algorithm for real-time optimization of large-scale financial portfolios, considering multiple constraints and risk factors."
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm to solve the following computational problem: {t['name']}. {t['description']}

Your response should include the following sections:

1. Problem Analysis (200-250 words):
   a) Analyze the given computational problem and its current classical approaches.
   b) Explain why a quantum approach might be beneficial for this problem.
   c) Identify the key quantum properties or phenomena that could be leveraged.

2. Quantum Algorithm Design (300-350 words):
   a) Describe your proposed quantum algorithm in detail.
   b) Explain the quantum operations and gates used in your algorithm.
   c) Discuss how your algorithm leverages quantum properties to solve the problem.
   d) Provide a high-level pseudocode or circuit diagram of your algorithm.
   e) Explain the novelty of your approach compared to existing quantum algorithms.

3. Complexity Analysis (200-250 words):
   a) Analyze the time and space complexity of your quantum algorithm.
   b) Compare the complexity of your algorithm to the best known classical algorithm for this problem.
   c) Provide a mathematical analysis of the speedup achieved by your quantum algorithm.
   d) Discuss any limitations or constraints of your approach.

4. Implementation Considerations (200-250 words):
   a) Describe the quantum hardware requirements for your algorithm.
   b) Discuss any challenges in implementing your algorithm on current or near-term quantum devices.
   c) Propose potential methods to mitigate errors or decoherence effects.
   d) Suggest a roadmap for experimental implementation and validation of your algorithm.

5. Potential Impact Analysis (250-300 words):
   a) Analyze the potential impact of your algorithm on the specific field related to the problem.
   b) Discuss broader implications for science, technology, and society in the following areas:
      - Scientific advancements
      - Technological innovations
      - Economic implications
      - Social and ethical considerations
   c) Identify potential risks or challenges associated with the algorithm's application.
   d) Propose areas for further research or improvement.

Ensure your response demonstrates a deep understanding of quantum computing principles, algorithmic design, and the specific problem domain. Be innovative in your approach while maintaining scientific accuracy and feasibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use LaTeX notation for any mathematical formulas. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a thorough analysis of the given computational problem and its quantum approach",
            "The proposed quantum algorithm is novel, well-described, and leverages quantum properties appropriately",
            "The algorithm design includes a clear explanation of quantum operations and gates used",
            "A high-level pseudocode or circuit diagram of the algorithm is provided",
            "The complexity analysis compares the quantum algorithm to classical approaches effectively, including a mathematical analysis of the speedup",
            "Implementation considerations and hardware requirements are discussed in detail, with a proposed roadmap for experimental validation",
            "The potential impact analysis is comprehensive, covering scientific, technological, economic, and social implications",
            "The response demonstrates a deep understanding of quantum computing principles and the problem domain",
            "The response is well-structured, follows the specified format, uses LaTeX notation for formulas, and meets the word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
