首先，感谢廖雪峰老师制作的Git教程：https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000，下面命令是我自己的理解，若有不正确的地方，欢迎指正，谢谢！

1. Git简介

// 1. 创建版本库

$ cd:e // 切换盘符

$ cd .. // 回到文件上一层(注: cd与..中间有个空格)

$ cd ~ // 回到当前目录的主目录

$ mkdir Git // 创建文件夹Git

$ touch fileName // 新建文件

$ vi fileName // 编辑文件

$ press i button // 开始进入编辑状态

$ press the Esc button // 退出vim编辑区

$ :wq // 退出编辑状态, 回到命令窗口

$ mkdir learngit // 创建文件夹learngit

$ pwd // 显示当前路径/e/Git/learngit

$ git init // 将当前目录变成一个Git可以管理的仓库

$ touch+文件名 // 直接新建一个文件

$ git add readme.txt // 将文件添加到Git仓库（把文件修改添加到暂存区）

$ git commit -m "wrote a readme.txt." // 将文件提交到仓库（把暂存区的所有内容提交到当前分支）

$ git add file1.txt // 添加file1.txt文件

$ git add file2.txt file3.txt // 同时添加file2.txt和file3.txt两个文件

$ git commit -m "add 3 files." // 一次性提交3个文件

2. 时光穿梭机：

// 2.1 版本回退

$ git status // 查看当前仓库状态（仓库下的工作区文件是否被修改过）

$ git diff readme.txt // 查看工作区的readme.txt与缓存区的readme.txt的区别

$ git log // 查看最近到最远的提交记录（详情: commit id + Author + Date + comment）

$ git log --pretty=oneline // 查看最近到最远的提交记录（简写：commit id + comment）

$ git reset --hard HEAD^ // 回到上一个版本（HEAD: 当前版本，HEAD^: 上一个版本，HEAD~100: 往上100个版本）

$ git reset --hard 1234567 // 回到指定版本号commit id（此处：commit id 假设为1234567******，Git会根据commit id的前几位自动寻找对应的版本）

$ cat readme.txt // 查看readme.txt的内容

$ git reflog // 查看每一次命令记录历史，确保能回到任意版本　　

// 2.2 工作区与暂存区

$ git diff readme.txt // 比较工作区（working directory）和暂存区（stage/index）的区别

$ git diff --cached // 比较暂存区（stage/index）和分支（master）的区别

// 2.3 管理修改（详见1. 创建版本库中的命令）

// 2.4 撤销修改

$ git checkout -- readme.txt // 撤销修改：1. 文件在添加到缓存区前修改，则回退到原工作区状态；2. 文件在添加到缓存区后修改，则回退到原缓存区状态。也即是将readme.txt撤回到最近一次git add或git commit状态（注：--表示在当前分支，如果没有，则切换到另一个分支）

$ cat readme.txt // 查看文件内容

$ git reset HEAD readme.txt // 1. 回退到最新版本；2. 将暂存区的修改回退到工作区

// 2.5 删除文件

$ rm test.txt // 删除工作区文件（类似于手动删除）

$ git status // 查看当前工作区与缓存区状态

$ git rm test.txt // 情况1：确认删除

$ git commit -m "remove test.txt" // 情况1：确认删除后，提交到版本库

$ git checkout -- readme.txt // 情况2：误删，需要回退（即：用版本库里的版本替换工作区的版本）

// 3. 远程仓库

// 3.1 添加远程库

git remote add origin git@server-name:path/repo-name.git // 关联一个远程仓库，如：$ git remote add origin git@github.com:ChrisLeejing/learngit.git

git push -u origin master // 第一次推送master分支的所有内容

注：在GitHub上创建新仓库时，如果勾选了README.md选项时，可能会出现下面错误，提示：远程仓库有readme.txt,而本地仓库没有README.txt,此时应该先进行合并文件，再进行推送。



git pull --rebase origin master // 推送之前，进行合并



合并文件之后，发现本地仓库中多了README.md文件，此时再进行推送修改到远程仓库就可以了。





再次执行：git push -u origin master, 即可推送本地仓库到远程仓库了



查看GitHub上的文件，已经更新！



git push origin master // 以后每次本地修改更新后，推送最新修改

// 3.2 从远程库克隆

$ git clone git@github.com:ChrisLeejing/gitskills.git // 以SSH方式克隆

$ git clone https://github.com/ChrisLeejing/gitskills.git // 以Https协议方式克隆

// 4. 分支管理

// 4.1 创建与合并分支

git branch // 查看所有分支（当前分支以‘*’标记）

git branch <name> // 创建分支（如：git branch dev）

git checkout <name> // 切换分支

git checkout -b <name> // 创建切换分支（如：git checkout -b dev）

git merge <name> // 合并分支到当前分支上

git branch -d <name> // 删除该分支

// 4.2 解决冲突

git log --graph // 查看分支合并图

git log --graph --pretty=oneline --abbrev-commit // 查看分支合并缩略图

// 4.3 分支管理策略

git merge --no-ff -m "注释" dev // 合并后的分支有历史记录，而Fast-Forward合并之后，分支没有历史记录

// 4.4 Bug分支

git stash // 隐藏分支工作现场，为修复bug准备

git stash list // 查看有哪些分支隐藏的工作现场，为恢复工作现场做准备

git stash apply // 恢复工作现场，但不删除存储的stash内容，结合git stash drop进行删除

git stash drop // 删除存储的stash内容，恢复到隐藏前的工作现场

git stash pop // 恢复到隐藏前的工作现场，相当于git stash apply和git stash drop

git stash apply stash@{0} // 可以多次stash，通过git stash list查看所有的stash，然后可以恢复到指定的隐藏的工作现场

// 4.5 Feature分支

注：当添加一个feature时，最好新建一个分支：git checkout -b <name>

git branch -D <name> // 强行删除一个没有被合并到主分支的分支

// 4.6 多人协作（最好结合工作场景理解）

git remote -v // 查看远程库详细信息

git push origin dev // push本地dev分支到远程dev

git push origin master // push本地master分支到远程master（时刻保持同步）

git pull // 将最新的pull/dev(master)爬下来

git checkout -b branch-name origin/branch-name // 在本地创建和远程分支对应的分支

git branch --set-upstream-to=origin/<branch> dev // 建立本地分支和远程分支的关联

// 4.7 Rebase

git rebase // 将本地未push的分支提交整理成直线，利于查看

// 5. 标签管理

// 5.1 创建标签

git tag <tagname> // 创建标签

git tag // 查看所有标签

git tag <tagname> commitId // 为某次提交创建指定标签

git show <tagname> // 查看指定标签具体内容

git tag -a <tagname> -m "v0.1 released" commitId // 为某次指定的提交创建标签，同时添加标签注释

git tag -d <tagname> // 删除某个标签

git push origin <tagname> // 推送某个标签到远程库

git push origin --tags // 一次性推送所有标签到远程库

git tag -d v0.9 // 删除远程库标签（第一步：删除本地库标签）

git push origin :refs/tags/v0.9 // 删除远程库标签（第二步：从远程库删除标签）

// 6. 使用GitHub

在GitHub上，可以自己fork任意开源仓库，自己拥有fork后的仓库的读与写操作权限，可以推送pull request给官方仓库贡献代码。

// 7. 使用码云（与GitHub类似，用到的时候，再注册使用练习，毕竟GitHub更加NB一些！）

// 8. 自定义Git（这里只是简单入门）

git config --global color.ui true // 让Git显示颜色

// 8.1 忽略特殊文件

忽略某些文件时，需要编写.gitignore文件，文件本身要放到版本库中，Git可以对.gitignore做版本管理！（注：不需要从头写.gitignore文件，GitHub已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接在线浏览：https://github.com/github/gitignore）

// 8.2 配置别名

git config --global alias.st status // 将st作为status的别名，以后就可以git st查看暂存区与工作区的状态了（还有类似co:checkout, ci:commit, br:branch，--global:是针对于当前用户起作用的，如果不加，则只针对于当前仓库）

cat .gitignore // 查看当前文件所有配置信息（包括别名信息）

// 8.3 搭建Git服务器（暂时用不上，用的时候，再复习一下）

到此，Git教程学完，感谢廖雪峰老师！为了让自己不遗忘，记下自己练习的Git命令地址：E:\Git\learngit\note.txt
