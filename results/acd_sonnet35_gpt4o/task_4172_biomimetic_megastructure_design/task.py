import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_inspirations = [
            'Coral reefs',
            'Mycelial networks',
            'Termite mounds',
            'Spider webs',
            'Whale baleen'
        ]
        megastructure_purposes = [
            'Vertical farming',
            'Carbon capture',
            'Water purification',
            'Energy generation',
            'Waste management'
        ]
        tasks = [
            {
                'inspiration': random.choice(biological_inspirations),
                'purpose': random.choice(megastructure_purposes)
            },
            {
                'inspiration': random.choice(biological_inspirations),
                'purpose': random.choice(megastructure_purposes)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a sustainable megastructure inspired by {t['inspiration']} for the purpose of {t['purpose']}. Then, analyze its potential environmental and societal impacts. Your response should include the following sections:

1. Biomimetic Design (300-350 words):
   a) Describe the key features of your megastructure and how they are inspired by {t['inspiration']}.
   b) Explain how these biomimetic features contribute to the structure's {t['purpose']} function.
   c) Discuss the materials and construction methods you would use, emphasizing sustainability.
   d) Include a basic schematic or description of the structure's layout.

2. Functional Analysis (250-300 words):
   a) Detail how your megastructure performs its {t['purpose']} function.
   b) Quantify the structure's expected performance (e.g., energy generated, water purified, etc.).
   c) Compare your biomimetic approach to conventional methods for {t['purpose']}.
   d) Discuss any potential synergies with other urban or environmental systems.

3. Environmental Impact Assessment (250-300 words):
   a) Analyze the potential positive environmental impacts of your megastructure.
   b) Identify any negative environmental consequences and propose mitigation strategies.
   c) Discuss how the structure might affect local ecosystems and biodiversity.
   d) Evaluate the structure's overall carbon footprint and resource efficiency.

4. Societal Implications (200-250 words):
   a) Examine how your megastructure might influence urban planning and development.
   b) Discuss potential economic impacts, including job creation and industry disruption.
   c) Address concerns about social equity and access to the benefits of the megastructure.
   d) Consider how the structure might shape public perception of biomimicry and sustainable technology.

5. Ethical Considerations (150-200 words):
   a) Identify key ethical issues related to the development and implementation of your megastructure.
   b) Discuss how to balance technological progress with environmental and social responsibility.
   c) Propose guidelines for the ethical development and use of biomimetic megastructures.

6. Future Developments (150-200 words):
   a) Suggest two potential improvements or expansions to your megastructure design.
   b) Propose a research agenda to address any uncertainties or challenges in your current design.
   c) Speculate on how this technology might evolve over the next few decades.

Ensure your response demonstrates a deep understanding of biological systems, engineering principles, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world concerns.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design clearly demonstrates inspiration from {t['inspiration']} and effectively addresses {t['purpose']}.",
            "The response shows a deep understanding of biomimicry, engineering, and environmental science.",
            "The functional analysis includes quantitative estimates of the structure's performance.",
            "The environmental and societal impact assessments are thorough and consider both positive and negative effects.",
            "Ethical considerations are thoughtfully addressed, with proposed guidelines for responsible development.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "All required sections are present and adequately addressed within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
