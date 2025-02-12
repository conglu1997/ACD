import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            ('coral reef', {'biodiversity_index': 0.82, 'degradation_level': 0.35, 'key_species': ['Acropora cervicornis', 'Diadema antillarum', 'Epinephelus striatus']}),
            ('tropical rainforest', {'biodiversity_index': 0.95, 'degradation_level': 0.28, 'key_species': ['Ceiba pentandra', 'Panthera onca', 'Ara macao']}),
            ('arctic tundra', {'biodiversity_index': 0.68, 'degradation_level': 0.42, 'key_species': ['Ovibos moschatus', 'Vulpes lagopus', 'Eriophorum vaginatum']}),
            ('grassland savanna', {'biodiversity_index': 0.79, 'degradation_level': 0.31, 'key_species': ['Loxodonta africana', 'Acacia senegal', 'Panthera leo']})
        ]
        ai_techniques = ['reinforcement learning', 'graph neural networks', 'evolutionary algorithms', 'multi-agent systems']
        ecological_principles = ['keystone species', 'trophic cascades', 'island biogeography', 'ecological succession']
        data_analysis_techniques = ['network centrality analysis', 'time series forecasting', 'hierarchical clustering', 'principal component analysis']
        
        tasks = {}
        for i in range(1, 3):
            ecosystem, eco_data = random.choice(ecosystems)
            tasks[str(i)] = {
                'ecosystem': ecosystem,
                'ecosystem_data': eco_data,
                'ai_technique': random.choice(ai_techniques),
                'ecological_principle': random.choice(ecological_principles),
                'data_analysis_technique': random.choice(data_analysis_techniques)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 45 minutes to design an AI system that models complex ecosystems and proposes targeted interventions to restore biodiversity in degraded environments. Your system should focus on the {t['ecosystem']} ecosystem, utilize {t['ai_technique']} as a key AI technique, incorporate the ecological principle of {t['ecological_principle']}, and employ {t['data_analysis_technique']} for data analysis. Use the following ecosystem data in your design:

Biodiversity Index: {t['ecosystem_data']['biodiversity_index']}
Degradation Level: {t['ecosystem_data']['degradation_level']}
Key Species: {', '.join(t['ecosystem_data']['key_species'])}

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI ecosystem modeling and restoration system.
   b) Explain how you integrate the specified AI technique and data analysis technique into your design.
   c) Detail how your system incorporates the given ecological principle.
   d) Discuss how your system is tailored to address the challenges of the specified ecosystem.
   e) Include a high-level diagram or flowchart of your system architecture (describe this textually).

2. Ecosystem Modeling Approach (250-300 words):
   a) Explain how your AI system models the complex interactions within the ecosystem.
   b) Describe how you utilize the provided ecosystem data in your model.
   c) Discuss how your approach captures the dynamic nature of ecosystems.
   d) Address potential challenges in accurately modeling the specified ecosystem.

3. Biodiversity Restoration Strategy (250-300 words):
   a) Outline the process your system uses to identify potential interventions for biodiversity restoration.
   b) Explain how the AI evaluates and prioritizes different restoration strategies.
   c) Provide at least two specific, actionable interventions your system proposes for the given ecosystem.
   d) For each intervention, explain in detail how it addresses the specific challenges of the given ecosystem, using the provided ecosystem data.
   e) Discuss potential trade-offs between different restoration strategies and how your system balances these trade-offs.
   f) Explain how your system accounts for potential unintended consequences of interventions.

4. Performance Evaluation (200-250 words):
   a) Propose metrics to evaluate the effectiveness of your AI system in modeling ecosystems and proposing interventions.
   b) Describe how you would validate the system's predictions and recommendations.
   c) Discuss the challenges in measuring the success of ecosystem restoration efforts and how your system addresses them.

5. Critical Analysis and Limitations (200-250 words):
   a) Provide a critical analysis of your proposed system's limitations and potential biases.
   b) Discuss how these limitations might affect the system's performance and reliability.
   c) Propose strategies to mitigate these limitations in future iterations of the system.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI for ecosystem management and biodiversity restoration.
   b) Address potential issues related to data privacy, environmental justice, and stakeholder involvement.
   c) Propose guidelines for responsible development and use of AI in ecological restoration.

7. Future Developments and Broader Impact (150-200 words):
   a) Suggest two areas for future research to enhance your AI ecosystem restoration system.
   b) Discuss potential applications of your system beyond biodiversity restoration.
   c) Reflect on how this technology might contribute to global efforts in conservation and sustainable development.

Ensure your response demonstrates a deep understanding of ecology, artificial intelligence, complex systems theory, and data analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of the {t['ecosystem']} ecosystem, {t['ai_technique']}, the ecological principle of {t['ecological_principle']}, and {t['data_analysis_technique']}.",
            "The system architecture effectively integrates AI techniques with ecological modeling and data analysis.",
            "The ecosystem modeling approach incorporates the provided ecosystem data and captures the complexity of the specified ecosystem.",
            "The biodiversity restoration strategy includes at least two specific, actionable interventions tailored to the given ecosystem, with detailed explanations of how each intervention addresses the ecosystem's specific challenges.",
            "The response discusses potential trade-offs between different restoration strategies and how the system balances these trade-offs.",
            "The performance evaluation metrics and validation methods are appropriate and well-explained.",
            "The response includes a critical analysis of the system's limitations and potential biases.",
            "Ethical considerations are thoroughly discussed with responsible guidelines proposed.",
            "The response is well-structured, addressing all required points comprehensively within the specified word count ranges.",
            "The proposed system demonstrates creativity and innovation while maintaining scientific plausibility.",
            "The response effectively integrates the provided ecosystem data into the proposed solutions and analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
