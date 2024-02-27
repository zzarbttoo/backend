from pathlib import Path 
import sys 

class PathManager:
    def __init__(self, depth=2):
        self.project_root = Path(__file__).resolve().parent

        for _ in range(depth):
            self.project_root = self.project_root.parent
        sys.path.append(str(self.project_root))

    #default path 설정은 pulse/realtime_pyfiles   
    def get_sub_project_root(self, subfolder="pulse/realtime_pyfiles"):
        pulse_root = self.project_root / subfolder
        sys.path.append(str(pulse_root))
        return pulse_root

