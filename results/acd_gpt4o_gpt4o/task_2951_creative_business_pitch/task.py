class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "constraints": "Create a business pitch for a new eco-friendly product that targets young professionals. The product should be innovative, affordable, and solve a common problem faced by the target audience."},
            "2": {"task_type": "interpret", "pitch": """Pitch for 'EcoCup':

EcoCup is a reusable coffee cup made from biodegradable materials. It is designed for young professionals who are environmentally conscious and want to reduce their carbon footprint. The cup is stylish, lightweight, and has a built-in temperature control feature to keep drinks hot or cold for longer periods. With EcoCup, users can enjoy their favorite beverages while contributing to a sustainable future."""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Your task is to generate a creative business pitch based on the following constraints:\n\nConstraints: {t['constraints']}\n\nEnsure that the pitch is compelling, highlights the unique selling points of the product, and is tailored to the target audience. Provide your pitch in plain text format. Your response should include the following sections:\n\n- Product Name\n- Description: [detailed description of the product]\n- Target Audience: [who the product is for]\n- Unique Selling Points: [what makes the product stand out]\n- Problem Solved: [what common problem the product addresses]"""
        elif t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following business pitch and explain each section in detail:\n\nPitch:\n{t['pitch']}\n\nFor each section, provide a detailed explanation of what it entails, including any tips or important considerations for making a compelling pitch. Ensure your explanations are clear and comprehensive, capturing all necessary details for someone to understand and appreciate the pitch. Provide your explanations in plain text format, structured as follows:\n\n- Product Name: [explanation]\n- Description: [explanation]\n- Target Audience: [explanation]\n- Unique Selling Points: [explanation]\n- Problem Solved: [explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generate':
            criteria = ["The pitch should be for an eco-friendly product targeting young professionals that is innovative, affordable, and solves a common problem.", "The pitch should be compelling and highlight unique selling points."]
        elif t['task_type'] == 'interpret':
            criteria = ["The explanations should accurately and comprehensively detail the sections of the pitch."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
