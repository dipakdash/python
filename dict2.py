#employee_dict = {'dipak':['dipak.dash@intel.com', 112352],'rohit':['rohit.jain@intel.com',231112], 'neel':['neel.rai@intel.com', 552131]}
employee_dict = {}

key_list = ['dipak', 'rohit', 'neel']
value_list = [['dipak.dash@intel.com', 112352], ['rohit.jain@intel.com',231112], ['neel.rai@intel.com', 552131]]

i = 0
for key in key_list:
    employee_dict.setdefault(key, []) = value_list[i]
    i = i + 1
    