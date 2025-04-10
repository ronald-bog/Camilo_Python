placas = ["AAA111", "BBB222", "CCC333", "DDD444"]

def eliminarPlaca(placa):
    placas.pop(placas.index(placa))

def main():
    eliminarPlaca("BBB222")
    print(placas)

if __name__ == "__main__":
    main()



























