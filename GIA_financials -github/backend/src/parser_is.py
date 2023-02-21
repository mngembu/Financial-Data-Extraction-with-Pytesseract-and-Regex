import re

from parser_generic import AuditReportParser


class ISParser(AuditReportParser):    #creating a child class FSParser from AuditReportParser
    def __init__(self, text):
        AuditReportParser.__init__(self, text)   #initialize the parent class

    def parse(self):     #write the actual method/parser for this child class
        return {
            'revenue': self.get_field('revenue'),
            'expenses': self.get_field('expenses'),
            'net surplus': self.get_field('netsurplus')
        }

    def get_field(self, field_name):
        pattern_dict = {
            'revenue': {'pattern': "([\d,]+) [\d,]+\n\nExpenses|([\d,]+) [\d,]+\nExpenses|([\d,]+) [\d,]+\n\nOperating expenses|([\d,]+) [\d,]+\nOperating expenses", 'flags': 0},
            'expenses': {'pattern': "(\([\d,]+\)) [\d,]+\n\(Deficiency\)|([\d,]+) [\d,]+\n\(Deficiency\)|([\d,]+) \([\d,]+\)\n\(Deficiency\)|([\d,]+) [\d,]+\nExcess \(deficiency\)|([\d,]+) [\d,]+\nExcess of|([\d,]+) [\d,]+\n\nExcess of| (-) \([\d,]+\)\nDeficiency| (-) - \nDeficiency", 'flags': 0},
            'netsurplus': {'pattern': "revenues over expenses \$ (\([\d,]+\)) \$ \([\d,]+\)|revenues over expenses \$ ([\d,]+) \$ \([\d,]+\)|revenues over expenses \$ ([\d,]+) \$ [\d,]+|revenues over expenses \$ (\([\d,]+\)) \$ [\d,]+", 'flags': 0}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            matches = [(tuple(int(x) if x.isdigit() else x for x in _ if x))[0] for _ in matches]  # getting only the digits
            matches = [s.replace('(', '-') for s in matches]
            matches = [s.replace(')', '') for s in matches]
            matches = [s.replace(',', '') for s in matches]
            return matches


#testing the code
# if __name__ == '__main__':
#    document_text = '''
#     GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Operations
#
# Year ended December 31, 2013, with comparative information for 2012
#
# 2013 2012
#
# Revenues
# Commercial $ 18,446,374 $ 18,090,637
# Provincial contract fees 2,208,589 2,108,213
# United Way 177,728 174,991
# Donations, grants and contributions 81,848 148,360
# Amortization of deferred capital contributions 62,167 55,857
# Unrealized gain on investments 12,448 12,736
# Interest revenue 4,963 3,503
# 20,994,117 20,594,297
#
# Expenses
# Human resource costs (note 14) 13,291,714 12,992,010
# Physical resource costs (note 14) 5,397,023 5,115,306
# Other operating costs (note 14) 1,663,814 1,573,217
# Amortization of property and equipment 523,050 461,945
# Material costs (note 14) 426,964 337,304
# 21,302,565 20,479,782
# (Deficiency) excess of revenues over expenses $ (308,448) $ 114,515
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Operations
#
# Year ended December 31, 2014, with comparative information for 2013
#
# 2014 2013
#
# Revenues
# Commercial $ 19,225,212 $ 18,446,374
# Provincial contract fees (note 6) 2,489,045 2,208,589
# United Way 156,856 177,728
# Donations, grants and contributions 67,483 81,848
# Amortization of deferred capital contributions 62,446 62,167
# Unrealized gain on investments 10,266 12,448
# Interest revenue 284 4,963
# 22,011,592 20,994,117
#
# Expenses
# Human resource costs (note 14) 13,664,328 13,291,714
# Occupancy costs (note 14) 5,654,644 5,397,023
# Other operating costs (note 14) 1,839,774 1,663,814
# Amortization of property and equipment 595,072 523,050
# Material costs (note 14) 461,187 426,964
# 22,215,005 21,302,565
# (Deficiency) of revenues over expenses $ (203,413) $ (308,448)
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Operations
#
# Year ended December 31, 2015, with comparative information for 2014
#
# 2015 2014
#
# Revenues
# Commercial $ 21,426,431 $ 19,225,212
# Provincial contract fees (note 6) 2,421,110 2,489,045
# United Way 162,491 156,856
# Donations, grants and contributions 58,258 67,483
# Amortization of deferred capital contributions 68,907 62,446
# Unrealized gain on investments 8,611 10,266
# Interest revenue 421 284
# 24,146,229 22,011,592
#
# Expenses
# Human resource costs (note 15) 14,168,964 13,664,328
# Occupancy costs (note 15) 5,843,996 5,654,644
# Other operating costs (note 15) 1,923,848 1,839,774
# Amortization of property and equipment 705,158 595,072
# Material costs (note 15) 436,912 461,187
# 23,078,878 22,215,005
# Excess (deficiency) of revenues over expenses $ 1,067,351 $ (203,413)
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Operations
#
# Year ended December 31, 2016, with comparative information for 2015
#
# 2016 2015
#
# Revenues
# Commercial $ 21,596,330 $ 21,426,431
# Provincial contract fees (note 7) 2,384,903 2,421,110
# United Way 164,928 162,491
# Donations, grants and contributions 51,473 58,258
# Amortization of deferred capital contributions 35,661 68,907
# Unrealized gain on investments 6,320 8,611
# Interest revenue 5,393 421
# 24,245,008 24,146,229
#
# Expenses
# Human resources (note 16) 14,064,283 14,168,964
# Occupancy (note 16) 6,119,256 5,843,996
# Other operating (note 16) 1,814,635 1,923,848
# Amortization of property and equipment 686,287 705,158
# Materials (note 16) 630,978 436,912
# 23,315,439 23,078,878
# Excess of revenues over expenses $ 929,569 $ 1,067,351
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Operations
#
# Year ended December 31, 2017, with comparative information for 2016
#
# 2017 2016
#
# Revenues
# Commercial $ 24,597,943 $ 21,596,330
# Provincial contract fees (note 7) 2,446,961 2,384,903
# United Way 124,305 164,928
# Donations, grants and contributions 134,897 51,473
# Amortization of deferred capital contributions 30,964 35,661
# Unrealized gain on investments 5,611 6,320
# Interest revenue 4,206 5,393
# 27,344,887 24,245,008
#
# Expenses
# Human resources (note 16) 16,571,203 14,064,283
# Occupancy (note 16) 7,847,365 6,119,256
# Other operating (note 16) 2,024,013 1,814,635
# Amortization of property and equipment 1,002,971 686,287
# Materials (note 16) 892,638 630,978
# 28,338,190 23,315,439
# Excess (deficiency) of revenues over expenses $ (993,303) $ 929,569
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Operations
#
# Year ended December 31, 2018, with comparative information for 2017
#
# 2018 2017
# Revenues
# Commercial $ 26,737,544 $ 24,597,943
# Provincial contract fees (note 7) 2,382,561 2,446,961
# Donations, grants and contributions 124,487 134,897
# Amortization of deferred capital contributions 25,336 30,964
# Interest revenue 6,994 4,206
# Unrealized gain on investments 3,451 5,611
# United Way - 124,305
# 29,280,373 27,344,887
# Expenses
# Human resources (note 14) 17,562,393 16,571,203
# Occupancy (note 14) 8,173,857 7,847,365
# Other operating (note 14) 2,229,033 2,024,013
# Amortization of property and equipment 1,166,158 1,002,971
# Materials (note 14) 780,436 892,638
# 29,911,877 28,338,190
# (Deficiency) of revenues over expenses $ (631,504) $ (993,303)
#
# oa Senha, Sistine aan i SSS ed
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Operations
#
# Year ended December 31, 2019, with comparative information for 2018
#
# 2019 2018
#
# Operating revenues
#
# Commercial $ 30,274,056 $ 26,737,544
#
# Provincial contract fees 2,204,619 2,382,561
#
# Donations, grants and contributions 272,570 124,487
#
# Interest revenue 13,367 10,445
#
# 32,764,612 29,255,037
#
# Operating expenses (note 13)
#
# Human resources 18,957,729 17,562,393
#
# Occupancy 9,222,993 8,507,149
#
# Other operating 2,226,654 2,229,033
#
# Materials 1,144,885 780,436
#
# 31,552,261 29,079,011
#
# Excess of revenues over expenses before the under-noted 1,212,351 176,026
# Amortization of deferred capital contributions 25,337 25,336
# Amortization of deferred tenant inducements 480,079 333,292
# Amortization of property and equipment (1,188,578) (1,166,158)
# Lease termination fee (712,619) -
# Loss on disposal of property and equipment (83,790) -
# Deficiency of revenues over expenses $ (267,220) $ (631,504)
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Operations
#
# Year ended December 31, 2020, with comparative information for 2019
#
# 2020 2019
#
# Operating revenues
#
# Commercial $ 23,614,342 $ 30,274,056
#
# Federal subsidies (note 13) 2,295,714 -
#
# Provincial contract fees 1,387,065 2,204,619
#
# Donations, grants and contributions 60,396 272,570
#
# Interest revenue 2,128 13,367
#
# 27,359,645 32,764,612
#
# Operating expenses (note 12)
#
# Human resources 15,047,405 18,957,729
#
# Occupancy 9,521,057 9,222,993
#
# Other operating 1,665,017 2,226,654
#
# Materials 1,167,831 1,144,885
#
# 27,401,310 31,552,261
#
# (Deficiency) excess of revenues over expenses
# before the under-noted (41,665) 1,212,351
# Amortization of deferred capital contributions 22,500 25,337
# Amortization of deferred tenant inducements 458,136 480,079
# Amortization of property and equipment (1,089,313) (1,188,578)
# Lease termination fee - (712,619)
# Loss on disposal of property and equipment - (83,790)
# Deficiency of revenues over expenses $ (650,342) $ (267,220)
#
# See accompanying notes to financial statements.
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Operations
#
# Year ended December 31, 2021, with comparative information for 2020
#
# 2021 2020
# Operating revenues
# Commercial $ 33,514,059 $ 23,614,342
# Federal subsidies (note 14) 688,637 2,295,714
# Provincial contract fees 2,060,788 1,387,065
# Donations, grants and contributions 221,419 60,396
# Interest revenue 5,147 2,128
# 36,490,050 27,359,645
# Operating expenses (note 13)
# Human resources 19,236,285 15,047,405
# Occupancy 12,004,258 9,521,057
# Other operating 2,249,229 1,665,017
# Materials 1,484,921 1,167,831
# 34,974,693 27,401,310
# Excess (deficiency) of revenues over expenses
# before the undernoted 1,515,357 (41,665)
# Amortization of deferred capital contributions 22,500 22,500
# Amortization of tenant inducements 517,564 458,136
# Amortization of property and equipment (1,155,994) (1,089,313)
# Gain on disposal of property and equipment 41,599 -
# Excess (deficiency) of revenues over expenses $ 941,026 $ (650,342)
#
# See accompanying notes to financial statements.

#    '''
#
#
#
#     pp = ISParser(document_text)
#     print(pp.parse())
