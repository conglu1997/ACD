import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "neural_pattern": "Default Mode Network activity",
                "musical_element": "Harmony",
                "cognitive_process": "Mind-wandering"
            },
            "2": {
                "neural_pattern": "Gamma wave oscillations",
                "musical_element": "Rhythm",
                "cognitive_process": "Attention and focus"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze music based on neural activity patterns, exploring the relationship between brain function and musical structure. Your system should focus on the following elements:

Neural Pattern: {t['neural_pattern']}
Musical Element: {t['musical_element']}
Cognitive Process: {t['cognitive_process']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for neural music synthesis and analysis.
   b) Explain how your system integrates neuroscientific data, music theory, and AI algorithms.
   c) Discuss any novel techniques or approaches used in your system design.
   d) Include a high-level diagram or flowchart of your AI system's architecture (describe it textually).

2. Neural-Musical Mapping (250-300 words):
   a) Explain how your system maps the given neural pattern to the specified musical element.
   b) Describe the key parameters and variables considered in this mapping process.
   c) Discuss how your system accounts for individual differences in brain activity and musical perception.

3. Music Generation Process (250-300 words):
   a) Detail how your AI system generates music based on the neural-musical mapping.
   b) Explain how it incorporates the specified cognitive process into the music generation.
   c) Provide an example of a musical phrase or structure that your system might generate, with a brief analysis.

4. Analysis Capabilities (200-250 words):
   a) Describe how your system analyzes existing music in relation to neural patterns and cognitive processes.
   b) Explain any machine learning or pattern recognition techniques used in the analysis.
   c) Discuss how your system could be used to gain insights into the relationship between music and brain function.

5. Potential Applications and Implications (200-250 words):
   a) Propose two potential applications of your neural music synthesis and analysis system.
   b) Discuss the implications of your system for our understanding of music cognition and creativity.
   c) Consider any ethical considerations or potential misuses of this technology.

6. Limitations and Future Directions (150-200 words):
   a) Identify the main limitations or challenges of your proposed system.
   b) Suggest approaches to address these limitations.
   c) Propose two directions for future research that could extend or improve your system.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts.",
            "The system design demonstrates a clear integration of neuroscience, AI, and music theory concepts.",
            "The neural-musical mapping and music generation process are logically explained and scientifically plausible.",
            "The analysis capabilities and potential applications are well-reasoned and innovative.",
            "The response addresses limitations and future directions thoughtfully.",
            "The overall submission shows a deep understanding of the interdisciplinary nature of the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
