from .models import Tool
def updateValue(data):
    if data['action'] == 0 or data['action'] == 1:                         #add or update
        for tool in Tool.objects.filter(type=data['tool_type']):
            if data['boolChecks_or_info'] == 0:     #boolchecks
                tool.boolChecks[data['key']]= data['boolChecks_value']
                tool.save()
            else:                                   #info
                tool.info[data['key']]= data['info_value']
                tool.save()
    if data['action'] == 2:
        for tool in Tool.objects.filter(type=data['tool_type']):
            if data['boolChecks_or_info'] == 0:     #boolchecks
                # tool.boolChecks.pop(data['key'], None)
                print(tool.boolChecks)
                print(type(tool.boolChecks))
                tool.boolChecks.pop(data['key'], None)

                tool.save()
            else:                                   #info
                tool.info.pop(data['key'], None)
                tool.save()
