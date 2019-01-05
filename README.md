# Mini Java Compiler Front End
### 李艾丽丝 15307130431 | 杨晨曦 15307130360

### 组员分工
李艾丽丝：保留字命名变量错误检测、词法语法错误包装、声明检查、类型匹配、返回值检查v   
杨晨曦：规则文件编写、符号表生成、函数参数表检查、错误修复、继承类的属性访问
### 依赖说明
1. ANTLR4
2. python3.6
3. antlr4-python3-runtime4.7.2

### 运行平台
MacOS Mojave 10.14.2 

### 运行方式
1. 安装好依赖的工具和库
2. 切至目录src下
3. 在命令行执行以下命令生成许多原本需要我们手写的文件，例如tokens, listen.java:
    ```
    antlr4 miniJavaExpr.g4
    ```
4. 执行以下命令来编译ANTLR生成的所有文件:
    ```
    javac *.java
    ```
5. 在命令行运行以下命令可对输入代码生成语法树（需要将待测代码复制在命令行，并以EOF结束）：
    ```
    grun miniJavaExpr goal -gui
    ```
6. 测试代码在/src/testCode和/src/testCases文件下，对测试代码做错误检测等可直接在命令行运行以下命令：
   ```
   python miniJavaMain.py --dir="your dir" --file="your file"
   ```
   若测试代码有错误会输出报错信息，若没有则不会输出