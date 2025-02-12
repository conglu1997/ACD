import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave function collapse"
        ]
        linguistic_elements = [
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Morphology"
        ]
        narrative_themes = [
            "Time travel",
            "Parallel universes",
            "Consciousness transfer",
            "Reality simulation"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_element": random.choice(linguistic_elements),
                "narrative_theme": random.choice(narrative_themes)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_element": random.choice(linguistic_elements),
                "narrative_theme": random.choice(narrative_themes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a narrative framework that incorporates the quantum computing concept of {t['quantum_concept']} to analyze and generate linguistic structures, focusing on the linguistic element of {t['linguistic_element']}. Then, use this framework to write a short story exploring the theme of {t['narrative_theme']}. Your response should include:

1. Quantum-Linguistic Framework (250-300 words):
   a) Explain how the quantum concept of {t['quantum_concept']} can be applied to analyze or generate {t['linguistic_element']}.
   b) Describe the key components and processes of your framework.
   c) Provide an example of how this framework would analyze or generate a specific linguistic structure.
   d) Discuss any novel insights or capabilities this approach might offer compared to traditional linguistic analysis.

   Example: If the quantum concept is "Superposition" and the linguistic element is "Semantics", you might discuss how words can exist in a superposition of meanings until context collapses them into a specific sense.

2. Narrative Structure (200-250 words):
   a) Describe how your quantum-linguistic framework informs or generates the narrative structure of your story.
   b) Explain how this structure relates to both the quantum concept and the linguistic element.
   c) Discuss how this approach might differ from traditional storytelling methods.

   Example: A story structure based on "Entanglement" might feature intertwined plotlines that affect each other instantaneously across different times or realities.

3. Short Story (400-500 words):
   Write a short story that explores the theme of {t['narrative_theme']} using your quantum-linguistic framework. Ensure that the story's structure and language reflect the principles of your framework.

4. Analysis (200-250 words):
   a) Analyze your story in terms of the quantum-linguistic framework you developed.
   b) Explain how specific elements of the story embody or demonstrate the quantum concept and linguistic element.
   c) Discuss any emergent properties or unexpected features that arose from using this approach.

5. Implications and Future Applications (150-200 words):
   a) Discuss potential implications of your quantum-linguistic approach for fields such as computational linguistics, cognitive science, or artificial intelligence.
   b) Propose two novel applications or research directions that could build on your framework.

   Example: A quantum-linguistic approach to "Pragmatics" might lead to more context-aware AI communication systems or new methods for analyzing social dynamics in large-scale online interactions.

Ensure your response demonstrates a deep understanding of quantum computing concepts, linguistics, and narrative theory. Be creative and innovative in your approach while maintaining scientific and logical consistency. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Remember to maintain scientific plausibility throughout your response, even as you explore creative and speculative ideas. Strive for coherence between all parts of your response, ensuring that your framework, story, analysis, and implications are all closely interconnected.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words.

Note on scoring: Your response will be evaluated based on your understanding of the quantum concept and linguistic element, the creativity and coherence of your story, the depth of your analysis, and the innovation of your proposed applications. Partial credit will be given for meeting individual criteria."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum concept {t['quantum_concept']} and its creative application to linguistics.",
            f"The quantum-linguistic framework effectively and innovatively incorporates the linguistic element of {t['linguistic_element']}.",
            f"The short story creatively explores the theme of {t['narrative_theme']} while clearly reflecting the quantum-linguistic framework.",
            "The analysis provides insightful and specific connections between the story, the quantum concept, and the linguistic element.",
            "The response includes all required sections with appropriate depth and maintains scientific plausibility throughout.",
            "The quantum-linguistic framework presents a novel and logically consistent approach to narrative generation and analysis.",
            "The implications and future applications discussed are innovative, well-reasoned, and have potential real-world impact.",
            "The entire response shows strong coherence, with clear connections between the framework, story, analysis, and implications."
        ]
        word_count = len(submission.split())
        if word_count < 1100 or word_count > 1600:
            return 0.0
        
        score = 0.0
        for criterion in criteria:
            if eval_with_llm_judge(instructions, submission, [criterion]):
                score += 0.125
        return score
