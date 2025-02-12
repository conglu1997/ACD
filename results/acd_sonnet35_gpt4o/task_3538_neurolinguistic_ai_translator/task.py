import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin", "English"),
            ("Spanish", "Arabic"),
            ("Japanese", "French"),
            ("Russian", "Hindi"),
            ("German", "Swahili"),
            ("Korean", "Portuguese")
        ]
        cognitive_processes = [
            "semantic processing",
            "syntactic parsing",
            "phonological encoding",
            "lexical retrieval",
            "pragmatic interpretation",
            "morphological analysis"
        ]
        ai_techniques = [
            "neural machine translation",
            "transfer learning",
            "attention mechanisms",
            "reinforcement learning",
            "generative adversarial networks",
            "transformers"
        ]
        
        tasks = {}
        for i in range(1, 3):
            lang_pair = random.choice(language_pairs)
            process = random.choice(cognitive_processes)
            technique = random.choice(ai_techniques)
            tasks[str(i)] = {
                "language_pair": lang_pair,
                "cognitive_process": process,
                "ai_technique": technique
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the neurolinguistic processes of bilingual language acquisition and translation for the language pair {t['language_pair'][0]} and {t['language_pair'][1]}, with a focus on the cognitive process of {t['cognitive_process']}. Your system should incorporate the AI technique of {t['ai_technique']}. Your response should include:

1. Neurolinguistic Framework (250-300 words):
   a) Explain the key principles of neurolinguistics relevant to bilingual language processing.
   b) Describe how the brain handles {t['cognitive_process']} in bilingual individuals.
   c) Discuss any differences in {t['cognitive_process']} between {t['language_pair'][0]} and {t['language_pair'][1]}.
   d) Propose a specific neurolinguistic experiment that could validate your model's predictions about {t['cognitive_process']} in bilinguals.

2. AI System Architecture (300-350 words):
   a) Provide a high-level overview of your AI system for modeling bilingual language acquisition and translation.
   b) Explain how your system incorporates neurolinguistic principles, particularly for {t['cognitive_process']}.
   c) Describe how you integrate {t['ai_technique']} into your system's design.
   d) Discuss potential limitations or challenges of using {t['ai_technique']} in this context.
   e) Include a visual representation (ASCII diagram) of your system architecture. The diagram should clearly show the main components and their relationships.

3. Language Acquisition Modeling (200-250 words):
   a) Explain how your system models the acquisition of {t['language_pair'][0]} and {t['language_pair'][1]}.
   b) Describe how {t['cognitive_process']} is represented and developed in your model.
   c) Discuss any unique challenges in modeling acquisition for this language pair.
   d) Consider potential cross-linguistic influences between the two languages during acquisition.
   e) Explain how your system handles code-switching between {t['language_pair'][0]} and {t['language_pair'][1]}.
   f) Propose how your system could be adapted to model the acquisition of a third language, discussing the challenges of multilingualism.

4. Translation Process (200-250 words):
   a) Detail how your system performs translation between {t['language_pair'][0]} and {t['language_pair'][1]}.
   b) Explain the role of {t['cognitive_process']} in the translation process.
   c) Provide an example of how your system would handle a specific translation challenge.
   d) Discuss how your system maintains neurolinguistic plausibility during translation.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate your system's performance in modeling bilingual language acquisition and translation.
   b) Describe how you would validate the neurolinguistic accuracy of your model.
   c) Suggest an experiment to test your system's capabilities in {t['cognitive_process']}.
   d) Propose a novel metric or evaluation method specific to {t['cognitive_process']} for the {t['language_pair'][0]}-{t['language_pair'][1]} pair.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss potential ethical implications of using AI to model human language acquisition and processing.
   b) Address concerns related to privacy, bias, and the impact on language education.
   c) Propose guidelines for the responsible development and use of your system.
   d) Consider potential societal impacts of your system on bilingual communities.
   e) Discuss potential applications of your system beyond language acquisition and translation, such as in cognitive rehabilitation or language disorder diagnosis.

Ensure your response demonstrates a deep understanding of neurolinguistics, bilingual language processing, and AI techniques. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section and include the ASCII diagram in the AI System Architecture section. Your total response should be between 1250-1550 words, excluding the ASCII diagram. You may adjust the word count for individual sections as needed, as long as you stay within the total word limit."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neurolinguistics, bilingual language processing, and AI techniques, particularly {t['ai_technique']}, with a proposed neurolinguistic experiment to validate the model's predictions.",
            f"The AI system architecture effectively incorporates neurolinguistic principles and models {t['cognitive_process']} in bilingual individuals, with a clear discussion of limitations, challenges, and a comprehensive ASCII diagram.",
            f"The language acquisition and translation processes are well-explained, accounting for the specific challenges of the {t['language_pair'][0]}-{t['language_pair'][1]} pair, including code-switching and potential adaptation for a third language.",
            "The response includes innovative approaches, a novel evaluation metric, and considers applications beyond language acquisition and translation while maintaining scientific plausibility.",
            "The ethical considerations and proposed guidelines are thoughtful, comprehensive, and consider societal impacts on bilingual communities and potential applications in cognitive rehabilitation or language disorder diagnosis.",
            f"The response effectively addresses all required points, demonstrating a holistic understanding of the intersection between neurolinguistics, AI, and the specific challenges of the {t['language_pair'][0]}-{t['language_pair'][1]} pair, including multilingualism.",
            "The proposed experiments, evaluation methods, and applications show creativity and a deep understanding of the field's current challenges and future directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
