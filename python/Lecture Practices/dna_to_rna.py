def main():
    dna = input("Please enter the DNA sequence which is to be converted to mRNA: ")
    mrna = convert_to_mrna(dna)
    print(mrna)
# main() assigns the string the user inputs into the variable dna. The string is passed when the function
# convert_to_mrna(dna) is called. The converted string is assigned to mrna which is then printed.


def convert_to_mrna(dna):
    dna = dna.replace("A", "U")
    dna = dna.replace("T", "A")
    dna = dna.replace("C", "x")
    dna = dna.replace("G", "C")
    dna = dna.replace("x", "G")
    return dna
# convert_to_mrna(dna) replaces the variables letters in the string and assigns them to dna. Since strings are mutable,
# it has to be constantly re-assigned to dna after each replacement (concatenation). dna is then returned to main().


if __name__ == '__main__':
    main()