import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Mandarin', 'Hindi', 'Spanish', 'Arabic']
        climate_topics = ['Carbon pricing', 'Renewable energy transition', 'Deforestation', 'Ocean acidification', 'Climate migration']
        cultural_contexts = ['Western', 'Eastern', 'Global South', 'Indigenous', 'Industrial']
        tasks = {
            '1': {
                'languages': random.sample(languages, 3),
                'topic': random.choice(climate_topics),
                'cultural_context': random.choice(cultural_contexts)
            },
            '2': {
                'languages': random.sample(languages, 3),
                'topic': random.choice(climate_topics),
                'cultural_context': random.choice(cultural_contexts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and generates climate change discourse across multiple languages and cultures, then use it to propose solutions for improving global climate communication. Focus on the following languages: {', '.join(t['languages'])}, the climate topic: {t['topic']}, and the cultural context: {t['cultural_context']}.

Your response should include:

1. AI System Design (300-350 words):
   a) Outline the architecture of your AI system, including components for multi-language processing, sentiment analysis, and discourse generation.
   b) Explain how your system would handle cultural nuances and idiomatic expressions related to climate change.
   c) Describe the training data and process you would use to make your system culturally aware and scientifically accurate.
   d) Provide a simple pseudocode snippet or flowchart illustrating how your system would process input and generate output across different languages.

2. Cross-Cultural Analysis (250-300 words):
   a) Using your AI system, analyze how the given climate topic is discussed in each of the specified languages and cultures.
   b) Identify key differences in terminology, framing, and sentiment across these cultures.
   c) Discuss how these differences might impact global understanding and cooperation on the issue.
   d) Provide a specific example of how a climate-related term or concept might be interpreted differently in each language and cultural context.

3. Solution Generation (250-300 words):
   a) Based on your analysis, propose an AI-generated solution for improving global communication and cooperation on the given climate topic.
   b) Explain how your solution addresses the cultural and linguistic differences identified.
   c) Provide an example of how your AI system would generate climate change discourse in each of the specified languages to support this solution.
   d) Describe a hypothetical scenario where your AI system facilitates a breakthrough in cross-cultural climate communication.

4. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues in using AI to analyze and generate climate change discourse across cultures.
   b) Address limitations of your approach and potential unintended consequences.
   c) Propose guidelines for responsible development and use of such AI systems in the context of global climate communication.
   d) Consider potential biases in your AI system and how they might be mitigated.

5. Evaluation and Future Directions (150-200 words):
   a) Design a method to evaluate the effectiveness of your AI system and proposed solution.
   b) Suggest future research directions or potential applications of your system beyond climate change communication.
   c) Propose a timeline for development, testing, and deployment of your AI system.

Ensure your response demonstrates a deep understanding of natural language processing, climate science, and cross-cultural communication. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and subsection. Use numbered lists for each main section and lettered lists for subsections. Your total response should be between 1150-1400 words. Include a word count at the end of your submission.

Example: For a system analyzing 'Carbon pricing' in 'English, Mandarin, and Hindi' within a 'Western' cultural context, you might consider how terms like 'carbon tax' or 'emissions trading' are understood and discussed differently in these languages and cultures."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed AI system design that addresses multi-language processing for {', '.join(t['languages'])}.",
            f"The cross-cultural analysis specifically discusses how {t['topic']} is addressed in the given languages and {t['cultural_context']} cultural context.",
            "The proposed solution clearly leverages AI to improve global climate communication and provides concrete examples in each specified language.",
            "The response thoroughly addresses ethical considerations, limitations, and potential biases of the AI system.",
            "The evaluation method and future directions are clearly articulated and relevant to the proposed system.",
            "The overall response demonstrates interdisciplinary knowledge integration and creative problem-solving.",
            "The response follows the specified format with clear headings and numbering.",
            "The response is within the specified word count range of 1150-1400 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
