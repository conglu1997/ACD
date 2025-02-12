import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        diseases = [
            "Alzheimer's disease",
            "Type 2 diabetes",
            "Breast cancer",
            "Parkinson's disease",
            "Cystic fibrosis"
        ]
        quantum_approaches = [
            "Density Functional Theory (DFT)",
            "Ab initio molecular dynamics",
            "Quantum Monte Carlo",
            "Coupled cluster theory",
            "Quantum machine learning"
        ]
        return {
            "1": {
                "disease": random.choice(diseases),
                "quantum_approach": random.choice(quantum_approaches)
            },
            "2": {
                "disease": random.choice(diseases),
                "quantum_approach": random.choice(quantum_approaches)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum chemistry-based AI system for rational drug design, focusing on targeting a specific protein implicated in {t['disease']}. Your system should incorporate {t['quantum_approach']} as a key component of its quantum chemical calculations. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for quantum chemistry-based drug design.
   b) Explain how {t['quantum_approach']} is integrated into the system's workflow.
   c) Detail the key components of your system, including data input, quantum chemical calculations, molecular docking, and drug candidate evaluation.
   d) Discuss how your system leverages AI/machine learning techniques in conjunction with quantum chemical methods.

2. Quantum Chemical Approach (250-300 words):
   a) Explain the principles of {t['quantum_approach']} and its relevance to drug design.
   b) Describe how your system applies {t['quantum_approach']} to model molecular interactions between potential drug candidates and the target protein.
   c) Discuss any approximations or assumptions made in your quantum chemical calculations.
   d) Compare the advantages of your approach to traditional computational chemistry methods.

3. Target Protein Analysis (200-250 words):
   a) Identify a specific protein target implicated in {t['disease']}.
   b) Explain the role of this protein in the disease mechanism.
   c) Describe how your system analyzes the protein's structure and identifies potential binding sites.
   d) Discuss how quantum effects might influence the protein-ligand interactions in this case.

4. Drug Candidate Generation and Evaluation (250-300 words):
   a) Explain how your system generates potential drug candidates.
   b) Describe the criteria used to evaluate and rank drug candidates.
   c) Detail how quantum chemical calculations inform the evaluation process.
   d) Provide an example of how your system would assess a specific drug candidate, including relevant quantum chemical calculations.

5. Performance Analysis and Validation (200-250 words):
   a) Propose methods to validate the accuracy of your system's quantum chemical calculations.
   b) Describe how you would benchmark your system against existing drug discovery approaches.
   c) Discuss potential limitations of your approach and suggest ways to address them.
   d) Explain how your system could be experimentally validated in a laboratory setting.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using AI and quantum chemistry in drug discovery.
   b) Address potential biases in your system and propose strategies to mitigate them.
   c) Suggest future research directions to enhance the integration of quantum chemistry and AI in drug design.
   d) Speculate on how advances in quantum computing might impact your system's capabilities.

Ensure your response demonstrates a deep understanding of quantum chemistry, computational biology, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of quantum chemistry, particularly {t['quantum_approach']}, as well as its application to drug design for {t['disease']}.",
            "The AI system design should be innovative, coherent, and effectively integrate quantum chemical methods with AI/machine learning techniques.",
            "The explanation of the quantum chemical approach should be scientifically accurate and clearly relate to drug design applications.",
            "The target protein analysis should be specific to the given disease and demonstrate understanding of protein-ligand interactions.",
            "The drug candidate generation and evaluation process should be logical and make effective use of quantum chemical calculations.",
            "The performance analysis and validation methods should be well-thought-out and scientifically sound.",
            "Ethical considerations should be thoroughly addressed, and future directions should be insightful and relevant.",
            "The overall response should be well-structured, adhere to the word count guidelines, and demonstrate exceptional interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
