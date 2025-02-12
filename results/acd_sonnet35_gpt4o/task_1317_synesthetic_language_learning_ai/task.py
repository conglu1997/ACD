import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ["Mandarin", "Arabic", "Russian", "Swahili", "Hindi"]
        sensory_modalities = ["color", "taste", "sound", "texture", "smell"]
        linguistic_aspects = ["phonemes", "tones", "grammar rules", "vocabulary", "idioms"]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "target_language": random.choice(languages),
                "primary_sensory_modality": random.choice(sensory_modalities),
                "secondary_sensory_modality": random.choice(sensory_modalities),
                "linguistic_aspect": random.choice(linguistic_aspects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses principles of synesthesia to enhance language learning for {t['target_language']}, focusing on the linguistic aspect of {t['linguistic_aspect']}. Your system should primarily use the sensory modality of {t['primary_sensory_modality']}, with {t['secondary_sensory_modality']} as a secondary modality. Then, analyze its potential effects on cognitive processes and language acquisition. Your response should include:

1. System Design (300-350 words):
   a) Describe the core components and architecture of your AI system.
   b) Explain how your system incorporates synesthetic principles to map {t['linguistic_aspect']} to {t['primary_sensory_modality']} and {t['secondary_sensory_modality']}.
   c) Provide specific examples of how your system would represent at least three different {t['linguistic_aspect']} in {t['target_language']}.
   d) Discuss how your system adapts to individual differences in sensory perception and learning styles.

2. Learning Process Analysis (250-300 words):
   a) Describe the step-by-step process of how a learner would interact with your system to acquire new {t['linguistic_aspect']} in {t['target_language']}.
   b) Analyze how this synesthetic approach might enhance memory formation and recall of {t['linguistic_aspect']}.
   c) Discuss potential cognitive load implications and how your system manages them.

3. Comparative Advantage (200-250 words):
   a) Compare your synesthetic language learning approach to traditional methods for teaching {t['linguistic_aspect']} in {t['target_language']}.
   b) Identify specific advantages and potential drawbacks of your system.
   c) Propose how your system could complement existing language learning methodologies.

4. Cognitive Impact Evaluation (200-250 words):
   a) Design an experiment to measure the cognitive effects of using your system for language learning.
   b) Specify key metrics and hypotheses for your experiment.
   c) Discuss potential long-term impacts on brain plasticity and cognitive processing.

5. Ethical Considerations and Limitations (150-200 words):
   a) Address potential ethical concerns related to altering sensory-linguistic associations.
   b) Discuss any limitations or contraindications for using your system.
   c) Propose guidelines for responsible implementation and use of synesthetic language learning AI.

6. Future Developments (150-200 words):
   a) Suggest potential expansions or modifications to your system for other languages or linguistic aspects.
   b) Discuss how this technology might evolve in the next decade.
   c) Speculate on potential applications beyond language learning.

Ensure your response demonstrates a deep understanding of synesthesia, language acquisition processes, and AI technologies. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from cognitive science, linguistics, and AI throughout your response.

Format your answer with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of synesthesia and its potential applications in language learning, specifically for {t['target_language']} and {t['linguistic_aspect']}.",
            f"The system design creatively and coherently incorporates {t['primary_sensory_modality']} and {t['secondary_sensory_modality']} into the language learning process.",
            "The learning process analysis and comparative advantage sections show a strong grasp of cognitive science and language acquisition principles.",
            "The proposed experiment for cognitive impact evaluation is well-designed and scientifically sound.",
            "The discussion of ethical considerations and future developments is insightful and comprehensive.",
            "The response demonstrates exceptional interdisciplinary reasoning and creativity in addressing the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
