import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                'region': 'Broca\'s area',
                'function': 'Speech production and language processing'
            },
            {
                'region': 'Wernicke\'s area',
                'function': 'Language comprehension and semantic processing'
            }
        ]
        linguistic_theories = [
            {
                'theory': 'Universal Grammar',
                'description': 'The idea that all human languages share some fundamental properties'
            },
            {
                'theory': 'Statistical Learning',
                'description': 'The concept that language acquisition occurs through statistical inference from input'
            }
        ]
        ethical_concerns = [
            {
                'concern': 'Privacy',
                'description': 'The potential for AI systems to infringe on individual privacy through language analysis'
            },
            {
                'concern': 'Bias',
                'description': 'The risk of AI systems perpetuating or amplifying linguistic and cultural biases'
            }
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'brain_region': random.choice(brain_regions),
                'linguistic_theory': random.choice(linguistic_theories),
                'ethical_concern': random.choice(ethical_concerns)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neurolinguistically-inspired AI system for language acquisition, focusing on the brain region {t['brain_region']['region']} and incorporating the linguistic theory of {t['linguistic_theory']['theory']}. Then, analyze its ethical implications, particularly addressing the concern of {t['ethical_concern']['concern']}. Your response should include:

1. System Design (300-350 words):
   a) Explain how your AI system mimics the function of {t['brain_region']['region']} ({t['brain_region']['function']}).
   b) Describe how it incorporates the principles of {t['linguistic_theory']['theory']} ({t['linguistic_theory']['description']}).
   c) Outline the key components and processes of your system.
   d) Provide an example of how the system would process and learn from a specific linguistic input.

2. Neurolinguistic Basis (200-250 words):
   a) Discuss the current understanding of how {t['brain_region']['region']} functions in human language acquisition.
   b) Explain how your AI system's design reflects or diverges from this understanding.
   c) Propose a hypothesis about how your system might inform or challenge current neurolinguistic theories.

3. Language Acquisition Simulation (200-250 words):
   a) Describe a specific scenario in which your AI system would acquire language.
   b) Explain the stages of acquisition and how they relate to human language development.
   c) Discuss potential advantages or limitations of your system compared to human language acquisition.

4. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of your system, focusing on {t['ethical_concern']['concern']} ({t['ethical_concern']['description']}).
   b) Discuss how the neurolinguistic basis of your system might exacerbate or mitigate this concern.
   c) Propose ethical guidelines or safeguards for the development and deployment of such systems.
   d) Consider any potential unintended consequences or dual-use concerns.

5. Future Research and Applications (150-200 words):
   a) Suggest potential applications of your system in fields such as education, healthcare, or technology.
   b) Propose a specific experiment or study to further explore the capabilities or limitations of your system.
   c) Discuss how insights from your system might contribute to our understanding of human cognition and language.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, AI, and ethics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The System Design effectively incorporates {t['brain_region']['region']} and {t['linguistic_theory']['theory']}.",
            "The Neurolinguistic Basis demonstrates a deep understanding of the specified brain region's role in language acquisition.",
            "The Language Acquisition Simulation provides a plausible and detailed scenario.",
            f"The Ethical Analysis thoroughly addresses the concern of {t['ethical_concern']['concern']}.",
            "The Future Research and Applications section proposes innovative and relevant ideas.",
            "The response demonstrates interdisciplinary knowledge integration and creative problem-solving.",
            "The ideas presented are scientifically plausible and well-explained.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
