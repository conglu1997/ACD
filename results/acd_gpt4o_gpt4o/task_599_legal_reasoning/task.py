class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"case_law": "In the case of Smith v. Jones, the court held that a contract is void if entered into under duress.", "scenario": "John signed a contract to sell his car to Mike after Mike threatened to harm him if he did not agree. Additionally, John was under significant financial stress at the time. Argue whether the contract is valid based on the given case law."},
            "2": {"statute": "Under the Employment Rights Act, an employee is entitled to a minimum of 20 days of paid leave per year.", "scenario": "Emily, an employee at Company X, has been denied her annual leave for two consecutive years. Despite her repeated requests, the company has refused to grant her leave, citing staffing issues. Argue whether she has a legal claim based on the given statute."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "case_law" in t:
            instructions = f"""Your task is to interpret the following case law and generate a legal argument based on the given scenario:\n\nCase Law: {t['case_law']}\nScenario: {t['scenario']}\n\nProvide a detailed legal argument, ensuring that your response correctly applies the principles from the case law to the scenario. Use clear and precise legal language."""
        else:
            instructions = f"""Your task is to interpret the following statute and generate a legal argument based on the given scenario:\n\nStatute: {t['statute']}\nScenario: {t['scenario']}\n\nProvide a detailed legal argument, ensuring that your response correctly applies the principles from the statute to the scenario. Use clear and precise legal language."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The legal argument should accurately apply the principles from the case law or statute to the scenario.",
            "The argument should be clear, logical, and use precise legal language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
