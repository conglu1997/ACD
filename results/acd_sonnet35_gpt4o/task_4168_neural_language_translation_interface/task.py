import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("English", "Mandarin"),
            ("Spanish", "Japanese"),
            ("French", "Arabic"),
            ("German", "Russian"),
            ("Hindi", "Swahili")
        ]
        neural_mechanisms = [
            "Semantic network activation",
            "Syntactic tree mapping",
            "Phonological pattern recognition",
            "Conceptual metaphor processing",
            "Pragmatic context integration"
        ]
        ai_techniques = [
            "Transformer-based language models",
            "Neuromorphic computing",
            "Quantum machine learning",
            "Neuro-symbolic AI",
            "Federated learning"
        ]
        return {
            "1": {
                "language_pair": random.choice(language_pairs),
                "neural_mechanism": random.choice(neural_mechanisms),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "language_pair": random.choice(language_pairs),
                "neural_mechanism": random.choice(neural_mechanisms),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface system that directly translates thoughts in {t['language_pair'][0]} to speech or text in {t['language_pair'][1]}, incorporating neurolinguistic principles and advanced AI techniques. Your system should focus on the neural mechanism of {t['neural_mechanism']} and utilize the AI technique of {t['ai_technique']}.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your brain-computer interface system.
   b) Explain how your system incorporates the specified neural mechanism.
   c) Detail how the AI technique is integrated into the translation process.
   d) Include a diagram or flowchart of your system architecture (describe it in words).

2. Neural Signal Processing (200-250 words):
   a) Explain how your system captures and interprets neural signals related to language.
   b) Describe the methods used to differentiate between linguistic and non-linguistic neural activity.
   c) Discuss how your system handles the variability in neural patterns across individuals.

3. Language Translation Process (200-250 words):
   a) Detail the step-by-step process of translating thoughts from the source language to the target language.
   b) Explain how your system addresses challenges specific to the given language pair.
   c) Discuss how the system maintains semantic and pragmatic accuracy in translation.

4. Training and Adaptation (150-200 words):
   a) Propose a method for training the system to accurately interpret and translate neural signals.
   b) Explain how the system could adapt to individual users' thought patterns and linguistic quirks.
   c) Discuss potential challenges in the training process and how they might be overcome.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of direct thought-to-language translation.
   b) Address privacy concerns and propose safeguards for protecting users' inner thoughts.
   c) Identify limitations of your system and suggest areas for future improvement.

6. Potential Applications and Impact (150-200 words):
   a) Propose two novel applications of your neural language translation interface.
   b) Discuss how this technology could impact fields such as neuroscience, linguistics, and international communication.
   c) Speculate on potential long-term societal effects of widespread adoption of this technology.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and AI system design. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, linguistics, and AI system design, particularly in relation to {t['neural_mechanism']} and {t['ai_technique']}.",
            f"The system architecture effectively incorporates the specified neural mechanism ({t['neural_mechanism']}) and AI technique ({t['ai_technique']}).",
            f"The language translation process addresses challenges specific to the given language pair ({t['language_pair'][0]} to {t['language_pair'][1]}).",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The ethical considerations and limitations are thoroughly discussed.",
            "The potential applications and impact are thoughtfully explored.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
