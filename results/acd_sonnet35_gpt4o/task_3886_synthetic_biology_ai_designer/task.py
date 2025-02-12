import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "environmental pollution detection and remediation",
            "targeted drug delivery and activation",
            "biofuel production and optimization",
            "food preservation and nutritional enhancement",
            "water purification and quality monitoring"
        ]
        biological_components = [
            "genetic circuits and metabolic pathways",
            "protein engineering and synthetic organelles",
            "CRISPR-Cas systems and orthogonal replication",
            "synthetic signal transduction and quorum sensing",
            "artificial symbionts and engineered microbiomes"
        ]
        return {
            "1": {
                "problem": random.choice(problems),
                "components": random.sample(biological_components, 2)
            },
            "2": {
                "problem": random.choice(problems),
                "components": random.sample(biological_components, 2)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can create and optimize synthetic biological circuits to solve the problem of {t['problem']} using a combination of {t['components'][0]} and {t['components'][1]}. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for designing synthetic biological circuits.
   b) Explain how your system integrates knowledge from biology, computer science, and the problem domain.
   c) Detail any novel approaches or algorithms used in your design.
   d) Include a high-level diagram or flowchart of your AI system architecture.

2. Synthetic Biology Design Process (200-250 words):
   a) Outline the steps your AI system takes to design a synthetic biological circuit.
   b) Explain how it optimizes the circuit for the given problem.
   c) Describe how your system ensures the biological feasibility and safety of its designs.
   d) Discuss how your system manages the complexity of multiple interacting biological components.

3. Problem-Specific Solution (250-300 words):
   a) Present a specific synthetic biological circuit design for solving the given problem.
   b) Explain how the circuit functions and how it addresses the problem.
   c) Discuss potential advantages of your approach compared to traditional solutions.
   d) Provide a schematic representation of your proposed synthetic biological circuit.
   e) Describe potential failure modes of your system and how to mitigate them.

4. Evaluation and Testing (150-200 words):
   a) Propose methods for evaluating the effectiveness of your AI-designed circuits.
   b) Describe simulations or experiments that could validate the design.
   c) Discuss potential challenges in implementing and testing these biological circuits.

5. Regulatory Considerations (150-200 words):
   a) Discuss relevant biosafety regulations and guidelines applicable to your proposed system.
   b) Explain how your AI system ensures compliance with these regulations.
   c) Propose strategies for addressing potential regulatory challenges or concerns.

6. Ethical Considerations and Implications (200-250 words):
   a) Analyze ethical implications of using AI-designed synthetic biology for {t['problem']}.
   b) Discuss potential risks and benefits to society and the environment.
   c) Propose guidelines for responsible development and use of this technology.

7. Future Applications and Developments (150-200 words):
   a) Suggest two potential future applications of your AI system in synthetic biology.
   b) Discuss how this technology might evolve and its potential impact on science and society.
   c) Propose a roadmap for further research and development in this field.

Ensure your response demonstrates a deep understanding of synthetic biology, AI systems, and the specific problem domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your response should be based solely on your existing knowledge - do not access external resources or the internet.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words. Include two diagrams as specified above - these do not count towards the word limit."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the problem of {t['problem']} using a combination of {t['components'][0]} and {t['components'][1]}.",
            "The AI system architecture should be clearly described and integrate knowledge from biology and computer science, with a high-level diagram provided.",
            "The synthetic biology design process should be logically explained, including optimization steps and management of multiple interacting components.",
            "A specific synthetic biological circuit design should be presented, explained, and illustrated with a schematic representation.",
            "Potential failure modes and mitigation strategies should be discussed.",
            "Evaluation methods and potential challenges should be discussed realistically.",
            "Relevant biosafety regulations and compliance strategies should be addressed.",
            "Ethical considerations should be thoroughly analyzed, considering both risks and benefits.",
            "Future applications and developments should be proposed with a clear roadmap.",
            "The response should demonstrate a deep understanding of synthetic biology and AI systems, using appropriate technical terminology.",
            "The writing should be clear, well-structured, and within the specified word limit.",
            "The proposed solution should be scientifically plausible, innovative, and demonstrate integration of multiple biological components."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
