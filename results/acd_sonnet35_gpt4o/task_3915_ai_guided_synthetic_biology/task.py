import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            "Biosensors for detecting heavy metals in water",
            "Biofuel production from lignocellulosic biomass",
            "Targeted drug delivery system for cancer therapy",
            "Self-healing concrete using engineered bacteria"
        ]
        constraints = [
            "Minimize metabolic burden on host organism (E. coli)",
            "Ensure genetic stability across 100+ generations",
            "Optimize for scalability in 10,000L bioreactors",
            "Design for modularity with standardized BioBrick parts"
        ]
        return {
            "1": {"application": random.choice(applications), "constraint": random.choice(constraints)},
            "2": {"application": random.choice(applications), "constraint": random.choice(constraints)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to guide the engineering of synthetic biological circuits for the following application: {t['application']}. Your system should incorporate principles from systems biology, genetic engineering, and machine learning to design and optimize genetic circuits. Additionally, your design must address the following constraint: {t['constraint']}.

Consider the following example scenario: A research team wants to develop a biosensor for detecting lead contamination in drinking water. They need an AI system that can design a genetic circuit in E. coli that produces a fluorescent signal in the presence of lead ions, while minimizing false positives and ensuring the system remains stable over multiple generations.

Your response should include the following sections, with the specified word counts:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-guided synthetic biology system.
   b) Explain how your system integrates knowledge from biology, genetics, and machine learning.
   c) Detail the data sources and types your system would use (e.g., genomic databases, metabolic pathway information).
   d) Propose a novel algorithm or approach for designing genetic circuits.

2. Circuit Design and Optimization (250-300 words):
   a) Explain how your system would design genetic circuits for the given application.
   b) Describe the optimization process, including how it addresses the specified constraint.
   c) Discuss how your system handles trade-offs between different design objectives (e.g., efficiency vs. stability).
   d) Propose a method for predicting circuit behavior and performance.

3. Machine Learning Integration (200-250 words):
   a) Describe how machine learning is used in your system for circuit design and optimization.
   b) Explain any novel ML techniques or architectures you would employ (e.g., reinforcement learning, graph neural networks).
   c) Discuss how your system could learn and improve from experimental data.

4. Experimental Validation (150-200 words):
   a) Propose a method for experimentally validating the circuits designed by your AI system.
   b) Describe how feedback from experiments would be incorporated into the AI system.
   c) Discuss potential challenges in translating in silico designs to in vivo functionality.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to AI-guided synthetic biology.
   b) Discuss biosafety and biosecurity implications of your system.
   c) Propose guidelines for responsible development and use of this technology.

6. Future Implications (150-200 words):
   a) Discuss how your system could impact the field of synthetic biology.
   b) Propose a potential future application enabled by your AI-guided approach.
   c) Speculate on how this technology might influence our understanding of biological systems.

Ensure your response demonstrates a deep understanding of synthetic biology, genetic engineering, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and original in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered subsections, and adhere to the specified word counts. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, genetic engineering, and artificial intelligence, using appropriate technical terminology.",
            "The proposed AI system is innovative, scientifically plausible, and effectively integrates principles from systems biology, genetic engineering, and machine learning.",
            f"The design specifically addresses the given application ({t['application']}) and constraint ({t['constraint']}).",
            "The response covers all required sections with appropriate depth, clarity, and adheres to the specified word counts.",
            "The proposed system architecture includes novel and original algorithms or approaches for designing genetic circuits.",
            "The machine learning integration section describes specific and innovative ML techniques or architectures relevant to synthetic biology.",
            "The experimental validation section proposes a feasible and comprehensive method for testing the AI-designed circuits and incorporating feedback.",
            "Ethical considerations and future implications are thoughtfully discussed, including specific biosafety and biosecurity concerns.",
            "The response demonstrates creativity and originality in addressing the task, going beyond standard approaches in the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
