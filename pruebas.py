import unittest
import requests
import os
from datetime import datetime
from Modulo_3_Loguica import *

class serviceSeller(unittest.TestCase):

    def test_datos(self):
        """
        Test that invalid plate raises ValueError
        """
        ocupacion='Docente'
        recidencia='Cuenca'
        nacionalidad = 'Ecuatoriana'
        fechaDeNacimiento= '2021-04-02'
        discapacidad='True'
        with self.assertRaises(ValueError):
            result = VotanteSiNo(ocupacion,recidencia, nacionalidad,fechaDeNacimiento,discapacidad ).ComprobarEcuatoriano()

    
    def test_datos2(self):
        """
        Test that invalid date raises ValueError
        """
        ocupacion='Ingeniero'
        recidencia='Bogota'
        nacionalidad = 'Venezolano'
        fechaDeNacimiento= '2021-10-23'
        discapacidad='False'
        with self.assertRaises(ValueError):
            result = VotanteSiNo(ocupacion,recidencia, nacionalidad,fechaDeNacimiento,discapacidad ).ComprobarEcuatoriano()

    
    def test_datos3(self):
        """
        Test that invalid time raises ValueError
        """
        ocupacion='Doctor'
        recidencia='Barcelona'
        nacionalidad = 'Española'
        fechaDeNacimiento= '2000-04-02'
        discapacidad='False'
        with self.assertRaises(ValueError):
            result = VotanteSiNo(ocupacion,recidencia, nacionalidad,fechaDeNacimiento,discapacidad ).ComprobarEcuatoriano()

    
    def test_datos4(self):
        """
        Test that missing API key raises requests.HTTPError
        """
        ocupacion='Ganadero'
        recidencia='Madrid'
        nacionalidad = 'Española'
        fechaDeNacimiento= '1991-06-12'
        discapacidad='False'
        with self.assertRaises(ValueError):
            result = VotanteSiNo(ocupacion,recidencia, nacionalidad,fechaDeNacimiento,discapacidad ).ComprobarEcuatoriano()


    def test_datos5(self):
        """
        Test that moved new holidays are restricted
        """
        ocupacion='Ganadero'
        recidencia='Cali'
        nacionalidad = 'Colombia'
        fechaDeNacimiento= '1984-10-16'
        discapacidad='False'
        with self.assertRaises(ValueError):
            result = VotanteSiNo(ocupacion,recidencia, nacionalidad,fechaDeNacimiento,discapacidad ).ComprobarEcuatoriano()



    def test_datos6(self):
        """
        Test that moved would-have-been holidays are not restricted
        """
        ocupacion='Arquitecto'
        recidencia='Londres'
        nacionalidad = 'Inglés'
        fechaDeNacimiento= '1987-01-17'
        discapacidad='True'
        with self.assertRaises(ValueError):
            result = VotanteSiNo(ocupacion,recidencia, nacionalidad,fechaDeNacimiento,discapacidad ).ComprobarEcuatoriano()


    def test_datos7(self):
        """
        Test that moved would-have-been continuous holidays are not restricted
        """
        ocupacion='Arquitecto'
        recidencia='Paris'
        nacionalidad = 'Frances'
        fechaDeNacimiento= '1982-03-24'
        discapacidad='True'
        with self.assertRaises(ValueError):
            result = VotanteSiNo(ocupacion,recidencia, nacionalidad,fechaDeNacimiento,discapacidad ).ComprobarEcuatoriano()



    
        

if __name__ == '__main__':
    unittest.main()
