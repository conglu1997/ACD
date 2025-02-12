import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            "plastic pollution in oceans",
            "soil contamination with heavy metals",
            "atmospheric carbon dioxide levels"
        ]
        organism_types = [
            "bacteria",
            "algae",
            "fungus"
        ]
        genetic_modifications = [
            "enhanced metabolic pathways",
            "novel enzyme production",
            "improved stress tolerance"
        ]
        
        tasks = [
            {
                "environmental_issue": random.choice(environmental_issues),
                "organism_type": random.choice(organism_types),
                "genetic_modification": random.choice(genetic_modifications)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical synthetic {t['organism_type']} to address the environmental issue of {t['environmental_issue']} using {t['genetic_modification']}. Then, analyze its potential ecological impact and ethical implications. Your response should include:

1. Organism Design (250-300 words):
   a) Describe the key features of your synthetic {t['organism_type']}, including its genetic modifications.
   b) Explain how the {t['genetic_modification']} enables the organism to address {t['environmental_issue']}.
   c) Discuss any safety mechanisms or controls built into the organism's design.

2. Environmental Remediation Mechanism (200-250 words):
   a) Explain in detail how your synthetic organism would function to remediate {t['environmental_issue']}.
   b) Discuss the expected efficiency and timeline of the remediation process.
   c) Compare your approach to existing solutions for this environmental issue.

3. Ecological Impact Assessment (200-250 words):
   a) Analyze potential positive and negative impacts of introducing your synthetic organism into the environment.
   b) Discuss possible interactions with existing ecosystems and biodiversity.
   c) Propose methods to monitor and control the organism's spread and activity.

4. Ethical Implications (200-250 words):
   a) Identify and discuss at least three ethical concerns raised by the use of this synthetic organism.
   b) Analyze the risks and benefits from different stakeholder perspectives (e.g., environmentalists, local communities, governments).
   c) Propose guidelines for responsible development and use of this technology.

5. Future Research and Development (150-200 words):
   a) Suggest two potential improvements or extensions to your synthetic organism.
   b) Discuss any technological barriers that need to be overcome.
   c) Propose a timeline for development, testing, and potential deployment of your solution.

Ensure your response demonstrates a deep understanding of synthetic biology, environmental science, and bioethics. Be creative in your approach while maintaining scientific plausibility. Use appropriate scientific terminology throughout your answer.

Format your response using the following structure:

1. Organism Design:
   [Your content here]

2. Environmental Remediation Mechanism:
   [Your content here]

3. Ecological Impact Assessment:
   [Your content here]

4. Ethical Implications:
   [Your content here]

5. Future Research and Development:
   [Your content here]

Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a synthetic {t['organism_type']} using {t['genetic_modification']} to address {t['environmental_issue']}",
            "The organism design should be scientifically plausible and clearly explained",
            "The environmental remediation mechanism must be thoroughly addressed",
            "The ecological impact assessment should consider both positive and negative effects",
            "Ethical implications must be thoughtfully considered from multiple perspectives",
            "The response should demonstrate interdisciplinary knowledge integration",
            "Future research directions should be relevant and well-justified",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1000-1250 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
