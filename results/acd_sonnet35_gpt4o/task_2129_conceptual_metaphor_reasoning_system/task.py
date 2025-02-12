import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Climate Change",
            "Economic Inequality",
            "Artificial Intelligence Ethics",
            "Quantum Computing",
            "Neurodegenerative Diseases"
        ]
        return {str(i+1): {"domain": domain} for i, domain in enumerate(random.sample(domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating, interpreting, and applying conceptual metaphors to solve complex problems in the domain of {t['domain']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for conceptual metaphor reasoning.
   b) Explain how your system generates and interprets conceptual metaphors.
   c) Detail how it applies these metaphors to problem-solving in the given domain.
   d) Include a high-level diagram or pseudocode representing the system's workflow.

2. Conceptual Metaphor Generation (200-250 words):
   a) Explain the process by which your system generates novel conceptual metaphors.
   b) Provide two examples of conceptual metaphors your system might generate for the given domain.
   c) Discuss how your system ensures the relevance and coherence of generated metaphors.

3. Metaphor-Based Problem Solving (250-300 words):
   a) Describe a specific problem in the given domain that your system would address.
   b) Explain how your system would apply conceptual metaphors to analyze and solve this problem.
   c) Discuss any advantages or unique insights this approach might provide compared to traditional problem-solving methods.

4. Cross-Domain Application (200-250 words):
   a) Explain how your system could transfer metaphors or problem-solving strategies from the given domain to another, unrelated domain.
   b) Provide an example of such a transfer, detailing the metaphor and its application in both domains.
   c) Discuss the potential benefits and challenges of this cross-domain metaphor application.

5. Evaluation and Refinement (150-200 words):
   a) Propose methods for evaluating the effectiveness and creativity of your system's metaphor-based reasoning.
   b) Describe how you would refine and improve your system based on these evaluations.
   c) Discuss potential limitations or biases in your approach and how you might address them.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss the potential impact of widespread use of such a system on human creativity and problem-solving.
   b) Consider any ethical concerns related to using AI-generated conceptual metaphors in decision-making processes.
   c) Propose guidelines for responsible development and use of conceptual metaphor AI systems.

Ensure your response demonstrates a deep understanding of conceptual metaphors, the given domain, and AI technologies. Be creative in your approach while maintaining scientific and ethical plausibility. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a clear description of an AI system for conceptual metaphor reasoning in the domain of {t['domain']}",
            "The system architecture should be well-explained and include all required components",
            "The response should provide examples of generated conceptual metaphors and their application to problem-solving",
            "The cross-domain application of metaphors should be clearly explained with a specific example",
            "The response should address evaluation methods, limitations, and ethical implications of the system",
            "The overall response should demonstrate creativity, interdisciplinary knowledge, and scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
