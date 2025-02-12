class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Design a login page for a mobile app. The page should include fields for username and password, a 'Login' button, a 'Forgot Password' link, and a logo at the top. The design should be user-friendly and visually appealing. Provide a detailed textual description of the layout and elements, and explain why your design choices enhance the user experience."
            },
            "2": {
                "description": "Design a homepage for an e-commerce website. The page should include a search bar, categories menu, featured products section, and a shopping cart icon. The design should be intuitive and facilitate easy navigation. Provide a detailed textual description of the layout and elements, and explain why your design choices improve usability and engagement."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a user interface based on the following description. Provide a clear and detailed textual description of the layout and elements. Additionally, explain why your design choices enhance the user experience.\n\nDescription:\n{t['description']}\n\nFormat your response as follows:\n1. Layout Description: [Provide a detailed description of the layout and elements]\n2. Design Rationale: [Explain why your design choices enhance UX and usability]\n\nExample Response:\n1. Layout Description: The login page includes a logo at the top center, below which are the username and password fields aligned vertically. Below the password field, there is a 'Login' button centered, followed by a 'Forgot Password' link at the bottom. The design uses a minimalist style with a focus on ease of use.\n2. Design Rationale: The centered layout ensures that the user's focus is directed towards the login fields. The minimalist style reduces clutter and enhances usability, making it easy for users to log in quickly. The 'Forgot Password' link is placed at the bottom for easy access without distracting from the primary login action."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The layout description should be clear and detailed.",
            "The design rationale should explain how the design enhances UX and usability.",
            "The design should be user-friendly and visually appealing.",
            "The design should meet the specified requirements and constraints.",
            "The response should be coherent and logically consistent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
