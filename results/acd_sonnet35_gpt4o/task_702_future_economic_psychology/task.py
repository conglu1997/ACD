import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        technologies = [
            {
                "name": "Universal Basic AI",
                "description": "Every citizen is assigned a personal AI assistant that can perform cognitive tasks, make decisions, and learn on their behalf."
            },
            {
                "name": "Emotion Regulation Implants",
                "description": "Widely available brain implants that allow users to precisely control and modulate their emotional states at will."
            },
            {
                "name": "Quantum Consciousness Network",
                "description": "A global network that allows individuals to share thoughts, memories, and experiences directly through quantum entanglement of neural patterns."
            },
            {
                "name": "Biological Age Reversal",
                "description": "A treatment that can reset an individual's biological age to 25, effectively granting indefinite lifespans."
            }
        ]
        return {str(i+1): tech for i, tech in enumerate(random.sample(technologies, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the psychological and economic impacts of the following hypothetical future technology on society, and propose adaptive strategies:

Technology: {t['name']}
Description: {t['description']}

Your task is to:

1. Psychological Impact Analysis (200-250 words):
   a) Discuss how this technology might affect individual and collective psychology.
   b) Analyze potential changes in human behavior, cognitive processes, and social interactions.
   c) Identify possible psychological challenges or benefits that may arise.

2. Economic Consequences (200-250 words):
   a) Examine how this technology could transform economic systems and markets.
   b) Analyze potential changes in employment, productivity, and wealth distribution.
   c) Discuss how traditional economic models might need to adapt to this new reality.

3. Societal Adaptation Strategies (250-300 words):
   a) Propose three strategies for society to adapt to and benefit from this technology.
   b) For each strategy, explain its implementation and potential outcomes.
   c) Address how these strategies mitigate risks and capitalize on opportunities identified in your analysis.

4. Ethical Considerations (100-150 words):
   Discuss two major ethical dilemmas that might arise from the widespread adoption of this technology and suggest approaches to address them.

5. Interdisciplinary Connections (100-150 words):
   Explain how insights from at least two other scientific disciplines (e.g., neuroscience, anthropology, information theory) could contribute to understanding and managing the societal impact of this technology.

Ensure your response demonstrates a deep understanding of human psychology, economic principles, and complex societal systems. Be creative yet logical in your analysis and proposals, considering both short-term and long-term implications. Use clear, concise language and organize your answer using appropriate subheadings."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of potential psychological impacts, including individual and societal effects",
            "The economic analysis is thorough and considers multiple facets of how the technology could transform existing systems",
            "The proposed adaptation strategies are creative, well-reasoned, and address the identified challenges and opportunities",
            "Ethical considerations are thoughtfully explored with plausible approaches to address them",
            "The interdisciplinary connections are relevant and demonstrate an understanding of how different fields can contribute to the analysis",
            "The overall response shows strong interdisciplinary thinking, creativity, and analytical depth"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
