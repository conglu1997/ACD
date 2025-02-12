import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "climate policy",
                "time_scales": ["immediate (0-5 years)", "decadal (5-30 years)", "centennial (30-100 years)"],
                "decision_type": "resource allocation",
                "example_decision": "Allocating funds between immediate disaster relief and long-term infrastructure adaptation"
            },
            {
                "domain": "artificial intelligence development",
                "time_scales": ["near-term (0-5 years)", "mid-term (5-15 years)", "long-term (15+ years)"],
                "decision_type": "ethical framework implementation",
                "example_decision": "Choosing between prioritizing short-term AI safety measures and investing in long-term value alignment research"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a temporal decision-making system that models cascading effects of choices across multiple time scales in the domain of {t['domain']}. Your system should focus on {t['decision_type']} decisions and consider the following time scales: {', '.join(t['time_scales'])}. Use the example decision of {t['example_decision']} as a starting point for your analysis. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your temporal decision-making system.
   b) Explain how your system models decisions and their consequences across different time scales.
   c) Detail any novel algorithms or techniques used in your model.
   d) Include a brief diagram or flowchart description of your system architecture.
   e) Provide at least one mathematical formula or quantitative rule that governs a key aspect of your system.

2. Decision Analysis (250-300 words):
   a) Analyze how your system would process the example decision across the given time scales.
   b) Discuss potential cascading effects and their implications.
   c) Provide a numerical example of how your system would quantify the impact of a decision at different time scales.

3. Temporal Dynamics (200-250 words):
   a) Explain how your system accounts for changing conditions over time.
   b) Describe any feedback loops or non-linear effects in your model.
   c) Discuss how your system handles uncertainty in long-term projections.

4. Interdisciplinary Integration (200-250 words):
   a) Identify at least three distinct academic or professional disciplines relevant to your system.
   b) Explain how knowledge from each discipline is incorporated into your model.
   c) Discuss any challenges in integrating these diverse fields.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of using your system for decision-making in {t['domain']}.
   b) Address potential biases or limitations in your approach.
   c) Propose a specific ethical framework for guiding decisions in your system, explaining how it addresses the unique challenges of {t['domain']}.
   d) Suggest guidelines for responsible use of temporal decision-making systems.

6. Practical Application (150-200 words):
   a) Describe how your system could be implemented in real-world {t['domain']} decision-making processes.
   b) Discuss potential benefits and challenges of adopting your system.
   c) Suggest a method to evaluate the effectiveness of your system in practice, including at least one quantitative metric.

Ensure your response demonstrates a deep understanding of complex systems, decision theory, and the specific domain of {t['domain']}. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and logical consistency.

Format your response with clear headings for each section and number your paragraphs within each section. Adhere to the word count guidelines provided for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of complex systems and decision theory",
            "The proposed system effectively models decisions and their consequences across multiple time scales",
            "The analysis integrates knowledge from multiple relevant disciplines",
            "The explanation is clear, well-structured, and uses appropriate technical terminology",
            "The response addresses all required sections comprehensively, adhering to the provided word count guidelines",
            "The proposed system demonstrates innovative thinking while maintaining scientific plausibility",
            "The response includes at least one mathematical formula or quantitative rule and provides numerical examples",
            "The response critically analyzes ethical implications and proposes a specific ethical framework for the given domain",
            "The practical application section includes a quantitative metric for evaluating the system's effectiveness"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
