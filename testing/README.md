#pytest 命名规则
- 文件名以 test_开头或者以_test结尾
- 类名以Test 开头
- 方法名以test_开头


#pytest 命令行参数
pytest --help
pytest -v 打印结果的详细信息
pytest -s 打印print的信息
pytest -k 跳过运行某个或者某些测试用例
pytest -x 遇到执行失败的用例就立刻停止执行
pytest -maxfail = 2 遇到2条失败的测试用例就立刻停止执行
pytest -m mark标签名 只执行加有该标签名的测试用例
pytest --collect-only 只收集测试用例
pytest --junit-xml = ./result.xml 将执行结果生成测试文件

#pytest 框架结构

模块级： setup_module/teardown_module 在模块始末调用（级别最高）
函数级： setup_function/teardown_function 只对函数用例调用（不在类中）
类级： setup_class/teardown_class 只在类中前后调用一次（在类中） 一定要要写在类里边
方法级: setup_method/tesrdown_method 在方法始末调用（在类中）
方法级： setup/teardown 运行在调用方法的前后

#参数化


#数字驱动

#pytest 配置


#fixture
### pytest fixture 用法

1. 使用 装饰器来定义fixture @pytest.fixture()
2. 如果想引用fixture的返回值的话，就使用fixture的名字来引用
3. 如果不需要引用fixture返回值，可以使用装饰器@pytest.mark.usefixtures('login')来引用

### yeild用法


### 理解conftest.py

在当前目录下创建一个conftest.py文件
1. conftest.py 文件不需要导入，直接引用里边定义的fixture方法
2. 就近原则， 当前模块> 当前目录的conftest.py>父级目录的conftes.py>祖辈目录(不会找兄弟结点)
3. 一点来说，conftest.py会存放一些公共的方法， 比如fixture, hook


# pytest 重点
重点1： pytest 常用参数
重点2： pytest参数化与数字驱动
重点3： pytest fixture的基本用法（autouse, conftest.py）
重点4： allure（环境，feature，story、日志、截图、视频）
重点5；打印日志
了解：hook

