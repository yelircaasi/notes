def parse_args(args: list[str]) -> tuple[str, dict]:
    command: str = ...
    positional: list[str] = ...
    attributes: dict = ...
    options: dict = ...
    return command, positional, attributes, options