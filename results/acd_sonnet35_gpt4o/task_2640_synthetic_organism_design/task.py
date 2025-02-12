import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            {
                "name": "Bioremediation",
                "target": "Heavy metal contamination",
                "environment": "Polluted soil"
            },
            {
                "name": "Medical therapy",
                "target": "Cancer cells",
                "environment": "Human body"
            },
            {
                "name": "Biofuel production",
                "target": "Cellulose",
                "environment": "Industrial bioreactor"
            },
            {
                "name": "Biosensing",
                "target": "Pathogenic bacteria",
                "environment": "Food supply chain"
            }
        ]
        return {
            "1": random.choice(applications),
            "2": random.choice(applications)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synthetic organism for the application of {t['name']}, specifically targeting {t['target']} in the environment of {t['environment']}. Your response should include:

1. Organism Design (200-250 words):
   a) Describe the base organism you're using and why you chose it.
   b) Explain the genetic modifications you're introducing.
   c) Detail the synthetic pathways or circuits you're engineering.
   d) Discuss how these modifications enable the organism to perform its intended function.

2. Functional Analysis (200-250 words):
   a) Explain how your synthetic organism interacts with its target in the specified environment.
   b) Provide a quantitative estimate of its efficiency or effectiveness.
   c) Discuss any potential side effects or unintended consequences.
   d) Propose a method for controlling or limiting the organism's activity.

3. Ecological Impact (150-200 words):
   a) Analyze potential unintended ecological impacts of your synthetic organism.
   b) Discuss how these impacts might cascade through the ecosystem.
   c) Propose strategies to monitor and mitigate these potential impacts.

4. Biosafety and Biocontainment (150-200 words):
   a) Describe the biosafety level required for working with your organism.
   b) Explain the biocontainment strategies you've implemented.
   c) Discuss potential risks of environmental release and how they're mitigated.

5. Comparative Analysis (200-250 words):
   a) Compare your synthetic organism to existing solutions or technologies for the same application.
   b) Analyze the advantages and disadvantages of your approach.
   c) Discuss any synergies or conflicts with existing methods.

6. Testing Protocol (150-200 words):
   a) Propose a comprehensive testing protocol for your synthetic organism.
   b) Include safety assessments, efficacy tests, and long-term monitoring strategies.
   c) Discuss how you would validate the organism's performance and safety in controlled and real-world conditions.

7. Ethical Implications (150-200 words):
   a) Analyze the ethical considerations of creating and using this synthetic organism.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of this technology.

8. Regulatory Framework (100-150 words):
   a) Discuss how existing regulations would apply to your synthetic organism.
   b) Propose any new regulations that might be necessary.
   c) Consider international implications and propose a framework for global governance.

9. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions of your synthetic organism.
   b) Discuss how this technology might evolve over the next decade.
   c) Propose a related research direction that could advance the field of synthetic biology.

Ensure your response demonstrates a deep understanding of synthetic biology, systems thinking, and ethical reasoning. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Include at least two relevant scientific citations in your response, using a consistent citation format.

Format your response with clear headings for each section. Your total response should be between 1400-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The synthetic organism design is innovative, well-reasoned, and scientifically plausible, with clear explanations of genetic modifications and synthetic pathways.",
            "The functional analysis includes specific, quantitative estimates of efficiency and a thorough discussion of potential side effects and control methods.",
            "The ecological impact analysis demonstrates a deep understanding of ecosystem interactions and proposes concrete monitoring and mitigation strategies.",
            "Biosafety and biocontainment strategies are thoroughly explained, appropriate for the organism, and consider multiple risk scenarios.",
            "The comparative analysis provides a balanced, insightful comparison with existing solutions, clearly articulating advantages and disadvantages.",
            "The proposed testing protocol is comprehensive, addressing safety, efficacy, and long-term monitoring in both controlled and real-world conditions.",
            "The ethical analysis is nuanced, considering multiple perspectives and potential impacts, with well-reasoned guidelines for responsible development.",
            "The regulatory framework discussion shows a clear understanding of existing regulations and proposes thoughtful additions for global governance.",
            "Future directions and improvements are innovative and demonstrate foresight in the field of synthetic biology.",
            "The response includes at least two relevant, properly formatted scientific citations.",
            "The overall response is well-structured, clear, and demonstrates strong interdisciplinary reasoning and deep understanding of synthetic biology principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
