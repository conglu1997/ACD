import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_phenomena = [
            {
                'phenomenon': 'Syntax acquisition',
                'human_aspect': 'Universal Grammar theory',
                'ai_aspect': 'Transformer architecture'
            },
            {
                'phenomenon': 'Semantic understanding',
                'human_aspect': 'Embodied cognition',
                'ai_aspect': 'Distributional semantics'
            },
            {
                'phenomenon': 'Pragmatic inference',
                'human_aspect': 'Theory of Mind development',
                'ai_aspect': 'Context-aware language models'
            },
            {
                'phenomenon': 'Morphological processing',
                'human_aspect': 'Dual-route model',
                'ai_aspect': 'Subword tokenization'
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(random.sample(linguistic_phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compare and contrast human language acquisition with AI language model training, focusing on {t['phenomenon']}. Your analysis should include:

1. Human Language Acquisition (200-250 words):
   a) Explain the process of {t['phenomenon']} in human language acquisition.
   b) Describe the role of {t['human_aspect']} in this process.
   c) Discuss any critical periods or developmental stages related to this phenomenon.

2. AI Language Model Training (200-250 words):
   a) Explain how {t['phenomenon']} is approached in AI language model training.
   b) Describe the role of {t['ai_aspect']} in this process.
   c) Discuss any key challenges or breakthroughs in modeling this phenomenon in AI.

3. Comparative Analysis (250-300 words):
   a) Identify key similarities and differences between human and AI approaches to {t['phenomenon']}.
   b) Analyze the strengths and limitations of each approach.
   c) Discuss how insights from one domain might inform or improve the other.

4. Cognitive Implications (150-200 words):
   a) Explore what the similarities and differences reveal about human cognition and artificial intelligence.
   b) Discuss any implications for our understanding of language and thought.

5. Future Directions (150-200 words):
   a) Propose a research question or experiment that could further our understanding of {t['phenomenon']} in both humans and AI.
   b) Suggest a potential innovation in AI language model design inspired by human language acquisition.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be analytical and insightful in your comparisons, drawing on current research and theories in both fields."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['phenomenon']} in both human language acquisition and AI language model training.",
            f"The explanation of {t['human_aspect']} and {t['ai_aspect']} is accurate and relevant.",
            "The comparative analysis is insightful and well-reasoned.",
            "The discussion of cognitive implications shows a nuanced understanding of both human and artificial intelligence.",
            "The proposed future directions are innovative and grounded in the preceding analysis.",
            "The response uses appropriate technical terminology from linguistics, cognitive science, and AI.",
            "The analysis is well-structured, clear, and within the specified word counts for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
