"""
463. 岛屿的周长

给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。
计算这个岛屿的周长。

示例：
输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
输出: 16
"""


def island_perimeter(grid):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    if not grid:
        return 0
    res = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(0, row):
        for j in range(0, col):
            if grid[i][j] == 0:
                continue
            for k in range(0, 4):
                t_x = i + dx[k]
                t_y = j + dy[k]
                if t_x < 0 or t_x >= row or t_y < 0 or t_y >= col or grid[t_x][t_y] == 0:
                    res += 1
    return res