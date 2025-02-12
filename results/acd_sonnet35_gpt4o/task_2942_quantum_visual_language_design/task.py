import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'quantum_principle': 'Superposition',
                'scientific_concept': 'Climate change feedback loops'
            },
            '2': {
                'quantum_principle': 'Entanglement',
                'scientific_concept': 'Neuroplasticity in the human brain'
            }
        }
        return {str(i): task for i, task in enumerate(random.sample(list(tasks.values()), len(tasks)), 1)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a visual language based on the quantum principle of {t['quantum_principle']}, then use it to represent the complex scientific concept of {t['scientific_concept']}. Your response should include:

1. Quantum-Inspired Visual Language (250-300 words):
   a) Explain how you've incorporated {t['quantum_principle']} into your visual language design.
   b) Describe the basic elements (shapes, colors, patterns) of your visual language.
   c) Explain the grammar or rules for combining these elements.
   d) Discuss how your visual language captures quantum properties that traditional languages cannot.

2. Visual Alphabet (150-200 words):
   a) Present a visual alphabet of at least 10 symbols in your language.
   b) For each symbol, provide:
      - A textual description or ASCII art representation
      - Its meaning or function in the language
      - How it relates to {t['quantum_principle']}

3. Representation of Scientific Concept (250-300 words):
   a) Use your quantum-inspired visual language to represent {t['scientific_concept']}.
   b) Provide a detailed textual description or ASCII art representation of your visual composition.
   c) Explain how each element in your composition contributes to representing the scientific concept.
   d) Discuss how your quantum-inspired approach provides unique insights into {t['scientific_concept']}.

4. Translation and Interpretation (200-250 words):
   a) Describe the process of 'reading' or interpreting your visual representation.
   b) Explain how your visual language could be translated back into a traditional written or spoken language.
   c) Discuss any ambiguities or multiple interpretations that arise from your quantum-inspired approach.

5. Applications and Implications (150-200 words):
   a) Propose two potential applications of your quantum-inspired visual language in scientific communication or education.
   b) Discuss how this approach might enhance our understanding or visualization of complex quantum phenomena.
   c) Consider any limitations or challenges in adopting such a visual language system.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and visual design principles. Be creative in your approach while maintaining scientific accuracy. Use appropriate terminology from each field and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words, not including the visual alphabet descriptions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle and its application to visual language design.",
            "The visual alphabet is creative, well-explained, and clearly relates to the quantum principle.",
            "The representation of the scientific concept is innovative and effectively uses the quantum-inspired visual language.",
            "The explanation of translation and interpretation is thorough and addresses potential ambiguities.",
            "The proposed applications are creative and well-justified.",
            "The response maintains a balance between creativity and scientific accuracy throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0