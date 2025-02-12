import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ai_architectures = [
            "Transformer-based language model",
            "Recurrent Neural Network (RNN)",
            "Generative Adversarial Network (GAN)",
            "Neuro-symbolic AI"
        ]
        cultural_contexts = [
            "Western",
            "East Asian",
            "Middle Eastern",
            "African"
        ]
        abstract_concepts = [
            "time",
            "love",
            "knowledge",
            "power"
        ]
        
        tasks = [
            {
                "ai_architecture": arch,
                "cultural_context": context,
                "abstract_concept": concept
            }
            for arch in ai_architectures
            for context in cultural_contexts
            for concept in abstract_concepts
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze how a {t['ai_architecture']} would generate and interpret metaphors for the abstract concept of '{t['abstract_concept']}' in a {t['cultural_context']} cultural context. Your response should include:

1. AI Architecture Analysis (150-200 words):
   a) Briefly explain how the {t['ai_architecture']} processes and generates language.
   b) Discuss potential strengths and limitations of this architecture for metaphor generation and interpretation.

2. Cultural Context (100-150 words):
   a) Describe key aspects of {t['cultural_context']} culture that might influence metaphor use for '{t['abstract_concept']}'.
   b) Provide two examples of common metaphors for '{t['abstract_concept']}' in this cultural context.

3. Metaphor Generation (150-200 words):
   a) Propose three novel metaphors that the AI might generate for '{t['abstract_concept']}' in this cultural context.
   b) Explain the reasoning behind each metaphor, considering both the AI architecture and cultural influences.

4. Interpretation and Analysis (150-200 words):
   a) Analyze how the AI might interpret and process these metaphors.
   b) Discuss any potential biases or limitations in the AI's understanding of the metaphors.

5. Cross-cultural Comparison (100-150 words):
   Compare how the same AI architecture might generate different metaphors for '{t['abstract_concept']}' in a contrasting cultural context.

6. Ethical Implications (100-150 words):
   Discuss potential ethical considerations or societal impacts of AI-generated metaphors in cross-cultural communication.

7. Future Research Direction (50-100 words):
   Propose a specific research question or experiment to further explore the interaction between AI architectures, metaphor processing, and cultural contexts.

8. Key Findings Summary (100-150 words):
   Provide a concise summary of the main insights and conclusions from your analysis.

Ensure your response demonstrates a deep understanding of the specified AI architecture, metaphor theory, and cultural influences on language. Be creative in your metaphor generation while maintaining cultural sensitivity and plausibility. The total word count for your response should be between 900-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified AI architecture and its potential impact on metaphor generation and interpretation.",
            "The cultural context is accurately represented, and the proposed metaphors are culturally appropriate and creative.",
            "The analysis of metaphor generation and interpretation is insightful and considers both technical and cultural factors.",
            "The cross-cultural comparison and ethical implications are thoughtfully discussed.",
            "The proposed research direction is relevant and well-formulated.",
            "The generated metaphors are novel, creative, and appropriate for the given context.",
            "The key findings summary effectively synthesizes the main insights from the analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0