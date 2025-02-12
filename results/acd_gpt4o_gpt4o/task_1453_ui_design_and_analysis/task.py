class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "requirements": "Design a login page for a mobile banking app. The page should include fields for username and password, a 'Login' button, a 'Forgot Password' link, and a 'Sign Up' link. The design should be user-friendly and visually appealing."},
            "2": {"task_type": "analyze", "ui_design": "The login page includes a username field, a password field, a 'Login' button, a 'Forgot Password' link, and a 'Sign Up' link. The 'Login' button is prominently placed in the center, while the other links are smaller and placed below the input fields. The color scheme is blue and white, with a clean and simple layout."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Your task is to design a user interface (UI) for a login page based on the given requirements.

Requirements: {t['requirements']}

Instructions:
1. Create a detailed description of the UI design, including the layout, colors, and any other design elements.
2. Ensure that the design is user-friendly and visually appealing.
3. Explain why you chose the specific design elements and how they contribute to the user experience.

Your response should be structured as follows:
UI Design: [Your detailed description of the UI design]
Explanation: [Your explanation of the design choices and their impact on user experience]"""
        elif t['task_type'] == 'analyze':
            return f"""Your task is to analyze the given UI design and provide a detailed explanation of its components and their impact on user experience.

UI Design: {t['ui_design']}

Instructions:
1. Break down the UI design into its essential components.
2. Explain the purpose and usability of each component.
3. Discuss the overall effectiveness of the design and any potential improvements.

Your response should be structured as follows:
Components: [List of components]
Purpose and Usability: [Explanation of purpose and usability of each component]
Effectiveness: [Discussion of overall effectiveness and potential improvements]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generate':
            criteria = ["The design should include all required elements (username field, password field, 'Login' button, 'Forgot Password' link, 'Sign Up' link).", "The design should be user-friendly and visually appealing.", "The explanation should justify the design choices and their contribution to user experience."]
        elif t['task_type'] == 'analyze':
            criteria = ["The analysis should break down the UI design into essential components.", "The explanation should cover the purpose and usability of each component.", "The discussion should address the overall effectiveness and potential improvements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
