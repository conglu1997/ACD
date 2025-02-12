class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "cognitive_bias": "Availability heuristic",
                "language_family": "Indo-European",
                "time_span": "100 years",
                "example_word": "technology",
                "current_usage": "refers to electronic devices and computer systems"
            },
            "2": {
                "cognitive_bias": "Confirmation bias",
                "language_family": "Sino-Tibetan",
                "time_span": "200 years",
                "example_word": "家 (jiā)",
                "current_usage": "means family or home"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates language evolution influenced by cognitive biases, then use it to analyze and predict linguistic changes in a given language family. Your task focuses on the {t['cognitive_bias']} in the {t['language_family']} language family over a {t['time_span']} period. Provide a comprehensive response covering the following aspects:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of the {t['cognitive_bias']} and its potential influence on language use and evolution.
   b) Describe how this bias might manifest in linguistic patterns within the {t['language_family']} family.
   c) Discuss current theories on language evolution and how they relate to cognitive biases.
   d) Provide a specific example of how the {t['cognitive_bias']} might affect the usage or meaning of the word "{t['example_word']}" (current usage: {t['current_usage']}) over time.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for modeling language evolution.
   b) Explain how your system incorporates the {t['cognitive_bias']} into its language evolution model.
   c) Describe the data structures and algorithms you would use to represent and process linguistic information.
   d) Discuss how your system accounts for socio-cultural factors in language change.
   e) Provide a simple, original pseudocode snippet (5-10 lines) demonstrating a core function of your system. Do not copy existing code.

3. Simulation Process (250-300 words):
   a) Provide a step-by-step explanation of how your AI system would simulate language evolution over the {t['time_span']} period.
   b) Explain how the {t['cognitive_bias']} is modeled and applied in each step of the simulation.
   c) Describe how your system handles the interaction between multiple languages or dialects within the {t['language_family']} family.
   d) Illustrate with a specific example how your system might simulate the evolution of "{t['example_word']}" over the given time span.

4. Predictive Analysis (200-250 words):
   a) Based on your simulation, predict three specific linguistic changes that might occur in the {t['language_family']} family over the {t['time_span']} period.
   b) Explain the reasoning behind each prediction, linking it to the {t['cognitive_bias']} and other relevant factors.
   c) Discuss the potential limitations or uncertainties in these predictions.
   d) Provide a hypothetical future usage scenario for "{t['example_word']}" based on your predictions.

5. Validation and Testing (200-250 words):
   a) Propose a method to validate the accuracy of your AI system's predictions.
   b) Describe an experiment to test the influence of the {t['cognitive_bias']} on language evolution in a controlled setting.
   c) Discuss the challenges in testing and validating models of language evolution.
   d) Suggest a metric for quantifying the impact of cognitive biases on language change.

6. Ethical and Societal Implications (150-200 words):
   a) Identify potential ethical concerns related to using AI to predict language evolution.
   b) Discuss the possible societal impacts of accurate language evolution predictions.
   c) Propose guidelines for the responsible use of such AI systems in linguistics and social planning.
   d) Consider how your system might be misused and suggest safeguards against such misuse.

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Discuss how your approach could contribute to our understanding of human cognition, language, and cultural evolution.
   c) Propose an interdisciplinary research project that could build upon your work.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Include concrete examples and case studies where appropriate. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response fully demonstrates a deep understanding of {t['cognitive_bias']} and its potential influence on language evolution, with specific, well-explained examples related to \"{t['example_word']}\".",
            f"The AI system design effectively incorporates principles of cognitive science, linguistics, and artificial intelligence to model language evolution in the {t['language_family']} family, including a relevant and original pseudocode snippet.",
            "The simulation process and predictive analysis are logically sound, well-explained, and include concrete, detailed examples and case studies.",
            "The response comprehensively addresses ethical implications and future directions, including potential misuse and specific safeguards.",
            "The overall response is creative, coherent, and demonstrates high-level interdisciplinary problem-solving skills while strictly adhering to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
