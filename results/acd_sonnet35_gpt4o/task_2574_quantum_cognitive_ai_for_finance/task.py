import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum annealing"
        ]
        cognitive_principles = [
            "Parallel distributed processing",
            "Hebbian learning",
            "Predictive coding",
            "Cognitive control"
        ]
        financial_aspects = [
            "Stock price movements",
            "Cryptocurrency volatility",
            "Forex market trends",
            "Commodity futures"
        ]
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_principle": random.choice(cognitive_principles),
                "financial_aspect": random.choice(financial_aspects)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_principle": random.choice(cognitive_principles),
                "financial_aspect": random.choice(financial_aspects)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for AI, incorporating the quantum concept of {t['quantum_concept']} and the cognitive principle of {t['cognitive_principle']}. Then, apply this architecture to develop a predictive model for {t['financial_aspect']}. Your response should include:

1. Quantum-Inspired Cognitive Architecture (300-350 words):
   a) Describe the key components of your architecture and how they integrate quantum and cognitive principles.
   b) Explain how {t['quantum_concept']} is implemented in your model.
   c) Detail how {t['cognitive_principle']} is incorporated into the architecture.
   d) Discuss any novel computational approaches used in your design.
   e) Include a visual representation of your architecture (use ASCII art or Unicode characters).

2. Implementation for Financial Prediction (250-300 words):
   a) Explain how your quantum-inspired cognitive AI would be applied to predict {t['financial_aspect']}.
   b) Describe the data inputs and processing mechanisms of your model.
   c) Discuss how quantum principles enhance the model's predictive capabilities.
   d) Address potential challenges in implementing this model for real-world financial analysis.

3. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired cognitive AI to traditional machine learning approaches for financial prediction.
   b) Discuss potential advantages and limitations of your approach.
   c) Analyze how the integration of quantum concepts might overcome limitations of classical AI in financial modeling.

4. Ethical Considerations and Safeguards (150-200 words):
   a) Discuss ethical implications of using quantum-inspired AI for financial predictions.
   b) Propose guidelines for responsible development and use of such systems in the financial sector.
   c) Address potential issues of fairness, transparency, and market manipulation.

5. Future Research Directions (150-200 words):
   a) Suggest two specific areas for future research to enhance your quantum-inspired cognitive AI.
   b) Explain how these research directions could address current limitations or expand the system's capabilities.
   c) Discuss potential applications of your architecture beyond financial prediction.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, artificial intelligence, and financial systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, cognitive science, artificial intelligence, and financial systems",
            "The quantum-inspired cognitive architecture is innovative, scientifically plausible, and effectively incorporates the specified quantum concept and cognitive principle",
            "The implementation for financial prediction is well-explained and logically applies the architecture to the given financial aspect",
            "The comparative analysis provides insightful comparisons between the proposed approach and traditional methods",
            "Ethical considerations are thoroughly discussed with relevant guidelines proposed",
            "Future research directions are thoughtfully suggested and well-justified",
            "The response is well-structured, uses appropriate technical terminology, and provides clear explanations for complex concepts",
            "The response stays within the specified word limit and follows the required format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
