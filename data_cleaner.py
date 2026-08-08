def clean_name(name: str) -> str:
    return " ".join(name.strip().split())

def clean_email(email: str) -> str:
    return email.strip().lower()

def remove_empty_names(names: list[str]) -> list[str]:
    return [name.strip() for name in names if name.strip()]