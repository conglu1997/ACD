import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ai_capability': 'Natural Language Understanding',
                'improvement_focus': 'Context Retention',
                'potential_risk': 'Privacy Concerns'
            },
            {
                'ai_capability': 'Multimodal Learning',
                'improvement_focus': 'Cross-Modal Integration',
                'potential_risk': 'Hallucination'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical self-improvement strategy for an AI system focusing on enhancing its {t['ai_capability']} capability, with a specific emphasis on improving {t['improvement_focus']}. Then, analyze its potential impacts and propose experiments to validate its effectiveness. Your response should include:

1. Self-Improvement Strategy (300-350 words):
   a) Describe the current limitations in the AI's {t['ai_capability']} capability, particularly regarding {t['improvement_focus']}.
   b) Propose a novel self-improvement mechanism that the AI could implement to enhance this capability.
   c) Explain how this mechanism would work, including any learning algorithms or architectural changes involved.
   d) Discuss how this improvement strategy differs from traditional machine learning approaches.
   e) Include a simple flowchart or diagram of your proposed strategy using ASCII art or Unicode characters (max 20 lines by 80 characters).

2. Implementation and Challenges (250-300 words):
   a) Outline the key steps for implementing this self-improvement strategy.
   b) Identify potential challenges or obstacles in the implementation process.
   c) Propose solutions to overcome these challenges.
   d) Discuss any resource requirements or constraints for this self-improvement process.

3. Impact Analysis (250-300 words):
   a) Analyze the potential positive impacts of this self-improvement on the AI's overall performance and capabilities.
   b) Discuss possible negative consequences or risks, including the specified {t['potential_risk']}.
   c) Explore how this self-improvement might affect the AI's interaction with humans and other AI systems.
   d) Consider long-term implications of recursive self-improvement in this specific capability.

4. Ethical Considerations (200-250 words):
   a) Identify ethical concerns related to AI self-improvement, particularly in the context of {t['ai_capability']}.
   b) Discuss potential societal impacts of AIs with enhanced {t['improvement_focus']} capabilities.
   c) Propose ethical guidelines or safeguards for developing and deploying self-improving AI systems.

5. Experimental Validation (250-300 words):
   a) Design an experiment to test the effectiveness of your proposed self-improvement strategy.
   b) Describe the methodology, including control groups and performance metrics.
   c) Explain how you would measure improvements in {t['improvement_focus']} specifically.
   d) Discuss potential challenges in validating self-improving AI systems and how to address them.

6. Comparative Analysis (150-200 words):
   a) Briefly describe an alternative approach to improving the AI's {t['ai_capability']} capability.
   b) Compare and contrast this alternative with your proposed self-improvement strategy.
   c) Discuss the potential advantages and disadvantages of each approach.

7. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or refinements to your self-improvement strategy.
   b) Propose a research question that explores the relationship between {t['ai_capability']}, {t['improvement_focus']}, and broader AI development.
   c) Discuss how insights from this self-improvement strategy could inform other areas of AI research.

Ensure your response demonstrates a deep understanding of AI systems, machine learning, and the specific capability you're focusing on. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and addressing potential risks and ethical concerns.

Throughout your response, cite or reference at least three relevant AI research papers or theories that support your proposed strategy and analysis.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1600-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The self-improvement strategy is innovative and specifically addresses {t['ai_capability']} with a focus on {t['improvement_focus']}.",
            "The implementation plan and challenges are well-thought-out and realistic.",
            f"The impact analysis thoroughly considers both positive and negative consequences, including {t['potential_risk']}.",
            "Ethical considerations are comprehensive and demonstrate a nuanced understanding of AI ethics.",
            "The experimental validation proposal is well-designed and addresses the challenges of testing self-improving AI systems.",
            "The response demonstrates a deep understanding of AI systems, machine learning, and the specific capability in focus.",
            "The proposed future research directions are insightful and build upon the presented self-improvement strategy.",
            "The ASCII art or Unicode flowchart effectively illustrates the proposed self-improvement strategy.",
            "The comparative analysis provides meaningful insights into the strengths and weaknesses of the proposed strategy.",
            "The response includes relevant citations to AI research papers or theories that support the proposed strategy and analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
