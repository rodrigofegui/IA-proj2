from skfuzzy import control

from src.rules import get_melasma_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import get_melasma_consequent


class TestMelasmaDiagnosis(ReferenceDiagnosisTest):
    output = get_melasma_consequent()

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_melasma_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['melasma'] = 4

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Dengue')

    def test_should_be_zika(self):
        self.medical_record.input['melasma'] = 1

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Zika')

    def test_should_be_chikungunya(self):
        self.medical_record.input['melasma'] = 5

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Chikungunya')

    # def test_could_be_dengue_or_chikungunya(self):
    #     self.medical_record.input['temperatura'] = 38
    #     self.medical_record.input['duração da febre'] = 4

    #     expected = {
    #         'Dengue': (30, self.FOR_SURE_LEVEL),
    #         'Chikungunya': (30, self.FOR_SURE_LEVEL),
    #         'Zika': (0, 10),
    #     }

    #     with self.subTest():
    #         for disease, perc in self._get_diagnosis():
    #             print('disease', disease)
    #             self.assertGreaterEqual(perc, expected[disease][0])
    #             self.assertLessEqual(perc, expected[disease][1])
