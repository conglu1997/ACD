import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Physics",
            "Biology",
            "Economics",
            "Music",
            "Architecture",
            "Cuisine",
            "Mathematics",
            "Literature"
        ]
        task1 = random.sample(domains, 2)
        task2 = random.sample(domains, 2)
        return {
            "1": {"domain1": task1[0], "domain2": task1[1]},
            "2": {"domain1": task2[0], "domain2": task2[1]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting conceptual blends between {t['domain1']} and {t['domain2']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for conceptual blending.
   b) Explain how your system represents and processes domain-specific knowledge.
   c) Detail the mechanisms for identifying potential connections between domains.
   d) Discuss how your system generates novel conceptual blends.

2. Conceptual Blending Process (200-250 words):
   a) Explain the steps your system takes to create a conceptual blend.
   b) Describe how your system ensures the coherence and novelty of generated blends.
   c) Discuss how your system handles potential conflicts or incompatibilities between domains.

3. Interpretation and Evaluation (200-250 words):
   a) Detail how your system interprets and explains the generated conceptual blends.
   b) Propose metrics for evaluating the quality, creativity, and usefulness of the blends.
   c) Describe how your system could learn and improve from feedback on its blends.

4. Example Blends (250-300 words):
   Provide two examples of conceptual blends your system might generate between {t['domain1']} and {t['domain2']}:
   a) Describe each blend in detail.
   b) Explain the reasoning behind these blends, highlighting key connections between the domains.
   c) Discuss potential applications or insights derived from these blends.

5. Cognitive Science Connections (150-200 words):
   a) Relate your system's approach to theories of human conceptual blending and creativity.
   b) Discuss how your system might inform or be informed by cognitive science research.

6. Potential Applications (150-200 words):
   a) Propose three potential applications of your conceptual blending AI system.
   b) Discuss how these applications might impact creativity and problem-solving in various fields.

7. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or challenges in your approach.
   b) Discuss any ethical considerations related to AI-generated conceptual blends.
   c) Propose guidelines for the responsible development and use of conceptual blending AI.

Ensure your response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and the specific domains involved. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) where indicated. Your total response should be between 1350-1700 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual blending and cognitive linguistics.",
            "The AI system design is innovative, coherent, and scientifically plausible.",
            "The conceptual blending process is well-explained and accounts for coherence and novelty.",
            "The example blends are creative and show meaningful connections between the given domains.",
            "The response includes thoughtful discussion of cognitive science connections, applications, and ethical considerations.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "All sections of the response are complete and adhere to the word count guidelines.",
            "The response follows the specified format with numbered sections and subheadings.",
            "The proposed AI system is capable of generating and interpreting conceptual blends between the specified domains.",
            "The response includes a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
