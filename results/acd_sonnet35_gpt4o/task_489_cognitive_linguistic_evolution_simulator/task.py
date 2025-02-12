import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "initial_language": "Proto-Indo-European",
                "time_span": "5000 years",
                "cognitive_factor": "Working memory capacity",
                "cultural_factor": "Trade networks"
            },
            {
                "initial_language": "Proto-Sino-Tibetan",
                "time_span": "3000 years",
                "cognitive_factor": "Theory of mind development",
                "cultural_factor": "Writing system invention"
            },
            {
                "initial_language": "Proto-Austronesian",
                "time_span": "4000 years",
                "cognitive_factor": "Spatial reasoning ability",
                "cultural_factor": "Maritime exploration"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language over time, starting with {t['initial_language']} and spanning {t['time_span']}. Your system should incorporate both cognitive and cultural factors in its simulation, with a particular focus on {t['cognitive_factor']} as a cognitive factor and {t['cultural_factor']} as a cultural factor.

Your response should include the following sections:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system represents and processes linguistic features (e.g., phonology, morphology, syntax).
   c) Discuss how your architecture incorporates the specified cognitive and cultural factors.

2. Evolutionary Mechanisms (150-200 words):
   a) Explain the algorithms or processes your system uses to simulate language change over time.
   b) Describe how your system models the interplay between cognitive constraints and cultural influences.
   c) Discuss how your system handles the emergence and extinction of linguistic features.

3. Data and Training (100-150 words):
   a) Describe the type and sources of data your system would require for training and simulation.
   b) Explain how your system would be initialized with the characteristics of the initial language.
   c) Discuss any challenges in data acquisition or representation for this task.

4. Simulation Output (150-200 words):
   a) Describe the format and content of your system's output (e.g., evolved language samples, statistical summaries).
   b) Explain how your system would demonstrate the impact of the specified cognitive and cultural factors on language evolution.
   c) Provide a brief example of how a specific linguistic feature might change over the given time span in your simulation.

5. Validation and Analysis (100-150 words):
   a) Propose methods for validating the accuracy and plausibility of your system's simulations.
   b) Discuss how your system's output could be used to generate and test hypotheses about historical language change.
   c) Explain how your system might provide insights into the relationship between cognition, culture, and language evolution.

6. Ethical Considerations and Limitations (100-150 words):
   a) Discuss potential ethical implications or misuses of such a language evolution simulation system.
   b) Address limitations of your approach and areas where human expertise would still be necessary.
   c) Suggest future improvements or extensions to your system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Your solution will be evaluated based on the depth of interdisciplinary integration, the creativity and plausibility of your system design, and how well you address all aspects of the task.

Format your response using clear headings for each section. Your total response should be between 800-1100 words, not including the headings. Remember, the key to a successful response lies in the innovative integration of concepts from multiple disciplines while maintaining scientific rigor and addressing the specific requirements of the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content",
            "The system design demonstrates integration of linguistics, cognitive science, and AI concepts",
            f"The system incorporates {t['cognitive_factor']} as a cognitive factor and {t['cultural_factor']} as a cultural factor",
            f"The simulation spans {t['time_span']} starting from {t['initial_language']}",
            "The response is creative while maintaining scientific plausibility",
            "The ethical considerations and limitations are thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
