import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture': 'Mayan',
                'time_period': '2000 BCE to 1500 CE',
                'linguistic_focus': 'lexical evolution',
                'cultural_events': ['rise of city-states', 'Spanish conquest', 'collapse of Classic Maya civilization'],
                'linguistic_phenomena': ['language contact', 'semantic shift', 'phonological changes']
            },
            {
                'culture': 'Japanese',
                'time_period': '500 CE to present',
                'linguistic_focus': 'honorific system',
                'cultural_events': ['feudal era', 'Meiji Restoration', 'post-WWII westernization', 'economic boom of the 1980s'],
                'linguistic_phenomena': ['grammaticalization', 'language standardization', 'loanword adaptation']
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language within the {t['culture']} cultural context from {t['time_period']}, focusing on the aspect of {t['linguistic_focus']}. Your system should consider the impact of major cultural events such as {', '.join(t['cultural_events'])}, and account for linguistic phenomena including {', '.join(t['linguistic_phenomena'])}.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating linguistic evolution.
   b) Explain how your system integrates cultural and historical data with linguistic models.
   c) Discuss any novel approaches or algorithms used in your design.
   d) Include a high-level diagram or flowchart of your system architecture (use ASCII art or a clear textual description).

2. Data Sources and Processing (200-250 words):
   a) Specify the types of data your system would require for accurate simulation.
   b) Describe how you would obtain or generate this data, considering the historical context.
   c) Explain how your system would process and integrate diverse data sources.
   d) Discuss any techniques used for handling incomplete or uncertain historical data.

3. Linguistic Evolution Modeling (250-300 words):
   a) Detail how your system models the specified aspect of linguistic evolution.
   b) Explain how the system accounts for the influence of cultural events on language.
   c) Describe how your model handles the specified linguistic phenomena.
   d) Provide an example of how your system would model a specific linguistic change over time.

4. Simulation Output and Analysis (200-250 words):
   a) Describe the format and content of your system's output. Include a sample output snippet.
   b) Explain how you would validate the simulation results against historical linguistic data.
   c) Discuss how your system could be used to generate hypotheses about language change.
   d) Propose a specific experiment using your system to investigate a linguistic phenomenon.

5. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or biases in your approach.
   b) Discuss ethical implications of simulating cultural and linguistic evolution.
   c) Propose guidelines for responsible use of such simulations in research.
   d) Address potential misuse or misinterpretation of simulation results.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cultural anthropology, and AI system design.",
            "The proposed system effectively integrates cultural and historical data with linguistic models.",
            f"The system adequately addresses the specified linguistic focus of {t['linguistic_focus']}.",
            f"The response considers the impact of all major cultural events mentioned: {', '.join(t['cultural_events'])}.",
            f"The system accounts for all specified linguistic phenomena: {', '.join(t['linguistic_phenomena'])}.",
            "The response includes a clear system architecture diagram or description.",
            "The simulation output section includes a sample output snippet.",
            "The response proposes a specific experiment using the system.",
            "The response addresses ethical implications and proposes guidelines for responsible use.",
            "The response is creative and speculative while maintaining scientific plausibility.",
            "The response follows the specified format with clear headings and appropriate use of bullet points or numbered lists."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
