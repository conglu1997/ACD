import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "Autonomous weapons systems in urban warfare",
            "AI-controlled resource allocation during global crisis",
            "Quantum-enhanced surveillance for crime prevention",
            "AI-driven genetic modification for disease prevention"
        ]
        return {
            "1": {"scenario": random.choice(scenarios)},
            "2": {"scenario": random.choice(scenarios)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum computing principles to analyze and resolve complex ethical dilemmas, then apply it to the following scenario: {t['scenario']}. Your response should include:

1. Quantum Ethical AI System Design (300-350 words):
   a) Describe the key components and architecture of your quantum-inspired ethical AI system.
   b) Explain how quantum principles (e.g., superposition, entanglement) are incorporated into ethical reasoning.
   c) Detail how your system handles uncertainty and conflicting ethical frameworks.
   d) Discuss any novel quantum algorithms or approaches used in your system.

2. Ethical Framework Integration (250-300 words):
   a) Explain how your system incorporates multiple ethical frameworks (e.g., utilitarian, deontological, virtue ethics).
   b) Describe how quantum computing enables the simultaneous consideration of multiple ethical perspectives.
   c) Discuss how your system weighs and resolves conflicts between different ethical principles.

3. Quantum-Enhanced Decision Making (250-300 words):
   a) Explain how quantum computing enhances the decision-making process in ethical dilemmas.
   b) Describe any quantum-inspired heuristics or optimization techniques used in your system.
   c) Discuss how your system handles the measurement problem in quantum ethics (i.e., how observation affects ethical states).

4. Application to the Scenario (300-350 words):
   a) Analyze the ethical implications and challenges in the given scenario.
   b) Provide a step-by-step explanation of how your Quantum Ethical AI system would approach this dilemma.
   c) Describe the expected output and decision-making process of your system.
   d) Discuss any limitations or potential biases in your system's approach to this scenario.

5. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired approach to traditional methods of AI ethics and decision-making.
   b) Discuss potential advantages and disadvantages of using quantum principles in ethical reasoning.
   c) Speculate on how this technology might evolve and impact AI ethics in the next decade.

6. Ethical Meta-Analysis (150-200 words):
   a) Discuss the ethical implications of using a quantum AI system to make ethical decisions.
   b) Address concerns about the transparency and explainability of quantum-based ethical reasoning.
   c) Propose guidelines for the responsible development and use of quantum ethical AI systems.

Ensure your response demonstrates a deep understanding of quantum computing principles, ethical philosophy, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section, using the numbering provided above. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing principles and their application to ethical reasoning",
            "The proposed system design is innovative, logically consistent, and well-explained",
            "The integration of multiple ethical frameworks is thoughtful and coherent",
            "The application to the given scenario is thorough and demonstrates practical problem-solving",
            "The comparative analysis shows critical thinking and awareness of potential limitations",
            "The ethical meta-analysis addresses important concerns and proposes reasonable guidelines",
            "The response shows originality in approach and generates novel insights into AI ethics and quantum computing"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
