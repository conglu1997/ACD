import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'context': 'love',
                'words': ['heart', 'beat', 'rhythm', 'dance', 'pulse']
            },
            '2': {
                'context': 'quantum computing',
                'words': ['state', 'observe', 'collapse', 'entangle', 'superpose']
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes 'quantum superposition sentences' where multiple meanings coexist simultaneously, inspired by the principles of quantum mechanics. Focus on the context of {t['context']} using the following words: {', '.join(t['words'])}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and analyzing quantum superposition sentences.
   b) Explain how these components interact to create and interpret sentences with multiple simultaneous meanings.
   c) Discuss how your system incorporates principles from quantum mechanics, particularly superposition.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Quantum Sentence Generation (200-250 words):
   a) Explain how your system would generate sentences with multiple coexisting meanings.
   b) Describe how you ensure that the generated sentences maintain coherence while embodying quantum-like properties.
   c) Provide an example of a generated quantum superposition sentence using the given context and words, and explain its multiple meanings.

3. Semantic Analysis (200-250 words):
   a) Detail how your system would analyze and quantify the semantic 'superposition' in generated sentences.
   b) Propose a method for measuring the degree of meaning entanglement in these sentences.
   c) Explain how your system would handle the 'collapse' of meaning when a sentence is interpreted by a reader.

4. Linguistic Quantum Mechanics (200-250 words):
   a) Draw parallels between quantum mechanical principles and your linguistic model.
   b) Discuss how concepts like entanglement, measurement, and wave function collapse apply to your sentence model.
   c) Propose a linguistic equivalent of Heisenberg's uncertainty principle in the context of your system.

5. Applications and Implications (150-200 words):
   a) Suggest potential applications of your quantum linguistic model in fields such as natural language processing, creative writing, or cognitive science.
   b) Discuss the implications of your model for our understanding of language and meaning.
   c) Speculate on how this approach might influence future developments in AI and linguistics.

6. Evaluation and Limitations (150-200 words):
   a) Propose a method to evaluate the 'quantum' nature of the generated sentences.
   b) Discuss the limitations of your approach and potential areas for improvement.
   c) Address any ethical considerations or potential misuses of this technology.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from quantum physics, linguistics, and AI, providing explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of both quantum mechanics principles and linguistic concepts.",
            "The proposed AI system architecture is well-designed and incorporates quantum-inspired elements in a plausible manner.",
            "The quantum sentence generation process is clearly explained and produces coherent sentences with multiple coexisting meanings.",
            "The semantic analysis approach effectively quantifies and analyzes the 'quantum' properties of the generated sentences.",
            "The parallels drawn between quantum mechanics and linguistics are insightful and well-reasoned.",
            "The proposed applications and implications of the model are innovative and demonstrate interdisciplinary thinking.",
            "The evaluation method and discussion of limitations show critical thinking and awareness of the model's constraints.",
            "The overall response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
