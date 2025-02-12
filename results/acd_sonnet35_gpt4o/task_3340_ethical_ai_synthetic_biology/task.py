import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "Gene Editing",
                "application": "Disease Resistance",
                "ethical_concern": "Unintended ecological consequences"
            },
            {
                "domain": "Protein Design",
                "application": "Novel Enzymes",
                "ethical_concern": "Dual-use potential for bioweapons"
            },
            {
                "domain": "Metabolic Engineering",
                "application": "Biofuel Production",
                "ethical_concern": "Competition with food resources"
            },
            {
                "domain": "Synthetic Genomics",
                "application": "De-extinction",
                "ethical_concern": "Altering natural ecosystems"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to guide synthetic biology experiments in the domain of {t['domain']}, specifically for {t['application']}. Your system should integrate advanced AI techniques with synthetic biology principles while addressing ethical considerations, particularly {t['ethical_concern']}. Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for guiding synthetic biology experiments.
   b) Explain how these components interact to process biological data and guide experiments.
   c) Discuss how your system incorporates machine learning techniques for prediction and optimization.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Synthetic Biology Integration (200-250 words):
   a) Explain how your AI system interfaces with synthetic biology tools and techniques.
   b) Describe how it processes and interprets biological data.
   c) Discuss any novel approaches your system uses to model complex biological systems.

3. Ethical Considerations (250-300 words):
   a) Address the specified ethical concern in detail.
   b) Explain how your AI system is designed to identify and mitigate potential ethical issues.
   c) Discuss any additional ethical considerations relevant to your system's application.
   d) Propose guidelines for responsible development and use of AI in synthetic biology.

4. Experimental Guidance (200-250 words):
   a) Describe how your AI system guides the design and execution of experiments.
   b) Explain how it optimizes experimental parameters and predicts outcomes.
   c) Discuss how the system handles uncertainty and unexpected results.

5. Societal Impact Analysis (200-250 words):
   a) Analyze potential societal impacts of your AI-guided synthetic biology system.
   b) Discuss both positive and negative potential outcomes.
   c) Propose measures to maximize benefits and minimize risks to society.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your AI system.
   b) Suggest areas for future research or improvements.
   c) Discuss how this technology could evolve in the next decade.

Ensure your response demonstrates a deep understanding of both artificial intelligence and synthetic biology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and plausible AI system architecture for guiding synthetic biology experiments in {t['domain']}.",
            f"The synthetic biology integration section adequately addresses the challenges specific to {t['application']}.",
            f"The ethical considerations component convincingly addresses {t['ethical_concern']} and proposes responsible guidelines.",
            "The experimental guidance section demonstrates a nuanced understanding of both AI and synthetic biology principles.",
            "The societal impact analysis is comprehensive and balanced, considering both potential benefits and risks.",
            "The limitations and future directions discussion is thoughtful and forward-looking.",
            "The overall response displays creativity, scientific plausibility, and a strong interdisciplinary approach to the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
