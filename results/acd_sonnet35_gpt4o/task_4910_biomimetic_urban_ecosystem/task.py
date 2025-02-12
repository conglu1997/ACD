class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "environmental_challenge": "Urban heat island effect",
                "biomimetic_inspiration": "Termite mounds"
            },
            "2": {
                "environmental_challenge": "Air pollution",
                "biomimetic_inspiration": "Spider webs"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic urban ecosystem that addresses the environmental challenge of {t['environmental_challenge']} using inspiration from {t['biomimetic_inspiration']}. Your response should include the following sections:

1. Biomimetic Analysis (250-300 words):
   a) Describe the key features and functions of {t['biomimetic_inspiration']} relevant to addressing {t['environmental_challenge']}.
   b) Explain how these natural mechanisms can be translated into urban design principles.
   c) Discuss any limitations or challenges in applying this biomimetic approach to urban environments.

2. Urban Ecosystem Design (300-350 words):
   a) Propose a detailed design for an urban ecosystem component inspired by {t['biomimetic_inspiration']}.
   b) Explain how your design addresses {t['environmental_challenge']}.
   c) Describe the materials, structures, and processes involved in your design.
   d) Include a simple diagram or sketch of your design (use ASCII art or a clear textual description).

3. Integration and Scalability (200-250 words):
   a) Explain how your biomimetic design can be integrated into existing urban infrastructure.
   b) Discuss the scalability of your solution from individual buildings to neighborhood and city-wide implementation.
   c) Address any potential conflicts with existing urban systems or regulations.

4. Environmental Impact Assessment (200-250 words):
   a) Analyze the potential environmental benefits of implementing your design.
   b) Discuss any possible negative environmental impacts and how they can be mitigated.
   c) Propose a method to quantitatively measure the effectiveness of your solution in addressing {t['environmental_challenge']}.

5. Social and Economic Implications (150-200 words):
   a) Discuss the potential social impacts of implementing your biomimetic urban ecosystem.
   b) Analyze the economic feasibility of your design, including implementation costs and potential long-term savings.
   c) Propose strategies to encourage public acceptance and adoption of your biomimetic solution.

6. Interdisciplinary Collaboration (150-200 words):
   a) Identify key disciplines and experts needed to implement your biomimetic urban ecosystem.
   b) Describe potential challenges in interdisciplinary collaboration and propose solutions.
   c) Explain how integrating multiple fields of expertise can enhance the effectiveness of your design.

7. Case Study (200-250 words):
   a) Provide a specific example or case study of how your biomimetic design could be applied in a real urban setting.
   b) Describe the unique challenges and opportunities presented by this specific location.
   c) Explain how your design would be adapted to suit the local environmental, social, and economic context.

8. Future Developments and Adaptations (150-200 words):
   a) Suggest two potential improvements or extensions to your biomimetic urban ecosystem design.
   b) Discuss how your approach might be adapted to address other urban environmental challenges.
   c) Propose a research agenda to further develop and refine biomimetic solutions for urban environments.

Ensure your response demonstrates a deep understanding of biology, architecture, environmental science, and urban planning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and practical feasibility.

Format your response with clear headings for each section, numbered as above. Include the word count for each section in parentheses at the end of the section. Your total response should be between 1600-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and creative application of biomimicry principles to urban design.",
            "The proposed solution effectively addresses the specified environmental challenge.",
            "The design is innovative, yet scientifically plausible and practically feasible.",
            "The response shows a deep understanding of biology, architecture, environmental science, and urban planning.",
            "The analysis of environmental impact, social implications, and economic feasibility is thorough and well-reasoned.",
            "The case study effectively illustrates the practical application of the biomimetic design in a real urban setting.",
            "The response addresses interdisciplinary collaboration and its importance in implementing the design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
