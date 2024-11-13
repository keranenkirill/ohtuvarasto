"""
This module contains the Varasto class for managing warehouse storage.
"""


class Varasto:
    """
    A class that represents a warehouse with a specific capacity and balance.
    """

    def __init__(self, tilavuus, alku_saldo=0):
        """
        Initializes a new warehouse.

        Args:
            tilavuus (float): The maximum capacity of the warehouse.
                              Must be positive.
            alku_saldo (float, optional): The initial balance of the warehouse.
                                          Defaults to 0.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # Invalid capacity, set to 0
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # Invalid balance, set to 0
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # Fits within capacity
            self.saldo = alku_saldo
        else:
            # Fill to capacity, discard the rest
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """
        Calculates how much more can be stored in the warehouse.

        Returns:
            float: The remaining capacity of the warehouse.
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Adds the specified amount to the warehouse balance.

        Args:
            maara (float): The amount to add. Must be non-negative.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Removes the specified amount from the warehouse balance.

        Args:
            maara (float): The amount to remove. Must be non-negative.

        Returns:
            float: The actual amount removed, 
                which might be less if the warehouse
                   does not have enough balance.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        """
        Returns a string representation of the warehouse.

        Returns:
            str: A string in the format 'saldo = X, vielä tilaa Y'.
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
