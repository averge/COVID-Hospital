from datetime import timedelta, datetime
from django.test import TestCase
from reglas.helpers import *


class ReglasTestClass(TestCase):
    def setUp(self):
        c1 = ConfiguracionRegla(key="saturacion_oxigeno", value=80)
        c2 = ConfiguracionRegla(key="frecuencia_respiratoria", value=40)
        c1.save()
        c2.save()

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_tiene_somnolencia(self):
        action = tiene_somnolencia(True)
        expected_action = "Somnolence. Evaluate transfer to UTI"
        self.assertEqual(action, expected_action)

        no_action = tiene_somnolencia(False)
        self.assertEqual(no_action, "No action required")

    def test_mecanica_ventilatoria(self):
        action_bad = mecanica_ventilatoria("bad")
        expected_action_bad = "Bad respiratory mechanics. Evaluate transfer to UTI"
        self.assertEqual(action_bad, expected_action_bad)

        action_regular = mecanica_ventilatoria("regular")
        expected_action_regular = "Regular respiratory mechanics. Evaluate transfer to UTI"
        self.assertEqual(action_regular, expected_action_regular)

        no_action = mecanica_ventilatoria("good")
        self.assertEqual(no_action, "No action required")

    def test_frecuencia_respiratoria(self):
        configurable = ConfiguracionRegla.get_frecuencia_respiratoria()
        if configurable is None:
            raise ValueError("No hay configurada una regla")
        value = configurable + 5
        action = frecuencia_respiratoria(value)
        expected_action = "Respiratory rate more than optimal (" + str(configurable) + "). Evaluate transfer to UTI"
        self.assertEqual(action, expected_action)

        no_action = frecuencia_respiratoria(value-10)
        self.assertEqual(no_action, "No action required")

    def test_diez_dias(self):
        value = datetime.today() - timedelta(days=10)
        action = diez_dias(value.date())
        expected_action = "10 days passed from the onset of symptoms. Evaluate discharge"
        self.assertEqual(action, expected_action)

        no_action = diez_dias(datetime.today().date())
        self.assertEqual(no_action, "No action required")

    def test_saturacion_oxigeno(self):
        configurable = ConfiguracionRegla.get_saturacion_oxigeno()
        if configurable is None:
            raise ValueError("No hay configurada una regla")
        value = configurable - 5
        action = saturacion_oxigeno(value)
        expected_action = "Oxygen saturation less than optimal (" +\
                          str(configurable) +\
                          "). Evaluate oxygen, therapy and prono"
        self.assertEqual(action, expected_action)

        no_action = saturacion_oxigeno(value+10)
        self.assertEqual(no_action, "No action required")

    def test_evolucion_oxigeno(self):
        configurable = ConfiguracionRegla.get_saturacion_oxigeno()
        if configurable is None:
            raise ValueError("No hay configurada una regla")
        last_value = configurable
        value = last_value - 5
        action = evolucion_oxigeno(last_value, value, True)
        expected_action = "Oxygen saturation dropped more than 3%. Evaluate oxygen, therapy and prono"
        self.assertEqual(action, expected_action)

        no_action = evolucion_oxigeno(value, last_value, False)
        self.assertEqual(no_action, "No action required")

        no_action = evolucion_oxigeno(last_value, last_value, True)
        self.assertEqual(no_action, "No action required")
