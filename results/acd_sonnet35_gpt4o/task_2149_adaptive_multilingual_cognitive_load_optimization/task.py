import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Arabic', 'Spanish', 'Russian', 'French', 'German', 'Japanese']
        cognitive_load_factors = ['working memory capacity', 'attention span', 'processing speed', 'prior knowledge', 'emotional state']
        text_types = ['academic paper', 'news article', 'technical manual', 'literary work', 'legal document']
        target_audiences = ['high school students', 'university professors', 'elderly individuals', 'second language learners', 'industry professionals']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'source_language': random.choice(languages),
                'target_language': random.choice([lang for lang in languages if lang != tasks.get(str(i-1), {}).get('source_language')]),
                'cognitive_load_factor': random.choice(cognitive_load_factors),
                'text_type': random.choice(text_types),
                'target_audience': random.choice(target_audiences)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that dynamically adjusts the complexity of multilingual text based on real-time cognitive load assessment. Then, apply your system to the following scenario:

Background: Cognitive Load Theory posits that learning is impaired when working memory is overwhelmed. It distinguishes between intrinsic load (inherent to the task), extraneous load (unnecessary cognitive effort), and germane load (effort that contributes to learning).

Scenario: Real-time translation and summarization of a {t['text_type']} from {t['source_language']} to {t['target_language']} for an audience of {t['target_audience']}, with a focus on optimizing for {t['cognitive_load_factor']}. Assume native-level proficiency in both source and target languages.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cognitive load assessment and text adaptation.
   b) Explain how your system integrates multilingual NLP capabilities with cognitive load theory.
   c) Detail the mechanisms for real-time text complexity adjustment.
   d) Discuss how your system accounts for the specified cognitive load factor.

2. Cognitive Load Assessment (200-250 words):
   a) Explain your approach to real-time assessment of cognitive load.
   b) Describe the metrics and indicators used to gauge cognitive load.
   c) Discuss how your system adapts to individual differences in cognitive processing.

3. Multilingual Text Adaptation (250-300 words):
   a) Describe your strategy for adjusting text complexity across languages.
   b) Explain how your system maintains semantic equivalence while modifying complexity.
   c) Discuss any language-specific challenges and how your system addresses them.

4. Scenario Application (250-300 words):
   a) Apply your system to the given scenario, describing the step-by-step process.
   b) Provide a short example (2-3 sentences) of original text in the source language and its adapted translation in the target language.
   c) Explain how your system optimizes for the specified cognitive load factor and target audience.

5. Evaluation and Metrics (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system.
   b) Describe quantitative and qualitative metrics for assessing performance.
   c) Discuss how you would measure improvements in comprehension and cognitive load reduction.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues related to cognitive load manipulation and information presentation.
   b) Address concerns about privacy and data collection for cognitive load assessment.
   c) Propose guidelines for responsible use of such AI systems in educational or professional settings.

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Propose a research question that could further the development of cognitive load-adaptive AI in multilingual contexts.

Ensure your response demonstrates a deep understanding of cognitive load theory, multilingual NLP, and AI system design. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively integrates cognitive load theory with multilingual NLP, focusing on {t['cognitive_load_factor']}.",
            f"The response addresses the specific scenario of translating a {t['text_type']} from {t['source_language']} to {t['target_language']} for {t['target_audience']}.",
            "The system architecture and cognitive load assessment methods are clearly explained and scientifically plausible.",
            "The multilingual text adaptation strategy is well-described and accounts for language-specific challenges.",
            "The scenario application includes a concrete example of adapted text in both the source and target languages.",
            "Evaluation methods and metrics are proposed to assess the system's effectiveness.",
            "Ethical considerations are thoroughly discussed with proposed guidelines for responsible use.",
            "Future directions and a relevant research question are proposed to advance the field.",
            "The response demonstrates deep understanding of cognitive science, linguistics, and AI, using appropriate terminology.",
            "The response includes multilingual content as requested in the scenario application section.",
            "The overall response is creative, well-structured, and adheres to the specified format and word count (1400-1750 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
