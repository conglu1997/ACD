import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        civilizations = [
            "Ancient Mesopotamia",
            "Indus Valley Civilization",
            "Ancient Egypt",
            "Minoan Civilization",
            "Maya Civilization"
        ]
        
        evidence_types = [
            "Architectural remains",
            "Written records",
            "Artifacts",
            "Environmental data",
            "Genetic information",
            "Isotope analysis results",
            "Geophysical survey data"
        ]
        
        historical_mysteries = [
            "Sudden collapse of the civilization",
            "Unexplained technological advancements",
            "Mysterious religious practices",
            "Unidentified trade networks",
            "Enigmatic artistic symbols",
            "Abrupt changes in social hierarchy",
            "Unexplained population movements"
        ]
        
        ai_approaches = [
            "Deep learning for pattern recognition",
            "Natural language processing for ancient texts",
            "Generative adversarial networks for visual reconstruction",
            "Reinforcement learning for hypothesis testing",
            "Knowledge graphs for connecting disparate evidence",
            "Bayesian networks for uncertainty modeling",
            "Computer vision for artifact analysis"
        ]
        
        return {
            "1": {
                "civilization": random.choice(civilizations),
                "primary_evidence": random.choice(evidence_types),
                "secondary_evidence": random.choice(evidence_types),
                "mystery": random.choice(historical_mysteries),
                "ai_approach": random.choice(ai_approaches)
            },
            "2": {
                "civilization": random.choice(civilizations),
                "primary_evidence": random.choice(evidence_types),
                "secondary_evidence": random.choice(evidence_types),
                "mystery": random.choice(historical_mysteries),
                "ai_approach": random.choice(ai_approaches)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to reconstruct and analyze the {t['civilization']} based primarily on {t['primary_evidence']} and secondarily on {t['secondary_evidence']}. Then use your system to generate hypotheses about the historical mystery: {t['mystery']}. Your AI approach should focus on {t['ai_approach']}.

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for archaeological reconstruction and analysis.
   b) Explain how it processes and integrates the primary and secondary evidence types.
   c) Detail how the system implements the specified AI approach.
   d) Discuss any novel features or innovations in your design.
   e) Include a small code snippet or pseudocode (30-50 lines) demonstrating a key aspect of your system's implementation of the specified AI approach.

2. Data Processing and Integration (250-300 words):
   a) Explain how your system handles the challenges of incomplete and fragmentary archaeological data.
   b) Describe the methods used to integrate different types of evidence.
   c) Discuss how the system deals with uncertainties and contradictions in the available evidence.

3. Civilization Reconstruction (300-350 words):
   a) Outline how your AI system would reconstruct key aspects of the specified civilization (e.g., social structure, technology, economy).
   b) Provide an example of a specific insight or reconstruction your system might generate.
   c) Explain how the system validates its reconstructions against known historical facts.

4. Mystery Analysis and Hypothesis Generation (300-350 words):
   a) Describe how your system approaches the specified historical mystery.
   b) Detail the process of generating hypotheses to explain the mystery.
   c) Provide two plausible hypotheses your system might generate, explaining the reasoning behind each.
   d) Discuss how your system would evaluate and rank these hypotheses.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues in using AI for historical reconstruction and hypothesis generation.
   b) Address concerns about cultural sensitivity and potential biases in your system.
   c) Analyze limitations of your approach and areas where human expertise remains crucial.

6. Interdisciplinary Implications (200-250 words):
   a) Explore how your AI system could impact the field of archaeology and historical research.
   b) Discuss potential applications of your system in other disciplines (e.g., anthropology, art history).
   c) Propose an experiment to test your system's effectiveness in generating new historical insights.

Ensure your response demonstrates a deep understanding of AI, archaeology, and historical analysis. Be creative and original in your approach while maintaining scientific plausibility. Use clear headings for each section of your response, numbered as above. Your total response should be between 1550-1850 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of both AI technologies and archaeological/historical analysis.",
            "The AI system design effectively incorporates the specified AI approach and evidence types.",
            "The civilization reconstruction and mystery analysis are creative, plausible, and well-reasoned.",
            "The response critically analyzes ethical implications and limitations of the proposed system.",
            "The discussion of interdisciplinary implications is insightful and considers multiple perspectives.",
            "The provided code snippet or pseudocode is relevant and demonstrates a key aspect of the system's implementation of the specified AI approach.",
            "The overall response is well-structured, innovative, and scientifically plausible.",
            "The response follows the specified format with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
