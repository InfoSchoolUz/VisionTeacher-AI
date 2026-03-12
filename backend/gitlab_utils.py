from typing import List


def make_issue_checklist(items: List[str]) -> str:
    if not items:
        return "- [ ] No tasks generated"
    return "\n".join([f"- [ ] {item}" for item in items])
