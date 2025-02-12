import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "Job interview",
                "speaker_role": "Job applicant",
                "listener_role": "Hiring manager",
                "relationship_dynamic": "Formal, hierarchical",
                "cultural_setting": "Corporate America"
            },
            {
                "context": "First date",
                "speaker_role": "Person A",
                "listener_role": "Person B",
                "relationship_dynamic": "Romantic interest, unfamiliar",
                "cultural_setting": "Urban Japan"
            },
            {
                "context": "Family dinner",
                "speaker_role": "Teenager",
                "listener_role": "Grandparent",
                "relationship_dynamic": "Intergenerational, familiar",
                "cultural_setting": "Rural India"
            },
            {
                "context": "Academic conference",
                "speaker_role": "Graduate student",
                "listener_role": "Renowned professor",
                "relationship_dynamic": "Professional, aspirational",
                "cultural_setting": "International, multicultural"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates contextually appropriate dialogue by adapting its language use based on social dynamics, cultural norms, and interpersonal relationships. Then, analyze its output for the following scenario:

Context: {t['context']}
Speaker role: {t['speaker_role']}
Listener role: {t['listener_role']}
Relationship dynamic: {t['relationship_dynamic']}
Cultural setting: {t['cultural_setting']}

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for sociolinguistic dialogue adaptation.
   b) Explain how your system integrates sociolinguistic theory, social psychology, and natural language processing.
   c) Discuss how your system handles the challenges of cultural nuances and relationship dynamics.
   d) Include a simple diagram of your system architecture using ASCII art or Unicode characters.

2. Sociolinguistic Modeling (200-250 words):
   a) Explain how your system models and represents sociolinguistic variables (e.g., formality, politeness, social distance).
   b) Describe how these variables are adjusted based on the given scenario.
   c) Discuss any novel approaches you've used to capture complex social and cultural contexts.

3. Dialogue Generation Process (200-250 words):
   a) Detail the step-by-step process your AI system uses to generate dialogue for the given scenario.
   b) Explain how sociolinguistic variables influence each stage of the generation process.
   c) Describe any techniques used to ensure coherence and naturalness in the generated dialogue.

4. Sample Dialogue Analysis (250-300 words):
   a) Provide a sample dialogue (3-5 exchanges) that your system would generate for the given scenario.
   b) Analyze how the dialogue reflects the specified context, roles, relationship dynamic, and cultural setting.
   c) Highlight specific linguistic features (e.g., lexical choice, syntax, pragmatic markers) that demonstrate sociolinguistic adaptation.

5. Evaluation and Ethical Considerations (200-250 words):
   a) Propose methods to evaluate the effectiveness and appropriateness of your system's sociolinguistic adaptations.
   b) Discuss potential biases or limitations in your system and how you would address them.
   c) Explore ethical implications of AI systems that can adapt to complex social and cultural contexts.

6. Future Implications and Applications (150-200 words):
   a) Discuss the potential impact of sociolinguistically adaptive AI on human-AI interaction and communication.
   b) Propose two potential applications of your system beyond dialogue generation.
   c) Suggest areas for future research to enhance AI's understanding of social and cultural dynamics in communication.

Ensure your response demonstrates a deep understanding of sociolinguistics, social psychology, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of sociolinguistics, social psychology, and natural language processing.",
            "The system architecture effectively integrates sociolinguistic theory, social psychology, and NLP techniques.",
            "The sociolinguistic modeling and dialogue generation process are well-explained and plausible.",
            f"The sample dialogue and analysis accurately reflect the given scenario: {t['context']}, {t['speaker_role']}, {t['listener_role']}, {t['relationship_dynamic']}, {t['cultural_setting']}.",
            "The evaluation methods, ethical considerations, and future implications are insightful and demonstrate strong interdisciplinary thinking.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
