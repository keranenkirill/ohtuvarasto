"""
This module demonstrates the use of the `Varasto` 
class by creating and manipulating
warehouse objects for different products.
"""

from varasto import Varasto


def test_creation():
    """
    Tests the creation of Varasto objects and prints their initial state.
    """
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    return mehua, olutta


def test_getters(olutta):
    """
    Tests the getters of the Varasto object.
    """
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def test_setters(mehua):
    """
    Tests the setters of the Varasto object.
    """
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def test_error_handling():
    """
    Tests error handling for invalid Varasto initialization.
    """
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def test_olut_cases(olutta):
    """
    Tests olut cases for adding and removing items from Varasto.
    """
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def test_mehu_cases(mehua):
    """
    Tests olut cases for adding and removing items from Varasto.
    """
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def main():
    """
    The main function to demonstrate the functionality of the Varasto class.
    It creates instances of Varasto, performs operations, 
    and prints the results.
    """
    mehua, olutta = test_creation()
    test_getters(olutta)
    test_setters(mehua)
    test_error_handling()
    test_olut_cases(olutta)
    test_mehu_cases(mehua)


if __name__ == "__main__":
    main()
