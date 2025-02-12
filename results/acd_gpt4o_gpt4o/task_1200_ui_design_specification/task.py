class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Create a login page for a mobile app. The page should include: 1) A field for the username, 2) A field for the password, 3) A 'Login' button, 4) A 'Forgot Password?' link, 5) The app's logo at the top, 6) A 'Sign Up' button, 7) Remember Me checkbox."
            },
            "2": {
                "requirements": "Design a dashboard interface for a project management tool. The dashboard should include: 1) A sidebar with navigation links (Home, Projects, Teams, Settings), 2) A main area displaying a list of projects with their statuses, 3) A 'Create New Project' button, 4) A search bar at the top, 5) A user profile section with a dropdown menu, 6) Notification icons."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed textual specification for a user interface based on the given requirements. Ensure that your specification is clear, comprehensive, and logically organized.

Requirements:\n{t['requirements']}\n
Your response should include:\n1. A description of the layout and positioning of each element.\n2. The visual appearance of each element (e.g., size, color, font).\n3. Any interactions or behaviors (e.g., button click actions).\n4. Any additional design considerations (e.g., accessibility, responsiveness).\n
Provide your specification in plain text format, ensuring it is well-structured and detailed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a comprehensive layout description.",
            "The visual appearance of each element should be clearly described.",
            "Any interactions or behaviors should be detailed.",
            "The response should be well-structured and logically organized.",
            "The response should include any additional design considerations such as accessibility and responsiveness."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
