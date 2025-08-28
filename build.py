import os, shutil

os.system("git clone https://github.com/element-hq/element-web.git")
os.chdir('element-web')
os.system("git reset --hard $(git describe --tags $(git rev-list --tags --max-count=1))")

os.system("yarn install")
os.system("cp config.sample.json config.json")
os.system("yarn dist")

os.mkdir("build")
os.system(f"tar -xzvf {os.path.join("dist", os.listdir("dist")[0])} -C ./build")

shutil.move(os.path.join("./build", os.listdir("./build")[0]), "../build")
