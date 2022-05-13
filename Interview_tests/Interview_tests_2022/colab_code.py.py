# import pytz as pytz
#
# a = int(input('enter:'))
# if a>1:
#   for i in range(2,a):
#     if a%i==0:
#       print('not prime')
#       break
#
#   else:
#     print('prime')
#
#
# vowels = 'aeiou'
# a_str = 'This is a test string for find the vowels'
# count = {}.fromkeys(vowels,0)
# for i in a_str:
#     if i in count:
#         count[i] += 1
# print(count)
#
# t = (1,2,[4,5])
# print(t,type(t))
# t[2][0] = 6
# print(t[2][0])
#
#
#  meter_reads_hold_reasons = ['My Meter Block Usage mismatch']
#
#  data = {"invoice_record": {
#             "id_ra_customer": 6916,
#             "invoice_number": 8451029284,
#             "start_date": "2020-11-03",
#             "end_date": "2020-12-14",
#             "date_generated": "2020-12-16",
#             "invoice_type": "S",
#             "hold_reason": "My Meter Block Usage mismatch__23",
#             "payment_method": "Credit card",
#             "automated_charges_excl_gst": {},
#             "id": 182456,
#             "calculate_charges_incl_gst": True},
#             "billing_charges_ids": [134455],
#             "washup_charges_ids": [42070],
#             "final_invoice_event_details": {
#                 "id": 1000000001,
#                 "event_date": "2020-02-08",
#                 "final_invoice_customer": True,
#                 "to_be_final_invoice_customer": True,
#                 "is_invoice_final": True
#             }
#         }
#
# # data['invoice_record']['hold_reasons'] = meter_reads_hold_reasons
# if data['invoice_record']['hold_reason']:
#   data['invoice_record']['hold_reason'] = data['invoice_record']['hold_reason'] + ',' + meter_reads_hold_reasons[0]
# print(data['invoice_record']['hold_reason'])
# v=1254963186314785.125488454
# print(round(v,3))
#
# s= 'this is the test string we have'
# vowel_lst = ['a','e','i','o','u']
# d={}
# for i in s:
#    if i in vowel_lst:
#        d[i] = s.count(i)
#
# print(d)
#
# try:
#     customer_id = self.customer_id
# except Exception as e:
#     if hasattr(e, 'code'):
#         error_body = eval(e.body) or ""
#         if error_body and error_body['error'] == 'invalid_token':
#             raise InvalidToken()
#         if not is_secure:
#             customer_id = ''
#         else:
#             assert "", "404"
#
# def add_frac(Frac):
#   fra = Frac.split('+')
#   den = []
#   num = []
#   for i in fra:
#     num.append(int(i.split('/')[0]))
#     den.append(int(i.split('/')[1]))
#   for j in range(len(den)):
#     x = num[j]
#     y = den[j]
#     if x > y:
#       greater = x
#     else:
#       greater = y
#     while (True):
#       if((greater % x == 0) and (greater % y == 0)):
#         lcm = greater
#         break
#     greater += 1
#     res = sum(num)/lcm
#   return res
#
# print(add_frac("2/5+3/5+4/5"))
#
#
#
# regular_consumption_details = {'overall_quality_method': None}
# washup_consumption_details = {'overall_quality_method': 'jhjk'}
#
# overall_method = max(regular_consumption_details.get('overall_quality_method') or '',
#                      washup_consumption_details.get('overall_quality_method') or '')
#
# print(overall_method)
#
# print('==================')
# print(regular_consumption_details.get('overall_quality_method'))
# print( washup_consumption_details.get('overall_quality_method'))
#
# data = {
#   "invoice_details": {
#     "id_ra_customer": [
#       56427,
#       5478587
#     ],
#     "invoice_number": 5781,
#     "start_date": "2020-11-25",
#     "end_date": "2020-12-01",
#     "date_generated": "2020-12-02",
#     "invoice_type": "S",
#     "hold_reason": "jkfasjkfjask jk",
#     "payment_method": "Credit card",
#     "total_to_pay": "100",
#     "date_to_pay": "2020-12-06",
#     "invoice_filename": "",
#     "invoice_status": "I",
#     "billing_charges_ids": [
#       1425,
#       5785
#     ],
#     "washup_charges_ids": [
#       142,
#       457
#     ],
#     "invoice_file": "",
#     "id": 145287,
#     "automated_charges_incl_gst": {
#       "billed_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "washup_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "concessions": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": "",
#         "gst": ""
#       }
#     },
#     "automated_charges_excl_gst": ""
#   },
#   "advance_pay_details": {
#     "statement_id": 1234,
#     "statement_amount": "100.00",
#     "statement_date_to_pay": "2020-12-15",
#     "bill_amount": "50.00",
#     "adjustment": "",
#     "additional_data": {}
#   },
#   "final_invoice_event_details": {
#     "id": 1232,
#     "event_date": "2020-11-25",
#     "final_invoice_customer": "True",
#     "to_be_final_invoice_customer": "True",
#     "is_invoice_final": "True"
#   },
#   "nmi_id": 14,
#   "jurisdiction_code": "NSW"
# }
#
# print(data['invoice_details']['hold_reason'])
# billing_charges_hold_reasons = 'oijijioajiojf kgf2'
# washup_hold_reasons = 'iojnvionoiofgn kgf1'
# invoice_hold_reasons = billing_charges_hold_reasons + washup_hold_reasons + \
#                                data['invoice_details']['hold_reason']
# print(invoice_hold_reasons)
#
# ripe_fruit_comms_config_data = [{'a':12,'b':(123,'Ram'),'c':'123Sai'},{'a':15,'b':(124,'Sai'),'c':'12Navn'}]
#
# for record in ripe_fruit_comms_config_data:
#     record['b'] = record['b'][0]
# print(ripe_fruit_comms_config_data)
#
# ls = [e['b']:e['b'][0] for e in ripe_fruit_comms_config_data if e['b']]
# print(ls)
#
# from datetime import datetime, date
#
# record = {'id': 1, 'id_ra_concession': (8, 'Queensland Government Electricity Rebate'), 'start_date': date.today(), 'end_date': False, 'running_total': False}
#
# from_date = '2020-12-17'
# date_com = datetime.strptime(from_date, '%Y-%m-%d').date()
#
# print(datetime.strptime('2020-12-20', '%Y-%m-%d'))
# start_date = max(date_com, record['start_date'])
# print(start_date)
#
# t = (2,)
# print(type(t))
# t = (2,[1,3,5],0)
# t[1][2] = 10
# print(t)
#
# from datetime import datetime
#
# record = {'id': 1, 'id_ra_concession': (8, 'Queensland Government Electricity Rebate'), 'start_date': datetime.date(2019, 1, 18), 'end_date': False, 'running_total': False}
# print(record[start_date])
# from_date = '2020-12-17'
# date_com = datetime.strptime(data['tradedate'], '%d/%m/%Y').date()
# print(date_com)
# start_date = max(from_date, record['start_date'])
# print(start_date)
#
# from datetime import datetime
#
# print(datetime.today().strftime('%Y-%m-%d %H:%M:%S'), type(datetime.today().strftime('%Y%m%d%H%M%S%f')))
#
#  import ast
#
#  def _is_washup_resulting_in_account_in_credit(invoice_record):
#         overcharge_threshold_value = 50
#         threshold_amount = -(overcharge_threshold_value and float(overcharge_threshold_value) or 50)
#         automated_charges = invoice_record['automated_charges_excl_gst'] or \
#                                      invoice_record['automated_charges_incl_gst']
#         print(automated_charges)
#         if isinstance(automated_charges, str):
#             print('Laalamilaaa')
#         if not automated_charges:
#             return False
#         if int(invoice_record['total_to_pay']) <= threshold_amount and \
#                 automated_charges['washup_charges']['rounded'] <= threshold_amount:
#             return True
#         return False
#
# ad = {
#   "invoice_details": {
#     "id_ra_customer": [
#       56427,
#       5478587
#     ],
#     "invoice_number": 5781,
#     "start_date": "2020-11-25",
#     "end_date": "2020-12-01",
#     "date_generated": "2020-12-02",
#     "invoice_type": "S",
#     "hold_reason": "",
#     "payment_method": "Credit card",
#     "total_to_pay": "100",
#     "date_to_pay": "2020-12-06",
#     "invoice_filename": "",
#     "invoice_status": "I",
#     "billing_charges_ids": [
#       1425,
#       5785
#     ],
#     "washup_charges_ids": [
#       142,
#       457
#     ],
#     "invoice_file": "",
#     "id": 145287,
#     "automated_charges_incl_gst": {
#       "billed_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "washup_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "concessions": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": "",
#         "gst": ""
#       }
#     },
#     "automated_charges_excl_gst": "jhgjhgjg"
#   },
# }
#
# inv = ad['invoice_details']
# print(inv)
# print(type(inv['automated_charges_incl_gst']))
# print('=========================================================')
# pr = _is_washup_resulting_in_account_in_credit(inv)
# print(pr)
#
# import math
#
# def sphere_volume(rad):
#   """This function will calculate the volume of a sphere"""
#   volume = 4/3*math.pi*pow(rad,3)
#   return round(volume)
#
# radius = int(input('Enter the radius(in number) of sphere : '))
# volume_of_sphere = sphere_volume(radius)
# print(volume_of_sphere)
#
# def get_remainder_basic_ops(dividend, divisor):
#   number = dividend/divisor
#   number_dec = (number-int(number))*divisor
#   return number_dec
#
# def get_remainder_divmod(divisor,dividend):
#   que,rem = divmod(divisor,dividend)
#   return rem
#
# print(get_remainder_divmod(15,4))
#
#
# def get_remainder_basic_ops(dividend, divisor):
#   number = dividend/divisor
#   number_dec = (number-int(number))*divisor
#   return number_dec
#
# def get_remainder_divmod(divisor,dividend):
#   que,rem = divmod(divisor,dividend)
#   return rem
#
# def get_remainder_mod(divisor,dividend):
#   rem = divisor % dividend
#   return rem
#
# divisor = int(input('Enter a divisor(interger values) :' ))
# dividend = int(input('Enter a dividend(interger values) : '))
# print(get_remainder_basic_ops(divisor,dividend))
# print(get_remainder_divmod(divisor,dividend))
# print(get_remainder_mod(divisor,dividend))
#
#
# from datetime import datetime
# to_date = '2021-05-15'
# d = datetime.strptime(to_date, '%Y-%m-%d').date()
# print(d)
#
# # a = [1,2,8,9,4,6]
# # n = len(a)
# # for i in range(n,-1,-1):
# #   print(i, n)
# # heapify
# def heapify(arr, n, i):
#    largest = i # largest value
#    l = 2 * i + 1 # left
#    r = 2 * i + 2 # right
#    # if left child exists
#    if l < n and arr[i] < arr[l]:
#       largest = l
#    # if right child exits
#    if r < n and arr[largest] < arr[r]:
#       largest = r
#    # root
#    if largest != i:
#       arr[i],arr[largest] = arr[largest],arr[i] # swap
#       # root.
#       heapify(arr, n, largest)
# # sort
# def heapSort(arr):
#    n = len(arr)
#    # maxheap
#    for i in range(n, -1, -1):
#       heapify(arr, n, i)
#    # element extraction
#    for i in range(n-1, 0, -1):
#       arr[i], arr[0] = arr[0], arr[i] # swap
#       heapify(arr, i, 0)
# # main
# arr = [2,5,3,8,6,5,4,7]
# heapSort(arr)
# n = len(arr)
# print ("Sorted array is")
# for i in range(n):
#    print (arr[i],end=" ")
#
# from datetime import datetime, date
# from dateutil.relativedelta import relativedelta
#
# billing_status_record = {}
# to_date = '2021-03-15'
# d = datetime.strptime(to_date, '%Y-%m-%d').date()
# billing_status_record['start_date'] = d
# print(billing_status_record)
# current_date = date.today()
# print(current_date)
# print(billing_status_record['start_date'] + relativedelta(months=1))
# if current_date >= billing_status_record['start_date'] + relativedelta(months=1):
#   print('we in if condition')
#
# from datetime import datetime, date
# from dateutil.relativedelta import relativedelta
#
#
# current_date = date.today()
# dat = current_date - relativedelta(months=6)
# print(current_date)
# print(dat)
#
# from datetime import datetime, date
#
# st, ed = '2021-02-10', '2021-06-10'
# # st_d = datetime.strptime(str(2021-02-10), '%Y-%m-%d').date()
# # en_d = datetime.strptime(str(ed or '9999-12-31'), '%Y-%m-%d').date()
# record = {'start_date':st, 'end_date':ed}
# existing_record = {'start_date':st, 'end_date':ed}
#
# existing_record_start_date = datetime.strptime(str(existing_record['start_date']), '%Y-%m-%d').date()
# existing_record_end_date = datetime.strptime(str(existing_record['end_date'] or '9999-12-31'), '%Y-%m-%d').date()
# event_start_date = datetime.strptime(record['start_date'], '%Y-%m-%d').date()
# event_end_date = datetime.strptime(record['end_date'], '%Y-%m-%d').date()
# print(existing_record_start_date, existing_record_end_date)
# print(event_start_date, event_end_date)
#
#
# def arrang_fun(l):
#   count = 0
#   for i in range(len(l)-1):
#     if (l[i],l[i+1]) == (0,1) or (l[i],l[i+1]) == (1,0):
#       count += count
#     else:
#       count += 1
#   return count
#
# a = [1,1,1,0,1,1,1]
# print(arrang_fun(a))
#
# ls = [16597327,16608286,14936719,14881619,14828479,14775293,14718160,14661798,14607322,14552385,14500896,14447471,14397073,14338495,14288837,14233931,14182368,14113095,14075533,14031215,13977395,
# 13926531,13874378,13821544,13773527,13725676,13678888,13627162,13578152,13527651,13478425,13428013,13383116,13337336,13286399,13238349,13187916,13140908,13092549,13047334,13002750,12951101,12906352,12858884,
# 12811590,12766691,12722875,12677774,12630779,12582973,12537951,12492026,12445756,12402881,12359987,12314738,12269636,12224255,12179523,12136641,12095196,12053521,12009825,11966174,11921038,11878896,11836321,
# 11795787,11755182,11697101,11659780,11624027,11583573,16549173,16733774,16857172,16917761,16979468,17112553,17171000]
# print(len(ls))
# print(len(set(ls)))
#
# qm = [['A'], ['A'], ['A'], ['V'], ['V', 'V'], ['V', 'V'], ['V'], ['V'], ['V'], ['V'], ['V'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A']]
#
# l = round(sum([float(len(i) - i.count('A'))/float(len(i)) for i in qm]),2)
# print(l)
# # m1 = [i for i in qm if len(i) != 1]
# # # print(m1)
# # l1 = sum([1 for i in m1 if len(set(i))==1])
# # print(l1)
# # print(l + l1)
#
#
# emp = ''
# print(len(emp.strip().split(',')),len([]))
#
# con = {'final_invoice': {'transfer_confirmed_final_invoice': False}, 'invoice_billed': True}
# print(not(con.get('final_invoice')['transfer_confirmed_final_invoice']) or (not context.get('invoice_billed')))
#
#
#
#
# from enum import Enum
#
# class NestApi(object):
#     def __init__(self, module_name):
#         self.logger = print(module_name)
#         self.message_code_model = None
#
#     def nest_assert(self, condition, error):
#         if not condition:
#             raise ValueError(error)
#
#
# class ServiceLanguageErrors(Enum):
#     """
#     Service Language Error Code
#     """
#     generic_error = 190
#     default_language_error = 191
#     version_error = 192
#
#
# class Language(NestApi):
#     """
#     core_model represents language_language
#     """
#     def __init__(self):
#         super().__init__(__name__)
#         self.__core_model = None
#         self.use_cr2 = False
#
#     def get_language_data(self, client, code, version, mode):
#         """
#         Method used to the language data with version, mode, code and client
#         @param client: id of the customer
#         @param code: Language code like en, du, sp
#         @param version: client version (client can be determined by x-client)
#         @param mode: mode which determines to fetch data from models or from cache (preview| prod)
#         @return: Language json data
#         """
#         # _method_name = self.__class__.__name__ + ":" + "get_language_data"
#         # language_model = self.core_model
#         # client_model = language_model.env.get('client')
#         service_language_errors = ServiceLanguageErrors(190)
#         try:
#             language_set = 0
#             if not language_set:
#                 # language_set = language_model.search([('is_default', '=', True)])
#                 default_language = [{'id': 5, 'code': 'en'}]
#                 self.nest_assert(not default_language, service_language_errors.default_language_error)
#                 code = default_language[0]['code']
#                 print('dgereegsssfdsd')
#         except Exception as e:
#             print(f":: Failed to get language code")
#
#
# se = Language()
# se.get_language_data('ra_web','','','')
#
# from datetime import datetime
#
# time_zone =  'Australia/Victoria'
# time_zone_obj = pytz.timezone(time_zone)
# d = datetime.now(time_zone_obj).strftime('%Y-%m-%d %H:%M:%S')
# print(d)
#
# import pytz
# t = pytz.all_timezones
# print(t)
# for i in t:
#   if i == 'Australia/Victoria':
#     print(i,type(i))
#
# lst,pair = [5,2,3,9,1], 0
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if(j <= i ): continue
#         if((lst[i] + lst[j]) == 10):
#             pair +=1
#             print("[%s, %s]" % (lst[i], lst[j]))
# print("number of pair = %s" % pair)
#
# l, sum = [1,2,3,7,8,9,7,10,20], 10
# while l:
#   num = l.pop()
#   diff = sum - num
#   if diff in l:
#     print((num,diff))
#
# from functools import reduce
# old_list = [1,8,9,5,6]
# doubled_list = list(map(lambda x: x * 2, old_list))
# print(doubled_list)
# print(reduce(lambda x,y: x+y, old_list))
#
# from functools import reduce
#
# l = [1,2,3,4,5,6]
# def sum_sq(l):
#   sq = [n**2 for n in l]
#   return sq
#
# print(list(reduce(lambda x,y: x+y,i) for i in [[1,2,3,4],[5,6,7,8]]))
# print(reduce(lambda x,y: x+y,l))
# gen = (var**(1/2) for var in l)
# print(list(gen))
#
# def fib(n):
#   t1,t2 = 0, 1
#   while n>0:
#     tn = t1+t2
#     t1,t2 = t2,tn
#     n -= 1
#     yield tn
#
#
# n = 5
# print(set(fib(n)))
#
#
# def my_deco(func):
#   def wrapper(*args,**kwargs):
#     print('before func call: ')
#     args = list(ar*2 for ar in args)
#     res = func(*args,**kwargs)
#     print('args: ', args)
#     print('kwargs: ', kwargs)
#     print('after func call: ', res*2)
#     return res
#   return wrapper
#
# @my_deco
# def f1(*args,**kwargs):
#   return args,kwargs
#
# f1(1,3,4,5,a=2,b=6)
#
# from itertools import combinations
#
# l, sum = [1,2,3,7,8,9,7,10,20], 10
# com_lst = list(combinations(l,3))
# # for i in com_lst:
# #   print(i, type(i)
# # req_lst = list(ele for ele in com_lst if sum(ele)==10)
# # print(req_lst, len(req_l))
# def type_fn(lst):
#   l =
# print(map(type_fn, com_lst))
#
#
# def sockMerchant(n, ar):
#     x=[]
#     ar.sort()
#     while len(ar)>1:
#       if ar[0]==ar[1]:
#         x.append(ar[:2])
#         del ar[:2]
#       else:
#         del ar[0]
#     return len(x)
#
#
# n = 7
# a = [1,2,1,2,1,3,2]
# a1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# r = sockMerchant(n,a1)
# print(r)
#
# import re
#
# st = 'DDUUDDUDUUUD'
# l1, l2 = [], []
# ls1 = [i for i in st]
# ls2 = [k for k in st]
# while len(ls1)>1:
#   pr = ''.join(ls1[:4])
#   if pr in ('DDUU','UUDD'):
#     l1.append(pr)
#     del ls1[:4]
#   else:
#     del ls1[0]
# while len(ls2)>1:
#   pr = ''.join(ls2[:2])
#   if pr in ('DU','UD'):
#     l2.append(pr)
#     del ls2[:2]
#   else:
#     del ls2[0]
# if l1 and (len(l1) >= len(l2)):
#   print(l1, len(l1))
# else:
#   print(l2, len(l2))
#
#
# # N=int(input())
# S='DDUUDDUDUUUD'
# L=V=0
# for s in S:
#     if s == 'U':
#         L += 1
#         if L == 0:
#             V += 1
#     else:
#         L -= 1
#
# print('V: ',V)
#
# import copy
#
# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = copy.copy(old_list)
#
# print("==============copy (shallow copy=================")
# print("Old list:", old_list, id(old_list))
# print("New list:", new_list, id(new_list))
#
# print('=================================')
# old_list.append(['Navn'])
# print("Old list:", old_list, id(old_list))
# print("New list:", new_list, id(new_list))
#
#
# print('==================Deep copy=====================')
# old_list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list1 = copy.deepcopy(old_list1)
#
# print("Old list1:", old_list1, id(old_list1))
# print("New list1:", new_list1, id(new_list1))
#
# print('==========================================')
# old_list1.append(['Ram'])
# print()
# print("Old list:", old_list1, id(old_list1))
# print("New list:", new_list1, id(new_list1))
#
#
#
# n = 5
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(j,end='')
#   print()
# for i in range(n,1,-1):
#   for k in range(1,i):
#     print(k,end='')
#   print()
#
# for idx in range(n-1):
#     print((n-idx) * ' ' + (2*idx+1) * '*')
# for idx in range(n-1, -1, -1):
#     print((n-idx) * ' ' + (2*idx+1) * '*')
#
# a = ['a','b','c']
# b = [1,2,3]
# d = {}
# for key, value in zip(a,b):
#   d[key] = value
# print(d)
#
# string = 'madam'
# rev = ''
# for i in string:
#   rev = i + rev
# if rev == string:
#   print('pallenfrome')
# else:
#   print('Not pallendrome')
#
# n = 98089
# temp = n
# rev = 0
# while n > 0:
#   rem = n%10
#   rev = rev*10 + rem
#   n = n//10
# if rev == temp:
#   print('pallenfrome')
# else:
#   print('Not pallendrome')
#
#
# # a = 1.37
# # st = str(a)
# # f = float(a)
# # print(f,type(f))
# s = 'GreenPower25%'
# print(s,type(s))
# l = [s.isdecimal()]
# print(s.isdecimal(), l)
# # if s.isdecimal:
# #   print('True')
# # else:
# #   print('False')
#
#
#
# a = int(input('enter:'))
# if a>1:
#   for i in range(2,a):
#     if a%i==0:
#       print('not prime')
#       break
#
#   else:
#     print('prime')
#
#
# vowels = 'aeiou'
# a_str = 'This is a test string for find the vowels'
# count = {}.fromkeys(vowels,0)
# for i in a_str:
#     if i in count:
#         count[i] += 1
# print(count)
#
# t = (1,2,[4,5])
# print(t,type(t))
# t[2][0] = 6
# print(t[2][0])
#
#
#  meter_reads_hold_reasons = ['My Meter Block Usage mismatch']
#
#  data = {"invoice_record": {
#             "id_ra_customer": 6916,
#             "invoice_number": 8451029284,
#             "start_date": "2020-11-03",
#             "end_date": "2020-12-14",
#             "date_generated": "2020-12-16",
#             "invoice_type": "S",
#             "hold_reason": "My Meter Block Usage mismatch__23",
#             "payment_method": "Credit card",
#             "automated_charges_excl_gst": {},
#             "id": 182456,
#             "calculate_charges_incl_gst": True},
#             "billing_charges_ids": [134455],
#             "washup_charges_ids": [42070],
#             "final_invoice_event_details": {
#                 "id": 1000000001,
#                 "event_date": "2020-02-08",
#                 "final_invoice_customer": True,
#                 "to_be_final_invoice_customer": True,
#                 "is_invoice_final": True
#             }
#         }
#
# # data['invoice_record']['hold_reasons'] = meter_reads_hold_reasons
# if data['invoice_record']['hold_reason']:
#   data['invoice_record']['hold_reason'] = data['invoice_record']['hold_reason'] + ',' + meter_reads_hold_reasons[0]
# print(data['invoice_record']['hold_reason'])
# v=1254963186314785.125488454
# print(round(v,3))
#
# s= 'this is the test string we have'
# vowel_lst = ['a','e','i','o','u']
# d={}
# for i in s:
#    if i in vowel_lst:
#        d[i] = s.count(i)
#
# print(d)
#
# try:
#     customer_id = self.customer_id
# except Exception as e:
#     if hasattr(e, 'code'):
#         error_body = eval(e.body) or ""
#         if error_body and error_body['error'] == 'invalid_token':
#             raise InvalidToken()
#         if not is_secure:
#             customer_id = ''
#         else:
#             assert "", "404"
#
# def add_frac(Frac):
#   fra = Frac.split('+')
#   den = []
#   num = []
#   for i in fra:
#     num.append(int(i.split('/')[0]))
#     den.append(int(i.split('/')[1]))
#   for j in range(len(den)):
#     x = num[j]
#     y = den[j]
#     if x > y:
#       greater = x
#     else:
#       greater = y
#     while (True):
#       if((greater % x == 0) and (greater % y == 0)):
#         lcm = greater
#         break
#     greater += 1
#     res = sum(num)/lcm
#   return res
#
# print(add_frac("2/5+3/5+4/5"))
#
#
#
# regular_consumption_details = {'overall_quality_method': None}
# washup_consumption_details = {'overall_quality_method': 'jhjk'}
#
# overall_method = max(regular_consumption_details.get('overall_quality_method') or '',
#                      washup_consumption_details.get('overall_quality_method') or '')
#
# print(overall_method)
#
# print('==================')
# print(regular_consumption_details.get('overall_quality_method'))
# print( washup_consumption_details.get('overall_quality_method'))
#
# data = {
#   "invoice_details": {
#     "id_ra_customer": [
#       56427,
#       5478587
#     ],
#     "invoice_number": 5781,
#     "start_date": "2020-11-25",
#     "end_date": "2020-12-01",
#     "date_generated": "2020-12-02",
#     "invoice_type": "S",
#     "hold_reason": "jkfasjkfjask jk",
#     "payment_method": "Credit card",
#     "total_to_pay": "100",
#     "date_to_pay": "2020-12-06",
#     "invoice_filename": "",
#     "invoice_status": "I",
#     "billing_charges_ids": [
#       1425,
#       5785
#     ],
#     "washup_charges_ids": [
#       142,
#       457
#     ],
#     "invoice_file": "",
#     "id": 145287,
#     "automated_charges_incl_gst": {
#       "billed_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "washup_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "concessions": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": "",
#         "gst": ""
#       }
#     },
#     "automated_charges_excl_gst": ""
#   },
#   "advance_pay_details": {
#     "statement_id": 1234,
#     "statement_amount": "100.00",
#     "statement_date_to_pay": "2020-12-15",
#     "bill_amount": "50.00",
#     "adjustment": "",
#     "additional_data": {}
#   },
#   "final_invoice_event_details": {
#     "id": 1232,
#     "event_date": "2020-11-25",
#     "final_invoice_customer": "True",
#     "to_be_final_invoice_customer": "True",
#     "is_invoice_final": "True"
#   },
#   "nmi_id": 14,
#   "jurisdiction_code": "NSW"
# }
#
# print(data['invoice_details']['hold_reason'])
# billing_charges_hold_reasons = 'oijijioajiojf kgf2'
# washup_hold_reasons = 'iojnvionoiofgn kgf1'
# invoice_hold_reasons = billing_charges_hold_reasons + washup_hold_reasons + \
#                                data['invoice_details']['hold_reason']
# print(invoice_hold_reasons)
#
# ripe_fruit_comms_config_data = [{'a':12,'b':(123,'Ram'),'c':'123Sai'},{'a':15,'b':(124,'Sai'),'c':'12Navn'}]
#
# for record in ripe_fruit_comms_config_data:
#     record['b'] = record['b'][0]
# print(ripe_fruit_comms_config_data)
#
# ls = [e['b']:e['b'][0] for e in ripe_fruit_comms_config_data if e['b']]
# print(ls)
#
# from datetime import datetime, date
#
# record = {'id': 1, 'id_ra_concession': (8, 'Queensland Government Electricity Rebate'), 'start_date': date.today(), 'end_date': False, 'running_total': False}
#
# from_date = '2020-12-17'
# date_com = datetime.strptime(from_date, '%Y-%m-%d').date()
#
# print(datetime.strptime('2020-12-20', '%Y-%m-%d'))
# start_date = max(date_com, record['start_date'])
# print(start_date)
#
# t = (2,)
# print(type(t))
# t = (2,[1,3,5],0)
# t[1][2] = 10
# print(t)
#
# from datetime import datetime
#
# record = {'id': 1, 'id_ra_concession': (8, 'Queensland Government Electricity Rebate'), 'start_date': datetime.date(2019, 1, 18), 'end_date': False, 'running_total': False}
# print(record[start_date])
# from_date = '2020-12-17'
# date_com = datetime.strptime(data['tradedate'], '%d/%m/%Y').date()
# print(date_com)
# start_date = max(from_date, record['start_date'])
# print(start_date)
#
# from datetime import datetime
#
# print(datetime.today().strftime('%Y-%m-%d %H:%M:%S'), type(datetime.today().strftime('%Y%m%d%H%M%S%f')))
#
#  import ast
#
#  def _is_washup_resulting_in_account_in_credit(invoice_record):
#         overcharge_threshold_value = 50
#         threshold_amount = -(overcharge_threshold_value and float(overcharge_threshold_value) or 50)
#         automated_charges = invoice_record['automated_charges_excl_gst'] or \
#                                      invoice_record['automated_charges_incl_gst']
#         print(automated_charges)
#         if isinstance(automated_charges, str):
#             print('Laalamilaaa')
#         if not automated_charges:
#             return False
#         if int(invoice_record['total_to_pay']) <= threshold_amount and \
#                 automated_charges['washup_charges']['rounded'] <= threshold_amount:
#             return True
#         return False
#
# ad = {
#   "invoice_details": {
#     "id_ra_customer": [
#       56427,
#       5478587
#     ],
#     "invoice_number": 5781,
#     "start_date": "2020-11-25",
#     "end_date": "2020-12-01",
#     "date_generated": "2020-12-02",
#     "invoice_type": "S",
#     "hold_reason": "",
#     "payment_method": "Credit card",
#     "total_to_pay": "100",
#     "date_to_pay": "2020-12-06",
#     "invoice_filename": "",
#     "invoice_status": "I",
#     "billing_charges_ids": [
#       1425,
#       5785
#     ],
#     "washup_charges_ids": [
#       142,
#       457
#     ],
#     "invoice_file": "",
#     "id": 145287,
#     "automated_charges_incl_gst": {
#       "billed_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "washup_charges": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": ""
#       },
#       "concessions": {
#         "unrounded_and_gst_applicable": "",
#         "rounded": "",
#         "gst": ""
#       }
#     },
#     "automated_charges_excl_gst": "jhgjhgjg"
#   },
# }
#
# inv = ad['invoice_details']
# print(inv)
# print(type(inv['automated_charges_incl_gst']))
# print('=========================================================')
# pr = _is_washup_resulting_in_account_in_credit(inv)
# print(pr)
#
# import math
#
# def sphere_volume(rad):
#   """This function will calculate the volume of a sphere"""
#   volume = 4/3*math.pi*pow(rad,3)
#   return round(volume)
#
# radius = int(input('Enter the radius(in number) of sphere : '))
# volume_of_sphere = sphere_volume(radius)
# print(volume_of_sphere)
#
# def get_remainder_basic_ops(dividend, divisor):
#   number = dividend/divisor
#   number_dec = (number-int(number))*divisor
#   return number_dec
#
# def get_remainder_divmod(divisor,dividend):
#   que,rem = divmod(divisor,dividend)
#   return rem
#
# print(get_remainder_divmod(15,4))
#
#
# def get_remainder_basic_ops(dividend, divisor):
#   number = dividend/divisor
#   number_dec = (number-int(number))*divisor
#   return number_dec
#
# def get_remainder_divmod(divisor,dividend):
#   que,rem = divmod(divisor,dividend)
#   return rem
#
# def get_remainder_mod(divisor,dividend):
#   rem = divisor % dividend
#   return rem
#
# divisor = int(input('Enter a divisor(interger values) :' ))
# dividend = int(input('Enter a dividend(interger values) : '))
# print(get_remainder_basic_ops(divisor,dividend))
# print(get_remainder_divmod(divisor,dividend))
# print(get_remainder_mod(divisor,dividend))
#
#
# from datetime import datetime
# to_date = '2021-05-15'
# d = datetime.strptime(to_date, '%Y-%m-%d').date()
# print(d)
#
# # a = [1,2,8,9,4,6]
# # n = len(a)
# # for i in range(n,-1,-1):
# #   print(i, n)
# # heapify
# def heapify(arr, n, i):
#    largest = i # largest value
#    l = 2 * i + 1 # left
#    r = 2 * i + 2 # right
#    # if left child exists
#    if l < n and arr[i] < arr[l]:
#       largest = l
#    # if right child exits
#    if r < n and arr[largest] < arr[r]:
#       largest = r
#    # root
#    if largest != i:
#       arr[i],arr[largest] = arr[largest],arr[i] # swap
#       # root.
#       heapify(arr, n, largest)
# # sort
# def heapSort(arr):
#    n = len(arr)
#    # maxheap
#    for i in range(n, -1, -1):
#       heapify(arr, n, i)
#    # element extraction
#    for i in range(n-1, 0, -1):
#       arr[i], arr[0] = arr[0], arr[i] # swap
#       heapify(arr, i, 0)
# # main
# arr = [2,5,3,8,6,5,4,7]
# heapSort(arr)
# n = len(arr)
# print ("Sorted array is")
# for i in range(n):
#    print (arr[i],end=" ")
#
# from datetime import datetime, date
# from dateutil.relativedelta import relativedelta
#
# billing_status_record = {}
# to_date = '2021-03-15'
# d = datetime.strptime(to_date, '%Y-%m-%d').date()
# billing_status_record['start_date'] = d
# print(billing_status_record)
# current_date = date.today()
# print(current_date)
# print(billing_status_record['start_date'] + relativedelta(months=1))
# if current_date >= billing_status_record['start_date'] + relativedelta(months=1):
#   print('we in if condition')
#
# from datetime import datetime, date
# from dateutil.relativedelta import relativedelta
#
#
# current_date = date.today()
# dat = current_date - relativedelta(months=6)
# print(current_date)
# print(dat)
#
# from datetime import datetime, date
#
# st, ed = '2021-02-10', '2021-06-10'
# # st_d = datetime.strptime(str(2021-02-10), '%Y-%m-%d').date()
# # en_d = datetime.strptime(str(ed or '9999-12-31'), '%Y-%m-%d').date()
# record = {'start_date':st, 'end_date':ed}
# existing_record = {'start_date':st, 'end_date':ed}
#
# existing_record_start_date = datetime.strptime(str(existing_record['start_date']), '%Y-%m-%d').date()
# existing_record_end_date = datetime.strptime(str(existing_record['end_date'] or '9999-12-31'), '%Y-%m-%d').date()
# event_start_date = datetime.strptime(record['start_date'], '%Y-%m-%d').date()
# event_end_date = datetime.strptime(record['end_date'], '%Y-%m-%d').date()
# print(existing_record_start_date, existing_record_end_date)
# print(event_start_date, event_end_date)
#
#
# def arrang_fun(l):
#   count = 0
#   for i in range(len(l)-1):
#     if (l[i],l[i+1]) == (0,1) or (l[i],l[i+1]) == (1,0):
#       count += count
#     else:
#       count += 1
#   return count
#
# a = [1,1,1,0,1,1,1]
# print(arrang_fun(a))
#
# ls = [16597327,16608286,14936719,14881619,14828479,14775293,14718160,14661798,14607322,14552385,14500896,14447471,14397073,14338495,14288837,14233931,14182368,14113095,14075533,14031215,13977395,
# 13926531,13874378,13821544,13773527,13725676,13678888,13627162,13578152,13527651,13478425,13428013,13383116,13337336,13286399,13238349,13187916,13140908,13092549,13047334,13002750,12951101,12906352,12858884,
# 12811590,12766691,12722875,12677774,12630779,12582973,12537951,12492026,12445756,12402881,12359987,12314738,12269636,12224255,12179523,12136641,12095196,12053521,12009825,11966174,11921038,11878896,11836321,
# 11795787,11755182,11697101,11659780,11624027,11583573,16549173,16733774,16857172,16917761,16979468,17112553,17171000]
# print(len(ls))
# print(len(set(ls)))
#
# qm = [['A'], ['A'], ['A'], ['V'], ['V', 'V'], ['V', 'V'], ['V'], ['V'], ['V'], ['V'], ['V'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A'], ['A']]
#
# l = round(sum([float(len(i) - i.count('A'))/float(len(i)) for i in qm]),2)
# print(l)
# # m1 = [i for i in qm if len(i) != 1]
# # # print(m1)
# # l1 = sum([1 for i in m1 if len(set(i))==1])
# # print(l1)
# # print(l + l1)
#
#
# emp = ''
# print(len(emp.strip().split(',')),len([]))
#
# con = {'final_invoice': {'transfer_confirmed_final_invoice': False}, 'invoice_billed': True}
# print(not(con.get('final_invoice')['transfer_confirmed_final_invoice']) or (not context.get('invoice_billed')))
#
#
#
#
# from enum import Enum
#
# class NestApi(object):
#     def __init__(self, module_name):
#         self.logger = print(module_name)
#         self.message_code_model = None
#
#     def nest_assert(self, condition, error):
#         if not condition:
#             raise ValueError(error)
#
#
# class ServiceLanguageErrors(Enum):
#     """
#     Service Language Error Code
#     """
#     generic_error = 190
#     default_language_error = 191
#     version_error = 192
#
#
# class Language(NestApi):
#     """
#     core_model represents language_language
#     """
#     def __init__(self):
#         super().__init__(__name__)
#         self.__core_model = None
#         self.use_cr2 = False
#
#     def get_language_data(self, client, code, version, mode):
#         """
#         Method used to the language data with version, mode, code and client
#         @param client: id of the customer
#         @param code: Language code like en, du, sp
#         @param version: client version (client can be determined by x-client)
#         @param mode: mode which determines to fetch data from models or from cache (preview| prod)
#         @return: Language json data
#         """
#         # _method_name = self.__class__.__name__ + ":" + "get_language_data"
#         # language_model = self.core_model
#         # client_model = language_model.env.get('client')
#         service_language_errors = ServiceLanguageErrors(190)
#         try:
#             language_set = 0
#             if not language_set:
#                 # language_set = language_model.search([('is_default', '=', True)])
#                 default_language = [{'id': 5, 'code': 'en'}]
#                 self.nest_assert(not default_language, service_language_errors.default_language_error)
#                 code = default_language[0]['code']
#                 print('dgereegsssfdsd')
#         except Exception as e:
#             print(f":: Failed to get language code")
#
#
# se = Language()
# se.get_language_data('ra_web','','','')
#
# from datetime import datetime
#
# time_zone =  'Australia/Victoria'
# time_zone_obj = pytz.timezone(time_zone)
# d = datetime.now(time_zone_obj).strftime('%Y-%m-%d %H:%M:%S')
# print(d)
#
# import pytz
# t = pytz.all_timezones
# print(t)
# for i in t:
#   if i == 'Australia/Victoria':
#     print(i,type(i))
#
# lst,pair = [5,2,3,9,1], 0
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if(j <= i ): continue
#         if((lst[i] + lst[j]) == 10):
#             pair +=1
#             print("[%s, %s]" % (lst[i], lst[j]))
# print("number of pair = %s" % pair)
#
# l, sum = [1,2,3,7,8,9,7,10,20], 10
# while l:
#   num = l.pop()
#   diff = sum - num
#   if diff in l:
#     print((num,diff))
#
# from functools import reduce
# old_list = [1,8,9,5,6]
# doubled_list = list(map(lambda x: x * 2, old_list))
# print(doubled_list)
# print(reduce(lambda x,y: x+y, old_list))
#
# from functools import reduce
#
# l = [1,2,3,4,5,6]
# def sum_sq(l):
#   sq = [n**2 for n in l]
#   return sq
#
# print(list(reduce(lambda x,y: x+y,i) for i in [[1,2,3,4],[5,6,7,8]]))
# print(reduce(lambda x,y: x+y,l))
# gen = (var**(1/2) for var in l)
# print(list(gen))
#
# def fib(n):
#   t1,t2 = 0, 1
#   while n>0:
#     tn = t1+t2
#     t1,t2 = t2,tn
#     n -= 1
#     yield tn
#
#
# n = 5
# print(set(fib(n)))
#
#
# def my_deco(func):
#   def wrapper(*args,**kwargs):
#     print('before func call: ')
#     args = list(ar*2 for ar in args)
#     res = func(*args,**kwargs)
#     print('args: ', args)
#     print('kwargs: ', kwargs)
#     print('after func call: ', res*2)
#     return res
#   return wrapper
#
# @my_deco
# def f1(*args,**kwargs):
#   return args,kwargs
#
# f1(1,3,4,5,a=2,b=6)
#
# from itertools import combinations
#
# l, sum = [1,2,3,7,8,9,7,10,20], 10
# com_lst = list(combinations(l,3))
# # for i in com_lst:
# #   print(i, type(i)
# # req_lst = list(ele for ele in com_lst if sum(ele)==10)
# # print(req_lst, len(req_l))
# def type_fn(lst):
#   l =
# print(map(type_fn, com_lst))
#
#
# def sockMerchant(n, ar):
#     x=[]
#     ar.sort()
#     while len(ar)>1:
#       if ar[0]==ar[1]:
#         x.append(ar[:2])
#         del ar[:2]
#       else:
#         del ar[0]
#     return len(x)
#
#
# n = 7
# a = [1,2,1,2,1,3,2]
# a1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# r = sockMerchant(n,a1)
# print(r)
#
# import re
#
# st = 'DDUUDDUDUUUD'
# l1, l2 = [], []
# ls1 = [i for i in st]
# ls2 = [k for k in st]
# while len(ls1)>1:
#   pr = ''.join(ls1[:4])
#   if pr in ('DDUU','UUDD'):
#     l1.append(pr)
#     del ls1[:4]
#   else:
#     del ls1[0]
# while len(ls2)>1:
#   pr = ''.join(ls2[:2])
#   if pr in ('DU','UD'):
#     l2.append(pr)
#     del ls2[:2]
#   else:
#     del ls2[0]
# if l1 and (len(l1) >= len(l2)):
#   print(l1, len(l1))
# else:
#   print(l2, len(l2))
#
#
# # N=int(input())
# S='DDUUDDUDUUUD'
# L=V=0
# for s in S:
#     if s == 'U':
#         L += 1
#         if L == 0:
#             V += 1
#     else:
#         L -= 1
#
# print('V: ',V)
#
# import copy
#
# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = copy.copy(old_list)
#
# print("==============copy (shallow copy=================")
# print("Old list:", old_list, id(old_list))
# print("New list:", new_list, id(new_list))
#
# print('=================================')
# old_list.append(['Navn'])
# print("Old list:", old_list, id(old_list))
# print("New list:", new_list, id(new_list))
#
#
# print('==================Deep copy=====================')
# old_list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list1 = copy.deepcopy(old_list1)
#
# print("Old list1:", old_list1, id(old_list1))
# print("New list1:", new_list1, id(new_list1))
#
# print('==========================================')
# old_list1.append(['Ram'])
# print()
# print("Old list:", old_list1, id(old_list1))
# print("New list:", new_list1, id(new_list1))
#
#
#
# n = 5
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(j,end='')
#   print()
# for i in range(n,1,-1):
#   for k in range(1,i):
#     print(k,end='')
#   print()
#
# for idx in range(n-1):
#     print((n-idx) * ' ' + (2*idx+1) * '*')
# for idx in range(n-1, -1, -1):
#     print((n-idx) * ' ' + (2*idx+1) * '*')
#
# a = ['a','b','c']
# b = [1,2,3]
# d = {}
# for key, value in zip(a,b):
#   d[key] = value
# print(d)
#
# string = 'madam'
# rev = ''
# for i in string:
#   rev = i + rev
# if rev == string:
#   print('pallenfrome')
# else:
#   print('Not pallendrome')
#
# n = 98089
# temp = n
# rev = 0
# while n > 0:
#   rem = n%10
#   rev = rev*10 + rem
#   n = n//10
# if rev == temp:
#   print('pallenfrome')
# else:
#   print('Not pallendrome')
#
#
# # a = 1.37
# # st = str(a)
# # f = float(a)
# # print(f,type(f))
# s = 'GreenPower25%'
# print(s,type(s))
# l = [s.isdecimal()]
# print(s.isdecimal(), l)
# # if s.isdecimal:
# #   print('True')
# # else:
# #   print('False')
#
