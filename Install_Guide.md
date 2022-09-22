# Web接口文档在线生成指导

By ChenYang 20220921

## 环境准备

- Git
- NodeJS v8.x ~ v10.x (gitbook 长久不更新,高于v10版本的 NodeJS 接口不兼容)
- Python3 (要求高于v3.5)

### 安装 gitbook

```shell

npm install gitbook-cli -g

```

### 预览文档

适用以下指令本机将默认启动一个端口为4000的HTTP服务,用于预览当前文档所生成的效果,若有文档改动需要重新执行.

```shell

gitbook serve

```

### 生成PDF

`2pdf` 目录存放生成 PDF 的脚本.

**安装**

首次执行需先安装依赖,可用 `venv` 虚拟环境测试:

```shell

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple

```

**生成**

若要生成 pdf, 则要提前启动 `gitbook serve` 预览环境, 然后执行以下指令,它将会默认访问地址为 `http://127.0.0.1:4000` 的页面,即本机 4000 端口的 gitbook 预览页面,并将其转换成 PDF.

```shell

source venv/bin/activate
python gitbook2pdf.py

```

若想指定其他地址,可直接跟网址, eg: `python gitbook2pdf https://webapi.gitbook.io`