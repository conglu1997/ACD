import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "emotions",
                "target_concept": "regret",
                "source_domain": "natural phenomena"
            },
            {
                "domain": "time",
                "target_concept": "procrastination",
                "source_domain": "physical objects"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting novel metaphors. Focus on the domain of {t['domain']}, specifically creating metaphors for the concept of {t['target_concept']} using elements from the source domain of {t['source_domain']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system for metaphor generation and interpretation.
   b) Explain how your system integrates knowledge from linguistics, cognitive science, and AI.
   c) Discuss how your system models the cognitive processes involved in metaphor creation and understanding.

2. Metaphor Generation Process (200-250 words):
   a) Explain the step-by-step process your AI system would use to generate a novel metaphor for {t['target_concept']} using elements from {t['source_domain']}.
   b) Describe any constraints or guidelines your system would follow to ensure the metaphor is both novel and meaningful.
   c) Provide an example of a metaphor your system might generate, along with an explanation of its components.

3. Metaphor Interpretation Mechanism (200-250 words):
   a) Describe how your AI system would interpret and extract meaning from a given metaphor.
   b) Explain how the system would handle ambiguity and multiple possible interpretations.
   c) Discuss how your system would evaluate the quality or effectiveness of a metaphor.

4. Cognitive Science Implications (150-200 words):
   a) Analyze how your AI system's approach to metaphor generation and interpretation relates to theories of human cognition and language processing.
   b) Discuss any insights your system might provide into the nature of human creativity and abstract thinking.

5. Natural Language Processing Applications (150-200 words):
   a) Propose two potential applications of your metaphor-generating AI system in the field of natural language processing or human-computer interaction.
   b) Discuss how these applications could enhance current language technologies.

6. Ethical Considerations and Limitations (100-150 words):
   a) Identify potential ethical concerns or limitations of using AI for metaphor generation and interpretation.
   b) Suggest ways to address these concerns in the development and deployment of such systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and AI principles. Be creative in your system design while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and AI principles.",
            "The AI system design is creative, innovative, and scientifically plausible.",
            "The metaphor generation and interpretation processes are clearly explained and logically sound.",
            "The response effectively analyzes the implications for cognitive science and natural language processing.",
            "The proposed applications and ethical considerations are thoughtful and well-reasoned.",
            f"The system successfully generates and interprets metaphors for {t['target_concept']} using elements from {t['source_domain']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
