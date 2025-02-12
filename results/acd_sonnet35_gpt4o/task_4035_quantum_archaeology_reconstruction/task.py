import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "archaeological_context": "Ancient Mayan city",
                "data_type": "LiDAR point cloud",
                "quantum_technique": "Quantum annealing"
            },
            {
                "archaeological_context": "Neolithic settlement",
                "data_type": "Geomagnetic survey data",
                "quantum_technique": "Quantum Fourier transform"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm to analyze and reconstruct archaeological sites and artifacts from fragmented data, focusing on an {t['archaeological_context']} using {t['data_type']} and the quantum technique of {t['quantum_technique']}. Then, evaluate its potential impact on the field of archaeology. Your response should include the following sections:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the overall structure and workflow of your quantum algorithm.
   b) Explain how you incorporate the specified quantum technique into your algorithm.
   c) Provide a detailed pseudocode or flowchart of your algorithm.
   d) Discuss any novel quantum operations or subroutines you've developed for this application.

2. Archaeological Data Analysis (250-300 words):
   a) Explain how your algorithm interprets and reconstructs archaeological features from the fragmented data.
   b) Describe specific challenges in analyzing the given archaeological context and data type.
   c) Provide a step-by-step example of how your algorithm would process a specific archaeological data point.
   d) Discuss how your quantum approach addresses these challenges compared to classical methods.

3. Quantum-Classical Hybrid Approach (200-250 words):
   a) Describe how your algorithm integrates quantum and classical computing components.
   b) Explain the role of classical pre-processing and post-processing in your approach.
   c) Discuss any performance trade-offs between quantum and classical parts of your algorithm.

4. Performance Analysis and Benchmarking (200-250 words):
   a) Propose a method to evaluate the accuracy and efficiency of your quantum algorithm.
   b) Suggest at least three specific, quantifiable performance metrics for archaeological data reconstruction.
   c) Describe how you would compare your quantum approach to state-of-the-art classical methods.
   d) Discuss potential limitations of your approach and how they might be addressed.

5. Impact on Archaeology (250-300 words):
   a) Analyze how your quantum algorithm could potentially transform archaeological research practices.
   b) Discuss at least two new research questions or possibilities enabled by your approach.
   c) Explore potential challenges in adopting quantum computing in archaeology.
   d) Suggest guidelines for integrating quantum methods into existing archaeological workflows.

6. Ethical Considerations and Data Management (150-200 words):
   a) Discuss ethical implications of using advanced quantum algorithms in archaeology.
   b) Address concerns related to data ownership, privacy, and cultural sensitivity.
   c) Propose specific safeguards and best practices for responsible use of quantum computing in archaeology.

7. Future Developments and Cross-disciplinary Applications (150-200 words):
   a) Suggest potential improvements or extensions to your quantum algorithm.
   b) Discuss how advancements in quantum hardware might impact your approach.
   c) Propose two potential applications of your algorithm in other fields beyond archaeology, explaining how it would be adapted for each.

Ensure your response demonstrates a deep understanding of both quantum computing and archaeology. Use appropriate technical terminology from both fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and include word counts for each section in parentheses at the end. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and word counts.",
            f"The quantum algorithm effectively incorporates the specified quantum technique ({t['quantum_technique']}) for analyzing {t['data_type']} in the context of an {t['archaeological_context']}, including a detailed pseudocode or flowchart.",
            "The design demonstrates a deep understanding of both quantum computing principles and archaeological data analysis, with specific examples of data processing.",
            "The response shows creativity and innovation in applying quantum computing to archaeological reconstruction, proposing novel approaches or techniques.",
            "The performance analysis includes at least three specific, quantifiable metrics for evaluating the algorithm's effectiveness in archaeological data reconstruction.",
            "The ethical implications and future developments are thoughtfully considered, with specific safeguards and cross-disciplinary applications proposed.",
            "The response provides clear, technically accurate explanations without simply repeating the instructions or providing generic information about quantum computing and archaeology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
