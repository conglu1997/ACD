class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "cognitive_state": "Sleep deprivation",
                "perception_domain": "Time perception",
                "target_concept": "Productivity"
            },
            "2": {
                "cognitive_state": "Synesthesia",
                "perception_domain": "Color-sound association",
                "target_concept": "Music composition"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets metaphors based on the cognitive state of {t['cognitive_state']}, focusing on {t['perception_domain']}, and applying it to the concept of {t['target_concept']}. Your response should include:

1. Cognitive State Simulation (200-250 words):
   a) Describe how your AI system models the given cognitive state.
   b) Explain how it simulates the altered perception in the specified domain.
   c) Discuss any challenges in accurately representing this cognitive state computationally.

2. Metaphor Generation Mechanism (250-300 words):
   a) Explain the process by which your AI generates metaphors based on the simulated cognitive state.
   b) Describe how it incorporates the altered perception into the metaphor creation.
   c) Provide an example of a generated metaphor for the target concept, explaining its connection to the cognitive state.

3. Linguistic Analysis (200-250 words):
   a) Analyze the linguistic properties of the generated metaphor.
   b) Compare its structure and characteristics to metaphors typically produced in normal cognitive states.
   c) Discuss how the altered cognitive state influences the linguistic features of the metaphor.

4. Cognitive Interpretation (200-250 words):
   a) Interpret the generated metaphor from a cognitive science perspective.
   b) Explain how the metaphor reflects the simulated cognitive state and altered perception.
   c) Discuss potential insights this metaphor generation process might offer into human cognition and creativity.

5. AI System Evaluation (150-200 words):
   a) Propose methods to evaluate the accuracy and creativity of your AI's metaphor generation.
   b) Discuss potential applications of this system in cognitive science or linguistics research.
   c) Identify limitations of your approach and suggest future improvements.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['cognitive_state']} and its effects on {t['perception_domain']}.",
            "The AI system's metaphor generation process is well-explained and plausible.",
            f"The generated metaphor for {t['target_concept']} is creative and clearly linked to the given cognitive state.",
            "The linguistic and cognitive analyses of the metaphor are insightful and well-reasoned.",
            "The proposed evaluation methods and future improvements are appropriate and thoughtful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
