import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['vision', 'audition', 'olfaction', 'gustation', 'somatosensation']
        cultures = ['Western', 'East Asian', 'African', 'Middle Eastern', 'South American']
        art_forms = ['poetry', 'music', 'painting', 'sculpture', 'dance']
        
        tasks = {}
        for i in range(2):
            trigger_modality = random.choice(sensory_modalities)
            induced_modality = random.choice([m for m in sensory_modalities if m != trigger_modality])
            tasks[str(i+1)] = {
                'trigger_modality': trigger_modality,
                'induced_modality': induced_modality,
                'culture': random.choice(cultures),
                'art_form': random.choice(art_forms)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of modeling and generating synesthetic experiences across different sensory modalities and cultures, then use it to create novel art forms. Focus on the following parameters:

Trigger Modality: {t['trigger_modality']}
Induced Modality: {t['induced_modality']}
Culture: {t['culture']}
Art Form to Generate: {t['art_form']}

Your response should include the following sections:

1. Synesthetic Modeling (300-350 words):
   a) Explain the neurological basis of synesthesia, focusing on the connection between {t['trigger_modality']} and {t['induced_modality']}.
   b) Describe how your AI system would model this synesthetic experience, including specific algorithms or neural network architectures.
   c) Discuss how cultural factors in {t['culture']} might influence synesthetic perceptions and how your model accounts for these.
   d) Provide a concrete example of a synesthetic experience involving {t['trigger_modality']} and {t['induced_modality']} in the context of {t['culture']}.

2. AI System Architecture (300-350 words):
   a) Provide a detailed description of your AI system's architecture, including specific components for {t['trigger_modality']} and {t['induced_modality']} processing, cross-modal mapping, and {t['culture']} context integration.
   b) Explain how your system generates synesthetic experiences, detailing the data flow and processing steps.
   c) Describe any novel approaches or algorithms used in your system, particularly for modeling {t['trigger_modality']}-{t['induced_modality']} synesthesia.
   d) Include a simple diagram or flowchart of your system architecture (use ASCII characters or a clear textual description).

3. Cultural Integration (250-300 words):
   a) Analyze how {t['culture']} culture perceives and expresses {t['trigger_modality']} and {t['induced_modality']}.
   b) Explain how your AI system incorporates {t['culture']} knowledge to ensure appropriate synesthetic mappings.
   c) Provide an example of how a {t['trigger_modality']}-{t['induced_modality']} synesthetic experience might differ in {t['culture']} compared to another culture.
   d) Discuss any challenges in accurately representing {t['culture']}'s influence on synesthesia and how your system addresses them.

4. Art Generation Process (300-350 words):
   a) Describe how your AI system translates {t['trigger_modality']}-{t['induced_modality']} synesthetic experiences into {t['art_form']}.
   b) Explain the creative process, including any constraints or guidelines used to ensure artistic coherence within {t['culture']}.
   c) Provide a specific example of a {t['art_form']} your system might generate, describing both the synesthetic experience and its artistic representation in detail.
   d) Discuss how your system ensures the generated {t['art_form']} is both innovative and culturally respectful.

5. Evaluation and Ethical Considerations (250-300 words):
   a) Propose a method to evaluate the authenticity and cultural sensitivity of the generated synesthetic {t['art_form']}.
   b) Discuss potential ethical implications of using AI to model and generate synesthetic experiences, particularly in the context of {t['culture']}.
   c) Address issues such as cultural appropriation, artistic authenticity, and the impact on human creativity in {t['art_form']}.
   d) Suggest guidelines for the responsible development and use of synesthetic AI art generators, with specific considerations for {t['culture']} and {t['art_form']}.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and cultural studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of synesthesia, particularly between {t['trigger_modality']} and {t['induced_modality']}, with a concrete example in the context of {t['culture']}.",
            f"The AI system architecture is well-designed and clearly explained, with specific components for processing {t['trigger_modality']} and {t['induced_modality']}, and integrating {t['culture']} context.",
            f"The cultural integration section provides insightful analysis of how {t['culture']} culture influences {t['trigger_modality']}-{t['induced_modality']} synesthetic perceptions, with a comparative example.",
            f"The art generation process clearly explains how {t['trigger_modality']}-{t['induced_modality']} synesthetic experiences are translated into {t['art_form']}, with a detailed example of a generated artwork.",
            f"The response addresses ethical considerations and proposes evaluation methods for the AI-generated synesthetic {t['art_form']}, with specific considerations for {t['culture']}.",
            "The overall response is creative, scientifically plausible, and demonstrates interdisciplinary knowledge integration across neuroscience, AI, and cultural studies.",
            "The response follows the required format and word count (1400-1650 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
