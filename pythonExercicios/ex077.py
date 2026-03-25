palavras = (
    "JavaScript",
    "Python",
    "Java",
    "TypeScript",
    "C#",
    "C++",
    "C",
    "PHP",
    "Go",
    "Swift",
    "Kotlin",
    "Rust",
    "Ruby",
    "Dart",
    "SQL",
    "HTML/CSS",
    "PHP",
    "Scala",
    "Shell",
    "R",
)
# Esse for pega cada palavra da tupla e faz um print com o final end='' para o proximo print ser na mesma linha
for palavra in palavras:
    print(f'Vogais na palavra {palavra.upper()}: ', end='')
    
    # Esse for pega cada letra da palavra selecionada
    for letra in palavra:

        # Esse if verifica se a letra selecionada é vogal, com o .lower() para não dar erro
        if letra.lower() in 'aeiou':
            # Ele dá um print colocando as vogais uma ao lado da outra com espaço entre elas
            print(letra, end=' ')
    print()
    