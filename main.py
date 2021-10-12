from person import Person

def main():
    person = Person('Sander', 21)
    print('Legg til en hobby. Når du er ferdig, skriv: "ferdig".')
    hobbyInput = ''
    while hobbyInput != 'ferdig':
        hobbyInput = input()
        if hobbyInput != 'ferdig':
            person.leggTilHobby(hobbyInput)
    person.skrivUt()


if __name__ == '__main__':
    main()