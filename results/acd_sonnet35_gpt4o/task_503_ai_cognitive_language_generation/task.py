import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "Confirmation Bias",
            "Availability Heuristic",
            "Anchoring Bias",
            "Framing Effect",
            "Loss Aversion"
        ]
        problem_domains = [
            "Resource Allocation",
            "Pattern Recognition",
            "Decision Making under Uncertainty",
            "Creative Problem Solving",
            "Ethical Dilemmas"
        ]
        tasks = [
            {
                "cognitive_bias": bias,
                "problem_domain": domain
            }
            for bias in cognitive_biases
            for domain in problem_domains
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and using a 'cognitive language' based on the {t['cognitive_bias']} to solve problems in the domain of {t['problem_domain']}. Then, analyze how this language affects the AI's cognitive processes and problem-solving abilities. Provide your response in the following format:

1. Cognitive Language Design (250-300 words):
   a) Describe the key features of the cognitive language based on {t['cognitive_bias']}.
   b) Explain how the language's structure, grammar, or vocabulary embodies this cognitive bias.
   c) Provide 3-5 example words or phrases in your language, with translations and explanations.

2. AI System Architecture (200-250 words):
   a) Describe the key components of your AI system that generates and uses this cognitive language.
   b) Explain how the system integrates the cognitive language into its problem-solving processes.
   c) Discuss any novel AI techniques or architectures you've incorporated to support this language-based cognition.

3. Problem-Solving Approach (200-250 words):
   a) Describe how your AI system would approach a specific problem in the domain of {t['problem_domain']} using the cognitive language.
   b) Explain the step-by-step process, highlighting how the language influences each stage.
   c) Provide a hypothetical example of the AI's problem-solving process, including sample 'thoughts' in the cognitive language.

4. Comparative Analysis (150-200 words):
   a) Compare how solutions generated using this cognitive language might differ from those of a traditional AI system.
   b) Discuss the potential advantages and limitations of using this language-based approach.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss the ethical considerations of creating AI systems with built-in cognitive biases.
   b) Explore the potential real-world applications and impacts of such AI systems.
   c) Propose safeguards or guidelines for the responsible development and use of these systems.

Ensure your response is creative, logically consistent, and demonstrates a deep understanding of linguistics, cognitive science, and AI. Use clear headings for each section and adhere to the word count guidelines provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes a cognitive language based on {t['cognitive_bias']} and provides clear examples",
            "The AI system architecture is well-explained and incorporates novel techniques for language-based cognition",
            f"The problem-solving approach in the domain of {t['problem_domain']} clearly demonstrates how the cognitive language influences the AI's thinking",
            "The comparative analysis provides insightful differences between this approach and traditional AI systems",
            "The ethical and practical implications are thoroughly discussed with thoughtful safeguards proposed",
            "The response demonstrates a deep understanding of linguistics, cognitive science, and AI throughout all sections",
            "The response is creative and logically consistent in its approach to language-based AI cognition",
            "The response adheres to the specified format and word count guidelines for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
