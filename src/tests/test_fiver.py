from skfuzzy import control

from src.rules import get_fiver_rules
from .class_test import ReferenceDiagnosisTest

FOR_SURE_LEVEL = 65

class TestFiverDiagnosis(ReferenceDiagnosisTest):
    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_fiver_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['temperatura'] = 40.1
        self.medical_record.input['duração da febre'] = 7

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Dengue')
        self.assertGreaterEqual(best_diagonis[1], FOR_SURE_LEVEL)

    def test_should_be_zika(self):
        self.medical_record.input['temperatura'] = 35.7
        self.medical_record.input['duração da febre'] = 1

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Zika')
        self.assertGreaterEqual(best_diagonis[1], FOR_SURE_LEVEL)

    def test_should_be_chikungunya(self):
        self.medical_record.input['temperatura'] = 39.7
        self.medical_record.input['duração da febre'] = 3

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Chikungunya')
        self.assertGreaterEqual(best_diagonis[1], FOR_SURE_LEVEL)

    def test_could_be_dengue_or_chikungunya(self):
        self.medical_record.input['temperatura'] = 38
        self.medical_record.input['duração da febre'] = 4

        expected = {
            'Dengue': (30, FOR_SURE_LEVEL),
            'Chikungunya': (30, FOR_SURE_LEVEL),
            'Zika': (0, 10),
        }

        with self.subTest():
            for disease, perc in self._get_diagnosis():
                print('disease', disease)
                self.assertGreaterEqual(perc, expected[disease][0])
                self.assertLessEqual(perc, expected[disease][1])