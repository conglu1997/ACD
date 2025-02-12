import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_themes = [
            {
                "theme": "Time",
                "languages": ["English", "Mandarin Chinese"],
                "cultural_context": "Western vs. Eastern perspectives on time"
            },
            {
                "theme": "Love",
                "languages": ["French", "Arabic"],
                "cultural_context": "Romantic vs. familial love in different cultures"
            }
        ]
        return {
            "1": random.choice(metaphor_themes),
            "2": random.choice(metaphor_themes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate and analyze metaphors related to the theme of {t['theme']} in {t['languages'][0]} and {t['languages'][1]}, considering the cultural context: {t['cultural_context']}.

1. Generate Metaphors (50-75 words each):
   a) Create a metaphor in {t['languages'][0]} related to {t['theme']}.
   b) Create a metaphor in {t['languages'][1]} related to {t['theme']}.
   Provide both the original language version and an English translation for each metaphor.

2. Linguistic Analysis (100-150 words for each metaphor):
   Analyze the linguistic structure of each metaphor, including:
   - Identification of the source and target domains
   - Explanation of how the metaphor is constructed grammatically
   - Discussion of any language-specific features that contribute to the metaphor's effectiveness

3. Cultural Implications (150-200 words):
   Compare and contrast the cultural implications of both metaphors, considering:
   - How each metaphor reflects cultural attitudes towards {t['theme']}
   - The role of {t['cultural_context']} in shaping these metaphors
   - Potential challenges in translating or explaining these metaphors across cultures

4. Cross-linguistic Comparison (100-150 words):
   Analyze how the concept of {t['theme']} is differently represented in the two languages through these metaphors. Consider:
   - Similarities and differences in conceptual mapping
   - How linguistic features of each language influence metaphor creation
   - The universality or culture-specificity of the metaphorical concepts used

5. Creative Extension (50-75 words):
   Propose a new metaphor for {t['theme']} that could be understood and appreciated in both cultures, explaining your reasoning.

Ensure your response demonstrates deep linguistic knowledge, cultural sensitivity, and creative thinking. Use appropriate terminology and provide clear explanations throughout your analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes two well-crafted metaphors in the specified languages, with accurate translations.",
            "The linguistic analysis demonstrates a deep understanding of metaphor structure and language-specific features.",
            "The cultural implications are thoroughly explored, showing insight into the given cultural context.",
            "The cross-linguistic comparison effectively highlights similarities and differences between the metaphors.",
            "The creative extension proposes a thoughtful metaphor that bridges both cultures.",
            "The overall analysis demonstrates strong linguistic knowledge, cultural sensitivity, and creative thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
