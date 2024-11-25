!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="w8dniQ58bVgucwzWYOCf")
project = rf.workspace("mig-sant-cmm").project("mig-sante")
version = project.version(1)
dataset = version.download("yolov11")
                
