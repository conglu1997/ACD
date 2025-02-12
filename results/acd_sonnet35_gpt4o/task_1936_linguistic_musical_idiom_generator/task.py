import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'source_language': 'Mandarin Chinese',
                'target_language': 'Spanish',
                'musical_element': 'rhythm',
                'linguistic_feature': 'tonal patterns'
            },
            {
                'source_language': 'Arabic',
                'target_language': 'Japanese',
                'musical_element': 'melody',
                'linguistic_feature': 'stress patterns'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an original AI system that generates and analyzes cross-cultural musical idioms based on linguistic features, focusing on translating the {t['linguistic_feature']} of {t['source_language']} into the musical traditions of {t['target_language']}, with emphasis on {t['musical_element']}. Your response should be creative and demonstrate a deep understanding of the subject matter, not simply describe existing systems. Include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system analyzes {t['linguistic_feature']} of {t['source_language']}.
   c) Detail how these linguistic features are mapped to {t['musical_element']} in {t['target_language']}'s musical tradition.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Linguistic-Musical Mapping (250-300 words):
   a) Provide a detailed explanation of how {t['linguistic_feature']} of {t['source_language']} are translated into {t['musical_element']} in the style of {t['target_language']}.
   b) Describe how your system accounts for the musical traditions and cultural context of {t['target_language']}.
   c) Give a specific example of a {t['linguistic_feature']} in {t['source_language']} and how it would be represented musically in {t['target_language']}.

3. AI and Machine Learning Techniques (250-300 words):
   a) Describe the AI and machine learning techniques used in your system (e.g., neural networks, rule-based systems, generative models).
   b) Explain how your system learns and adapts to different linguistic and musical patterns.
   c) Discuss any novel algorithms or approaches in your design.
   d) Provide a brief pseudocode or mathematical representation of a key algorithm in your approach.

4. Data Requirements and Preprocessing (200-250 words):
   a) Specify the types and sources of linguistic and musical data your system would require.
   b) Describe any necessary data preprocessing or feature extraction steps.
   c) Discuss challenges in obtaining or creating appropriate training data for this task.
   d) Propose a method for generating synthetic training data to improve your system's performance.

5. Output Analysis and Evaluation (250-300 words):
   a) Propose a method for evaluating the musical output of your system.
   b) Describe how you would assess the cultural authenticity and aesthetic quality of the generated musical idioms.
   c) Discuss potential metrics for measuring the system's success in translating linguistic features to musical elements.
   d) Provide an example of how you would score a generated musical piece based on your evaluation criteria.

6. Potential Applications and Ethical Considerations (200-250 words):
   a) Suggest two potential applications of your system in music composition, language learning, or cultural exchange.
   b) Discuss ethical considerations in creating AI-generated music based on cultural and linguistic features.
   c) Propose guidelines for responsible use and development of such systems.
   d) Address potential biases in your system and how you would mitigate them.

Ensure your response demonstrates a deep understanding of linguistics, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1750 words.

Example: To illustrate the complexity of the task, consider how the tonal patterns in Mandarin Chinese (where pitch changes can alter word meaning) might be mapped to rhythmic patterns in Spanish flamenco music. Your system would need to account for the four tones in Mandarin and find creative ways to represent them using the complex rhythmic structures of flamenco, such as the 12-beat compás."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of an original AI system that generates and analyzes cross-cultural musical idioms based on {t['linguistic_feature']} of {t['source_language']} and {t['musical_element']} of {t['target_language']}.",
            "The system architecture is clearly described with key components and their interactions explained, including a high-level diagram or pseudocode.",
            f"The linguistic-musical mapping process is thoroughly explained with a specific example of how {t['linguistic_feature']} in {t['source_language']} would be represented musically in {t['target_language']}.",
            "AI and machine learning techniques are described in detail, including learning and adaptation mechanisms, with a brief pseudocode or mathematical representation of a key algorithm.",
            "Data requirements and preprocessing steps are specified, along with potential challenges and a method for generating synthetic training data.",
            "A comprehensive method for evaluating the musical output and assessing cultural authenticity is proposed, including specific evaluation criteria and an example of how a generated musical piece would be scored.",
            "Potential applications and ethical considerations are discussed with proposed guidelines for responsible use and strategies for mitigating biases.",
            "The response adheres to the specified word count limits for each section and the overall word count range of 1450-1750 words.",
            "The proposed system demonstrates creativity and originality, not simply describing existing approaches."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
