class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A person is experiencing conflicting emotions of excitement and anxiety before a major life event.",
                "emotional_context": "Career change"
            },
            "2": {
                "scenario": "An individual is dealing with complex feelings of grief, relief, and guilt after the passing of a terminally ill loved one.",
                "emotional_context": "Loss and bereavement"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of emotional reasoning and empathy, then apply it to analyze and respond to the following complex emotional scenario: {t['scenario']} The emotional context is: {t['emotional_context']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for emotional reasoning and empathy.
   b) Explain how your system integrates psychological theories, neuroscientific data, and machine learning techniques.
   c) Detail any novel approaches or algorithms used in your system, particularly for handling complex, conflicting emotions.
   d) Include a high-level diagram or flowchart of your system architecture (described textually).

2. Emotional Processing (200-250 words):
   a) Explain how your system would process and interpret emotional data.
   b) Describe the specific techniques used to identify and analyze complex, conflicting emotions.
   c) Discuss how your system accounts for individual and cultural variations in emotional expression and interpretation.

3. Empathy Generation (200-250 words):
   a) Detail the process of generating empathetic responses based on the analyzed emotions.
   b) Explain how your system ensures the generated responses are contextually appropriate and genuinely empathetic.
   c) Describe any mechanisms for maintaining emotional congruence and avoiding inappropriate responses.

4. Scenario Analysis (200-250 words):
   a) Apply your AI system to analyze the given emotional scenario.
   b) Provide a detailed breakdown of the emotions involved, their potential causes, and interactions.
   c) Generate an empathetic response to the scenario, explaining the reasoning behind each element of the response.

5. Ethical Implications (150-200 words):
   a) Discuss the ethical considerations of using AI for emotional reasoning and empathy.
   b) Analyze potential risks of AI-generated empathy and propose safeguards.
   c) Explore the philosophical implications of artificial emotional intelligence on human-AI relationships.

6. Evaluation and Validation (100-150 words):
   a) Propose a method to evaluate the accuracy and effectiveness of your system's emotional reasoning and empathetic responses.
   b) Describe potential experiments or studies to validate your system's performance.
   c) Discuss how you would ensure the system's effectiveness across different cultures and emotional contexts.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your system to enhance its capabilities.
   b) Discuss how your system could be applied in fields such as mental health, education, or human-computer interaction.
   c) Propose a research question that arises from your system design.

Ensure your response demonstrates a deep understanding of emotional intelligence, psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of emotional intelligence, psychology, and artificial intelligence, accurately explaining relevant concepts and their applications.",
            "The proposed AI system effectively incorporates psychological theories and neuroscientific data, providing a plausible framework for emotional reasoning and empathy.",
            "The scenario analysis and empathetic response generation show a nuanced understanding of complex emotions and appropriate contextual responses.",
            "The discussion of ethical implications is thoughtful and considers multiple perspectives on the use of AI for emotional reasoning.",
            "The response is creative and original while maintaining scientific plausibility and rigor.",
            "The writing is clear, well-organized, and adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
