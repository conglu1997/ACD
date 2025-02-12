import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "climate change",
            "global unity",
            "artificial intelligence",
            "human rights",
            "biodiversity"
        ]
        cultures = [
            "Western",
            "East Asian",
            "South Asian",
            "African",
            "Middle Eastern"
        ]
        ethical_considerations = [
            "cultural appropriation",
            "unintended offensive symbolism",
            "accessibility",
            "power dynamics",
            "environmental impact"
        ]
        return {
            "1": {
                "concept": random.choice(concepts),
                "cultures": random.sample(cultures, 3),
                "ethical_consideration": random.choice(ethical_considerations)
            },
            "2": {
                "concept": random.choice(concepts),
                "cultures": random.sample(cultures, 3),
                "ethical_consideration": random.choice(ethical_considerations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can create, interpret, and ethically evaluate visual metaphors across different cultures, then apply it to generate a universal symbol for the concept of {t['concept']}. Your system should consider the perspectives of the following cultures: {', '.join(t['cultures'])}. Pay particular attention to the ethical consideration of {t['ethical_consideration']}. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for creating and interpreting visual metaphors.
   b) Explain how your system incorporates cultural knowledge and visual processing capabilities.
   c) Detail the mechanism for ethical evaluation of visual symbols.
   d) Discuss any novel techniques or approaches used in your design.

2. Cross-Cultural Visual Analysis (200-250 words):
   a) Analyze how the concept of {t['concept']} is visually represented in each of the specified cultures.
   b) Identify common themes and significant differences in these representations.
   c) Explain how your AI system would process and learn from these cultural variations.

3. Universal Symbol Generation (250-300 words):
   a) Describe the process your AI system would use to generate a universal symbol for {t['concept']}.
   b) Explain how it balances cultural specificity with global understandability.
   c) Provide a detailed description of the proposed universal symbol.
   d) Discuss how your system ensures the symbol is accessible and meaningful across cultures.

4. Ethical Evaluation (200-250 words):
   a) Analyze the ethical implications of your generated symbol, focusing on {t['ethical_consideration']}.
   b) Explain how your AI system would identify and mitigate potential ethical issues.
   c) Discuss any trade-offs between cultural sensitivity and universal understanding.

5. Limitations and Future Improvements (150-200 words):
   a) Identify potential limitations of your AI system and the generated symbol.
   b) Propose future enhancements to improve cross-cultural visual communication.
   c) Discuss how this technology could impact global communication and understanding.

Ensure your response demonstrates a deep understanding of visual semiotics, cultural anthropology, and AI ethics. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining cultural sensitivity and ethical responsibility.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of visual metaphors and their cultural interpretations, especially for the concept of {t['concept']}.",
            f"The AI system design effectively incorporates cultural knowledge and ethical considerations, particularly {t['ethical_consideration']}.",
            f"The proposed universal symbol balances cultural specificity with global understandability for {t['concept']}.",
            "The ethical evaluation is thorough and considers multiple perspectives.",
            "The response shows creativity and innovation in visual communication while maintaining cultural sensitivity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
