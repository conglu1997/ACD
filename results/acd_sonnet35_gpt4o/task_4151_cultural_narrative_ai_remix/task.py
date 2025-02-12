import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_narratives = [
            {
                "tradition": "Greek Mythology",
                "narrative": "The Myth of Sisyphus",
                "theme": "Existential struggle and perseverance"
            },
            {
                "tradition": "Native American Folklore",
                "narrative": "The Rainbow Crow",
                "theme": "Self-sacrifice and transformation"
            },
            {
                "tradition": "Chinese Philosophy",
                "narrative": "The Butterfly Dream of Zhuangzi",
                "theme": "Reality, perception, and the nature of existence"
            },
            {
                "tradition": "African Oral Tradition",
                "narrative": "Anansi the Spider",
                "theme": "Wisdom, cunning, and the power of stories"
            }
        ]
        
        contemporary_issues = [
            "Climate change and environmental sustainability",
            "Social media's impact on mental health and society",
            "Artificial intelligence and its ethical implications",
            "Global wealth inequality and economic justice"
        ]
        
        return {
            "1": {
                "narrative": random.choice(cultural_narratives),
                "issue": random.choice(contemporary_issues)
            },
            "2": {
                "narrative": random.choice(cultural_narratives),
                "issue": random.choice(contemporary_issues)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze, deconstruct, and creatively remix cultural narratives, then use it to generate a novel narrative addressing a contemporary social issue. Use the following specifications:

Cultural Narrative: {t['narrative']['tradition']} - {t['narrative']['narrative']} (Theme: {t['narrative']['theme']})
Contemporary Issue: {t['issue']}

Your response should include:

1. AI System Design (250-300 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how it analyzes and deconstructs cultural narratives.
   c) Detail the creative process for remixing and generating new narratives.
   d) Discuss how your system ensures cultural sensitivity and ethical considerations.

2. Narrative Analysis (200-250 words):
   a) Provide a brief analysis of the given cultural narrative.
   b) Identify key elements, symbols, and themes.
   c) Explain how these elements might be relevant to the contemporary issue.

3. Generated Narrative (300-350 words):
   a) Present a new narrative that addresses the given contemporary issue.
   b) Incorporate elements from the original cultural narrative.
   c) Ensure the narrative is culturally sensitive and ethically sound.
   d) Explain how your AI system generated this narrative.

4. Comparative Analysis (200-250 words):
   a) Compare the original narrative with the AI-generated one.
   b) Discuss how the contemporary issue is addressed in the new narrative.
   c) Analyze the effectiveness of the remix in conveying both traditional and modern themes.

5. Ethical Implications (150-200 words):
   a) Discuss potential ethical concerns in remixing cultural narratives.
   b) Address issues of cultural appropriation and misrepresentation.
   c) Propose guidelines for responsible use of AI in cultural narrative generation.

6. Potential Applications (100-150 words):
   a) Suggest two potential applications of your AI system.
   b) Explain how these applications could benefit society or specific fields.

Ensure your response demonstrates a deep understanding of narrative structures, cultural sensitivity, and AI capabilities. Be creative while maintaining respect for the original cultural narratives. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given cultural narrative and contemporary issue.",
            "The AI system design is comprehensive, innovative, and addresses cultural sensitivity.",
            "The generated narrative effectively incorporates elements from the original cultural narrative while addressing the contemporary issue.",
            "The comparative analysis provides insightful observations about the original and generated narratives.",
            "The response thoughtfully addresses ethical implications and potential applications of the AI system.",
            "The overall submission shows creativity, cultural sensitivity, and a strong grasp of AI capabilities in narrative generation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
