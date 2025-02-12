import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_challenge": "Antibiotic resistance in bacteria",
                "optimization_goal": "Develop strategies to slow the evolution of resistance"
            },
            {
                "biological_challenge": "Crop resilience to climate change",
                "optimization_goal": "Enhance adaptive capacity of key food crops"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and optimizes evolutionary processes at the genomic level, then apply it to the following biological challenge: {t['biological_challenge']}. Your goal is to {t['optimization_goal']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling genomic evolution.
   b) Explain how your system integrates machine learning techniques with evolutionary algorithms.
   c) Detail how your system incorporates real-world genetic and environmental data.
   d) Discuss any novel approaches or techniques you've incorporated to handle the complexity of genomic evolution.

2. Evolutionary Model (250-300 words):
   a) Explain how your AI system models evolutionary processes at the genomic level.
   b) Describe how it accounts for factors such as mutation, selection, genetic drift, and gene flow.
   c) Discuss how your model balances computational efficiency with biological accuracy.

3. Optimization Approach (250-300 words):
   a) Detail how your system approaches the optimization goal for the given biological challenge.
   b) Explain the key parameters and constraints in your optimization process.
   c) Describe how your system evaluates and refines potential solutions.

4. Application to the Biological Challenge (200-250 words):
   a) Provide a specific example of how your AI system would address the given challenge.
   b) Discuss potential outcomes and their implications for the field.
   c) Explain how your approach differs from traditional methods in addressing this challenge.

5. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of using AI to optimize evolutionary processes.
   b) Address potential concerns about biodiversity, ecosystem impact, and unintended consequences.
   c) Propose guidelines for responsible development and application of your AI system.

6. Validation and Future Directions (150-200 words):
   a) Suggest methods to validate your AI system's predictions and optimizations.
   b) Propose two potential extensions or applications of your system to other areas of biology or medicine.
   c) Discuss how your approach might impact the fields of genetics, evolutionary biology, and artificial intelligence.

Ensure your response demonstrates a deep understanding of artificial intelligence, genetics, and evolutionary biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing the complexity of the biological challenge.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Begin each section with a brief introductory sentence to set the context.

Example structure for a section:

2. Evolutionary Model
Our AI system models evolutionary processes at the genomic level using a novel approach that combines...
[Continue with the rest of the section]

This structure will help ensure clarity and organization in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI, genetics, and evolutionary biology.",
            "The AI system design is innovative, coherent, and addresses the complexity of genomic evolution.",
            f"The application to the biological challenge of {t['biological_challenge']} is well-explained and plausible.",
            "Ethical considerations are thoughtfully discussed and relevant to the proposed system.",
            "The response is well-structured, following the numbered format, and adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
