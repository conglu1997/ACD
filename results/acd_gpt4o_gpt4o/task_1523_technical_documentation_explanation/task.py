class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "technical_documentation": "You are provided with a brief technical summary of a computer network system. The system includes several components such as switches, routers, firewalls, servers, and load balancers. Your task is to explain how data flows from a user's computer to a web server, including the roles of each component in the network."
            },
            "2": {
                "technical_documentation": "You are given a technical description of an internal combustion engine. The description includes various parts such as the piston, crankshaft, valves, spark plug, fuel injectors, and the timing belt. Your task is to explain the process of how fuel is converted into mechanical energy, detailing the function of each part in the engine."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        technical_documentation = t["technical_documentation"]
        instructions = f"""Your task is to read the following technical documentation and explain the described system or concept in a clear and concise manner.

Technical Documentation: {technical_documentation}

Provide your explanation in plain text format. Ensure that your explanation is accurate, detailed, and easy to understand. Your response should effectively simplify the complex technical information provided.

Your response should be structured as follows:
- Introduction: [Brief introduction to the system or concept]
- Components: [Detailed explanation of each component]
- Process: [Step-by-step explanation of the process or data flow]
- Conclusion: [Summary of the explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be accurate and detailed.",
            "The explanation should be easy to understand.",
            "The explanation should effectively simplify the complex technical information.",
            "The response should be well-structured, following the given format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
