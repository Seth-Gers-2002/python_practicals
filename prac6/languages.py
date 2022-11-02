from prac6.programminglanguage import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]

    for language in languages:
        if language.is_dynamic():
            print(f"{language.field} is dynamic")


main()
