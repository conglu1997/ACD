import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scientific_concepts = [
            {
                "concept": "Quantum Entanglement",
                "field": "Quantum Physics",
                "description": "A phenomenon where particles become interconnected and the quantum state of each particle cannot be described independently of the others."
            },
            {
                "concept": "Neuroplasticity",
                "field": "Neuroscience",
                "description": "The brain's ability to reorganize itself by forming new neural connections throughout life."
            },
            {
                "concept": "Dark Energy",
                "field": "Cosmology",
                "description": "A hypothetical form of energy that exerts a negative, repulsive pressure, behaving like the opposite of gravity."
            },
            {
                "concept": "Epigenetics",
                "field": "Genetics",
                "description": "The study of heritable changes in gene expression that do not involve changes to the underlying DNA sequence."
            }
        ]
        return {
            "1": random.choice(scientific_concepts),
            "2": random.choice(scientific_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes metaphors for complex scientific concepts, then use it to create and evaluate metaphors for {t['concept']} in the field of {t['field']}. Your response should include:

1. AI System Design (300-350 words):
   a) Describe the architecture of your AI system for generating and analyzing scientific metaphors.
   b) Explain how your system integrates knowledge from science, linguistics, and cognitive psychology.
   c) Detail any novel algorithms or techniques used in your metaphor generation and analysis process.
   d) Provide a high-level pseudocode or flowchart illustrating a key process in your system.
   e) Include a textual description of a visual representation (e.g., diagram, graph) of your AI system's architecture.

2. Metaphor Generation (250-300 words):
   a) Use your AI system to generate three distinct metaphors for {t['concept']}.
   b) Explain the rationale behind each metaphor, linking it to specific aspects of the scientific concept.
   c) Discuss how these metaphors might aid in understanding or remembering the concept.
   d) Compare your generated metaphors with existing ones in scientific literature or popular science communication for this concept.

3. Metaphor Analysis (250-300 words):
   a) Analyze the strengths and limitations of each generated metaphor in conveying the scientific concept.
   b) Discuss how your AI system evaluates the accuracy and effectiveness of the metaphors.
   c) Explain how your system accounts for potential cultural or contextual variations in metaphor interpretation.
   d) Propose a method for empirically testing the effectiveness of your generated metaphors in enhancing understanding of {t['concept']}.

4. Cognitive Implications (200-250 words):
   a) Discuss how metaphor use might influence understanding and reasoning about {t['concept']}.
   b) Explain potential cognitive benefits and drawbacks of using metaphors for scientific communication.
   c) Analyze how your AI-generated metaphors might interact with or challenge existing mental models of {t['concept']}.

5. Scientific Communication Applications (200-250 words):
   a) Suggest three potential applications of your AI system in scientific communication or education.
   b) Discuss how these applications might improve public understanding of complex scientific ideas.
   c) Address potential challenges in implementing your system in real-world scientific communication contexts.
   d) Propose a strategy for integrating your AI system with existing science communication platforms or educational tools.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to using AI-generated metaphors for scientific communication.
   b) Discuss the implications of simplifying complex concepts through metaphors.
   c) Propose guidelines for the responsible use of AI-generated metaphors in science education and communication.
   d) Consider the potential societal impacts of widespread use of AI-generated scientific metaphors.

Ensure your response demonstrates a deep understanding of the scientific concept, metaphor theory, and AI capabilities. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific accuracy and plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['concept']} and metaphor theory.",
            "The AI system design is innovative, well-explained, and incorporates knowledge from relevant fields.",
            "The visual representation of the AI system architecture is clearly described and logical.",
            "The generated metaphors are creative, relevant, and effectively aid in understanding the scientific concept.",
            "The metaphor analysis is thorough, considering accuracy, effectiveness, cultural variations, and comparison with existing metaphors.",
            "The proposed method for empirically testing metaphor effectiveness is well-designed and feasible.",
            "The cognitive implications and analysis of mental model interactions are insightful and well-reasoned.",
            "The suggested applications and integration strategies are innovative and practical.",
            "The ethical considerations are comprehensive, addressing both immediate and long-term societal impacts.",
            "The response is well-structured, clear, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
