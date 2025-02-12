import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_domains = ['Fluid Dynamics', 'Ecology', 'Quantum Mechanics', 'Thermodynamics']
        target_domains = ['Economics', 'Social Networks', 'Artificial Intelligence', 'Climate Change']
        metaphor_types = ['Structural', 'Ontological', 'Orientational']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'source_domain': random.choice(source_domains),
                'target_domain': random.choice(target_domains),
                'metaphor_type': random.choice(metaphor_types)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses metaphorical reasoning to solve complex problems in scientific domains. Your system should apply concepts from {t['source_domain']} as a metaphorical framework to understand and solve problems in {t['target_domain']}, using a {t['metaphor_type']} metaphor. Your response should include:

1. Metaphor Design (250-300 words):
   a) Explain the key concepts and principles of {t['source_domain']} that will serve as the source domain for your metaphor.
   b) Describe how these concepts can be metaphorically mapped to {t['target_domain']}.
   c) Provide specific examples of how this {t['metaphor_type']} metaphor can be used to understand complex problems in {t['target_domain']}.
   d) Discuss any limitations or potential mismatches in this metaphorical mapping.

2. AI System Architecture (300-350 words):
   a) Describe the overall structure and components of your AI system.
   b) Explain how your system represents and processes metaphorical knowledge.
   c) Detail the mechanisms for applying metaphorical reasoning to problem-solving in {t['target_domain']}.
   d) Discuss how your system integrates domain-specific knowledge with metaphorical reasoning.
   e) Include a high-level diagram or flowchart of your system's architecture (use ASCII art or a structured text description).

3. Problem-Solving Process (200-250 words):
   a) Outline the step-by-step process your AI system would follow to solve a problem in {t['target_domain']} using metaphorical reasoning.
   b) Provide a specific example of a complex problem in {t['target_domain']} and how your system would approach it.
   c) Explain how the metaphorical framework enhances the problem-solving capabilities of your AI system.

4. Learning and Adaptation (200-250 words):
   a) Describe how your AI system learns and refines its metaphorical reasoning over time.
   b) Explain how it adapts to new problems or domains that may not perfectly fit the existing metaphorical framework.
   c) Discuss any mechanisms for generating new metaphors or combining existing ones to tackle novel situations.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your AI system's metaphorical reasoning.
   b) Suggest experiments to validate your system's problem-solving capabilities in {t['target_domain']}.
   c) Discuss how you would compare your system's performance to traditional AI approaches in the same domain.

6. Ethical Considerations and Potential Applications (150-200 words):
   a) Discuss any ethical implications of using metaphorical AI systems for scientific problem-solving.
   b) Explore potential applications of your system beyond {t['target_domain']}.
   c) Consider how this approach might influence scientific research and discovery processes.

Ensure your response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, {t['source_domain']}, and {t['target_domain']}. Use appropriate terminology and provide clear explanations. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['source_domain']} and {t['target_domain']}, and creatively applies concepts from the former to the latter using a {t['metaphor_type']} metaphor.",
            "The AI system architecture is well-designed and clearly explained, with a logical integration of metaphorical reasoning and domain-specific knowledge.",
            "The problem-solving process and learning mechanisms are thoroughly described and demonstrate how metaphorical reasoning enhances the AI's capabilities.",
            "The response shows innovative thinking in applying metaphorical reasoning to AI while maintaining scientific plausibility.",
            "Ethical considerations and potential applications are thoughtfully discussed, showing an understanding of the broader implications of this technology.",
            "The response is well-structured, clear, and adheres to the specified format and word count, with all required sections adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
