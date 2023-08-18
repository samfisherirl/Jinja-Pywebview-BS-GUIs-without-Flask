# handle javascript requests
# self.title = title
# self.path = path
# self.exe = exe
# self.id = id
# from running_process_and_paths
try:
    import running_processes_and_paths
except:
    pass

def return_object(process, Data):
    print(process)
    response = {
        'message': 'Hello {}!'.format(process)
    }
    # print(response)

    list = [str(i.title + '\n' + i.path) for k, i in Data.items() if int(i.id) == int(process.strip())]
    print("this is the truncated list")
    print(str(list))
    
    #dic = [i for k, i in Data.items() if int(i.id) == int(process.strip())]
    #for k, i in Data.items():
    # if int(i.id) == int(process.strip()
    # if int(dic[0].id) == int(process.strip()):
    #     print(dic.title)
    #     print(dic.path)
    # [print(i.title) for k, i in Data.items() if int(i.id) == int(process.strip())]

    return response


if __name__ == "__main__":
    Data = running_processes_and_paths.get()
    return_object('2', Data)