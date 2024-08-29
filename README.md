# 退乎前备份知乎回答：zhihubackup

每个知乎答主都有退乎的梦想，但退乎前如果删光回答，则十分可惜。因此，我用Python写了60行的脚本，可以在退乎前备份自己的所有回答和文章，以免事后后悔。

## 安装

用[pipx](https://github.com/pypa/pipx)安装zhihubackup到独立环境中：

```sh
pip install pipx
pipx install zhihubackup
```

## 使用

2024年7月起，知乎添加了如下所示的验证操作：

```json
{'error': {'need_login': True, 'redirect': 'https://www.zhihu.com/account/unhuman?type=S6E3V1&need_login=true', 'code': 40352, 'message': '系统监测到您的网络环境存在异常，为保证您的正常访问，请点击下方验证按钮进行验证。在您验证完成前，该提示将多次出现。'}}
```

因此需要从浏览器中手动获取zhihu.com的cookie：
[Chrome获取Cookie](https://developer.chrome.com/docs/devtools/application/cookies?hl=zh-cn)
[Edge获取Cookie](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/storage/cookies)

将获取的cookie设置为环境变量：

```sh
export ZHUHU_COOKIE="q_c1=...; ...; osd=..."
```

假如你是@贱贱，你的id是`splitter`，那么可以执行命令：

```sh
zhihubackup splitter
```

静等一段时间。运行结束后，可以看到产生了名为`splitter`的文件夹：
```
- splitter
|- answer   (842 files)
|- article  (101 files)
|- pin      (3214 files)
|- question (57 files)

```
备份已经成功，现在可以删光回答和文章了。
