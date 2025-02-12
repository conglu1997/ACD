class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_description": "Write a step-by-step tutorial on how to implement a basic RESTful API in Python using Flask.",
                "instructions": "Generate a step-by-step tutorial on how to implement a basic RESTful API in Python using the Flask framework. Ensure that the tutorial includes the following components: 1. Introduction to RESTful APIs and Flask. 2. Installation and setup instructions. 3. Code examples with explanations for creating endpoints (GET, POST, PUT, DELETE). 4. Running the server and testing the API. Submit your tutorial as a plain text string in the following format:\n\nIntroduction:\n[Your introduction]\n\nInstallation and Setup:\n[Installation instructions]\n\nCode Examples:\n[Code examples with explanations]\n\nRunning and Testing:\n[Running and testing instructions]\n"
            },
            "2": {
                "task_description": "Write a step-by-step tutorial on how to create a simple web scraper in Python using BeautifulSoup.",
                "instructions": "Generate a step-by-step tutorial on how to create a simple web scraper in Python using the BeautifulSoup library. Ensure that the tutorial includes the following components: 1. Introduction to web scraping and BeautifulSoup. 2. Installation and setup instructions. 3. Code examples with explanations for fetching and parsing HTML content. 4. Extracting specific elements from a webpage. Submit your tutorial as a plain text string in the following format:\n\nIntroduction:\n[Your introduction]\n\nInstallation and Setup:\n[Installation instructions]\n\nCode Examples:\n[Code examples with explanations]\n\nExtracting Elements:\n[Instructions for extracting elements]\n"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a step-by-step tutorial on the following programming task: {t['task_description']}. Ensure that the tutorial includes the specified components. Here are the detailed instructions:\n\n{t['instructions']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The tutorial should be clear and logically structured.",
            "The tutorial should accurately cover the specified components.",
            "The code examples should be correct and functional."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
