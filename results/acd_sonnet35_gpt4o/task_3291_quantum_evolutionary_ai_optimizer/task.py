import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "domain": "Climate change mitigation",
                "specific_problem": "Optimizing global carbon capture and storage strategies",
                "quantum_principle": "Quantum annealing",
                "evolutionary_concept": "Genetic drift"
            },
            {
                "domain": "Sustainable urban planning",
                "specific_problem": "Designing energy-efficient smart cities",
                "quantum_principle": "Quantum superposition",
                "evolutionary_concept": "Adaptive radiation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(challenges, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-classical AI system that leverages principles of evolutionary biology and quantum computing to optimize complex multi-objective problems, then apply it to the challenge of {t['specific_problem']} in the domain of {t['domain']}. Your system should incorporate the quantum principle of {t['quantum_principle']} and the evolutionary concept of {t['evolutionary_concept']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your hybrid quantum-classical AI system.
   b) Explain how quantum and classical components interact.
   c) Detail how your system incorporates {t['quantum_principle']} and {t['evolutionary_concept']}.
   d) Discuss how these principles contribute to solving multi-objective optimization problems.

2. Optimization Algorithm (250-300 words):
   a) Outline your hybrid quantum-evolutionary optimization algorithm.
   b) Explain how it leverages both quantum and classical resources.
   c) Describe how it handles multiple, potentially conflicting objectives.
   d) Provide a simple pseudocode (about 10-15 lines) illustrating a key part of your algorithm.

3. Application to {t['domain']} (250-300 words):
   a) Analyze how your system would approach the problem of {t['specific_problem']}.
   b) Identify key variables and constraints in this optimization problem.
   c) Explain how your system's quantum and evolutionary components contribute to solving this specific challenge.
   d) Discuss potential advantages of your approach over classical methods.

4. Performance Evaluation (200-250 words):
   a) Propose specific, measurable metrics to evaluate your system's performance on {t['specific_problem']}.
   b) Describe a detailed methodology for benchmarking your system against classical alternatives.
   c) Discuss potential limitations or challenges in accurately assessing performance, and propose solutions.

5. Ethical and Practical Considerations (150-200 words):
   a) Identify potential ethical implications of using your system for {t['domain']}.
   b) Discuss practical challenges in implementing your system at scale, including technological and resource constraints.
   c) Propose comprehensive guidelines for responsible development and use of quantum-evolutionary AI optimizers.

6. Future Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your system, explaining their potential impact.
   b) Propose a novel application of your quantum-evolutionary AI optimizer in a different domain, detailing how it would be adapted.
   c) Speculate on how advances in this field might influence AI and quantum computing research in the next decade.

Ensure your response demonstrates a deep understanding of quantum computing, evolutionary biology, artificial intelligence, and {t['domain']}. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately covers all six required sections, addressing {t['domain']}, {t['specific_problem']}, {t['quantum_principle']}, and {t['evolutionary_concept']}.",
            "The system architecture demonstrates a clear integration of quantum computing, evolutionary biology, and AI principles.",
            "The optimization algorithm effectively combines quantum and classical approaches to solve multi-objective problems.",
            "The application to the specific problem shows a deep understanding of both the technical solution and the domain-specific challenges.",
            "The performance evaluation section proposes specific, measurable metrics and a detailed benchmarking methodology.",
            "The response includes a thoughtful analysis of ethical implications and practical considerations, with comprehensive guidelines for responsible development.",
            "The submission demonstrates creativity and innovation while maintaining scientific plausibility.",
            "The response provides clear explanations of complex concepts and uses appropriate technical terminology.",
            "The submission includes a pseudocode snippet illustrating a key part of the algorithm.",
            "The response falls within the specified word count range of 1300-1600 words and includes a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
