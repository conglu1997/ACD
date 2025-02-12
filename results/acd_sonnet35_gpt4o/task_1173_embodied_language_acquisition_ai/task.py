class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "environment": "urban",
                "target_language": "Mandarin Chinese",
                "focus_area": "spatial prepositions and motion verbs",
                "specific_challenge": "Learning the difference between 'shàng' (上, up/on) and 'xià' (下, down/under) in various contexts"
            },
            "2": {
                "environment": "natural",
                "target_language": "Inuktitut",
                "focus_area": "weather-related vocabulary and verb aspect",
                "specific_challenge": "Acquiring the multiple words for 'snow' and their aspectual variations"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that learns language through simulated physical interactions with its environment, based on theories of embodied cognition in human language acquisition. Your system should focus on learning {t['target_language']} in a simulated {t['environment']} environment, with particular emphasis on acquiring {t['focus_area']}. Specifically, address the challenge of {t['specific_challenge']}.

Provide your response in the following format:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of embodied cognition relevant to language acquisition.
   b) Describe how these principles apply to the acquisition of {t['focus_area']} in {t['target_language']}.
   c) Discuss any unique challenges or opportunities presented by the {t['environment']} environment for language learning.
   d) Explain how your framework addresses {t['specific_challenge']}.

2. System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system simulates physical interactions in the {t['environment']} environment.
   c) Detail how your system processes and learns from these interactions to acquire language.
   d) Discuss how your architecture specifically addresses the acquisition of {t['focus_area']} and {t['specific_challenge']}.
   e) Provide a visual representation of your system architecture (describe it textually, using ASCII art if helpful).

3. Learning Process (250-300 words):
   a) Provide a step-by-step example of how your system would learn a specific {t['target_language']} word or phrase related to {t['specific_challenge']}.
   b) Explain how this process mirrors human embodied language acquisition.
   c) Describe how your system generalizes from individual experiences to broader linguistic concepts.
   d) Include a pseudocode snippet (5-10 lines) illustrating a key algorithm in your learning process.

4. Evaluation Methods (200-250 words):
   a) Propose quantitative and qualitative methods to evaluate your system's language acquisition progress.
   b) Describe how you would compare your system's performance to human language learners.
   c) Suggest a novel metric for measuring the 'embodiedness' of the acquired language knowledge.
   d) Propose an experiment to test your system's ability to handle {t['specific_challenge']}.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues related to simulating embodied experiences for AI language learning.
   b) Address any limitations of your approach, particularly in relation to aspects of language that may be difficult to learn through embodied experiences.
   c) Propose guidelines for the responsible development and use of embodied language acquisition AI systems.
   d) Discuss potential biases that might arise in your system and how you would mitigate them.

Ensure your response demonstrates a deep understanding of embodied cognition, language acquisition theories, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c, d, e as appropriate. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of embodied cognition and its application to language acquisition.",
            f"The system design effectively addresses the acquisition of {t['focus_area']} in {t['target_language']}, particularly {t['specific_challenge']}.",
            f"The proposed AI system adequately simulates physical interactions in a {t['environment']} environment.",
            "The learning process example clearly illustrates how the system acquires language through embodied experiences.",
            "The pseudocode snippet effectively illustrates a key algorithm in the learning process.",
            "The visual representation of the system architecture is clear and informative.",
            "The evaluation methods are comprehensive and include a specific experiment to test the system's ability to handle the given challenge.",
            "The ethical considerations are thoughtful and address potential biases in the system.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response adheres to the specified format and word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
