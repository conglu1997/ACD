import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "language": "Hopi",
                "feature": "Tenseless language",
                "task": "Describe a sequence of events"
            },
            {
                "language": "Pirahã",
                "feature": "Lack of number words and limited color terms",
                "task": "Categorize and count objects"
            },
            {
                "language": "Guugu Yimithirr",
                "feature": "Absolute spatial reference system",
                "task": "Navigate through a complex environment"
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can dynamically shift between different linguistic frameworks, focusing on the unique features of {t['language']} ({t['feature']}). Then, analyze how this system would approach the task: {t['task']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system that enable linguistic framework shifting.
   b) Explain how your system incorporates the specific features of {t['language']}.
   c) Detail the mechanism for dynamically altering perception and problem-solving approaches.
   d) Include a simple diagram or schematic representation of your system (describe it textually).

2. Linguistic Implementation (200-250 words):
   a) Explain how you model the unique linguistic features of {t['language']} in your AI system.
   b) Discuss how these features might influence the system's cognitive processes.
   c) Compare this to how the system might operate using a more familiar language like English.

3. Task Approach Analysis (250-300 words):
   a) Describe in detail how your AI system would approach the task: {t['task']}.
   b) Explain how the linguistic features of {t['language']} influence the problem-solving strategy.
   c) Discuss potential advantages or challenges this linguistic framework presents for the given task.

4. Cognitive Implications (200-250 words):
   a) Analyze how your system's approach to the task might differ from that of a human speaker of {t['language']}.
   b) Discuss what this reveals about the relationship between language and cognition in AI systems.
   c) Propose a hypothesis about human cognition that could be tested using your system.

5. Ethical and Philosophical Considerations (150-200 words):
   a) Discuss the ethical implications of creating AI systems that can shift between linguistic frameworks.
   b) Explore how this technology might impact our understanding of language, thought, and consciousness.
   c) Address potential concerns about cultural appropriation or misrepresentation.

6. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your system for future research.
   b) Explain how these extensions might further our understanding of linguistic relativity in AI.

Ensure your response demonstrates a deep understanding of linguistic theories, cognitive science principles, and AI system design. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic relativity and the specific features of the given language",
            "The AI system design is innovative, plausible, and well-explained",
            "The analysis of the task approach is thorough and shows clear links between linguistic features and problem-solving strategies",
            "The response addresses cognitive implications and proposes testable hypotheses",
            "Ethical and philosophical considerations are thoughtfully discussed",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
