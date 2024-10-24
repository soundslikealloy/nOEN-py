# -*- coding: utf-8 -*-
# Copyright 2023 by Eloi Martinez-Rabert.  All rights reserved.
# This code is part of the Python-dna distribution and governed by its
# license.  Please see the LICENSE.txt file that should have been included
# as part of this package.
# doctest: +NORMALIZE_WHITESPACE
# doctest: +SKIP

"""
This module contain functions to get data for various purposes.

- :func:`createDict` creates and saves the dictionary with all information and data sets from Excel File (nameFile.xlsx).

- :func:`loadData` for getting the whole information and data sets from Excel file (nameFile.xlsx). Please see README file for more information.

- :func:`loadResults` for getting the nOEN outcomes of the data set already analysed and plot them.

- :func:`writeResults` for writing results in Excel file.

"""

import os.path
import pandas as pd
import numpy as np
from itertools import combinations as _comb
from itertools import compress

def createDict(mainKeyName, iDict, info):
    """
    - :input:`mainKeyName` (str). Mode of dictionary creation ['data', 'comb', 'coeff', 'saveDict'].
    - :input:`iDict` (dict). Dictionary file.
    - :input:`info` (dict). New information included into dictionary file (iDict).

    """
    if mainKeyName == 'data':
        iDict['data'] = info 
        print(' > Structure dataset: Done.')
        return iDict      
    elif mainKeyName == 'comb':
        iDict['comb'] = info 
        print(' > Structure comb: Done.')
        return iDict
    elif mainKeyName == 'coeff':
        iDict['coeff'] = info 
        print(' > Structure coeff: Done.')
        return iDict
    elif mainKeyName == 'saveDict':
        path = '../../Results/'
        fullPathSave = path + info + '.npy'
        if os.path.isfile(fullPathSave):
            cDict = loadResults(info)
            if cDict['data']['results']:
                val = input(' > Do you want to overwrite `' + info + '.npy`? [Y/N]: ')
                if val == 'Y' or val == 'y':
                    np.save(fullPathSave, iDict)
                    print(' > Data structure saved - `' + info +'.npy`.')
                else:
                    print(' > Data structure not saved. If you don\'t want to overwrite results files, use another name for data Excel.')
            else:
                np.save(fullPathSave, iDict)
                print(' > Data structure saved - `' + info +'.npy`.') 
        else:
            np.save(fullPathSave, iDict)
            print(' > Data structure saved - `' + info +'.npy`.')
    else:
        print(' > No expected Structure: `' + mainKeyName + '`')


def loadData(fileName):
    """
    - :input:`fileName` (str). Name of file with data and info.

    """  
    print('\n>> Loading data...')
    path = '../../Results/'
    fullPathFile = path + fileName + '.npy'
    if os.path.isfile(fullPathFile):
        print(' > File `' + fileName + '.npy` with results.')
        rDict = loadResults(fileName)
    else:
        print(' > New file .npy.')
        # Path name of Data
        path = '../../Data/'
        fullPath = path + fileName + '.xlsx'
        # Initialization 
        leDict = {}             # Full dictionary (`data` + `comb` + `coeff`)
        combDict = {}           # Dictionary of combinations (`comb`)
        coeffDict = {}          # Dictionary of Iota coefficients (`coeff`)
        # Structure dataset (data)
        di = pd.read_excel(fullPath, sheet_name = 't_0')
        df = pd.read_excel(fullPath, sheet_name = 't_max')
        varNames = np.array(df.keys())
        di = np.array(di)
        df = np.array(df)
        numVar = len(varNames)
        leDict = createDict('data', leDict, {'inocula': di, 'final': df, 'varNames': varNames, 'numVar': numVar, 'results': False})
        # Structures combinations & Iota coefficients (`comb`, `coeff`)
        v = np.arange(1, numVar+1)
        nCoef = []
        for i in range(2, numVar+1):
            nameK2 = 'D' + str(i)
            relP = 2/(2**i)     # Reliable point (relP = 2/2^D)
            ## Combinations (`comb`)
            c = np.array(list(_comb(v, i)))
            nc = c.shape[0]
            nCoef.append(nc)
            combDict[nameK2] = c
            ## Coefficients (`coeff`)
            coeffDict[nameK2] = {}
            for i_c in c:
                nameK3_comb = "_".join(varNames[i_c - 1])
                coeffDict[nameK2][nameK3_comb] = {'iD': i_c, 'D': i, 'reliablePoint': relP, 'numObs': [], 'coeffInfo': {'signs1': [], 'signs2': [], 'deltas': [], 'd_pval': [], 'iota': [], 'iota_pval': []}}
        combDict['numcoeff'] = nCoef
        leDict = createDict('comb', leDict, combDict)
        leDict = createDict('coeff', leDict, coeffDict)
        # Save structure
        createDict('saveDict', leDict, fileName)
        rDict = loadResults(fileName)
    
    return rDict


def loadResults(fileName):
    path = '../../Results/'
    fullPathSave = path + fileName + '.npy'
    readResults = np.load(fullPathSave, allow_pickle = 'TRUE').item()

    return readResults


def extractResults(dict_, D, idS):
    D_field = 'D' + str(D)
    idS = idS
    varNames = dict_['data']['varNames']
    iVar = []
    for i in idS:
        iVar.append(varNames[i])
    nameK3_comb = "_".join(iVar)
    
    symU = dict_['coeff'][D_field][nameK3_comb]['coeffInfo']['signs1']
    symD = dict_['coeff'][D_field][nameK3_comb]['coeffInfo']['signs2']
    iota = dict_['coeff'][D_field][nameK3_comb]['coeffInfo']['iota']
    pval = dict_['coeff'][D_field][nameK3_comb]['coeffInfo']['iota_pval']
    num_obs = dict_['coeff'][D_field][nameK3_comb]['numObs']
    rely = dict_['coeff'][D_field][nameK3_comb]['reliablePoint']
    
    return iota, pval, num_obs, rely, symU, symD

def writeResults(fileName, Dim = 0, varSelect = 0, onlySig = False):
    """
    - :input:`fileName` (str). Name of file with data and info.
    - :input:`Dim` (list). List with dimensions we want to write (default: 0 -> 'All').

    """
    path = '../../Results/'
    fullPathFile = path + fileName + '.npy'
    fullPathSave = path + fileName + '_results.xlsx'
    if os.path.isfile(fullPathFile):
        if os.path.isfile(fullPathSave):
            val = input(' > Do you want to overwrite `' + fileName + '_results.xlsx`? [Y/N]: ')
        else:
            val = 'Y'
        if val == 'Y' or val == 'y':
            rDict = loadResults(fileName)
            D = rDict['data']['numVar']
            numComb = rDict['comb']['numcoeff']
            print('\n>> Writing results ' + '`' + fileName + '.npy` to `' + fileName + '_results.xlsx`.')
            # Data Sheet
            data = rDict['data']['final']
            varNames = rDict['data']['varNames']
            nd = data.shape[0]
            df = pd.DataFrame(data, columns = varNames.tolist(), index = np.arange(1, nd+1))
            if not varSelect == 0:
                # Check if variable name(s) exists
                cvarNames = np.isin(varSelect, varNames)
                getnotNames = list(compress(varSelect, ~cvarNames))
                if getnotNames:
                    print(' > Variable(s) `' + ' '.join(getnotNames) + '` not found.')
            with pd.ExcelWriter(fullPathSave) as writer:
                df.to_excel(writer, sheet_name='Data')
                if Dim == 0:
                    vD = np.arange(2, D+1)
                else:
                    vD = Dim
                for d in vD:
                    sName = 'D' + str(d)
                    infoR = pd.DataFrame(np.array(['· Dimension ' + str(d), '· Reliable point: ' + str(2/(2**d)), '· Total number of observations: ' + str(nd), '· Total number of var combinations: ' + str(numComb[d-2])]))
                    infoR.to_excel(writer, sheet_name = sName, index = False, header = False)
                    headR = ['[ ' + '± ' * d + ']', '[ ' + '∓ ' * d + ']', 'δ coeff.', 'ι coeff.', 'p-values']
                    for c in rDict['comb'][sName]:
                        if not varSelect == 0:
                            # Check if variable(s) is present in combination `c`
                            ind = np.array(np.where(np.isin(varNames, varSelect)), dtype = int) + 1
                            checkVar = any(np.isin(c, ind))
                            if not checkVar:
                                continue
                        sRow = writer.sheets[sName].max_row
                        jvarName = "_".join(varNames[c - 1])
                        ExcelName = jvarName.replace("_", " ")
                        dvarName = pd.DataFrame(["[" + ExcelName + "]"])
                        dvarName.to_excel(writer, sheet_name = sName, startrow = sRow+1, index = False, header = False)
                        r = rDict['coeff'][sName][jvarName]['coeffInfo']
                        numObsComb = pd.DataFrame(['Number of observations: ' + str(rDict['coeff'][sName][jvarName]['numObs'])])
                        numObsComb.to_excel(writer, sheet_name = sName, startrow = sRow+2, index = False, header = False)
                        if onlySig:
                            checkSig = np.any(r['iota_pval'] < 0.051)
                            if not checkSig:
                                noSigMSN = pd.DataFrame(['No significant data trends were found.'])
                                noSigMSN.to_excel(writer, sheet_name = sName, startrow = sRow+3, index = False, header = False)
                                continue
                        if d == 2:
                            rM = [r['signs1'][0], r['signs2'][0], '-', r['iota'], r['iota_pval']]
                            R = pd.DataFrame([rM], columns = headR)
                            R[headR[-2:]] = R[headR[-2:]].astype(float)
                        else:
                            rMSings = np.array([r['signs1'], r['signs2']]).T
                            rMcoeffs = np.array([r['deltas'], r['iota'], r['iota_pval']], dtype = 'float').T
                            rM = np.append(rMSings, rMcoeffs, axis = 1)
                            R = pd.DataFrame(rM, columns = headR).infer_objects()
                            R[headR[-3:]] = R[headR[-3:]].astype(float)
                        R.to_excel(writer, sheet_name = sName, float_format = '%.4f', startrow = sRow+3, index = False)
            print('>> Writing done.')
        else:
            print(' > Results not written. If you don\'t want to lose existing results files, change the name of existing Excel or make a copy into another folder before.')
    else:
        print(' > `' + fileName + '.npy` does not exist.')


#-DEBUGGING
# Load results
# loadData('data-py')
# results = loadResults('data-py')
# print(results)
# Write results to Excel
# writeResults('data-py')
#----------