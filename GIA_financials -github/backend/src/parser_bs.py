import re

from parser_generic import AuditReportParser

class BSParser(AuditReportParser):    #creating a child class FSParser from AuditReportParser
    def __init__(self, text):
        AuditReportParser.__init__(self, text)   #initialize the parent class

    def parse(self):     #write the actual method/parser for this child class
        return {
            'net assets': self.get_netassets()
        }


    def get_netassets(self):
        pattern = "Net assets \(deficiency\) ([\d,]+)|Net assets ([\d,]+)|Net \(deficiency\) assets ([\(\d,\)]+)"
        netassets = re.findall(pattern, self.text, flags=re.DOTALL)
        netassets = [(tuple(int(x) if x.isdigit() else x for x in _ if x))[0] for _ in netassets]  # getting only the digits
        netassets = [s.replace('(', '-') for s in netassets]
        netassets = [s.replace(')', '') for s in netassets]
        netassets = [s.replace(',', '') for s in netassets]
        return netassets


#testing the code
# if __name__ == '__main__':
#     document_text = '''
#     GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Financial Position
#
# December 31, 2013, with comparative information for 2012
#
# 2013 2012
# ASSETS
# Current
# Cash and cash equivalents $ 685,805 $ 954,184
# Investments (note 3) 317,736 207,199
# Accounts receivable 194,258 270,841
# Inventory 6,630 7,190
# Prepaid expenses and deposits 49,995 56,895
# 1,254,424 1,496,309
# Investments (note 3) 219,524 317,613
# Prepaid expenses and deposits 317,811 319,641
# Property and equipment (note 4) 2,324,810 2,617,059
# $ 4,116,569 $ 4,750,622
# LIABILITIES
# Current
# Accounts payable and accrued liabilities (note 11) $ 1,483,988 $ 1,338,910
# Deferred revenues 77,208 67,486
# Deferred contributions (note 6) 130,768 326,898
# Current portion of obligations under capital lease (note 8) 20,244 19,397
# 1,712,208 1,752,691
# Deferred capital contributions (note 7) 122,447 184,614
# Obligations under capital lease (note 8) 38,725 58,961
# Accrued benefit liability (note 10) - 24,000
# Straight-line rent and tenant inducements payable (note 9) 1,504,531 1,683,250
# 3,377,911 3,703,516
# Net assets 738,658 1,047,106
#
# $ 4,116,569 $ 4,750,622
# Commitments (note 12)
# See accompanying notes to financial statements.
#
# On behalf of the Board:
#
# , Director , Director
#
#
#
# GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Financial Position
#
# December 31, 2014, with comparative information for 2013
#
# 2014 2013
# ASSETS
# Current
# Cash and cash equivalents $ 537,968 $ 685,805
# Investments (note 3) 320,756 317,736
# Accounts receivable 208,843 194,258
# Inventory 1,785 6,630
# Prepaid expenses and deposits 32,625 49,995
# 1,101,977 1,254,424
# Investments (note 3) 226,770 219,524
# Prepaid expenses and deposits 333,297 317,811
# Property and equipment (note 4) 2,338,481 2,324,810
# $ 4,000,525 $ 4,116,569
# LIABILITIES
# Current
# Accounts payable and accrued liabilities (note 11) $ 1,918,956 $ 1,483,988
# Deferred revenues 57,902 77,208
# Deferred contributions (note 6) 57,271 130,768
# Current portion of obligations under capital lease (note 8) 17,800 20,244
# 2,051,929 1,712,208
# Deferred capital contributions (note 7) 128,702 122,447
# Obligations under capital lease (note 8) 21,122 38,725
# Straight-line rent and tenant inducements payable (note 9) 1,263,527 1,504,531
# 3,465,280 3,377,911
# Net assets 535,245 738,658
#
# $ 4,000,525 $ 4,116,569
#
# Commitments (note 12)
# See accompanying notes to financial statements.
#
# On behalf of the Board:
#
# , Director , Director
#
#
#
# GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Financial Position
#
# December 31, 2015, with comparative information for 2014
#
# 2015 2014
# ASSETS
# Current
# Cash $ 1,392,919 $ 537,968
# Investments (note 3) 332,792 320,756
# Accounts receivable 412,864 208,843
# Prepaid expenses, deposits and other 41,351 34,410
# 2,179,926 1,101,977
# Investments (note 3) 223,345 226,770
# Prepaid expenses and deposits 340,619 333,297
# Property and equipment (note 4) 2,320,701 2,338,481
# $ 5,064,591 $ 4,000,525
# LIABILITIES
# Current
# Accounts payable and accrued liabilities (note 11) $ 1,841,350 $ 1,918,956
# Deferred revenues 56,860 57,902
# Deferred contributions (note 6) 412,414 57,271
# Current portion of obligations under capital lease (note 8) 19,235 17,800
# 2,329,859 2,051,929
# Deferred capital contributions (note 7) 59,795 128,702
# Obligations under capital lease (note 8) 1,887 21,122
# Straight-line rent and tenant inducements payable (note 9) 1,070,454 1,263,527
# 3,461,995 3,465,280
# Net assets 1,602,596 535,245
#
# $ 5,064,591 $ 4,000,525
#
# Commitments (note 12)
# See accompanying notes to financial statements.
#
# On behalf of the Board:
#
# , Director , Director
#
#
#
# GOODWILL INDUSTRIES OF ALBERTA
#
# Statement of Financial Position
#
# December 31, 2016, with comparative information for 2015
#
# 2016 2015
# ASSETS
# Current
# Cash $ 1,815,125 $ 1,392,919
# Investments (note 3) 450,777 332,792
# Accounts receivable 682,354 412,864
# Prepaid expenses, deposits and other 212,712 41,351
# 3,160,968 2,179,926
# Investments (note 3) 386,680 223,345
# Prepaid expenses and deposits 392,444 340,619
# Property and equipment (note 4) 3,789,429 2,320,701
# $ 7,729,521 $ 5,064,591
# LIABILITIES
# Current
# Accounts payable and accrued liabilities (note 6) $ 2,409,959 $ 1,841,350
# Deferred revenues 50,140 56,860
# Deferred contributions (note 7) 415,989 412,414
# Current portion of obligation under capital lease (note 9) 1,887 19,235
# Current portion of long-term debt (note 10) 68,994 -
# 2,946,969 2,329,859
# Deferred capital contributions (note 8) 24,134 59,795
# Obligations under capital lease (note 9) - 1,887
# Long-term debt (note 10) 331,006 -
# Straight-line rent and tenant inducements (note 11) 1,895,247 1,070,454
# 5,197,356 3,461,995
# Net assets 2,532,165 1,602,596
# $ 7,729,521 $ 5,064,591
# Credit facility (note 5)
# Commitments (note 12)
# See accompanying notes to financial statements.
# On behalf of the Board:
# , Director , Director
#
#
#
# —S Z = , Director
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Financial Position
#
# December 31, 2017, with comparative information for 2016
#
# 2017 2016
# ASSETS
# Current
# Cash and cash equivalents $ 1,046,845 $ 1,815,125
# Investments (note 3) 568,068 450,777
# Accounts receivable 1,059,476 682,354
# Prepaid expenses, deposits and other 207,838 212,712
# 2,882,227 3,160,968
# Investments (note 3) 275,000 386,680
# Prepaid expenses and deposits 544,225 392,444
# Property and equipment (note 4) 6,678,586 3,789,429
# $ 10,380,038 $ 7,729,521
# LIABILITIES
# Current
# Accounts payable and accrued liabilities (note 6) $ 2,705,188 $ 2,409,959
# Deferred revenues 62,922 50,140
# Deferred contributions (note 7) 430,907 415,989
# Current portion of obligation under capital lease - 1,887
# Current portion of long-term debt (note 9) 151,192 68,994
# 3,350,209 2,946,969
# Deferred capital contributions (note 8) 193,170 24,134
# Long-term debt (note 9) 1,679,814 331,006
# Straight-line rent and tenant inducements (note 10) 3,617,983 1,895,247
# 8,841,176 5,197,356
# Net assets 1,538,862 2,532,165
#
# $ 10,380,038 $ 7,729,521
#
# Credit facility (note 5)
# Commitments and contingencies (note 11)
#
# See accompanying notes to financial statements.
#
# On behalf of the Board:
#
# , Director
#
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Financial Position
#
# December 31, 2018, with comparative information for 2017
#
# 2018 2017
# ASSETS
# Current
# Cash and cash equivalents $ 985,833 $ 1,046,845
# Investments (note 3) 500,000 568,068
# Accounts receivable 309,903 1,059,476
# Prepaid expenses, deposits and other 200,845 207,838
# 1,996,581 2,882,227
# Investments (note 3) 275,000 275,000
# Prepaid expenses and deposits 617,867 544,225
# Property and equipment (note 4) 6,261,708 6,678,586
# $ 9,151,156 $ 10,380,038
# LIABILITIES
# Current
# Accounts payable and accrued liabilities (note 6) $ 1,681,116 $ 2,705,188
# Deferred revenues 80,335 62,922
# Deferred contributions (note 7) 590,490 430,907
# Current portion of long-term debt (note 9) 444,180 151,192
# 2,796,121 3,350,209
# Deferred capital contributions (note 8) 167,834 193,170
# Long-term debt (note 9) 1,235,634 1,679,814
# Straight-line rent and tenant inducements (note 10) 4,044,209 3,617,983
# 8,243,798 8,841,176
# Net assets 907,358 4,538,862
#
# $ 9,151,156 $ 10,380,038
#
# Credit facility (note 5)
# Commitments and contingencies (note 11)
#
# See accompanying notes to financial statements.
#
# On behalf of the Board:
#
# Le lj YA, , Director Dwitig >= Director
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Financial Position
#
# December 31, 2019, with comparative information for 2018
#
# 2019 2018
#
# ASSETS
#
# Current
#
# Cash and cash equivalents $ 1,828,340 $ 985,833
# Investments (note 3) 512,013 500,000
# Accounts receivable 513,579 309,903
# Prepaid expenses and deposits 709,339 818,712
# 3,563,271 2,614,448
# Non-current investments (note 3) 275,000 275,000
# Property and equipment (note 4) 6,366,669 6,261,708
#
# $ 10,204,940 $ 9,151,156
#
# LIABILITIES AND NET ASSETS
#
# Current
# Accounts payable and accruals (note 6) $ 1,662,463 $ 1,681,116
# Deferred revenues 678,628 670,825
# Scheduled cash repayments for long-term debt (note 7) 472,301 444,180
# 2,813,392 2,796,121
# Callable debt (note 7) 350,000 -
# 3,163,392 2,796,121
# Long-term debt (note 7) 763,334 1,235,634
# Deferred capital contributions (note 8) 142,497 167,834
# Straight-line rent and tenant inducements (note 9) 5,495,579 4,044,209
# 9,564,802 8,243,798
# Net assets 640,138 907,358
#
# $ 10,204,940 $ 9,151,156
# Credit facility (note 5)
# Commitments and contingencies (note 10)
# Subsequent event (note 14)
#
# See accompanying notes to financial statements.
#
# On behalf of the Board:
#
# , Director , Director
#
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Financial Position
#
# December 31, 2020, with comparative information for 2019
#
# 2020 2019
# ASSETS
# Current
# Cash and cash equivalents $ 2,566,410 $ 1,828,340
# Investments (note 3) 500,000 512,013
# Accounts receivable 651,105 513,579
# Prepaid expenses and deposits 893,063 709,339
# 4,610,578 3,563,271
# Non-current investments (note 3) 275,000 275,000
# Property and equipment (note 4) 5,740,027 6,366,669
# $ 10,625,605 $ 10,204,940
# LIABILITIES AND NET ASSETS
# Current
# Accounts payable and accruals (note 5) $ 3,366,617 $ 1,662,463
# Deferred revenues 660,252 678,628
# Current portion of long-term debt (note 6) 473,555 472,301
# 4,500,424 2,813,392
# Callable debt (note 6) 342,923 350,000
# 4,843,347 3,163,392
# Long-term debt (note 6) 561,377 763,334
# Unamortized deferred capital contributions (note 7) 119,997 142,497
# Straight-line rent and tenant inducements (note 8) 5,111,088 5,495,579
# 10,635,809 9,564,802
# Net (deficiency) assets (10,204) 640,138
# $ 10,625,605 $ 10,204,940
# Credit facility (note 6)
# Commitments and contingencies (note 10)
# Impacts of COVID-19 (note 13)
# See accompanying notes to financial statements.
# On behalf of the Board:
# , Director , Director
#
#
#
# GOODWILL INDUSTRIES OF ALBERTA (Registered Society)
#
# Statement of Financial Position
#
# December 31, 2021, with comparative information for 2020
#
# 2021 2020
#
# ASSETS
#
# Current
#
# Cash and cash equivalents $ 2,401,680 $ 2,566,410
# Investments (note 3) 775,000 500,000
# Accounts receivable 310,013 651,105
# Prepaid expenses and deposits 841,595 893,063
# 4,328,288 4,610,578
# Non-current investments (note 3) - 275,000
# Property and equipment (note 4) 7,384,662 5,740,027
#
# $ 11,712,950 $ 10,625,605
#
# LIABILITIES AND NET ASSETS (DEFICIENCY)
#
# Current
# Accounts payable and accruals (note 5) $ 1,976,105 $ 3,366,617
# Deferred revenues 694,599 660,252
# Current portion of long-term debt (note 6) 765,650 816,478
# Current portion of obligation under capital lease (note 7) 15,388 -
# 3,451,742 4,843,347
# Long-term debt (note 6) 851,282 561,377
# Obligations under capital lease (note 7) 63,705 -
# Unamortized deferred capital contributions (note 8) 97,497 119,997
# Straight-line rent and tenant inducements (note 9) 6,317,902 5,111,088
# 10,782,128 10,635,809
# Net assets (deficiency) 930,822 (10,204)
#
# $ 11,712,950 $ 10,625,605
# Credit facility (note 6)
# Commitments and contingencies (note 11)
# Impacts of COVID-19 (note 14)
#
# See accompanying notes to financial statements.
#
# On behalf of the Board:
#
# , Direct 7 , Director
#
# '''
#
#
#     pp = BSParser(document_text)
#     print(pp.parse())