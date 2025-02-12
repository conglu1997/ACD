import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            {"concept": "time", "aspects": ["flow", "measurement", "perception"]},
            {"concept": "consciousness", "aspects": ["self-awareness", "subjective experience", "qualia"]},
            {"concept": "justice", "aspects": ["fairness", "retribution", "social order"]}
        ]
        scientific_theories = [
            {"theory": "quantum entanglement", "key_principles": ["non-local correlations", "superposition", "measurement problem"]},
            {"theory": "neural plasticity", "key_principles": ["synaptic reorganization", "learning and memory", "brain adaptation"]},
            {"theory": "climate change feedback loops", "key_principles": ["amplification", "complex interactions", "tipping points"]}
        ]
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "theory": random.choice(scientific_theories)
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "theory": random.choice(scientific_theories)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze novel metaphors based on abstract concepts, then apply it to explain complex scientific theories. Your task involves the following steps:

1. Metaphor Generation System Design (250-300 words):
   a) Describe the key components of your AI system for generating novel metaphors.
   b) Explain how your system integrates knowledge from linguistics, cognitive science, and the target domains.
   c) Detail how the system accounts for cultural differences and context in metaphor interpretation.
   d) Discuss any novel algorithms or approaches used in your system.

2. Abstract Concept Analysis (200-250 words):
   a) Analyze the abstract concept of {t['concept']['concept']}.
   b) Identify its key characteristics and associations, considering the aspects: {', '.join(t['concept']['aspects'])}.
   c) Explain how your AI system would represent and process this concept for metaphor generation.

3. Metaphor Generation and Analysis (250-300 words):
   a) Generate two novel metaphors for {t['concept']['concept']} using your AI system.
   b) For each metaphor, explain:
      - The logical connection between the source and target domains
      - The emotional or intuitive impact of the metaphor
      - Potential cultural variations in interpretation
   c) Analyze the strengths and limitations of each generated metaphor.

4. Scientific Theory Explanation (250-300 words):
   a) Briefly explain the key principles of {t['theory']['theory']}: {', '.join(t['theory']['key_principles'])}.
   b) Generate a novel metaphor to explain {t['theory']['theory']} using your AI system.
   c) Analyze how this metaphor aids in understanding the scientific theory:
      - Identify which aspects of the theory are well-represented by the metaphor
      - Discuss any limitations or potential misunderstandings the metaphor might introduce
      - Explain how the metaphor could be refined or extended to address these limitations

5. Evaluation and Ethical Considerations (150-200 words):
   a) Propose methods to evaluate the effectiveness and creativity of your AI's metaphor generation.
   b) Discuss potential applications of this system in education, scientific communication, or creative writing.
   c) Address ethical considerations, such as bias in metaphor generation or the impact on human creativity.

Ensure your response demonstrates a deep understanding of metaphor theory, cognitive science, and the specific abstract concept and scientific theory. Use appropriate technical terminology and provide clear explanations for complex ideas. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (e.g., '1. Metaphor Generation System Design', '2. Abstract Concept Analysis'). Number your paragraphs within each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed design of an AI system for metaphor generation and analysis, with clear components and novel approaches",
            f"The abstract concept of {t['concept']['concept']} is thoroughly analyzed, addressing all specified aspects",
            f"Two novel and distinct metaphors are generated and analyzed for the concept of {t['concept']['concept']}",
            f"A novel metaphor is generated and analyzed to explain {t['theory']['theory']}, addressing all key principles",
            "The response addresses specific evaluation methods and ethical considerations for the AI system",
            "The overall response demonstrates a deep understanding of metaphor theory, cognitive science, and the specific abstract concept and scientific theory",
            "The response follows the specified format and word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
