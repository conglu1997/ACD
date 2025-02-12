import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Martian surface",
            "Deep sea hydrothermal vent",
            "Radioactive wasteland",
            "Extreme desert"
        ]
        target_organisms = [
            "Photosynthetic bacteria",
            "Extremophile fungi",
            "Genetically modified plants",
            "Synthetic microbial communities"
        ]
        ecological_goals = [
            "Oxygen production",
            "Soil formation",
            "Water cycle establishment",
            "Carbon sequestration"
        ]
        
        tasks = {}
        for i in range(2):
            environment = random.choice(environments)
            organism = random.choice(target_organisms)
            goal = random.choice(ecological_goals)
            
            tasks[str(i+1)] = {
                "environment": environment,
                "organism": organism,
                "goal": goal
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synthetic biology approach to terraforming a {t['environment']} using {t['organism']} with the primary ecological goal of {t['goal']}. Your response should include the following sections:

1. Synthetic Biology Design (300-350 words):
   a) Describe the key genetic modifications or synthetic pathways you would introduce to the {t['organism']}.
   b) Explain how these modifications enable the organism to survive in the {t['environment']}.
   c) Detail how the modified organism contributes to the goal of {t['goal']}.
   d) Discuss any novel synthetic biology techniques or tools you would use in this design.

2. Deployment and Ecological Succession (250-300 words):
   a) Outline a strategy for introducing the modified organisms into the {t['environment']}.
   b) Describe the expected stages of ecological succession following the introduction.
   c) Explain how you would monitor and manage the terraforming process over time.
   d) Discuss potential challenges and how you would address them.

3. Ecological Impact Analysis (250-300 words):
   a) Analyze the potential short-term and long-term impacts of your approach on the {t['environment']}.
   b) Discuss any potential unintended consequences and how you might mitigate them.
   c) Explain how your approach might affect any existing extremophile organisms in the environment.
   d) Evaluate the sustainability and resilience of the newly established ecosystem.

4. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of terraforming the {t['environment']}.
   b) Analyze the potential risks and benefits to human society and scientific knowledge.
   c) Consider the rights of any potential existing life forms in the environment.
   d) Propose guidelines for responsible terraforming practices.

5. Alternative Approaches (150-200 words):
   a) Briefly describe two alternative synthetic biology approaches to achieving the same goal.
   b) Compare these alternatives to your main approach in terms of efficiency, risk, and ethical implications.

6. Future Research Directions (150-200 words):
   a) Identify key areas where further research is needed to improve your terraforming approach.
   b) Propose a specific experiment or study to address one of these research needs.
   c) Speculate on potential applications of your synthetic biology approach beyond terraforming.

Ensure your response demonstrates a deep understanding of synthetic biology, ecology, and the specific challenges of the given environment. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of synthetic biology, ecology, and the specific challenges of the {t['environment']}",
            f"The proposed approach effectively uses {t['organism']} to achieve the goal of {t['goal']}",
            "The ecological impact analysis is comprehensive and considers potential unintended consequences",
            "The ethical implications are thoroughly discussed, including risks, benefits, and guidelines for responsible practices",
            "The response is creative and innovative while maintaining scientific plausibility",
            "The alternative approaches and future research directions are well-reasoned and relevant",
            "The response follows the required format and falls within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
