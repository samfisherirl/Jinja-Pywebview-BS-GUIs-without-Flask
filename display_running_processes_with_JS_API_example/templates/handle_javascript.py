# handle javascript requests
# self.title = title
# self.path = path
# self.exe = exe
# self.id = id
# from running_process_and_paths


def return_object(process, Data):
    print(process)
    response = {
        'message': 'Hello {}!'.format(process)
    }
    # print(response)
    for k, i in Data.items():
        if int(i.id) == int(process.strip()):
            print(i.title)
            print(i.path)
    # [print(i.title) for k, i in Data.items() if int(i.id) == int(process.strip())]

    return response
