import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            {
                "system": "Ant colony optimization",
                "key_feature": "Stigmergy",
                "problem_domain": "Supply chain optimization"
            },
            {
                "system": "Slime mold network formation",
                "key_feature": "Decentralized decision-making",
                "problem_domain": "Urban planning"
            }
        ]
        return {
            "1": random.choice(biological_systems),
            "2": random.choice(biological_systems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel reasoning system inspired by {t['system']}, focusing on the key feature of {t['key_feature']}. Then, apply this system to solve a complex problem in the domain of {t['problem_domain']}. Your response should include:

1. Biological System Analysis (200-250 words):
   a) Explain the key principles and mechanisms of {t['system']}.
   b) Describe how {t['key_feature']} contributes to the system's effectiveness.
   c) Discuss any limitations or constraints of this biological system.

2. Novel Reasoning System Design (300-350 words):
   a) Describe your novel reasoning system inspired by {t['system']}.
   b) Explain how you've incorporated and adapted {t['key_feature']} into your system.
   c) Discuss any additional features or mechanisms you've included.
   d) Provide a high-level diagram or flowchart of your reasoning system using ASCII art (max 20 lines x 80 characters).
   e) Explain how your system differs from traditional human reasoning approaches.

3. Problem Analysis (200-250 words):
   a) Identify a specific, complex problem within the domain of {t['problem_domain']}.
   b) Analyze the key challenges and limitations of current approaches to this problem.
   c) Explain why traditional problem-solving methods might be insufficient.

4. Application of Novel Reasoning System (300-350 words):
   a) Apply your novel reasoning system to the identified problem.
   b) Describe the step-by-step process of how your system approaches the problem.
   c) Explain how the key features of your system address the challenges identified.
   d) Discuss any potential advantages or unique insights provided by your approach.
   e) Address any limitations or potential drawbacks of using your system for this problem.

5. Comparative Analysis (200-250 words):
   a) Compare your novel reasoning system's approach to traditional problem-solving methods.
   b) Discuss how your system might complement or challenge existing approaches in {t['problem_domain']}.
   c) Analyze the potential impact of your system on the field of {t['problem_domain']}.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of applying biomimetic reasoning to {t['problem_domain']}.
   b) Propose guidelines for responsible development and use of such systems.
   c) Suggest potential extensions or improvements to your reasoning system.
   d) Identify other domains where your novel reasoning approach might be beneficial.

Ensure your response demonstrates a deep understanding of the biological system, creative system design, and the problem domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Include word counts for each section in parentheses at the end of the section.

Note: Do not simply describe the biological system or restate known problem-solving approaches. Your task is to create a novel reasoning system inspired by the biological system and apply it creatively to the given problem domain."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['system']} and {t['key_feature']} without simply restating known information.",
            "The novel reasoning system design is creative, well-explained, and plausibly inspired by the biological system, with a clear ASCII art diagram.",
            f"The application to the {t['problem_domain']} problem is thorough, innovative, and demonstrates potential advantages over traditional approaches.",
            "The comparative analysis provides insightful comparisons between the novel system and traditional methods, highlighting unique aspects of the biomimetic approach.",
            "Ethical considerations and future directions are thoughtfully addressed, with specific guidelines and potential applications proposed.",
            "The overall response is well-structured, coherent, and demonstrates interdisciplinary knowledge application, staying within the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
