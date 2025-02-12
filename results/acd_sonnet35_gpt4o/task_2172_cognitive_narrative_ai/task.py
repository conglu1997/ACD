class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "narrative_type": "Hero's Journey",
                "cultural_context": "Norse mythology",
                "cognitive_framework": "Schema theory",
                "target_audience": "Young adults"
            },
            "2": {
                "narrative_type": "Nonlinear narrative",
                "cultural_context": "Afrofuturism",
                "cognitive_framework": "Dual process theory",
                "target_audience": "Adult science fiction readers"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating complex narratives based on cognitive and cultural frameworks, then apply it to the following scenario:

Narrative Type: {t['narrative_type']}
Cultural Context: {t['cultural_context']}
Cognitive Framework: {t['cognitive_framework']}
Target Audience: {t['target_audience']}

Note: Schema theory refers to how people use mental structures to organize and interpret information. Dual process theory proposes that human thinking involves two distinct cognitive systems: one fast and intuitive, the other slow and deliberative.

Your task has the following parts:

1. Cognitive-Cultural Narrative Framework (250-300 words):
   a) Explain the key elements of the specified narrative type and its significance in storytelling.
   b) Describe how the given cognitive framework relates to narrative comprehension and generation.
   c) Discuss the importance of the cultural context in shaping narratives and reader expectations.
   d) Explain how these elements interact to create meaningful stories for the target audience.
   e) Provide at least two specific examples of how the cognitive framework manifests in the given narrative type and cultural context.

2. AI System Architecture (300-350 words):
   a) Provide a high-level overview of your AI system's architecture for narrative analysis and generation.
   b) Detail the components for natural language processing, cultural knowledge representation, and cognitive modeling.
   c) Explain how the system incorporates the specified cognitive framework in its narrative processing.
   d) Describe how the system handles cultural context and adapts to different narrative types.
   e) Discuss at least one novel or unconventional feature of your system design.
   f) Explain how your system would handle potential conflicts between cognitive frameworks and cultural norms.

3. Narrative Analysis Process (250-300 words):
   a) Describe how your AI system would analyze an existing narrative within the given parameters.
   b) Explain the metrics and features the system would use to evaluate narrative structure, cognitive engagement, and cultural relevance.
   c) Provide an example of how the system might break down a sample story from the specified cultural context.
   d) Discuss how the system would identify and interpret culturally specific elements in the narrative.
   e) Explain how the system would adapt its analysis for different target audiences.

4. Narrative Generation Process (300-350 words):
   a) Explain the step-by-step process your AI system would use to generate a new narrative based on the given parameters.
   b) Describe how the system ensures coherence, emotional resonance, and cultural authenticity in the generated narrative.
   c) Provide a detailed outline or summary (at least 150 words) of a story your system might generate, highlighting how it incorporates the specified elements.
   d) Explain how your system would balance adherence to narrative structure with creative innovation.
   e) Discuss how the system would adapt its generation process for different target audiences.

5. Evaluation and Refinement (200-250 words):
   a) Propose a method for evaluating the quality, cognitive engagement, and cultural relevance of the generated narratives.
   b) Describe how your AI system would improve its narrative generation based on feedback from target audience members and cultural experts.
   c) Suggest specific metrics for measuring the system's performance in creating cognitively engaging and culturally relevant stories.
   d) Propose a method for continuous learning and adaptation of the AI system based on new cultural inputs and changing cognitive theories.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical implications of an AI system capable of analyzing and generating culturally-specific narratives.
   b) Address the importance of avoiding cultural appropriation and stereotyping in AI-generated stories.
   c) Consider potential benefits and risks of using such a system in education, entertainment, or cultural preservation.
   d) Propose guidelines for responsible development and use of AI-generated narratives.

7. Limitations and Future Work (150-200 words):
   a) Discuss at least three potential limitations or challenges of your proposed AI system.
   b) Suggest areas for future research or improvement in cognitive-cultural narrative AI.
   c) Speculate on how advancements in this field might impact our understanding of human cognition and storytelling.

Ensure your response demonstrates a deep understanding of cognitive science, cultural studies, narratology, and AI system design. Be creative and innovative while maintaining scientific rigor and cultural sensitivity. Your total response should be between 1600-1950 words.

Format your response with clear headings for each section (e.g., '1. Cognitive-Cultural Narrative Framework:', '2. AI System Architecture:', etc.). Use appropriate subheadings where necessary to organize your thoughts clearly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified narrative type, cognitive framework, and cultural context, explaining their interactions and significance for the target audience, with specific examples provided.",
            "The AI system architecture is well-designed and addresses the complexities of narrative analysis and generation, with clear explanations of how it incorporates cognitive modeling and cultural knowledge. A novel feature is discussed, and potential conflicts are addressed.",
            "The narrative analysis process is well-explained, with appropriate metrics for evaluating structure, cognitive engagement, and cultural relevance. The system's adaptation for different audiences is clearly described.",
            "The narrative generation process is clearly described, with a convincing and detailed example that incorporates the specified elements and demonstrates cultural authenticity. The balance between structure and innovation is explained.",
            "The proposed evaluation method and refinement process are robust and include specific metrics and a method for continuous learning.",
            "The discussion of ethical and societal implications is thoughtful and considers multiple perspectives, including guidelines for responsible development and use.",
            "Potential limitations and future work are clearly discussed, with speculation on the impact on human cognition and storytelling.",
            "The overall response demonstrates creativity, interdisciplinary knowledge, and a deep understanding of the complexities involved in AI-driven narrative analysis and generation.",
            "The response follows the specified format with clear headings and appropriate organization, addressing all sub-points in each section.",
            "The response meets the specified word count requirements for each section and overall."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
