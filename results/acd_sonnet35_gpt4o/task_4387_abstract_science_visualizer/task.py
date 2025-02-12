import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "scientific_concept": "Quantum entanglement",
                "field": "Quantum physics",
                "target_audience": "High school students",
                "specific_aspect": "Measurement of entangled particles"
            },
            "2": {
                "scientific_concept": "Epigenetic inheritance",
                "field": "Molecular biology",
                "target_audience": "General public with basic science knowledge",
                "specific_aspect": "Transgenerational epigenetic effects"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates the complex scientific concept of {t['scientific_concept']} from the field of {t['field']} into an intuitive visual representation for {t['target_audience']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for translating scientific concepts into visual representations.
   b) Explain how your system integrates knowledge from {t['field']}, cognitive psychology, and data visualization.
   c) Detail the AI algorithms or models used in your system for concept understanding and visual generation.
   d) Discuss any novel approaches in your design for handling abstract scientific concepts.
   e) Include a high-level diagram or pseudocode illustrating your system's architecture (describe it textually).
   f) Propose a novel visualization technique or tool that hasn't been widely used in scientific communication before.

2. Concept Analysis and Decomposition (250-300 words):
   a) Explain how your AI system analyzes and breaks down the concept of {t['scientific_concept']}.
   b) Describe the key features or components of the concept that your system identifies.
   c) Discuss how your system handles the abstract or counter-intuitive aspects of the concept.
   d) Explain how your system adapts its analysis for {t['target_audience']}.
   e) Provide at least one quantitative metric for assessing the complexity of the concept.
   f) Describe how your system would specifically handle the aspect of {t['specific_aspect']}.

3. Visual Representation Generation (250-300 words):
   a) Detail the process by which your AI generates visual representations from the analyzed concept.
   b) Describe the types of visual elements (e.g., shapes, colors, animations) your system employs and why.
   c) Explain how your system ensures the visual representation is both accurate and intuitive.
   d) Discuss how your system tailors the visualization for {t['target_audience']}.
   e) Provide a detailed description of the visual representation your system would generate for {t['scientific_concept']}. Include specific details about layout, color scheme, and any interactive elements.
   f) Compare your proposed visualization approach with at least one existing method for communicating the same scientific concept.

4. Cognitive and Learning Principles (200-250 words):
   a) Discuss the cognitive and learning theories your system incorporates in its visualizations.
   b) Explain how your system addresses different learning styles and cognitive processes.
   c) Describe how your system measures and optimizes for comprehension and retention of the concept.
   d) Include at least one quantitative estimate of the visualization's effectiveness based on cognitive science principles.

5. Evaluation and Refinement (200-250 words):
   a) Propose methods for evaluating the effectiveness of your system's visualizations.
   b) Describe an experiment to test your system's performance with {t['target_audience']}.
   c) Explain how your system could use feedback to improve its visualizations over time.
   d) Discuss potential challenges in evaluating abstract concept visualizations and how you would address them.
   e) Address potential biases in your AI system and how these might be mitigated.
   f) Propose a method for measuring the long-term impact of your visualization system on scientific literacy.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI to visualize scientific concepts.
   b) Address concerns about oversimplification or misrepresentation of complex ideas.
   c) Explain the limitations of your system and cases where it might not be appropriate to use.
   d) Discuss any potential controversies or alternative interpretations of {t['scientific_concept']} and how your system would handle them.
   e) Explore potential unintended consequences of widespread use of your visualization system.

7. Broader Impacts and Applications (150-200 words):
   a) Discuss how your system could impact science education and public understanding of science.
   b) Suggest two other fields or areas where your system could be applied.
   c) Describe how this technology might influence scientific communication and collaboration.
   d) Propose at least two interdisciplinary applications of your visualization system beyond science education.
   e) Discuss how your system might adapt to future advancements in the scientific understanding of {t['scientific_concept']}.

Ensure your response demonstrates a deep understanding of {t['field']}, cognitive science, data visualization, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex ideas. Be innovative in your approach while maintaining scientific accuracy.

Include at least three citations or references to relevant scientific literature or theories throughout your response.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified scientific concept, cognitive science, data visualization, and artificial intelligence.",
            "The proposed AI system is innovative and plausible, integrating knowledge from multiple disciplines.",
            "The visual representation generation process is well-explained and appropriate for the target audience.",
            "The response includes at least one quantitative metric for concept complexity and one quantitative estimate of visualization effectiveness.",
            "The response addresses ethical considerations, limitations, and potential controversies related to the scientific concept and the proposed system.",
            "The response includes at least three relevant citations or references to scientific literature or theories.",
            "The response proposes a novel visualization technique or tool and compares it with an existing method.",
            "The response discusses potential biases in the AI system and how they might be mitigated.",
            "The response includes a specific example of how the system would handle the given aspect of the scientific concept.",
            "The response proposes a method for measuring the long-term impact on scientific literacy.",
            "The response discusses potential unintended consequences of widespread use of the visualization system.",
            "The response proposes interdisciplinary applications beyond science education.",
            "The response discusses how the system might adapt to future advancements in scientific understanding.",
            "The response is well-structured, following the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
