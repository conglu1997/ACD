import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "climate science",
            "quantum physics",
            "economics",
            "medicine"
        ]
        metaphor_types = [
            "spatial",
            "embodied",
            "structural",
            "ontological"
        ]
        tasks = [
            {
                "domain": domain,
                "metaphor_type": metaphor_type
            }
            for domain in domains
            for metaphor_type in metaphor_types
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can understand, generate, and apply cognitive metaphors to enhance its reasoning and problem-solving capabilities in the domain of {t['domain']}, focusing on {t['metaphor_type']} metaphors. Your response should include the following sections:

1. Cognitive Metaphor Analysis (300-350 words):
   a) Explain the concept of cognitive metaphors and their role in human reasoning.
   b) Analyze how {t['metaphor_type']} metaphors are typically used in {t['domain']}.
   c) Provide 2-3 examples of such metaphors and explain their cognitive significance.
   d) Discuss how these metaphors might influence problem-solving approaches in {t['domain']}.

2. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for understanding and generating cognitive metaphors.
   b) Explain how your system integrates knowledge from cognitive science, linguistics, and {t['domain']}.
   c) Detail the specific mechanisms your system uses to process and apply {t['metaphor_type']} metaphors.
   d) Discuss any novel AI techniques or approaches your system employs.

3. Metaphor Generation and Application (250-300 words):
   a) Explain how your AI system generates new cognitive metaphors for {t['domain']}.
   b) Describe the process by which your system applies these metaphors to problem-solving tasks.
   c) Provide an example of a novel metaphor your system might generate and how it would be applied.
   d) Discuss how your system evaluates the effectiveness and appropriateness of generated metaphors.

4. Enhanced Reasoning Demonstration (200-250 words):
   a) Present a specific problem or challenge in {t['domain']} that your AI system would address.
   b) Demonstrate how your system would use cognitive metaphors to approach this problem.
   c) Compare this approach to traditional AI problem-solving methods in {t['domain']}.
   d) Discuss potential insights or solutions that might emerge from this metaphor-enhanced reasoning.

5. Cognitive and Computational Analysis (200-250 words):
   a) Analyze how your AI system's use of cognitive metaphors compares to human cognitive processes.
   b) Discuss potential cognitive advantages or limitations of your system's approach.
   c) Explain how your system balances metaphorical thinking with logical reasoning and domain-specific knowledge.
   d) Consider how this approach might influence the development of more human-like AI systems.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of AI systems that can generate and apply cognitive metaphors.
   b) Consider how this technology might impact human-AI interaction and collaboration.
   c) Propose two potential future research directions or applications for metaphor-enhanced AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, artificial intelligence, and {t['domain']}. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should thoroughly address {t['metaphor_type']} metaphors in the context of {t['domain']}",
            "The AI system design should be innovative, well-explained, and scientifically plausible",
            "The response should demonstrate a deep understanding of cognitive science, linguistics, and artificial intelligence",
            "The example problem and metaphor application should be relevant and insightful",
            "The analysis of cognitive processes and computational approaches should be thorough and well-reasoned",
            "The ethical considerations and future directions should be thoughtful and relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
