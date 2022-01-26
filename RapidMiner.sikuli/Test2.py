import shutil
import json

Settings.MoveMouseDelay=0.1
Settings.DelayBeforeMouseDown=0.1
Settings.ObserveScanRate=0.01
Settings.AutoWaitTimeout=0.5
dictionary_data = {}


count = 0
while not exists(Pattern("1641430148345.png").similar(0.74)):
    if exists(Pattern("1641429183481.png").similar(0.80).targetOffset(2,2)):
        operator_dict={}
        rightClick(Pattern("1641429183481.png").similar(0.80).targetOffset(3,2))
        if exists("Sans titre-1.png"):
            click("Sans titre.png")
            wait(1)           
            matchName=Region(694,295,564,18).text()
            if (exists(Pattern("1642599732954.png").similar(0.81))):
                matchFalse=find(capture(Region(608,251,701,531)))
                zFalse=matchFalse.findAll(Pattern("1642599732954.png").similar(0.81))
                for coord in zFalse:
                    count=count+1
                    operator_dict[Region(coord.getTarget().getX()+10,coord.getTarget().getY()-10,217,25).text()]=False
            if (exists(Pattern("1642599775439.png").similar(0.85))):
                matchTrue=find(capture(Region(608,251,701,531)))
                zTrue=matchTrue.findAll(Pattern("1642599775439.png").similar(0.85))
                for coord in zTrue:
                    count=count+1
                    operator_dict[Region(coord.getTarget().getX()+10,coord.getTarget().getY()-10,217,25).text()] = True
                
            image=capture(Region(608,251,701,531))
            try:
                os.makedirs("C:\\Users\\tnersissian\\Documents\\Test2.sikuli\\Operator\\Capabilities\\"+matchName.replace("/",""))
            except Exception as e:
                print(e)
            shutil.move(image,"C:\\Users\\tnersissian\\Documents\\Test2.sikuli\\Operator\\Capabilities\\"+matchName.replace("/",""))
            dictionary_data[matchName]=operator_dict     
            click("1641430556092.png") 
            type(Key.DOWN)
        else:
            mouseMove(Location(500, 500))
            type(Key.ENTER)
            type(Key.DOWN)                

json_dump = json.dumps(dictionary_data)

def write_json(target_path, target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    print(os.path.join(target_path, target_file))
    with open(os.path.join(target_path, target_file), 'w') as f:
        json.dump(data, f)


write_json("C:\\Users\\tnersissian\\Documents\\Test2.sikuli","json_data.json",json_dump)

print(dictionary_data)
print("Finish")