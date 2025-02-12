import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        archaeological_periods = [
            "Paleolithic",
            "Neolithic",
            "Bronze Age",
            "Iron Age",
            "Classical Antiquity",
            "Medieval Period"
        ]
        geographical_regions = [
            "Mesopotamia",
            "Ancient Egypt",
            "Indus Valley",
            "Ancient Greece",
            "Mesoamerica",
            "Ancient China"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "period": random.choice(archaeological_periods),
                "region": random.choice(geographical_regions)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for archaeological site discovery and artifact analysis focused on the {t['period']} period in the region of {t['region']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI archaeological discovery system.
   b) Explain how it integrates various data sources (e.g., satellite imagery, historical records, geological data).
   c) Detail the AI/ML techniques used for site identification and artifact analysis.
   d) Discuss how your system ensures accuracy and reliability in its predictions.

2. Discovery Process (250-300 words):
   a) Outline the step-by-step process your AI uses to identify potential archaeological sites.
   b) Explain how the system accounts for the specific characteristics of the {t['period']} period and {t['region']}.
   c) Describe how your AI system prioritizes sites for further investigation.

3. Artifact Analysis (250-300 words):
   a) Detail how your system analyzes and categorizes discovered artifacts.
   b) Explain how it integrates expert knowledge about the {t['period']} period and {t['region']}.
   c) Discuss any novel features that enhance the system's analytical capabilities.

4. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues related to using AI in archaeology, particularly in the context of {t['region']}.
   b) Discuss how your system addresses concerns about cultural sensitivity and heritage preservation.
   c) Propose guidelines for the responsible use of AI in archaeological research.

5. Impact on Archaeological Practice (200-250 words):
   a) Analyze how your AI system might change traditional archaeological methods.
   b) Discuss potential benefits and challenges of integrating AI into archaeology.
   c) Consider how this technology might influence our understanding of the {t['period']} period in {t['region']}.

6. Future Developments (150-200 words):
   a) Propose two potential enhancements or expansions of your system.
   b) Discuss how emerging technologies might further revolutionize AI-assisted archaeology.

Ensure your response demonstrates a deep understanding of both artificial intelligence and archaeology. Use appropriate terminology from both fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and historical accuracy.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both AI technologies and archaeological principles",
            "The proposed AI system is innovative and tailored to the specific archaeological period and region",
            "The response addresses ethical considerations and cultural sensitivity in AI-assisted archaeology",
            "The analysis of the system's impact on archaeological practice is thoughtful and comprehensive",
            "The response is well-structured, clear, and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
