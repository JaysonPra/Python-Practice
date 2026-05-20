from string.templatelib import Template


def build_template(t_string: Template) -> str:
    values: list[str] = []

    for i in t_string:
        if isinstance(i, str):
            values.append(i)
        else:
            values.append(str(i.value))

    return "".join(values)


name: str = "Jayson"
age: int = 21
template: Template = t"Your name is {name} and your age is {age}."

print(build_template(template))
