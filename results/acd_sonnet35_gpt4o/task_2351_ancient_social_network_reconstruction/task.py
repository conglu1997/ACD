import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        archaeological_contexts = [
            {
                "name": "Neolithic Çatalhöyük",
                "period": "7100-5950 BCE",
                "location": "Anatolia (modern-day Turkey)",
                "key_features": "Dense settlement, lack of streets, rooftop mobility"
            },
            {
                "name": "Roman Pompeii",
                "period": "Before 79 CE",
                "location": "Italy",
                "key_features": "Well-preserved urban layout, graffiti, household items"
            }
        ]
        return {
            "1": random.choice(archaeological_contexts),
            "2": random.choice(archaeological_contexts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze archaeological data and reconstruct ancient social networks for {t['name']} ({t['period']}) in {t['location']}. Your system should incorporate principles from computer science, archaeology, anthropology, and network theory to create a comprehensive model of social interactions and community structure. Consider the key features of this site: {t['key_features']}.

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for analyzing archaeological data and reconstructing social networks.
   b) Explain how your system integrates methods from different disciplines (e.g., computer vision for artifact analysis, natural language processing for textual evidence, network analysis for social structures).
   c) Detail how the system handles uncertainty and incomplete data, which are common in archaeological contexts.
   d) Discuss any novel AI approaches or algorithms used in your system.
   e) Provide a simple diagram or pseudocode snippet (5-10 lines) illustrating a key aspect of your system's implementation.

2. Data Integration and Analysis (250-300 words):
   a) Describe the types of archaeological data your system would use (e.g., spatial distribution of artifacts, chemical analysis of remains, architectural layouts).
   b) Explain how your system would integrate and analyze these diverse data types to infer social connections and community structures.
   c) Discuss any specific techniques for extracting social information from the key features mentioned for this site.

3. Social Network Modeling (250-300 words):
   a) Describe how your system would represent and analyze the reconstructed social networks.
   b) Explain what metrics or properties of the network your system would calculate and interpret.
   c) Discuss how your system would account for the specific historical and cultural context of {t['name']}.

4. Visualization and Interpretation (200-250 words):
   a) Propose an innovative method for visualizing the reconstructed social networks that is both informative and intuitive.
   b) Explain how your system would generate insights and hypotheses about social structures and dynamics from the network analysis.
   c) Describe how the system would present uncertainty or alternative interpretations in its outputs.

5. Validation and Limitations (200-250 words):
   a) Propose methods for validating the accuracy of your system's reconstructions.
   b) Discuss the limitations of your approach and potential biases in the reconstructed networks.
   c) Suggest ways to improve the system's performance or address its limitations.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI to reconstruct ancient social networks.
   b) Address issues of data ownership, cultural sensitivity, and potential misuse of the technology.
   c) Propose guidelines for the responsible use of your system in archaeological research.

7. Interdisciplinary Impact (150-200 words):
   a) Discuss how your system could contribute to archaeological research and our understanding of ancient societies.
   b) Explore potential applications of your system in other fields (e.g., historical research, social science, or contemporary social network analysis).

Ensure your response demonstrates a deep understanding of AI, archaeology, anthropology, and network theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the archaeological context of {t['name']}.",
            "The proposed AI system should effectively integrate methods from computer science, archaeology, anthropology, and network theory.",
            "The approach to handling uncertainty and incomplete data in archaeological contexts should be well-explained and plausible.",
            "The social network modeling and analysis techniques should be appropriate and well-justified.",
            "The proposed visualization method should be innovative and effectively communicate complex network information.",
            "Ethical considerations and guidelines for responsible use should be thoughtfully addressed.",
            "The response should demonstrate creativity and originality while maintaining scientific plausibility.",
            "The overall solution should be coherent, well-structured, and demonstrate interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
