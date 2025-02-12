import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ecosystem": "Coral reefs",
                "linguistic_focus": "Metaphor analysis",
                "conservation_challenge": "Ocean acidification"
            },
            {
                "ecosystem": "Amazon rainforest",
                "linguistic_focus": "Framing effects",
                "conservation_challenge": "Deforestation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""
        Design an AI system that uses ecolinguistics and natural language processing to analyze environmental discourse and develop strategies for biodiversity conservation. Your system should focus on the {t['ecosystem']} ecosystem, with particular emphasis on the linguistic aspect of {t['linguistic_focus']} and addressing the conservation challenge of {t['conservation_challenge']}. Your response should include:

        1. System Architecture (250-300 words):
           a) Describe the key components of your AI system for ecolinguistic analysis and conservation strategy development.
           b) Explain how these components interact to process environmental discourse and generate conservation strategies.
           c) Detail how your system incorporates principles from ecolinguistics, NLP, and environmental science.

        2. Linguistic Analysis Mechanism (200-250 words):
           a) Explain the process of analyzing environmental discourse using your chosen linguistic focus.
           b) Describe how your system identifies and interprets relevant linguistic patterns and structures.
           c) Discuss any novel NLP techniques or algorithms required for this analysis.

        3. Conservation Strategy Generation (200-250 words):
           a) Outline how your system translates linguistic insights into actionable conservation strategies.
           b) Explain how it addresses the specific conservation challenge mentioned.
           c) Describe how your system ensures the generated strategies are ecologically sound and culturally sensitive.

        4. Machine Learning and Adaptation (150-200 words):
           a) Describe how your system learns and improves its analysis and strategy generation over time.
           b) Explain the role of feedback loops and adaptive algorithms in refining the system's performance.
           c) Discuss how your system could be applied to different ecosystems and conservation challenges.

        5. Ethical and Societal Implications (200-250 words):
           a) Analyze the ethical considerations of using AI for environmental discourse analysis and conservation planning.
           b) Discuss potential impacts on local communities and indigenous knowledge systems.
           c) Consider both positive and negative societal implications of this technology.

        6. Evaluation and Future Directions (100-150 words):
           a) Propose methods for evaluating the effectiveness of your system in real-world conservation efforts.
           b) Identify potential limitations or challenges in implementing your system.
           c) Suggest future research directions to enhance the integration of ecolinguistics and AI for conservation.

        Ensure your response demonstrates a deep understanding of linguistics, environmental science, artificial intelligence, and conservation biology. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the {t['ecosystem']} ecosystem, with emphasis on {t['linguistic_focus']} and the conservation challenge of {t['conservation_challenge']}.",
            "The system architecture and linguistic analysis mechanism are innovative yet scientifically plausible.",
            "The conservation strategy generation process demonstrates a deep understanding of both linguistic insights and ecological principles.",
            "The machine learning and adaptation approach is well-explained and considers real-world applications.",
            "The ethical and societal implications are thoroughly analyzed, considering multiple perspectives.",
            "The response shows a high level of interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
