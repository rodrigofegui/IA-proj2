from numpy import arange
from skfuzzy import control
import skfuzzy as fuzzy

disease = control.Consequent(arange(0, 11, .1), 'diagnosis')

disease.automf(names=['unidentified', 'dengue', 'zika', 'chikungunya'])


def get_melasma_consequent():
    melasma = control.Consequent(arange(0, 11, .1), 'diagnosis')

    melasma['unidentified'] = fuzzy.gbellmf(melasma.universe, 1.2, 5, 1.25)# .1
    melasma['dengue'] = fuzzy.sigmf(melasma.universe, 5, .34)
    melasma['dengue'] = [
        v * melasma['dengue'].mf[i]
        for i, v in enumerate(fuzzy.gbellmf(melasma.universe, 1.2, 5, 3.75))
    ]  # approx. .3 to .5
    melasma['zika'] = fuzzy.sigmf(melasma.universe, -1.5, .34)
    melasma['zika'] = [
        v * melasma['zika'].mf[i]
        for i, v in enumerate(fuzzy.gbellmf(melasma.universe, 1.2, 5, 6.25))
    ]  # approx. .9 to .1
    melasma['chikungunya'] = fuzzy.sigmf(melasma.universe, 0, 0)
    melasma['chikungunya'] = [
        v * melasma['chikungunya'].mf[i]
        for i, v in enumerate(fuzzy.gbellmf(melasma.universe, 1.2, 5, 8.75))
    ] # .5

    return melasma


def get_muscle_pain_consequent():
    muscle_pain = control.Consequent(arange(0, 11, .1), 'diagnosis')

    muscle_pain['dengue'] = fuzzy.trimf(muscle_pain.universe, [0, 1, 1])
    muscle_pain['zika'] = fuzzy.tripmf(muscle_pain.universe, [0, 2, 3])
    muscle_pain['chikungunya'] = fuzzy.trimf(muscle_pain.universe, [1, 2, 3])

    return muscle_pain


def get_joint_pain_consequent():
    joint_pain = control.Consequent(arange(0, 11, .1), 'diagnosis')

    joint_pain['unidentified'] = (
        fuzzy.gaussmf(joint_pain.universe, 2.5, .75) +
        fuzzy.gaussmf(joint_pain.universe, 7.5, .75)
    )
    joint_pain['dengue'] = fuzzy.gaussmf(joint_pain.universe, 0, .75)
    joint_pain['zika'] = fuzzy.gaussmf(joint_pain.universe, 5, .75)
    joint_pain['chikungunya'] = fuzzy.gaussmf(joint_pain.universe, 10, .75)

    return joint_pain
