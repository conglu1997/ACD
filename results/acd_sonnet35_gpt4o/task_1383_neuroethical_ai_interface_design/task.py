import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            "memory enhancement",
            "emotion regulation",
            "direct brain-to-brain communication",
            "motor control for prosthetics",
            "accelerated learning",
            "dream manipulation",
            "cognitive performance optimization"
        ]
        target_populations = [
            "general public",
            "military personnel",
            "individuals with neurological disorders",
            "children with learning disabilities",
            "elderly with cognitive decline",
            "high-performance athletes",
            "space explorers"
        ]
        return {
            "1": {
                "application": random.choice(applications),
                "target_population": random.choice(target_populations)
            },
            "2": {
                "application": random.choice(applications),
                "target_population": random.choice(target_populations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system that integrates artificial intelligence for {t['application']}, targeted at {t['target_population']}. Then, analyze its ethical implications, propose governance frameworks, and design an experiment to test its efficacy and safety. Your response should include:

1. BCI System Design (250-300 words):
   a) Describe the key components and functioning of your BCI system.
   b) Explain how AI is integrated into the system and its role in {t['application']}.
   c) Discuss the neuroscientific principles underlying your design.
   d) Address specific considerations for {t['target_population']}.

2. Technical Challenges and Solutions (150-200 words):
   a) Identify at least three major technical challenges in implementing your BCI system.
   b) Propose innovative solutions to these challenges.
   c) Discuss any trade-offs or limitations in your proposed solutions.

3. Ethical Analysis (200-250 words):
   a) Analyze potential ethical issues arising from your BCI system, considering both individual and societal impacts.
   b) Discuss how your system might affect concepts of privacy, autonomy, and human identity.
   c) Consider potential dual-use concerns and unintended consequences.
   d) Address specific ethical considerations for {t['target_population']}.

4. Governance Framework (150-200 words):
   a) Propose a comprehensive governance framework for the development, testing, and deployment of your BCI system.
   b) Suggest specific policies or regulations to address the ethical issues identified.
   c) Discuss the roles of different stakeholders (e.g., researchers, companies, government, users) in this framework.

5. Experimental Design (200-250 words):
   a) Propose a detailed experiment to test the efficacy and safety of your BCI system.
   b) Describe the methodology, including participant selection, control groups, and measurement techniques.
   c) Discuss how you would address ethical concerns in your experimental design.
   d) Explain how you would measure both intended outcomes and potential side effects.

6. Societal Implications (100-150 words):
   a) Analyze potential long-term societal impacts of widespread adoption of your BCI system.
   b) Discuss how it might influence social structures, economic systems, or human evolution.
   c) Consider both utopian and dystopian scenarios.

7. Future Research Directions (100-150 words):
   a) Suggest two key areas for further research to advance BCI technology ethically and responsibly.
   b) Explain how these research directions could address current limitations or ethical concerns.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, ethics, policy-making, and scientific methodology. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your design while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of BCI technology and AI integration for {t['application']}.",
            f"The BCI system design addresses specific considerations for {t['target_population']}.",
            "The ethical analysis is comprehensive and considers both individual and societal impacts.",
            "The proposed governance framework is well-structured and addresses key ethical issues.",
            "The experimental design is scientifically sound and addresses both efficacy and safety concerns.",
            "The response shows innovative thinking while maintaining scientific and ethical plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
