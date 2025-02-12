import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "confirmation bias",
            "availability heuristic",
            "anchoring bias",
            "framing effect"
        ]
        political_contexts = [
            "presidential debate",
            "social media discourse",
            "legislative session",
            "international diplomacy"
        ]
        tasks = [
            {
                "bias": random.choice(cognitive_biases),
                "context": random.choice(political_contexts)
            },
            {
                "bias": random.choice(cognitive_biases),
                "context": random.choice(political_contexts)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing system that models cognitive biases and decision-making processes, then use it to analyze and predict linguistic patterns in political discourse. Focus on the cognitive bias of {t['bias']} in the context of {t['context']}.

For this task, consider quantum computing principles such as superposition, entanglement, and quantum interference. Your system should incorporate these concepts in novel ways to enhance natural language processing and cognitive modeling.

Your response should include:

1. Quantum NLP Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired NLP system.
   b) Explain how quantum principles are incorporated into your language processing model.
   c) Detail how your system models the specified cognitive bias.
   d) Provide a high-level diagram of your system architecture (describe it in words).

2. Cognitive Bias Modeling (250-300 words):
   a) Explain the psychological mechanisms underlying the specified cognitive bias.
   b) Describe how your system represents and simulates this bias using quantum-inspired algorithms.
   c) Discuss any challenges in translating cognitive processes into computational models.

3. Political Discourse Analysis (250-300 words):
   a) Explain how your system analyzes linguistic patterns in the given political context.
   b) Describe specific linguistic features or markers your system looks for.
   c) Discuss how the modeled cognitive bias influences these linguistic patterns.

4. Prediction and Inference (200-250 words):
   a) Describe how your system makes predictions about future linguistic patterns or decision outcomes.
   b) Explain the role of quantum superposition or entanglement in your prediction process.
   c) Discuss the potential accuracy and limitations of these predictions.

5. Ethical Implications (150-200 words):
   a) Identify potential ethical issues arising from the use of this technology in political analysis.
   b) Discuss the implications for privacy, free will, and democratic processes.
   c) Propose guidelines for the responsible development and use of such systems.

6. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired approach to traditional NLP methods for political discourse analysis.
   b) Discuss potential advantages and disadvantages of your approach.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, linguistics, and political communication. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a quantum-inspired NLP system focusing on the cognitive bias of {t['bias']} in the context of {t['context']}.",
            "The system architecture should incorporate quantum principles in language processing.",
            "The cognitive bias modeling should be scientifically plausible and well-explained.",
            "The political discourse analysis should be relevant to the given context and bias.",
            "The response should demonstrate interdisciplinary knowledge integration across quantum computing, cognitive science, linguistics, and political science.",
            "The ethical implications and comparative analysis should be thoughtful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0