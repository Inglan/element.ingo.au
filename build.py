import os

os.system("git clone https://github.com/element-hq/element-web.git")
os.chdir('element-web')
os.system("git reset --hard $(git describe --tags $(git rev-list --tags --max-count=1))")

os.system("yarn install")

os.system("cp config.sample config.json")

os.system("yarn dist")