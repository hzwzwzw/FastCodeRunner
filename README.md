# FastCodeRunner

`FastCodeRunner`从标准输入流读取代码，将其保存为一个单文件并运行。这只是一个再简单不过的小脚本，目的是为了当被人在聊天框中发了一大坨代码时简单地运行它而不必打开IDE.

为了契合生活场景的痛点（例如对方发了道题但没发样例来），程序可以调用大模型API构造输入以尝试交互。在这个意义上讲，它和直接生成代码并云端运行的`ChatGPT`相比，唯一的优势可能是可以运行C++程序。

占坑，还没有完成。