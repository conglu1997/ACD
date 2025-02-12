class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "alien_environment": "High-gravity gas giant with floating colonies",
                "sensory_capabilities": "Echolocation and electromagnetic field sensing",
                "time_span": "10,000 years"
            },
            "2": {
                "alien_environment": "Low-gravity moon with underground habitats",
                "sensory_capabilities": "Infrared vision and vibration sensing",
                "time_span": "50,000 years"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to simulate the co-evolution of language and cognition in a hypothetical alien species living in a {t['alien_environment']}, with {t['sensory_capabilities']} as their primary sensory capabilities. Your simulation should cover a time span of {t['time_span']}. Your response should include:

1. Simulation Framework (300-350 words):
   a) Describe the architecture of your AI system for simulating language and cognitive evolution.
   b) Explain how your system incorporates the given alien environment and sensory capabilities.
   c) Detail the key parameters and variables your simulation will track over time.
   d) Discuss how your system models the interaction between language development and cognitive evolution.

2. Initial Conditions and Evolutionary Pressures (250-300 words):
   a) Describe the initial cognitive and communicative capabilities of your alien species.
   b) Identify at least three major evolutionary pressures in the given environment that would drive language and cognitive development.
   c) Explain how these pressures are represented in your simulation.

3. Language and Cognition Co-evolution (300-350 words):
   a) Outline the major stages of language evolution in your simulation over the given time span.
   b) Describe how cognitive capabilities develop alongside language, highlighting key milestones.
   c) Provide examples of how the alien species' unique sensory capabilities influence their language and thought processes.
   d) Explain any feedback loops between language and cognition in your model.

4. Comparative Analysis (200-250 words):
   a) Compare the evolved alien language and cognition to human language and cognition.
   b) Discuss similarities and differences in the evolutionary trajectories.
   c) Analyze how the results support or challenge theories of universal grammar and cognitive development.

5. Implications and Predictions (200-250 words):
   a) Discuss the implications of your simulation for our understanding of the relationship between language, cognition, and environment.
   b) Make three specific, testable predictions about alien languages or cognitive capabilities based on your simulation.
   c) Propose how these predictions could be tested if we were to encounter an alien civilization.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues in simulating and predicting alien cognitive evolution.
   b) Address limitations of your approach and potential biases in the simulation.
   c) Suggest guidelines for the responsible use of such simulations in xenolinguistics and astrobiology.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary biology. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Use appropriate subheadings (a, b, c, d) within each section. Your total response should be between 1400-1700 words. Use scientific terminology accurately and provide brief explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and evolutionary biology.",
            "The AI system design is innovative, plausible, and effectively incorporates the given alien environment and sensory capabilities.",
            "The simulation framework and evolutionary stages are well-explained and logically consistent.",
            "The comparative analysis and implications are insightful and well-reasoned.",
            "The response addresses ethical considerations and limitations thoughtfully.",
            "The overall response is creative, coherent, and adheres to the specified word count and formatting guidelines.",
            "Scientific terminology is used accurately and complex concepts are briefly explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
