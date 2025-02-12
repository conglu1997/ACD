import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'domain': 'financial markets',
                'decision_type': 'investment strategies',
                'quantum_concept': 'superposition',
                'constraint': 'model must account for market volatility index (VIX) > 30'
            },
            {
                'domain': 'public health policy',
                'decision_type': 'vaccine distribution',
                'quantum_concept': 'entanglement',
                'constraint': 'model must factor in a population density > 1000 people per square km'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models human decision-making in the domain of {t['domain']} using quantum probability theory, with a focus on {t['decision_type']} and incorporating the quantum concept of {t['quantum_concept']}. Your system must also account for the following constraint: {t['constraint']}. Your response should include:

1. Quantum Cognition Framework (250-300 words):
   a) Explain how quantum probability theory can be applied to model human decision-making in {t['domain']}.
   b) Describe how the quantum concept of {t['quantum_concept']} is incorporated into your model.
   c) Compare your quantum approach to traditional classical probability models for decision-making.
   d) Explain how your model addresses the given constraint: {t['constraint']}.

2. AI System Architecture (300-350 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Explain how your system integrates quantum cognitive models with machine learning techniques.
   c) Describe the key components and their interactions within your system.
   d) Discuss any novel elements in your design that enable quantum-inspired cognitive modeling.

3. Decision-Making Process (250-300 words):
   a) Outline the steps your AI system takes to model and simulate human decision-making for {t['decision_type']}.
   b) Explain how quantum probabilities are calculated and used in the decision process.
   c) Provide an example of how a specific decision might be modeled using your system.
   d) Describe how the constraint {t['constraint']} influences the decision-making process.

4. Implementation Challenges (200-250 words):
   a) Discuss the main technical challenges in implementing your quantum cognition AI system.
   b) Propose solutions or approaches to address these challenges.
   c) Consider any limitations of current AI and quantum computing technologies that might affect your system.

5. Scenario Application (300-350 words):
   a) Apply your AI system to a specific scenario within {t['domain']} related to {t['decision_type']}.
   b) Provide a step-by-step walkthrough of how your system would process this scenario, including:
      - Relevant quantum states and operations
      - How decisions are modeled and evaluated
      - The final output or recommendation
   c) Compare the results of your quantum-inspired system to what you would expect from a classical AI approach.
   d) Explain how the constraint {t['constraint']} affects the scenario outcome.

6. Ethical and Societal Implications (200-250 words):
   a) Discuss potential ethical considerations of using quantum cognition AI for decision-making in {t['domain']}.
   b) Explore the societal implications of deploying such systems for {t['decision_type']}.
   c) Propose guidelines or safeguards for the responsible development and use of quantum cognition AI.

7. Future Research Directions (150-200 words):
   a) Suggest areas for future research to enhance or extend your quantum cognition AI system.
   b) Discuss potential applications of your approach to other domains or decision types.
   c) Speculate on how advancements in quantum computing might impact the development of cognitive AI systems.

Ensure your response demonstrates a deep understanding of quantum theory, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, exactly as numbered above. Your total response should be between 1650-2000 words. Each section should be a cohesive paragraph or set of paragraphs; do not use bullet points or numbered lists within sections."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum theory, cognitive science, and artificial intelligence, integrating these fields in a novel and coherent manner.",
            "The quantum cognition framework is clearly explained and effectively applied to the given domain and decision type.",
            "The AI system architecture is well-designed, incorporating both quantum-inspired cognitive models and machine learning techniques.",
            "The decision-making process is thoroughly described, with a clear explanation of how quantum probabilities are used.",
            "The response adequately addresses the given constraint and explains its influence on the model and decision-making process.",
            "Implementation challenges are realistically addressed, with plausible solutions proposed.",
            "The scenario application provides a detailed and logical walkthrough of the system's operation, including the impact of the given constraint.",
            "Ethical and societal implications are thoughtfully considered, with relevant guidelines proposed.",
            "Future research directions are insightful and well-reasoned.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The writing is clear, well-structured, and adheres to the specified format and word count.",
            "The response demonstrates scientific accuracy in its treatment of quantum theory and its application to cognitive modeling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
