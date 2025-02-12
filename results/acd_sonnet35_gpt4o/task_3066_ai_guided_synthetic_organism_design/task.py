import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organisms = [
            {
                "organism_type": "bacteria",
                "desired_function": "bioremediation of plastic waste",
                "environmental_constraint": "marine ecosystems"
            },
            {
                "organism_type": "yeast",
                "desired_function": "production of novel pharmaceuticals",
                "environmental_constraint": "controlled laboratory settings"
            },
            {
                "organism_type": "algae",
                "desired_function": "enhanced carbon sequestration",
                "environmental_constraint": "freshwater ecosystems"
            },
            {
                "organism_type": "plant",
                "desired_function": "drought-resistant food production",
                "environmental_constraint": "arid climates"
            },
            {
                "organism_type": "fungus",
                "desired_function": "biodegradation of toxic waste",
                "environmental_constraint": "contaminated soil"
            },
            {
                "organism_type": "archaea",
                "desired_function": "methane production for biofuel",
                "environmental_constraint": "anaerobic digesters"
            }
        ]
        return {
            "1": random.choice(organisms),
            "2": random.choice(organisms)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system to guide the creation of a synthetic {t['organism_type']} with the function of {t['desired_function']}, optimized for {t['environmental_constraint']}. Then, analyze its potential applications, ethical implications, and biosafety considerations. Your response should include:\n\n1. AI System Architecture (250-300 words):\n   a) Describe the key components of your AI system for synthetic organism design.\n   b) Explain how your system integrates knowledge from biology, genetics, and environmental science.\n   c) Discuss any novel features or algorithms in your architecture specific to synthetic biology.\n   d) Provide a high-level diagram or detailed description of your AI system's structure.\n\n2. Synthetic Organism Design Process (200-250 words):\n   a) Outline the step-by-step process your AI system would follow to design the synthetic {t['organism_type']}.\n   b) Explain how the system would optimize the organism for its desired function and environmental constraints.\n   c) Discuss how your AI would predict and mitigate potential unintended consequences of the synthetic organism.\n\n3. Genetic Modifications and Pathways (150-200 words):\n   a) Propose specific genetic modifications or engineered pathways that your AI might suggest for the synthetic {t['organism_type']}.\n   b) Explain how these modifications contribute to the desired function of {t['desired_function']}.\n   c) Discuss any potential challenges in implementing these genetic changes and how your AI system would address them.\n\n4. Performance Analysis and Validation (200-250 words):\n   a) Describe how your AI system would predict and evaluate the performance of the synthetic organism.\n   b) Propose a set of in silico tests and simulations to validate the organism's function and safety.\n   c) Discuss how the AI would iterate and improve the design based on performance data.\n\n5. Applications and Implications (200-250 words):\n   a) Suggest two potential real-world applications for your synthetic {t['organism_type']} beyond its primary function.\n   b) Analyze how these applications might impact relevant industries or environmental conservation efforts.\n   c) Discuss any potential risks or unintended consequences of releasing this synthetic organism into {t['environmental_constraint']}.\n   d) Explain the trade-offs between the organism's designed function and its potential environmental impact.\n\n6. Biosafety and Containment (150-200 words):\n   a) Propose specific biosafety measures for handling and containing the synthetic organism.\n   b) Discuss potential risks of horizontal gene transfer or uncontrolled proliferation.\n   c) Describe how your AI system would incorporate biosafety considerations into the design process.\n\n7. Ethical Considerations and Governance (150-200 words):\n   a) Identify potential ethical issues or concerns raised by your AI-designed synthetic organism.\n   b) Propose a framework for responsible development and testing of AI-guided synthetic organisms.\n   c) Discuss the role of regulations and international cooperation in governing this technology.\n\n8. Future Research Directions (100-150 words):\n   a) Suggest areas for future research in AI-guided synthetic biology, building on your proposed system.\n   b) Discuss potential interdisciplinary collaborations that could advance this field.\n\nEnsure your response demonstrates a deep understanding of synthetic biology, artificial intelligence, bioethics, and biosafety. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and addressing real-world constraints.\n\nFormat your response using clear headings for each section. Your total response should be between 1400-1800 words. Include a word count at the end of your response.\n\nProvide a visual representation (described in text) of your AI system architecture in section 1.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response proposes an AI system to design a synthetic {t['organism_type']} for {t['desired_function']} in {t['environmental_constraint']}.",
            "The AI system architecture is well-explained and integrates knowledge from relevant fields, including a visual representation.",
            "The synthetic organism design process is detailed and addresses potential challenges.",
            "Specific genetic modifications are proposed and explained in relation to the desired function.",
            "The response includes a thorough analysis of applications, implications, and trade-offs between function and environmental impact.",
            "Biosafety considerations and containment measures are thoroughly discussed.",
            "The proposed framework for responsible development demonstrates an understanding of bioethics and governance.",
            "The response adheres to the specified word count range and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
