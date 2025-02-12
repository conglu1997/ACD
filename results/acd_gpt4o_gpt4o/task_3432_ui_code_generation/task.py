class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Create a simple login form with fields for username and password, a checkbox for 'Remember Me', and a submit button. The form should be centered on the page."},
            "2": {"prompt": "Create a responsive navigation bar with links to Home, About, Services, and Contact pages. The navigation bar should be styled with a background color and change color when a link is hovered over."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate HTML and CSS code based on the following user interface design prompt:

Prompt:
{t['prompt']}

Ensure that your code is syntactically correct and meets the requirements of the prompt. The code should be formatted correctly and provided in plain text format. Your solution must be a valid HTML document with a <style> tag for CSS."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The HTML and CSS code should be syntactically correct.",
            "The code should meet the requirements of the prompt.",
            "The design should be visually appealing and functional.",
            "The solution must be a valid HTML document with a <style> tag for CSS."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
