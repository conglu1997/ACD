import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        temporal_aspects = [
            {
                "aspect": "Tense and Aspect",
                "concepts": ["past", "present", "future", "perfect", "progressive", "habitual"]
            },
            {
                "aspect": "Temporal Deixis",
                "concepts": ["now", "then", "yesterday", "tomorrow", "ago", "later"]
            }
        ]
        return {str(i+1): aspect for i, aspect in enumerate(random.sample(temporal_aspects, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a temporal linguistic framework that models how language encodes and processes time-related concepts, focusing on the temporal aspect of {t['aspect']}. Then, apply this framework to enhance an AI system's temporal reasoning capabilities. Your response should include:

1. Temporal Linguistic Framework (300-350 words):
   a) Describe the key components of your temporal linguistic framework.
   b) Explain how it models the encoding and processing of the following time-related concepts: {', '.join(t['concepts'])}.
   c) Discuss how your framework integrates insights from cognitive science and linguistics.
   d) Provide a visual representation or diagram of your framework. Use ASCII art or a textual description of the diagram if you cannot generate images.

2. Cognitive Processing Model (250-300 words):
   a) Propose a model for how the human brain might process and represent the temporal aspects in your framework.
   b) Explain how this model accounts for cultural and linguistic variations in temporal cognition.
   c) Discuss any novel hypotheses your model generates about human temporal reasoning.

3. AI System Enhancement (250-300 words):
   a) Describe how you would implement your temporal linguistic framework in an AI system.
   b) Explain how this implementation could enhance the AI's ability to understand and generate time-related language.
   c) Provide a specific example of how your enhanced AI system would process a complex temporal statement.
   d) Include a brief pseudocode snippet (5-10 lines) demonstrating a key function of your implementation.

4. Comparative Analysis (200-250 words):
   a) Compare your temporal framework and its AI implementation to current approaches in natural language processing.
   b) Discuss potential advantages and limitations of your approach.
   c) Analyze how your framework might address current challenges in AI temporal reasoning.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness of your temporal linguistic framework in enhancing AI temporal reasoning.
   b) Describe the methodology, including data collection and evaluation metrics.
   c) Discuss potential outcomes and their implications for both AI development and our understanding of human temporal cognition.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss any ethical considerations arising from developing AI systems with enhanced temporal reasoning capabilities.
   b) Explore potential practical applications of your framework in fields such as language education, cognitive therapy, or predictive modeling.

7. Future Research Directions (100-150 words):
   a) Propose two potential extensions or modifications to your temporal linguistic framework.
   b) Briefly describe how these extensions could further our understanding of temporal cognition or improve AI language processing.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Temporal Linguistic Framework:') followed by your response for that section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence in the context of {t['aspect']}.",
            "The proposed temporal linguistic framework is innovative, well-explained, and integrates insights from cognitive science and linguistics.",
            f"The framework effectively models the encoding and processing of the specified time-related concepts: {', '.join(t['concepts'])}.",
            "A clear visual representation or diagram of the framework is provided.",
            "The cognitive processing model is plausible and accounts for cultural and linguistic variations in temporal cognition.",
            "The AI system enhancement is clearly described and demonstrates how the framework could improve temporal reasoning in AI.",
            "A relevant pseudocode snippet is included to demonstrate a key function of the implementation.",
            "The comparative analysis thoroughly discusses advantages, limitations, and potential improvements over current approaches.",
            "The experimental design is well-thought-out and would effectively test the framework's impact on AI temporal reasoning.",
            "Ethical and practical implications are insightfully discussed, considering both risks and potential applications.",
            "The proposed future research directions are innovative and have the potential to advance the field.",
            "The response is well-formatted with clear headings and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
