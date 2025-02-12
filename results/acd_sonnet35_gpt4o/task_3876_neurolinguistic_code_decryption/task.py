import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'brain_region': 'Broca\'s area',
                'linguistic_feature': 'syntax',
                'encryption_method': 'neural noise',
                'communication_context': 'interspecies dialogue'
            },
            {
                'brain_region': 'Wernicke\'s area',
                'linguistic_feature': 'semantics',
                'encryption_method': 'temporal coding',
                'communication_context': 'thought-to-text interface'
            },
            {
                'brain_region': 'Angular gyrus',
                'linguistic_feature': 'metaphor comprehension',
                'encryption_method': 'spatial patterns',
                'communication_context': 'dream interpretation'
            },
            {
                'brain_region': 'Inferior frontal gyrus',
                'linguistic_feature': 'phonological processing',
                'encryption_method': 'frequency modulation',
                'communication_context': 'silent speech decoding'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that decodes linguistic meaning directly from neural activity patterns in the {t['brain_region']}, focusing on {t['linguistic_feature']}. Then, use this system to solve a complex communication puzzle involving {t['encryption_method']} in the context of {t['communication_context']}. Your response should include:

1. Neural Decoding System Design (250-300 words):
   a) Describe the key components and processes of your neural decoding system.
   b) Explain how your system specifically targets the {t['brain_region']} and decodes {t['linguistic_feature']}.
   c) Discuss any novel approaches or algorithms used in your design.
   d) Address potential challenges in accurately interpreting neural signals and how you overcome them.

2. Linguistic-Neural Mapping (200-250 words):
   a) Explain how your system maps neural activity patterns to linguistic elements.
   b) Describe how you handle ambiguities or variations in neural representations of language.
   c) Discuss how your system accounts for individual differences in brain structure and function.

3. Encryption Analysis (200-250 words):
   a) Analyze how {t['encryption_method']} could be used to encrypt linguistic information in neural signals.
   b) Propose a method for your system to decrypt this neural-linguistic code.
   c) Discuss potential vulnerabilities or limitations of your decryption approach.

4. Communication Puzzle Solution (250-300 words):
   a) Present a hypothetical communication puzzle involving {t['communication_context']}.
   b) Explain how your neural decoding system would approach solving this puzzle.
   c) Describe the step-by-step process of decrypting and interpreting the neural-linguistic code.
   d) Discuss any challenges specific to {t['communication_context']} and how your system addresses them.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to direct neural-linguistic decoding.
   b) Analyze possible societal impacts of this technology, both positive and negative.
   c) Propose guidelines for responsible development and use of neural-linguistic decoding systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how these extensions could enhance its capabilities or applications.
   c) Propose an interdisciplinary research project that could emerge from this work.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and cryptography. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of neural activity in {t['brain_region']} and its role in {t['linguistic_feature']}.",
            "The neural decoding system design is well-thought-out, addressing potential challenges and including innovative approaches.",
            f"The proposed method for decrypting {t['encryption_method']} in neural-linguistic codes is scientifically plausible and creative.",
            f"The communication puzzle solution effectively applies the neural decoding system to {t['communication_context']}.",
            "The discussion of ethical and societal implications is thoughtful and comprehensive.",
            "The suggested future research directions are promising and well-justified.",
            "The response balances technical accuracy with clear explanations accessible to a scientifically literate audience.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
