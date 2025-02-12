class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "documentation": """### Feature: User Authentication

#### Endpoint: POST /api/auth/login

- **Description**: Authenticates a user and returns a JWT token.
- **Request Body**:
  - **username**: string, required
  - **password**: string, required
- **Response**:
  - **200 OK**: {"token": "<JWT_TOKEN>"}
  - **401 Unauthorized**: {"error": "Invalid credentials"}

#### Endpoint: POST /api/auth/register

- **Description**: Registers a new user.
- **Request Body**:
  - **username**: string, required
  - **password**: string, required
  - **email**: string, required
- **Response**:
  - **201 Created**: {"message": "User registered successfully"}
  - **400 Bad Request**: {"error": "User already exists"}

"""},
            "2": {"task_type": "generate", "feature": "User Profile Management", "details": """Create technical documentation for a feature that allows users to manage their profiles. The feature should include endpoints for viewing the profile, updating profile information, and deleting the profile. Include request and response formats, and possible error messages. Additionally, specify any authentication requirements and potential error codes for each endpoint."""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following technical documentation and answer the questions below:\n\n{t['documentation']}\n\nQuestions:\n1. What is the purpose of the POST /api/auth/login endpoint?\n2. What are the required fields in the request body for the POST /api/auth/register endpoint?\n3. What response is returned when the user provides invalid credentials to the POST /api/auth/login endpoint?"""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate technical documentation for the following feature:\n\nFeature: {t['feature']}\n\nDetails: {t['details']}\n\nEnsure that your documentation includes a description of the feature, endpoints, request and response formats, authentication requirements, and possible error messages. Provide your documentation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The answers should accurately reflect the information in the documentation."]
        elif t['task_type'] == 'generate':
            criteria = ["The documentation should be clear, comprehensive, and cover all specified details."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
