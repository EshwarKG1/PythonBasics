from datetime import datetime
import subprocess

git_dir = "/home/acufore/Eshwar/myWorking"
git_branch = "RPI_testing"

def git_commit():
        print("Adding files to Local GIT repository...", end= ' ')
        tmp=subprocess.call( ["git", "add", "."], cwd= git_dir )
        if not tmp:
                print("DONE")
        else:
                print("ERROR !")
                
        now = datetime.now()
        comment = 'Updated ' + now.strftime( "%d-%b" )
        
        print("Committing files...", end= ' ')
        tmp=subprocess.call( ["git", "commit", "-m", comment ], cwd=git_dir )
        if not tmp:
                print("DONE")
        else:
                print("ERROR !")
                
        print("Pushing the files to " + git_branch + " branch....", end= ' ')
        tmp=subprocess.call( ["git", "push", "-u", "origin", git_branch, "--force"], cwd=git_dir )
        if not tmp:
                print("DONE")
        else:
                print("ERROR !")

def git_pull():
        print( "Pulling Files from "+ git_branch +" GIT repository...", end= ' ' )
        tmp=subprocess.call( ["git", "pull", "origin", git_branch ], cwd=git_dir )
        if not tmp:
                print("DONE")
        else:
                print("ERROR !")
                        
if __name__ == '__main__':
        ret = int(input("GIT Operations\n\t 1. Git Commit\n\t 2. Git Pull\nOption: "))
        if ret == 1:
                git_commit()
        elif ret == 2:
                git_pull()
        else:
                print("[ERROR] Wrong Choice !\n")
