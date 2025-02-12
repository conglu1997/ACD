class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "civilization": "Ancient Maya",
                "time_period": "Classical Period (250-900 CE)",
                "key_aspects": ["urban development", "agricultural practices", "trade networks", "political structure", "religious beliefs"],
                "archaeological_data": {
                    "urban_centers": ["Tikal", "Calakmul", "Copan"],
                    "agricultural_findings": ["raised fields", "terraced hillsides", "evidence of intensive maize cultivation"],
                    "trade_artifacts": ["jade ornaments", "obsidian tools", "cacao residues"],
                    "political_structures": ["hieroglyphic texts mentioning divine kingship", "palace complexes", "stelae with royal proclamations"],
                    "religious_artifacts": ["pyramid temples", "ritual caches", "carved altars"]
                },
                "contradictory_finding": "Recent excavations have uncovered evidence suggesting extensive use of wheeled transportation, contradicting the long-held belief that the Maya did not use the wheel for practical purposes.",
                "quantitative_data": {
                    "urban_population_density": [100, 150, 200, 250, 300, 350, 400, 450],
                    "agricultural_yield": [1000, 1200, 1100, 1300, 1500, 1400, 1600, 1800],
                    "years": [250, 350, 450, 550, 650, 750, 850, 900]
                }
            },
            "2": {
                "civilization": "Indus Valley Civilization",
                "time_period": "Mature Harappan period (2600-1900 BCE)",
                "key_aspects": ["city planning", "water management", "craft production", "social organization", "writing system"],
                "archaeological_data": {
                    "urban_layout": ["grid pattern streets", "standardized brick sizes", "great bath at Mohenjo-daro"],
                    "water_systems": ["covered drains", "wells", "sophisticated sewage systems"],
                    "crafts": ["seals with animal motifs", "glazed faience beads", "copper and bronze tools"],
                    "social_indicators": ["absence of monumental structures", "standardized weights and measures", "lack of evidence for extreme social stratification"],
                    "writing_samples": ["Indus script on seals and pottery", "signboards", "copper tablets"]
                },
                "contradictory_finding": "New analysis of Indus script samples suggests a hierarchical social structure with clear evidence of royalty, challenging the prevailing theory of a relatively egalitarian society.",
                "quantitative_data": {
                    "city_size": [50, 75, 100, 125, 150, 175, 200, 225],
                    "trade_volume": [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],
                    "years": [2600, 2450, 2300, 2150, 2000, 1950, 1925, 1900]
                }
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes archaeological data to reconstruct and simulate the development of the {t['civilization']} during the {t['time_period']}, focusing on the following key aspects: {', '.join(t['key_aspects'])}. Your system should incorporate principles from machine learning, data analysis, and archaeological theory.

Use the following archaeological data in your analysis:
{', '.join([f'{k}: {v}' for k, v in t['archaeological_data'].items()])}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Overall structure and components of your AI system
   b) Integration of different AI techniques
   c) Handling and processing of various types of archaeological data
   d) Proposal of a novel AI technique or algorithm specifically tailored for archaeological data analysis

2. Data Analysis and Interpretation (250-300 words):
   a) Analysis and interpretation of the provided archaeological data
   b) Novel algorithms or approaches developed for this purpose
   c) Handling of uncertainties and gaps in the archaeological record
   d) Quantitative analysis of the provided time series data:
      {', '.join([f'{k}: {v}' for k, v in t['quantitative_data'].items()])}
      Describe how your AI system would analyze this data to identify trends and make predictions about the civilization's development.

3. Civilization Simulation (250-300 words):
   a) Simulation of the civilization's development over time
   b) Modeling of interactions between different aspects of the civilization
   c) Generation and testing of hypotheses about the civilization's development
   d) Integration of quantitative analysis results into the simulation model

4. Archaeological Theory Integration (250-300 words):
   a) Incorporation of established archaeological theories and methodologies
   b) Balancing of computational analysis with traditional archaeological interpretation
   c) Comparison and contrast of your AI system's approach with traditional archaeological methods
   d) Addressing the following contradictory finding: {t['contradictory_finding']}
      Explain how your AI system would handle this situation and potentially revise existing theories.

5. Visualization and Interaction (200-250 words):
   a) Presentation of findings and simulations to users
   b) Interactive features for exploring different scenarios or hypotheses
   c) Use of visualizations for public engagement and education
   d) Innovative ways to visualize the quantitative data and its implications

6. Ethical Considerations and Limitations (200-250 words):
   a) Ethical issues in using AI to interpret cultural heritage
   b) Respect for and incorporation of indigenous knowledge and perspectives
   c) Limitations of the AI system and how these are communicated to users
   d) Potential biases in the AI system and strategies to mitigate them

Ensure your response demonstrates a deep understanding of both AI techniques and archaeological practices. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from both fields and provide clear explanations for complex concepts.

Your total response should be between 1450-1750 words. Format your response with clear headings for each section, and number your paragraphs within each section for clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of AI techniques and archaeological practices, particularly as they relate to the {t['civilization']} during the {t['time_period']}.",
            "The proposed AI system architecture is innovative, well-structured, and effectively integrates various AI techniques for archaeological data analysis.",
            "The response includes a novel AI technique or algorithm specifically tailored for archaeological data analysis, with a clear explanation of its functionality and potential benefits.",
            f"The system's approach to data analysis, interpretation, and civilization simulation addresses all the key aspects mentioned: {', '.join(t['key_aspects'])}.",
            f"The response effectively incorporates and analyzes the provided archaeological data: {', '.join([f'{k}: {v}' for k, v in t['archaeological_data'].items()])}.",
            "The quantitative analysis of the time series data is thorough and demonstrates the AI system's capability to identify trends and make predictions.",
            "The response shows a thoughtful integration of archaeological theory with AI-driven analysis, including a detailed comparison with traditional archaeological methods.",
            f"The response adequately addresses the contradictory finding: {t['contradictory_finding']}, explaining how the AI system would handle this situation and potentially revise existing theories.",
            "The visualization and interaction features of the system are innovative, well-designed, and would be useful for both professional archaeologists and public engagement.",
            "Ethical considerations, including respect for indigenous knowledge, are thoroughly addressed, and limitations and potential biases of the AI system are clearly explained with mitigation strategies.",
            "The response is well-structured, adheres to the word count guidelines, and consistently uses appropriate terminology from both AI and archaeology fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
