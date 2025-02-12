class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "organism": "Morpho butterfly",
                "property": "Structural coloration",
                "application_field": "Sustainable textile industry"
            },
            "2": {
                "organism": "Namib desert beetle",
                "property": "Water harvesting",
                "application_field": "Drought-resistant architecture"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel biomimetic material inspired by the {t['organism']}, focusing on its {t['property']} property. Then, analyze its potential applications in the field of {t['application_field']} and evaluate its environmental impact. Your response should include:

1. Biomimetic Material Design (300-350 words):
   a) Describe the key features of your biomimetic material, explaining how it mimics the {t['property']} of the {t['organism']}.
   b) Detail the material's composition, structure, and manufacturing process.
   c) Explain how your design improves upon existing materials or technologies in the field.
   d) Include a diagram or schematic representation of your material's structure (described in words).

2. Scientific Principles (250-300 words):
   a) Explain the biological principles behind the {t['organism']}'s {t['property']}.
   b) Discuss how these principles are translated into your material design.
   c) Describe any challenges in replicating the natural property and how you addressed them.

3. Applications in {t['application_field']} (250-300 words):
   a) Propose three specific applications of your biomimetic material in the field of {t['application_field']}.
   b) Explain how each application leverages the unique properties of your material.
   c) Discuss potential challenges in implementing these applications and how they might be overcome.

4. Performance Analysis (200-250 words):
   a) Propose methods to evaluate the performance of your biomimetic material.
   b) Compare your material's expected performance to current industry standards.
   c) Discuss any limitations of your material and potential areas for improvement.

5. Environmental Impact Assessment (250-300 words):
   a) Analyze the potential environmental benefits of using your biomimetic material.
   b) Discuss any potential negative environmental impacts and how they could be mitigated.
   c) Compare the lifecycle environmental impact of your material to conventional alternatives.

6. Ethical Considerations and Future Directions (200-250 words):
   a) Discuss ethical implications of developing and using biomimetic materials.
   b) Address any potential concerns about exploiting natural designs or organisms.
   c) Propose guidelines for responsible development and use of biomimetic technologies.
   d) Suggest potential future research directions or improvements for your material.

Ensure your response demonstrates a deep understanding of biomimicry, materials science, and environmental sustainability. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world challenges.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['organism']}'s {t['property']} and how it can be applied to material design.",
            f"The biomimetic material design is innovative and plausibly applicable to {t['application_field']}.",
            "The analysis includes a thorough consideration of environmental impacts and ethical implications.",
            "The response integrates knowledge from biology, materials science, engineering, and environmental studies.",
            "The proposed applications and performance analysis are well-reasoned and scientifically sound.",
            "The response adheres to the specified word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
