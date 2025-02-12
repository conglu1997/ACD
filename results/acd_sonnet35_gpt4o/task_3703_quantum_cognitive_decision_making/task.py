import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "Financial Markets",
                "quantum_principle": "Superposition",
                "cognitive_bias": "Confirmation Bias",
                "constraint": "Must incorporate at least three quantum states in decision representation"
            },
            {
                "domain": "Climate Change Policy",
                "quantum_principle": "Entanglement",
                "cognitive_bias": "Anchoring Effect",
                "constraint": "Must model at least two interdependent decision factors using entanglement"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for decision-making that incorporates principles from quantum computing and cognitive psychology, then apply it to a complex real-world scenario in {t['domain']}. Your architecture should specifically utilize the quantum principle of {t['quantum_principle']} and address the cognitive bias of {t['cognitive_bias']}. Additionally, your design must adhere to this constraint: {t['constraint']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain how {t['quantum_principle']} can be applied to model decision-making processes.
   b) Describe how {t['cognitive_bias']} influences decision-making and how it can be represented in a quantum-inspired model.
   c) Discuss the potential advantages of a quantum-inspired approach over classical decision-making models.

2. Architecture Design (300-350 words):
   a) Describe the key components of your quantum-inspired cognitive architecture.
   b) Explain how your architecture incorporates {t['quantum_principle']} in its decision-making process.
   c) Detail how your model accounts for and potentially mitigates {t['cognitive_bias']}.
   d) Include a diagram or formal description of your architecture's structure and processes. For the diagram, use ASCII characters to create a visual representation. For a formal description, use mathematical notation or pseudocode.

3. Application to {t['domain']} (250-300 words):
   a) Describe a specific decision-making scenario in {t['domain']}.
   b) Explain how your architecture would model and approach this scenario.
   c) Discuss how the quantum-inspired elements of your model influence the decision-making process in this context.
   d) Provide a step-by-step walkthrough of how your model would process a given input and produce a decision output.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired architecture to traditional decision-making models used in {t['domain']}.
   b) Identify potential advantages and limitations of your approach.
   c) Discuss how your model might lead to different decisions or insights compared to classical approaches.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss any ethical implications of using quantum-inspired models for decision-making in {t['domain']}.
   b) Address potential limitations or challenges in implementing your architecture in real-world situations.
   c) Propose guidelines for the responsible development and use of quantum-inspired cognitive models.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your architecture for future development.
   b) Propose a novel research question that could be investigated using your quantum-inspired cognitive model.
   c) Discuss how advancements in quantum computing might influence the practical implementation of your model.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive psychology, and the specific domain of application. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of quantum computing principles, cognitive psychology, and {t['domain']}.",
            f"The architecture design should clearly incorporate {t['quantum_principle']} and address {t['cognitive_bias']} in a novel and plausible way, while adhering to the constraint: {t['constraint']}.",
            f"The application to {t['domain']} should be well-reasoned and demonstrate how the quantum-inspired approach could lead to new insights or decisions, including a clear step-by-step walkthrough of the decision-making process.",
            "The comparative analysis should provide a thoughtful discussion of the advantages and limitations of the proposed approach, with specific examples or scenarios.",
            "The response should address ethical considerations and limitations thoughtfully, demonstrating awareness of potential challenges in real-world implementation.",
            "The submission must include a diagram or formal description of the architecture using ASCII characters or mathematical notation/pseudocode.",
            "The response should be well-structured, following the provided format, and include a word count between 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
