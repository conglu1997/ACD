import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nanomaterials = [
            "Carbon nanotubes",
            "Graphene oxide",
            "Titanium dioxide nanoparticles",
            "Iron oxide nanoparticles"
        ]
        removal_mechanisms = [
            "Adsorption",
            "Photocatalytic degradation",
            "Magnetic separation",
            "Biocatalytic breakdown"
        ]
        ecological_factors = [
            "Impact on marine food chains",
            "Bioaccumulation in organisms",
            "Changes in water chemistry",
            "Effects on microbial communities"
        ]
        
        tasks = {}
        for i in range(1, 3):
            material = random.choice(nanomaterials)
            mechanism = random.choice(removal_mechanisms)
            factor = random.choice(ecological_factors)
            tasks[str(i)] = {"material": material, "mechanism": mechanism, "factor": factor}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a nanotechnology-based system for environmental remediation of microplastics in oceans using {t['material']} and the {t['mechanism']} process. Then, analyze its potential ecological impact, focusing on {t['factor']}. Your response should include:\n\n1. System Design (300-350 words):\n   a) Describe the key components and mechanisms of your nanotechnology-based remediation system.\n   b) Explain how it incorporates {t['material']} and utilizes the {t['mechanism']} process.\n   c) Detail how the system targets and removes microplastics from ocean environments.\n   d) Provide a diagram or schematic representation of your system's structure and processes.\n\n2. Nanomaterial Properties and Interactions (250-300 words):\n   a) Analyze the specific properties of {t['material']} that make it suitable for this application.\n   b) Discuss potential interactions between the nanomaterial and microplastics.\n   c) Explain any modifications or functionalization of the nanomaterial to enhance its performance.\n\n3. Removal Mechanism Analysis (250-300 words):\n   a) Provide a detailed explanation of how the {t['mechanism']} process works in your system.\n   b) Discuss the efficiency and scalability of this mechanism for ocean-wide application.\n   c) Address any potential limitations or challenges of using this mechanism in marine environments.\n\n4. Ecological Impact Assessment (300-350 words):\n   a) Analyze the potential effects of your system on {t['factor']}.\n   b) Discuss both positive and negative potential impacts on marine ecosystems.\n   c) Propose methods to mitigate any adverse effects identified.\n   d) Compare the ecological impact of your system to current microplastic remediation methods.\n\n5. Implementation and Scalability (200-250 words):\n   a) Propose a strategy for deploying your system on a large scale in ocean environments.\n   b) Discuss logistical challenges and potential solutions for widespread implementation.\n   c) Analyze the cost-effectiveness and long-term sustainability of your approach.\n\n6. Future Directions and Ethical Considerations (150-200 words):\n   a) Suggest two potential improvements or extensions of your system for future development.\n   b) Discuss ethical implications of using nanotechnology for environmental remediation.\n   c) Propose guidelines for responsible development and use of such systems.\n\nEnsure your response demonstrates a deep understanding of nanotechnology, environmental science, and marine ecology. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing real-world environmental challenges.\n\nFormat your response using clear headings for each section. Your total response should be between 1450-1750 words.\n\nExample: When discussing the removal mechanism, you might explain how adsorption works at the nanoscale, or how photocatalytic degradation breaks down microplastics into harmless components. For ecological impact, consider how the introduction of nanomaterials might affect plankton populations or bioaccumulation in larger marine organisms."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of nanotechnology, environmental science, and marine ecology",
            "The system design is innovative, scientifically plausible, and addresses the specific task requirements",
            "The analysis of nanomaterial properties, removal mechanisms, and ecological impacts is thorough and insightful",
            "The implementation strategy and future directions are well-reasoned and practical",
            "The response includes all required sections with appropriate length and detail",
            "The proposed system effectively balances technological innovation with ecological considerations",
            "The response uses appropriate technical terminology from all relevant fields"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
