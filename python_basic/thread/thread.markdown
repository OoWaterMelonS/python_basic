多线程 Threading 是一种让程序拥有分身效果. 能同时处理多件事情. 
一般的程序只能从上到下一行行执行代码, 不过 多线程 (Threading) 就能打破这种限制.


我们在多线程 (Threading) 里提到过, 它是有劣势的, GIL 让它没能更有效率的处理一些分摊的任务. 
而现在的电脑大部分配备了多核处理器, 多进程 Multiprocessing 能让电脑更有效率的分配任务给每一个处理器,
 这种做法解决了多线程的弊端. 也能很好的提升效率.