# Exercise_06
对于所给问题，由于该问题的误差分布遵循均匀分布，采用[PSO算法](https://zh.wikipedia.org/wiki/%E7%B2%92%E5%AD%90%E7%BE%A4%E4%BC%98%E5%8C%96)可以得到很好的效果。

事实上，由于此题的分布为均匀分布，通过PSO的群聚行为，可以很快的求出可行解，对PSO算法进行改进后，虽然对于此题的均匀分布问题效率可能会有一定幅度的下降，但可以处理非均匀分布的问题。
下图是采用改进后的PSO求得的一个可行解，为了简化问题，只考虑了二维空间的点的分布，对于加入风阻误差的三维问题，只需小小的修改一下[源代码](https://github.com/maphyca/compuational_physics_2014301020045/blob/master/homework/exercise_06.py)即可
![](https://raw.githubusercontent.com/maphyca/compuational_physics_2014301020045/master/homework/figure_1.png)
求出的解为speed= 1278.725427129032 ,angle= 0.9379894692646149
