import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_load_factors = [
            {
                "factor": "syntactic complexity",
                "description": "Use nested clauses and complex grammatical structures"
            },
            {
                "factor": "working memory load",
                "description": "Increase distance between related elements in the sentence"
            },
            {
                "factor": "semantic ambiguity",
                "description": "Incorporate words or phrases with multiple possible interpretations"
            }
        ]
        return {
            "1": random.choice(cognitive_load_factors),
            "2": random.choice(cognitive_load_factors)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates sentences with varying levels of cognitive load, focusing on the factor of {t['factor']}. Then, analyze and explain the cognitive demands of processing these sentences. Your response should include:

1. System Design (250-300 words):
   a) Describe the architecture of your AI system for generating sentences with varying cognitive load.
   b) Explain how your system incorporates the specific cognitive load factor of {t['factor']}.
   c) Discuss any novel components or mechanisms in your system that enable it to model cognitive load.

2. Sentence Generation (200-250 words):
   a) Generate three sentences (each 15-25 words long) with increasing levels of cognitive load based on {t['factor']}.
   b) Explain how each sentence demonstrates an increase in cognitive load.
   c) Discuss the specific linguistic features or structures used to manipulate cognitive load.

3. Cognitive Load Analysis (250-300 words):
   a) Analyze the cognitive demands of processing each generated sentence.
   b) Explain the specific cognitive processes involved in comprehending these sentences.
   c) Discuss how the {t['factor']} affects the overall cognitive load of each sentence.

4. Comparative Analysis (200-250 words):
   a) Compare the cognitive load of your generated sentences to a simple baseline sentence.
   b) Discuss how different linguistic features contribute to cognitive load.
   c) Explain how your analysis relates to theories of human language processing.

5. AI Implications (150-200 words):
   a) Discuss the challenges and limitations of modeling cognitive load in AI systems.
   b) Explain how this task reveals insights about AI language understanding compared to human processing.
   c) Propose potential applications or extensions of this cognitive load modeling in AI.

6. Conclusion (50-100 words):
   Summarize the key insights from your analysis and discuss the broader implications for AI language models and cognitive linguistics.

Ensure your response demonstrates a deep understanding of cognitive linguistics and AI language processing. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics and AI language processing.",
            "The generated sentences clearly show increasing levels of cognitive load based on the given factor and adhere to the specified word limit.",
            "The analysis of cognitive demands is thorough and well-explained.",
            "The comparative analysis provides meaningful insights into cognitive load and language processing.",
            "The discussion of AI implications is insightful and considers both challenges and potential applications.",
            "The conclusion effectively summarizes key insights and broader implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
