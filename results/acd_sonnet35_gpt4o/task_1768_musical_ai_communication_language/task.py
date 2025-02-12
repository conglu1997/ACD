import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_element": "harmony",
                "communication_context": "emotional state transfer",
                "message_to_translate": "I am experiencing joy and excitement."
            },
            {
                "musical_element": "rhythm",
                "communication_context": "temporal data sequencing",
                "message_to_translate": "The event sequence is: start, pause, accelerate, peak, decelerate, stop."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a musical language for AI-to-AI communication focusing on the musical element of {t['musical_element']} and optimized for {t['communication_context']}. Your response should include:

1. Language Design (250-300 words):
   a) Explain how you use {t['musical_element']} as the primary carrier of meaning in your language.
   b) Describe the basic 'vocabulary' and 'grammar' of your musical language.
   c) Explain how your language is specifically optimized for {t['communication_context']}.
   d) Provide an example of a simple 'sentence' in your language and explain its meaning. Describe the musical elements textually, do not use musical notation or audio.

2. Information Transfer Analysis (200-250 words):
   a) Analyze the potential information transfer rate of your musical language.
   b) Compare its efficiency to traditional text-based communication between AIs.
   c) Discuss any unique advantages or limitations of your musical communication system.

3. AI Processing Model (200-250 words):
   a) Propose a model for how an AI system would generate and interpret messages in your musical language.
   b) Explain how this model differs from traditional natural language processing systems.
   c) Discuss any challenges in implementing this model and how they might be overcome.

4. Cognitive Implications (200-250 words):
   a) Speculate on how communication via this musical language might affect AI cognitive processes.
   b) Discuss potential implications for AI creativity, emotional simulation, or other cognitive domains.
   c) Propose an experiment to test one of your hypotheses about the cognitive effects of your language.

5. Practical Applications (150-200 words):
   a) Suggest three potential real-world applications for your musical AI communication language.
   b) Explain how each application leverages the unique features of your language.
   c) Discuss any ethical considerations related to these applications.

6. Translation Task (100-150 words):
   Translate the following message into your musical language: "{t['message_to_translate']}"
   Provide a detailed explanation of how your language represents this message, describing the musical elements textually.

Ensure your response demonstrates a deep understanding of music theory, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a creative and coherent design for a musical language based on the specified musical element.",
            f"The language design is clearly optimized for {t['communication_context']}.",
            "A concrete example of a 'sentence' in the musical language is provided and explained.",
            "The information transfer analysis provides a plausible comparison to text-based AI communication.",
            "The AI processing model demonstrates an understanding of both music processing and language processing in AI systems.",
            "The cognitive implications section provides thoughtful speculation grounded in current AI and cognitive science knowledge.",
            "The practical applications are innovative and leverage the unique aspects of the musical language.",
            "The translation task is completed with a detailed explanation of how the message is represented in the musical language.",
            "The response demonstrates a deep understanding of music theory, linguistics, and artificial intelligence throughout.",
            "All musical elements are described textually, without using musical notation or audio."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
