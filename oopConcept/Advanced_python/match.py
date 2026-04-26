# def http_status(status):
#     match status:
#         case 200:
#             return "ok"
        
#         case 404:
#             return "not found"
#         case 500:
#             return "internal server error"
#         case _:
#             return "unknown status"
        
# print(http_status(404))


dict1 = {"a":1, "b":2, "c":3}
dict2 = {"c":2, "d":5, "e":6}

merged = dict1 | dict2
print(merged)