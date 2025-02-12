import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'linguistic_feature': 'Syntax',
                'meme_type': 'Internet memes',
                'time_scale': '50 years'
            },
            {
                'linguistic_feature': 'Lexicon',
                'meme_type': 'Cultural idioms',
                'time_scale': '100 years'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language through memes, focusing on the linguistic feature of {t['linguistic_feature']} and the meme type of {t['meme_type']}. Your system should project language changes over a {t['time_scale']} period. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of memetics and how they apply to language evolution.
   b) Describe how {t['linguistic_feature']} is influenced by {t['meme_type']}.
   c) Discuss relevant linguistic theories that inform your model of language change.

2. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system models the spread and evolution of linguistic memes.
   c) Detail how you incorporate machine learning techniques to simulate language change.
   d) Provide a visual representation of your architecture (use ASCII art or describe in words).

3. Data and Training (200-250 words):
   a) Describe the types of data your system would use for training and simulation.
   b) Explain how you would collect or generate this data.
   c) Discuss any challenges in data collection or synthesis and how you'd address them.

4. Simulation Process (250-300 words):
   a) Outline the step-by-step process of how your system simulates language evolution.
   b) Explain how your system accounts for factors like population dynamics and social networks.
   c) Describe how you would validate the accuracy of your simulations.

5. Case Study (200-250 words):
   Provide a specific example of how your system might simulate the evolution of a linguistic feature over the specified time period. Include:
   a) An initial linguistic state
   b) Key memes that influence the evolution
   c) The projected linguistic change after the specified time period

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of simulating and potentially influencing language evolution.
   b) Address any limitations of your approach and how they might be mitigated.

7. Future Applications (150-200 words):
   a) Propose two potential applications of your system beyond theoretical linguistics.
   b) Discuss how this technology might impact fields like natural language processing or social sciences.

Ensure your response demonstrates a deep understanding of linguistics, memetics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistics, memetics, and artificial intelligence, particularly in relation to {t['linguistic_feature']} and {t['meme_type']}.",
            "The AI system architecture is innovative, well-explained, and scientifically plausible.",
            f"The simulation process and case study effectively demonstrate language evolution over a {t['time_scale']} period.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The proposed future applications are creative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
