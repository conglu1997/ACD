import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "Healthcare",
                "decision": "Treatment options for a chronic illness",
                "framing_types": ["Gain frame", "Loss frame"]
            },
            {
                "domain": "Finance",
                "decision": "Investment strategies for retirement",
                "framing_types": ["Risk-averse frame", "Risk-seeking frame"]
            },
            {
                "domain": "Environmental Policy",
                "decision": "Adoption of renewable energy sources",
                "framing_types": ["Long-term benefit frame", "Short-term cost frame"]
            },
            {
                "domain": "AI Ethics",
                "decision": "Implementation of facial recognition technology",
                "framing_types": ["Security enhancement frame", "Privacy invasion frame"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze how linguistic framing affects decision-making processes in AI systems and humans, then design an experiment to test these effects. Focus on the domain of {t['domain']} for the decision of {t['decision']}. Your response should include:

1. Linguistic Analysis (200-250 words):
   a) Explain how the decision could be framed using the {t['framing_types'][0]} and the {t['framing_types'][1]}.
   b) Provide specific examples of language that would be used in each framing.
   c) Analyze how these framings might influence human decision-making, citing relevant psycholinguistic theories.

2. AI Decision-Making Model (250-300 words):
   a) Design a hypothetical AI decision-making model that takes linguistic input as part of its decision process.
   b) Explain how this model might process and be influenced by the different linguistic framings.
   c) Discuss potential biases or vulnerabilities in the AI system related to linguistic framing.

3. Experimental Design (250-300 words):
   a) Propose an experiment to test the effects of linguistic framing on both human and AI decision-making in this scenario.
   b) Describe the methodology, including participant selection, experimental conditions, and data collection methods.
   c) Explain how you would measure and compare the impact of framing on humans versus AI systems.

4. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using linguistic framing to influence decision-making in {t['domain']}.
   b) Consider potential consequences for individuals, society, and AI development.
   c) Propose guidelines for the responsible use of framing in AI-human interactions.

5. Interdisciplinary Implications (150-200 words):
   a) Explain how this research could contribute to fields such as cognitive science, AI ethics, and behavioral economics.
   b) Discuss potential applications or consequences of this knowledge in real-world scenarios.

Ensure your response demonstrates a deep understanding of psycholinguistics, decision theory, and AI systems. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your experimental design while maintaining scientific rigor.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) where applicable. Your total response should be between 1000-1250 words. Do not include any introductory or concluding paragraphs outside of the numbered sections."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a thorough linguistic analysis of the two framing types with specific examples",
            "A plausible AI decision-making model is designed and explained, including its processing of linguistic frames",
            "The experimental design is well-structured, addressing both human and AI decision-making with clear methodology",
            "Ethical considerations are thoughtfully discussed, including guidelines for responsible use",
            "Interdisciplinary implications are explored in depth, with concrete examples of potential applications",
            "The response demonstrates a deep understanding of psycholinguistics, decision theory, and AI systems, using appropriate terminology",
            "The writing is clear, well-organized, and adheres to the specified structure and word count guidelines",
            "The response avoids generic statements and provides specific, context-relevant information for the given domain and decision"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
