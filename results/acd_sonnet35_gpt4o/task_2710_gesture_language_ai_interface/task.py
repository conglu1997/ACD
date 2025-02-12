import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Arabic', 'Swahili', 'Russian']
        cognitive_factors = ['spatial cognition', 'embodied cognition', 'mental imagery', 'working memory']
        cultural_contexts = ['urban environment', 'traditional rural setting', 'multicultural metropolis', 'isolated island community']
        sample_sentences = [
            "The red bird flew over the tall mountain.",
            "In the market, people haggle over fresh fruits and vegetables.",
            "The ancient ritual begins at sunset on the longest day of the year.",
            "Scientists discovered a new species of deep-sea creature."
        ]
        
        tasks = {
            "1": {
                "language": random.choice(languages),
                "cognitive_factor": random.choice(cognitive_factors),
                "cultural_context": random.choice(cultural_contexts),
                "sample_sentence": random.choice(sample_sentences)
            },
            "2": {
                "language": random.choice(languages),
                "cognitive_factor": random.choice(cognitive_factors),
                "cultural_context": random.choice(cultural_contexts),
                "sample_sentence": random.choice(sample_sentences)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates between {t['language']} and a novel gesture-based language, with a focus on {t['cognitive_factor']} in the context of a {t['cultural_context']}. Your response should include:

1. Gesture Language Design (250-300 words):
   a) Describe the key features and structure of your novel gesture-based language.
   b) Explain how it incorporates {t['cognitive_factor']}.
   c) Discuss how the {t['cultural_context']} influences the language design.
   d) Provide examples of at least 5 basic gestures and their meanings.

2. AI System Architecture (300-350 words):
   a) Describe the overall structure of your AI translation system.
   b) Explain how it processes and translates between {t['language']} and the gesture language.
   c) Detail how the system accounts for {t['cognitive_factor']} in its translation process.
   d) Discuss any novel AI techniques or algorithms used in your system.
   e) Include a high-level diagram or pseudocode to illustrate your system's architecture.

3. Translation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system would translate the following sentence from {t['language']} to the gesture language: "{t['sample_sentence']}"
   b) Explain how the system handles ambiguity and context in translation.
   c) Discuss how {t['cognitive_factor']} influences the translation process.

4. Cultural and Cognitive Considerations (200-250 words):
   a) Analyze how your system addresses cultural nuances in the {t['cultural_context']}.
   b) Discuss potential cognitive benefits or challenges of using a gesture-based language.
   c) Explain how your system could adapt to different cultural contexts or cognitive factors.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss the potential impact of your system on communication in the {t['cultural_context']}.
   b) Address ethical considerations in developing and implementing such a system.
   c) Propose guidelines for responsible use and development.

6. Evaluation and Future Directions (150-200 words):
   a) Suggest methods to evaluate the effectiveness and accuracy of your translation system.
   b) Propose potential applications beyond language translation.
   c) Discuss how your system could be extended or improved in future iterations.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (e.g., '1. Gesture Language Design', '2. AI System Architecture', etc.). Your total response should be between 1250-1550 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed and plausible design for a novel gesture-based language with at least 5 example gestures.",
            f"The AI system architecture effectively incorporates {t['cognitive_factor']} and considers the {t['cultural_context']}.",
            f"The translation process for the sample sentence '{t['sample_sentence']}' is clearly explained and plausible.",
            "Cultural and cognitive considerations specific to the given context are thoroughly addressed.",
            "Ethical implications and practical applications are thoughtfully discussed with concrete examples.",
            "The response demonstrates creativity and interdisciplinary knowledge integration throughout all sections.",
            "The response follows the required format with clear headings and is within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
