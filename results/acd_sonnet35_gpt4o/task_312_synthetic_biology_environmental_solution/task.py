import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            {
                "issue": "Plastic pollution in oceans",
                "target": "Microplastics",
                "ecosystem": "Marine"
            },
            {
                "issue": "Soil contamination",
                "target": "Heavy metals",
                "ecosystem": "Terrestrial"
            },
            {
                "issue": "Air pollution in urban areas",
                "target": "Particulate matter",
                "ecosystem": "Urban"
            },
            {
                "issue": "Eutrophication in freshwater systems",
                "target": "Excess nutrients",
                "ecosystem": "Freshwater"
            }
        ]
        return {
            "1": random.choice(environmental_issues),
            "2": random.choice(environmental_issues)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synthetic organism to address the environmental issue of {t['issue']} by targeting {t['target']} in a {t['ecosystem']} ecosystem. Your task is to create an innovative solution using synthetic biology principles and analyze its potential impacts and implementation challenges. Provide your response in the following format:

1. Organism Design (250-300 words):
   a) Describe the synthetic organism you propose, including its basic biological characteristics.
   b) Explain the key genetic modifications or synthetic pathways you would engineer into the organism.
   c) Detail how the organism would target and remediate {t['target']}.
   d) Discuss any safety mechanisms or controls built into the organism's design.

2. Environmental Impact (200-250 words):
   a) Analyze the potential positive effects of your synthetic organism on the {t['ecosystem']} ecosystem.
   b) Discuss possible negative consequences or risks, including unintended ecological interactions.
   c) Propose a monitoring system to track the organism's effectiveness and environmental impact.

3. Implementation Strategy (200-250 words):
   a) Outline a plan for testing and gradually introducing the synthetic organism into the target environment.
   b) Discuss potential regulatory hurdles and how you would address them.
   c) Propose a containment strategy to prevent uncontrolled spread of the organism.

4. Ethical Analysis (150-200 words):
   a) Identify three major ethical concerns raised by your synthetic biology solution.
   b) Analyze these concerns using one ethical framework (e.g., utilitarianism, deontology, virtue ethics).
   c) Suggest ways to address one of the ethical concerns.

5. Interdisciplinary Collaboration (150-200 words):
   a) Identify three key disciplines or fields of expertise needed for this project.
   b) Explain the role of each discipline in the development and implementation of your solution.
   c) Discuss potential challenges in integrating these diverse fields and how you would address them.

Ensure your response demonstrates a deep understanding of synthetic biology, environmental science, and ethical reasoning. Be creative in your approach while maintaining scientific plausibility and addressing potential risks and challenges."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The synthetic organism is designed to specifically address {t['issue']} by targeting {t['target']} in a {t['ecosystem']} ecosystem",
            "The response includes a detailed description of the organism's design, including genetic modifications and safety mechanisms",
            "The environmental impact analysis covers both positive effects and potential risks",
            "The implementation strategy addresses testing, regulatory issues, and containment",
            "The ethical analysis identifies and examines relevant concerns",
            "The interdisciplinary collaboration section identifies relevant fields and discusses integration challenges",
            "The overall response demonstrates creativity, scientific plausibility, and comprehensive problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
