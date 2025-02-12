class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A government is proposing a policy to implement universal basic income (UBI) to address poverty and unemployment. Critics argue that UBI would disincentivize work and lead to inflation. Supporters claim it would provide a safety net, reduce poverty, and stimulate economic growth by increasing consumer spending. Additionally, proponents argue that it could streamline welfare programs and reduce administrative costs.",
                "perspective": "Support the implementation of UBI"
            },
            "2": {
                "scenario": "A country is debating whether to implement stricter immigration controls. Proponents argue that it is necessary for national security, preserving cultural identity, and protecting jobs for citizens. Opponents claim it is inhumane, that immigrants contribute positively to society and the economy, and that diversity strengthens social fabric. Furthermore, they argue that strict controls could lead to labor shortages and harm industries that rely on immigrant workers.",
                "perspective": "Oppose stricter immigration controls"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following socio-political scenario and construct an argument based on the given perspective. Your argument should include:

1. A summary of the scenario.
2. Identification of the key socio-political principles and theories relevant to the scenario.
3. A logical argument supporting the given perspective, addressing the main points raised by the opposing side.
4. A counterargument addressing potential criticisms from the opposing perspective.

Submit your argument as a plain text string in the following format:

Scenario:
{t['scenario']}

Perspective:
{t['perspective']}

Argument:
[Your argument here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should accurately summarize the scenario.",
            "The argument should correctly identify and apply the relevant socio-political principles and theories.",
            "The argument should be logical, coherent, and well-structured.",
            "The argument should demonstrate understanding of socio-political concepts.",
            "The argument should include a counterargument addressing potential criticisms from the opposing perspective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0