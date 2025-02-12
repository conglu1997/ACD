import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Physics",
            "Biology",
            "Economics",
            "Urban Planning",
            "Environmental Science",
            "Social Psychology"
        ]
        problem_types = [
            "Resource Allocation",
            "Pattern Recognition",
            "Prediction and Forecasting",
            "Optimization",
            "Conflict Resolution",
            "System Design"
        ]
        return {
            "1": {"domain": random.choice(domains), "problem_type": random.choice(problem_types)},
            "2": {"domain": random.choice(domains), "problem_type": random.choice(problem_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses analogical reasoning to solve complex problems, focusing on the domain of {t['domain']} and the problem type of {t['problem_type']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI analogical reasoning system.
   b) Explain how your system identifies and applies relevant analogies.
   c) Discuss any novel elements in your design that enable cross-domain problem-solving.
   d) Provide a high-level diagram or flowchart of your system's architecture (describe it textually).

2. Analogical Reasoning Process (200-250 words):
   a) Explain how your AI system identifies potential source domains for analogies.
   b) Describe the process of mapping concepts between the source and target domains.
   c) Discuss how your system evaluates and selects the most appropriate analogies.

3. Domain-Specific Application (200-250 words):
   a) Provide a specific example of how your system would approach a {t['problem_type']} problem in {t['domain']}.
   b) Explain how it would identify and apply analogies from other domains to solve this problem.
   c) Discuss any domain-specific challenges and how your system addresses them.

4. Learning and Adaptation (150-200 words):
   a) Describe how your AI system learns from successful and unsuccessful applications of analogies.
   b) Explain how it generalizes problem-solving strategies across different domains.
   c) Discuss any potential limitations in the system's ability to adapt to novel problem spaces.

5. Cognitive Science Foundations (200-250 words):
   a) Discuss the cognitive science principles underlying your AI system's analogical reasoning process.
   b) Compare your system's approach to human analogical reasoning, highlighting similarities and differences.
   c) Propose an experiment to test whether your AI system's analogical reasoning aligns with human cognitive processes.

6. Implications for Human Problem-Solving (150-200 words):
   a) Analyze how your AI system might influence or enhance human problem-solving capabilities.
   b) Discuss potential applications of your system in education or professional training.
   c) Consider any potential negative impacts on human cognitive skills or creativity.

7. Ethical Considerations and Future Developments (150-200 words):
   a) Discuss ethical implications of deploying AI systems with advanced analogical reasoning capabilities.
   b) Propose guidelines for responsible development and use of such systems.
   c) Suggest potential future enhancements or research directions for your AI analogical reasoning system.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific domain and problem type. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of analogical reasoning and its application in AI systems, particularly in the domain of {t['domain']} and for {t['problem_type']} problems.",
            "The proposed AI system architecture is well-explained, innovative, and plausible.",
            "The analogical reasoning process is clearly described and grounded in cognitive science principles.",
            "The domain-specific application example is relevant, detailed, and demonstrates cross-domain problem-solving.",
            "The response addresses learning, adaptation, and potential limitations of the AI system.",
            "The implications for human problem-solving and ethical considerations are thoughtfully discussed.",
            "The response is well-structured, coherent, and demonstrates creativity while maintaining scientific rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
