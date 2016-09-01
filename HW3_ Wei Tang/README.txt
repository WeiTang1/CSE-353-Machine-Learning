Wei Tang
CSE 353

The code is well documented.

Any input file would be divided in to 5 sub data sets in my program 
so there' no need to seperate the data by hand

to change the input file chagne the line at 246

for default, i use a small sample size with 5K entries due to the limitition of my laptop I can't process large data

My program is capable of processing large data but it just take forever

by running python id3.py

My program would print the tree and the test result 
and it would print the average of the 5 test

Program output with Smalldata.tsv:

Weis-MBP:HW3 weitang$ python id3.py 
Genterate tree: 
{5: {'Separated': '<=50K', 'Widowed': '<=50K', 'Divorced': '<=50K', 'Married-spouse-absent': '<=50K', 'Never-married': {3: {'Masters': '<=50K', 'Prof-school': '>50K', '12th': '<=50K', 'Assoc-voc': '<=50K', '1st-4th': '<=50K', 'Assoc-acdm': '<=50K', 'HS-grad': '<=50K', 'Bachelors': {6: {'Farming-fishing': '<=50K', 'Armed-Forces': '<=50K', 'Craft-repair': '<=50K', 'Other-service': '<=50K', 'Transport-moving': '<=50K', 'Prof-specialty': '<=50K', 'Sales': {12: {-48.5: {2: {-138520.5: {1: {'Self-emp-inc': '<=50K', 'State-gov': '<=50K', 'Without-pay': '<=50K', 'Private': {4: {-13.0: {7: {'Own-child': '<=50K', 'Wife': '<=50K', 'Unmarried': '<=50K', 'Other-relative': '<=50K', 'Husband': '<=50K', 'Not-in-family': {8: {'Asian-Pac-Islander': '<=50K', 'Amer-Indian-Eskimo': '<=50K', 'White': {9: {'Male': {10: {-0.0: '<=50K'}}, 'Female': '<=50K'}}, 'Other': '<=50K', 'Black': '<=50K'}}}}, 13.0: '<=50K'}}, 'Local-gov': '<=50K', 'Self-emp-not-inc': '<=50K', 'Federal-gov': '<=50K'}}, 138520.5: '<=50K'}}, 48.5: '>50K'}}, 'Exec-managerial': {0: {36.0: '>50K', -36.0: '<=50K'}}, 'Handlers-cleaners': '<=50K', 'Adm-clerical': '<=50K', 'Protective-serv': '<=50K', 'Tech-support': '<=50K', 'Priv-house-serv': '<=50K', 'Machine-op-inspct': '<=50K'}}, '9th': '<=50K', '5th-6th': '<=50K', 'Some-college': '<=50K', '11th': '<=50K', '10th': '<=50K', 'Doctorate': '<=50K', 'Preschool': '<=50K', '7th-8th': '>50K'}}, 'Married-AF-spouse': '<=50K', 'Married-civ-spouse': '<=50K'}}
Testing result:
0.768558951965
Genterate tree: 
{7: {'Own-child': '<=50K', 'Wife': '>50K', 'Unmarried': '<=50K', 'Other-relative': '<=50K', 'Husband': '<=50K', 'Not-in-family': {10: {-6739.5: {6: {'Farming-fishing': '<=50K', 'Armed-Forces': '<=50K', 'Craft-repair': '<=50K', 'Other-service': '<=50K', 'Transport-moving': '<=50K', 'Prof-specialty': {4: {10.0: {8: {'Asian-Pac-Islander': '<=50K', 'Amer-Indian-Eskimo': '<=50K', 'White': {11: {-0.0: '<=50K'}}, 'Other': '<=50K', 'Black': '<=50K'}}, -10.0: {9: {'Male': '>50K', 'Female': '<=50K'}}}}, 'Sales': '<=50K', 'Exec-managerial': {5: {'Separated': '>50K', 'Widowed': '<=50K', 'Divorced': {2: {-192026.5: '<=50K', 192026.5: {0: {-35.5: '<=50K', 35.5: {3: {'Masters': '<=50K', 'Prof-school': '<=50K', '12th': '<=50K', 'Assoc-voc': '<=50K', '1st-4th': '<=50K', 'Assoc-acdm': '<=50K', 'HS-grad': '<=50K', 'Bachelors': '>50K', '9th': '<=50K', '5th-6th': '<=50K', 'Some-college': '<=50K', '11th': '<=50K', '10th': '<=50K', 'Doctorate': '<=50K', 'Preschool': '<=50K', '7th-8th': '<=50K'}}}}}}, 'Married-spouse-absent': '<=50K', 'Never-married': {12: {-51.5: '<=50K', 51.5: {1: {'Self-emp-inc': '<=50K', 'State-gov': '<=50K', 'Without-pay': '<=50K', 'Private': '>50K', 'Local-gov': '<=50K', 'Self-emp-not-inc': '<=50K', 'Federal-gov': '<=50K'}}}}, 'Married-AF-spouse': '<=50K', 'Married-civ-spouse': '<=50K'}}, 'Handlers-cleaners': '<=50K', 'Adm-clerical': '<=50K', 'Protective-serv': '<=50K', 'Tech-support': '<=50K', 'Priv-house-serv': '<=50K', 'Machine-op-inspct': '<=50K'}}, 6739.5: '>50K'}}}}
Testing result:
0.747816593886
Genterate tree: 
{7: {'Own-child': '<=50K', 'Wife': '>50K', 'Unmarried': '<=50K', 'Other-relative': '<=50K', 'Husband': '<=50K', 'Not-in-family': {6: {'Farming-fishing': '<=50K', 'Armed-Forces': '<=50K', 'Craft-repair': '<=50K', 'Other-service': '<=50K', 'Transport-moving': '<=50K', 'Prof-specialty': {11: {-0.0: '>50K'}}, 'Sales': '<=50K', 'Exec-managerial': {10: {-0.0: '>50K'}}, 'Handlers-cleaners': '<=50K', 'Adm-clerical': '<=50K', 'Protective-serv': '<=50K', 'Tech-support': '<=50K', 'Priv-house-serv': '<=50K', 'Machine-op-inspct': '<=50K'}}}}
Testing result:
0.727074235808
Genterate tree: 
{7: {'Own-child': '<=50K', 'Wife': '>50K', 'Unmarried': '<=50K', 'Other-relative': '<=50K', 'Husband': '<=50K', 'Not-in-family': {3: {'Masters': '<=50K', 'Prof-school': '>50K', '12th': '<=50K', 'Assoc-voc': '<=50K', '1st-4th': '<=50K', 'Assoc-acdm': '<=50K', 'HS-grad': '<=50K', 'Bachelors': {1: {'Self-emp-inc': '>50K', 'State-gov': '<=50K', 'Without-pay': '<=50K', 'Private': {8: {'Asian-Pac-Islander': '<=50K', 'Amer-Indian-Eskimo': '<=50K', 'White': {0: {25.0: '<=50K', -25.0: {6: {'Farming-fishing': '<=50K', 'Armed-Forces': '<=50K', 'Craft-repair': '<=50K', 'Other-service': '<=50K', 'Transport-moving': '<=50K', 'Prof-specialty': '<=50K', 'Sales': '<=50K', 'Exec-managerial': {12: {-45.0: '>50K', 45.0: '<=50K'}}, 'Handlers-cleaners': '<=50K', 'Adm-clerical': '<=50K', 'Protective-serv': '<=50K', 'Tech-support': '<=50K', 'Priv-house-serv': '<=50K', 'Machine-op-inspct': '<=50K'}}}}, 'Other': '<=50K', 'Black': {5: {'Separated': '<=50K', 'Widowed': '<=50K', 'Divorced': {10: {5260.0: '>50K', -5260.0: '<=50K'}}, 'Married-spouse-absent': '<=50K', 'Never-married': '>50K', 'Married-AF-spouse': '<=50K', 'Married-civ-spouse': '<=50K'}}}}, 'Local-gov': {9: {'Male': '<=50K', 'Female': {4: {-13.0: {11: {-0.0: '<=50K'}}, 13.0: '<=50K'}}}}, 'Self-emp-not-inc': {2: {-212006.5: '>50K', 212006.5: '<=50K'}}, 'Federal-gov': '<=50K'}}, '9th': '<=50K', '5th-6th': '<=50K', 'Some-college': '<=50K', '11th': '<=50K', '10th': '<=50K', 'Doctorate': '>50K', 'Preschool': '<=50K', '7th-8th': '<=50K'}}}}
Testing result:
0.758733624454
Genterate tree: 
{7: {'Own-child': '<=50K', 'Wife': '>50K', 'Unmarried': '<=50K', 'Other-relative': '<=50K', 'Husband': '<=50K', 'Not-in-family': {10: {-7731.5: {3: {'Masters': '<=50K', 'Prof-school': '<=50K', '12th': '<=50K', 'Assoc-voc': '<=50K', '1st-4th': '<=50K', 'Assoc-acdm': '<=50K', 'HS-grad': '<=50K', 'Bachelors': {5: {'Separated': '<=50K', 'Widowed': '<=50K', 'Divorced': {9: {'Male': '>50K', 'Female': '<=50K'}}, 'Married-spouse-absent': '>50K', 'Never-married': {2: {-137656.5: {0: {-31.5: '<=50K', 31.5: {1: {'Self-emp-inc': '<=50K', 'State-gov': '<=50K', 'Without-pay': '<=50K', 'Private': {6: {'Farming-fishing': '<=50K', 'Armed-Forces': '<=50K', 'Craft-repair': '<=50K', 'Other-service': '<=50K', 'Transport-moving': '<=50K', 'Prof-specialty': '>50K', 'Sales': '<=50K', 'Exec-managerial': '<=50K', 'Handlers-cleaners': '<=50K', 'Adm-clerical': '<=50K', 'Protective-serv': '<=50K', 'Tech-support': '<=50K', 'Priv-house-serv': '<=50K', 'Machine-op-inspct': '<=50K'}}, 'Local-gov': '<=50K', 'Self-emp-not-inc': '<=50K', 'Federal-gov': '<=50K'}}}}, 137656.5: '<=50K'}}, 'Married-AF-spouse': '<=50K', 'Married-civ-spouse': '<=50K'}}, '9th': '<=50K', '5th-6th': '<=50K', 'Some-college': '<=50K', '11th': {8: {'Asian-Pac-Islander': '<=50K', 'Amer-Indian-Eskimo': '<=50K', 'White': {4: {-7.0: {11: {-0.0: '<=50K'}}, 7.0: '<=50K'}}, 'Other': '<=50K', 'Black': '<=50K'}}, '10th': '<=50K', 'Doctorate': '<=50K', 'Preschool': '<=50K', '7th-8th': '<=50K'}}, 7731.5: '>50K'}}}}
Testing result:
0.775109170306
average 0.755458515284
Weis-MBP:HW3 weitang$ 

so the average is 0.75 
