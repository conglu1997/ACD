import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cultures": ["Ancient Egyptian", "Norse"],
                "cognitive_bias": "Anchoring bias",
                "linguistic_feature": "Evidentiality markers"
            },
            {
                "cultures": ["Aztec", "Aboriginal Australian"],
                "cognitive_bias": "Confirmation bias",
                "linguistic_feature": "Honorifics"
            },
            {
                "cultures": ["Ancient Greek", "Maori"],
                "cognitive_bias": "Availability heuristic",
                "linguistic_feature": "Ergative-absolutive alignment"
            },
            {
                "cultures": ["Inuit", "Mesopotamian"],
                "cognitive_bias": "Dunning-Kruger effect",
                "linguistic_feature": "Tonal language features"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a complex cultural narrative that integrates elements from {t['cultures'][0]} and {t['cultures'][1]} cultures, incorporating the cognitive bias of {t['cognitive_bias']} and the linguistic feature of {t['linguistic_feature']}. Your narrative should be a myth or legend that explains a natural phenomenon or cultural practice. Your response should include:

1. Narrative (300-350 words):
   Write a cohesive story that blends elements from both cultures, incorporates the specified cognitive bias, and uses the given linguistic feature. Ensure the narrative is creative, engaging, and culturally respectful.

2. Cultural Analysis (150-200 words):
   Explain how you integrated elements from both cultures in your narrative. Discuss any challenges in blending these potentially disparate cultural elements and how you resolved them.

3. Cognitive Bias Explanation (100-150 words):
   Describe how you incorporated the specified cognitive bias into your narrative. Explain its relevance to the story and how it might influence the characters' decisions or the overall plot.

4. Linguistic Feature Implementation (100-150 words):
   Detail how you utilized the given linguistic feature in your narrative. Provide specific examples from your story and explain how this feature affects the narrative's tone, structure, or meaning.

5. Anthropological Implications (150-200 words):
   Discuss the potential anthropological implications of your synthesized narrative. How might such a blended myth reflect or influence a hypothetical culture? Consider aspects like social structure, belief systems, or cultural practices.

6. Reflection on Cross-Cultural Synthesis (100-150 words):
   Reflect on the process of creating this cross-cultural narrative. Discuss the challenges and opportunities in synthesizing elements from different cultures, and consider the broader implications for understanding cultural exchange and evolution.

Ensure your response demonstrates a deep understanding of the specified cultures, cognitive biases, and linguistic features. Be creative in your narrative while maintaining cultural sensitivity and logical consistency. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The narrative must integrate elements from {t['cultures'][0]} and {t['cultures'][1]} cultures",
            f"The cognitive bias of {t['cognitive_bias']} must be clearly incorporated and explained",
            f"The linguistic feature of {t['linguistic_feature']} must be effectively utilized and analyzed",
            "The response must include all six required sections with appropriate content",
            "The narrative should be creative, engaging, and culturally respectful",
            "The analysis should demonstrate deep understanding of cultural synthesis and its implications"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
