import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion": "Schadenfreude",
                "context": "Social media interactions",
                "application": "Sentiment analysis"
            },
            {
                "emotion": "Nostalgia",
                "context": "Personal narratives",
                "application": "Therapeutic chatbot"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that encodes and processes emotional states within its language representation, focusing on the emotion of {t['emotion']} in the context of {t['context']}. Then, apply this system to the task of {t['application']}. Your response should include:

1. Emotional Encoding Mechanism (250-300 words):
   a) Describe how your AI system encodes the specified emotion within its language representation.
   b) Explain the neurological and psychological basis for your approach.
   c) Discuss how this encoding interacts with other linguistic features (e.g., syntax, semantics).
   d) Provide a simple diagram or pseudocode snippet illustrating a key aspect of your emotional encoding mechanism.

2. Contextual Integration (200-250 words):
   a) Explain how your system integrates the encoded emotion with the given context.
   b) Describe any novel techniques used to maintain emotional consistency across different contexts.
   c) Discuss potential challenges in accurately representing emotions in the specified context.

3. Application Implementation (250-300 words):
   a) Detail how your emotionally-aware AI system is applied to the specified task.
   b) Provide a concrete example of the system in use, including input, processing steps, and output.
   c) Analyze the potential benefits and limitations of using emotionally-encoded language for this application.

4. Comparative Analysis (200-250 words):
   a) Compare your emotion-encoding approach to traditional methods in affective computing and natural language processing.
   b) Discuss how your system might perform differently from humans in emotional language tasks.
   c) Identify potential biases or limitations in your approach and suggest mitigation strategies.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns or societal impacts of AI systems with emotional awareness.
   b) Discuss the implications for human-AI interaction and emotional manipulation.
   c) Propose guidelines for responsible development and use of emotionally-intelligent AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your emotional language encoding system.
   b) Propose an experiment to further explore the relationship between AI, language, and emotions.
   c) Speculate on how this research might influence our understanding of human emotions and cognition.

Ensure your response demonstrates a deep understanding of emotions, linguistics, and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of the emotional encoding mechanism",
            "The contextual integration is well-explained and addresses potential challenges",
            "The application implementation provides a concrete example with clear input, processing, and output",
            "The comparative analysis critically evaluates the approach against traditional methods",
            "Ethical considerations are thoroughly discussed with proposed guidelines",
            "Future research directions are innovative and well-reasoned",
            "The response demonstrates a deep understanding of emotions, linguistics, and AI systems",
            "The approach is creative while maintaining scientific and technological plausibility",
            "Appropriate technical terminology is used throughout the response",
            "The response is well-structured with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
